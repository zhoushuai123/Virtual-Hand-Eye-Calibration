# Camera Calibration

for using of arucomarker, the parameter of camera will be needed

## Environment

ROS melodic

OpenCV(default contained in ROS)


## Step 0: Package
download package and build

	http://wiki.ros.org/image_pipeline
	
	https://github.com/ros-perception/image_pipeline

## Step 1: ttt file

put the camera you want to calibrate into the environment. Add a non-thread script to pubilish the image to ros topic

## Step 2: Ready to calibrate

MUST run roscore first

run coppeliaSim

run rosrun camera_calibration cameracalibrator.py --size 9x6 --square 0.021 image:=/image camera:=/image --no-service-check

## Step 3: Calibrate and get parameters

referrence: https://www.youtube.com/watch?v=yAYqt3RpT6c





