# **Object Detection Classifier in Windows 10**

## Purpose
The project is supposed to make use of the capabilities of modern machine along with a camera in order to process, learn, and identify an object on its own. By doing so, we would be able to provide a useful software in which it would be a great use for image processing and for projects that involves machine learning, face detection, and tracking. 

## Scope/s
The project does not work on mac OS and it might require a good laptop specification in order to work properly. The program can only accept live data as input and cannot process images for detection.

## Overview/s
The group would like to create a program that can detect an object and classify it with a label using TensorFlow, which is used for machine learning applications such as neural networks. The program will be written and implanted using Python. The program can only accept live data as input, which means that it cannot detect object when the input is an image.

## Basic Functional Requirement/s
- The program makes use of a camera. 
- It should be able to identify objects even if they are partially covered. 
- Must be able to learn new objects by giving it reference images for the program to learn. 
- The project should be scalable meaning additional hardware should be easy to integrate.

## Basic Non-Functional Requirement/s
- Must run on Windows or Linux with compatible hardware. 
- Implemented using Python. 

## Web Camera Requirements
- The clarity which the camera will be able to detect the given image. Stable and non-moving/blurred image will be required. Specific resolution of the camera enables higher performance in image detection. 

## Installation
Install the required applications that will be used in running the program.

## Step 1: Install the Cuda toolkits and the cudnn, which should be compatible to each other for smooth execution of the program.

## Cuda
![GetImage](https://user-images.githubusercontent.com/52278031/67069927-40317800-f1b1-11e9-8907-002f9352e623.jpeg)

## Cudnn
![GetImage (1)](https://user-images.githubusercontent.com/52278031/67069983-635c2780-f1b1-11e9-95ef-d1993d883c7d.jpeg)

## Step 2: Install Tensorflow using pip command and then check the version of the packages fr the compatibility.
Download the package of Tensorflow using the command prompt or directly download the package from the site using these commands
> pip3 install -U pip virtualenv pip3 --user --upgrade tensorflow

then after installing, check the version of the packages by typing:
> python3 --version pip3 --version virtualenv --version

then, activate the environment using the activate command,
> activate tesorflow1

## Step 3: Download the packages needed in running the program.
Guide for downloading packages:
```
conda install -c anaconda protobuf
pip install pillow
pip install lxml
pip install Cython
pip install contextlib2
pip install jupyter
pip install matplotlib
pip install pandas          //used for the feed of the webcam-realtime
pip install opecv-python    //used for the feed of the webcam-realtime
```
## Step 4: Setting up the environment variables
## Go to Advanced Settings
![GetImage (2)](https://user-images.githubusercontent.com/52278031/67071049-29405500-f1b4-11e9-8b76-8913d8f5d702.jpeg)

## Go to Environment Variables
![GetImage](https://user-images.githubusercontent.com/52278031/67071067-32c9bd00-f1b4-11e9-8376-6490ab8a4144.jpeg)

## Go to PYHTONPATH
![GetImage (1)](https://user-images.githubusercontent.com/52278031/67071126-57be3000-f1b4-11e9-8791-ecd5ba500404.jpeg)

## Add the following paths:
![61795134-4b486680-ae55-11e9-9208-c9c6752cf1c9](https://user-images.githubusercontent.com/52278031/67071487-43c6fe00-f1b5-11e9-8b5a-408088f015dc.jpg)

## Step 5
Dowload the zip file from the github and and clone and type the following commands to execute the machine learning.
> python --version

> python SampleSignIn.py

The sample sign in window will pop up,

![GetImage](https://user-images.githubusercontent.com/52278031/67071785-0a42c280-f1b6-11e9-98ad-840b468d3d35.png)

Enter valid username and valid password that is already registered in the database:
```
Username: noot
Password: noot
```
Then, the object detection classifier program is ready.
