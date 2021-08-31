import argparse
from pathlib import Path

import yaml
import tensorflow as tf
from tensorflow import keras
from utils.decoders import CTCGreedyDecoder

parser = argparse.ArgumentParser()
parser.add_argument('--images', type=str, default="test_images/5_Delighted.png",
                    help='Image file or folder path.')
parser.add_argument('--config', type=Path, default="saved_model/config.yml",
                    help='The config file path.')
parser.add_argument('--model', type=str, default="saved_model/saved_model.h5",
                    help='The saved model.')
args = parser.parse_args()

config = tf.compat.v1.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.3
tf.compat.v1.keras.backend.set_session(
    tf.compat.v1.Session(config=config))

with args.config.open() as f:
    config = yaml.load(f, Loader=yaml.Loader)['dataset_builder']


def read_img_and_resize(path, shape):
    img = tf.io.read_file(path)
    img = tf.io.decode_jpeg(img, channels=shape[2])
    if shape[1] is None:
        img_shape = tf.shape(img)
        scale_factor = shape[0] / img_shape[0]
        img_width = scale_factor * tf.cast(img_shape[1], tf.float64)
        img_width = tf.cast(img_width, tf.int32)
    else:
        img_width = shape[1]
    img = tf.image.resize(img, (shape[0], img_width))
    return img


model = keras.models.load_model(args.model, compile=False)
decoder = CTCGreedyDecoder(config['table_path'])

p = Path(args.images)
if p.is_dir():
    img_paths = p.iterdir()
else:
    img_paths = [p]

for img_path in img_paths:
    img = read_img_and_resize(str(img_path), config['img_shape'])
    img = tf.expand_dims(img, 0)
    outputs = model(img)
    if not isinstance(outputs, tuple):
        outputs = decoder(outputs)
    print(f'Path: {img_path}, y_pred: {outputs[0].numpy()}, '
          f'probability: {outputs[1].numpy()}')
