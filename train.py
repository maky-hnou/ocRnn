import argparse
import shutil
from pathlib import Path

import yaml
import tensorflow as tf

from dataset_factory import DatasetBuilder
from model import Model
from loss import CTCLoss
from metrics import SequenceAccuracy
from callbacks import XTensorBoard


def train(config_file, save_dir, model_path):
    with open(config_file, 'r') as configs:
        config = yaml.load(configs, Loader=yaml.Loader)['train']
    print('configration:', config)

    strategy = tf.distribute.MirroredStrategy()
    batch_size = \
        config['batch_size_per_replica'] * strategy.num_replicas_in_sync

    dataset_builder = DatasetBuilder(**config['dataset_builder'])
    train_ds = dataset_builder.build(
        config['train_ann_paths'], batch_size, True)
    val_ds = dataset_builder.build(config['val_ann_paths'], batch_size, False)

    model_class = Model(config['dataset_builder']['img_shape'],
                        dataset_builder.num_classes)
    model = model_class.build()
    model.compile(optimizer=tf.keras.optimizers.Adam(config['learning_rate']),
                  loss=CTCLoss(), metrics=[SequenceAccuracy()])

    if config['restore']:
        model.load_weights(config['restore'], by_name=True, skip_mismatch=True)

    model.summary()

    callbacks = [
        tf.keras.callbacks.ModelCheckpoint(model_path),
        tf.keras.callbacks.ReduceLROnPlateau(**config['reduce_lr']),
        XTensorBoard(log_dir=str(save_dir), **config['tensorboard'])]

    model.fit(train_ds, epochs=config['epochs'], callbacks=callbacks,
              validation_data=val_ds)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--config', type=Path, required=True,
        help='The config file path.')
    parser.add_argument(
        '--save_dir', type=Path, required=True,
        help='The path to save the model, config file and logs')
    args = parser.parse_args()

    args.save_dir.mkdir(exist_ok=True)
    if list(args.save_dir.iterdir()):
        raise ValueError(f'{args.save_dir} is not a empty folder')
    shutil.copy(args.config, args.save_dir / args.config.name)
    prefix = '{epoch}_{sequence_accuracy:.4f}_{val_sequence_accuracy:.4f}'
    model_path = f'{args.save_dir}/{prefix}.h5'
    train(args.config, args.save_dir, model_path)
