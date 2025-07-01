from controller import Robot
import sys
import struct
import string
import numpy as np
from math import *
import cv2 as cv

robot = Robot()
timestep = int(robot.getBasicTimeStep())

# Device initialization
Camera1 = robot.getDevice("CamL")
Camera2 = robot.getDevice("CamR")
color_sensor = robot.getDevice("Color_Sensor")
emitter = robot.getDevice("emitter")
receiver = robot.getDevice("receiver")
gps = robot.getDevice("gps")
dis_sensor1 = robot.getDevice("Dis_Sen_Middle")
dis_sensor2 = robot.getDevice("Dis_Sen_Right")
dis_sensor3 = robot.getDevice("Dis_Sen_Left")
dis_sensor4 = robot.getDevice("Dis_Sen_Right_Angle")
dis_sensor5 = robot.getDevice("Dis_Sen_Left_Angle")
wheelL = robot.getDevice("Wheel_Left motor")
wheelR = robot.getDevice("Wheel_Right motor")
IMU = robot.getDevice("imu")
lid = robot.getDevice("lidar")

# Enable all sensors
receiver.enable(timestep)
dis_sensor1.enable(timestep)
dis_sensor2.enable(timestep)
dis_sensor3.enable(timestep)
dis_sensor4.enable(timestep)
dis_sensor5.enable(timestep)
Camera1.enable(timestep)
Camera2.enable(timestep)
IMU.enable(timestep)
color_sensor.enable(timestep)
gps.enable(timestep)
lid.enable(timestep)

# Motor configuration
wheelL.setVelocity(0)
wheelR.setVelocity(0)
wheelL.setPosition(float("inf"))
wheelR.setPosition(float("inf"))

while robot.step(timestep) != -1:
    print("Front sensor value:", dis_sensor1.getValue())
    front_sensor_value = dis_sensor1.getValue() * 100
    if front_sensor_value < 10:
        wheelL.setVelocity(-5)
        wheelR.setVelocity(5)
    else:
        wheelL.setVelocity(5)
        wheelR.setVelocity(5)
