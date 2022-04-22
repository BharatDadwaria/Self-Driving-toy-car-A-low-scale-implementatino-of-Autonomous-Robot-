# Self-Driving-toy-car-A-low-scale-implementatino-of-Autonomous-Robot-

The main aim of this project to create a low scale implimentation of A Mobile robot to shift it towards complete autonomous mode. This project was final semester project in Integrated M.Sc Computer Science from Central University of Rajasthan under supervision of Dr. Muzzammil Hussain. I have built the whole mobile robot from scratch. The whole mobile robot contains many components from electronics to mechanical and Programmed through computers.


<p align="center">
  <img src="https://github.com/BharatDadwaria/Self-Driving-toy-car-A-low-scale-implementatino-of-Autonomous-Robot-/blob/master/IMG_20190416_130608122.jpg?raw=true">
</p>


#### Components
* Raspebrry Pi
* H-Bridge
* HC-SR04 (Ultrasonic sensor)
* Camera Module (Raspberry pi 5 MP Camera module)

Later on some advanced components are being added 
* NVidia Jetson Nano (4GB DDR4 , 128Cuda Cores)
* RPLidar (Lidar Sensor)
* Advance power supply for motors

The whole project is divided into two units:
## Robotics :
This module contains all the physical connection between different operators more related to electronics and mechenical engineering. Motors are being connected to the Raspberry pi for programming purpose through GPIO (General Purpose Input Output) pins on Raspberry Pi from H-Bridge. We added HC-SR04 (Ultrasonic sensor) to measure the objects in front of mobile robot and implimented Obstacle avoidance if any obstacles appeare in front of the mobile robot. In order to sense the environment more precisly we also added a Raspberry Pi 5MP Camera module and programmed it to capture the real-time videos and processed the real time image for our deep learning task. In order to make it completely mobile robot (wireless operationable) we remotly controlled the mobile robot from another computer.  
### Circuit Architecture

<p align="center">
  <img src="https://raw.githubusercontent.com/BharatDadwaria/Self-Driving-toy-car-A-low-scale-implementatino-of-Autonomous-Robot-/master/sdc_circuit.PNG">
</p>

## Deep Learning
This submodule contains all the major AI Programming parts. At the time of M.Sc project, due to limited computational power on Raspberry pi (1GB DDR3), we deployed pretrained stop sign detector and later on updated the Computational module to NVIDIA Jetson Nano (4GB DDR4, 128 Cuda cores) to deploy more deep learning tasks especially Computer Vision tasks.
In the update we also added RPLidar Module to our mobile robot for future navigation and mapping purpose. We are planning to implement Basic SLAM Navigation to make it completely Autonomous Mobile robot.


