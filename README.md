# ocRnn  

![Python version][python-version]
[![GitHub issues][issues-image]][issues-url]
[![GitHub forks][fork-image]][fork-url]
[![GitHub Stars][stars-image]][stars-url]
[![License][license-image]][license-url]

## About this repo:  
An OCR based on an end-to-end trainable Recurrent Neural Network

## Content of the repo:  
The project has been organized as follows:  
- `requirements.txt`: a text file containing the needed packages to run the repo.  
- `train_model.py`: a file with the training code.  
- `test_model.py`: a file with the testing code.  
- `config/`: the fodler containing the config files.  
- `data/`: the folder that contains an example of the dataset used for training.  
- `model/`: the folder that contains the model's architecture.  
- `saved_model/`: the folder that contains the trained model, ready to be used.  
- `test_images/`: the folder containing some images for test purpose.  
- `utils/`: the folder that contains the utils files/methods.

## Use the Repo:  
*N.B:* use Python 3.8  

**1. Clone the repo:**  
on your terminal, run `git clone https://github.com/maky-hnou/ocRnn.git`  
Then get into the project folder: `ocRnn/`  
We need to install some dependencies:  
`sudo apt install python3-pip libpq-dev python3-dev`  

**2. Install requirements:**  
Before running the app, we need to install some packages.  
- *<ins>Optional</ins>* Create a virtual environment:  To do things in a clean way, let's create a virtual environment to keep things isolated.  
Install the virtual environment wrapper: `pip3 install virtualenvwrapper`  
Add the following lines to `~/.bashrc`:  
```
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
export VIRTUALENVWRAPPER_VIRTUALENV=~/.local/bin/virtualenv
source ~/.local/bin/virtualenvwrapper.sh
```
Run `source ~/.bashrc`  
Run `mkvirtualenv ocrnn`  
Activate the virtual environment: `workon ocrnn` (To deactivate the virtual environment, run `deactivate`)  
- Install requirements: To install the packages needed to run the application, run `pip3 install -r requirements.txt`  

*N.B:* If you don't have GPU, or don't have Cuda and Cudnn installed, replace `tensorflow-gpu` by `tensorflow` in requirements.txt.

**3- Run the training:**  
*The dataset:*  The dataset used to train the model is available via this [link](https://www.robots.ox.ac.uk/~vgg/data/text/): a 10 GB dataset.  

[python-version]:https://img.shields.io/badge/python-3.8-brightgreen.svg
[issues-image]:https://img.shields.io/github/issues/maky-hnou/ocRnn.svg
[issues-url]:https://github.com/maky-hnou/ocRnn/issues
[fork-image]:https://img.shields.io/github/forks/maky-hnou/ocRnn.svg
[fork-url]:https://github.com/maky-hnou/ocRnn/network/members
[stars-image]:https://img.shields.io/github/stars/maky-hnou/ocRnn.svg
[stars-url]:https://github.com/maky-hnou/ocRnn/stargazers
[license-image]:https://img.shields.io/github/license/maky-hnou/ocRnn.svg
[license-url]:https://github.com/maky-hnou/ocRnn/blob/main/LICENSE
