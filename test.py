from controller import Robot, Camera, GPS 
import numpy as np

robot = Robot()

lidar = robot.getDevice("lidar")
gps = robot.getDevice("gps")
compass = robot.getDevice("inertial_unit")

left_wheel = robot.getDevice("wheel2 motor")
right_wheel = robot.getDevice("wheel1 motor")

timestep = int(robot.getBasicTimeStep())

lidar.enable(timestep)
gps.enable(timestep)
compass.enable(timestep)

left_wheel.setPosition(float('inf'))
right_wheel.setPosition(float('inf'))

gps_data = []
compass_data = []
lidarData = []

def get_sensor_data():
     global gps_data, compass_data, lidarData

     gps_data = gps.getValues()
     compass_data = compass.getRollPitchYaw()
     lidarData = np.array(lidar.getRangeImage()).reshape(4, 512) * 100

def stop():
     steps = 160
     while robot.step(timestep) != -1:
          get_sensor_data()
          left_wheel.setVelocity(0)
          right_wheel.setVelocity(0)

          steps -= 1

          if steps == 0:
               break

while robot.step(timestep) != -1:
     get_sensor_data()

     if lidarData[2][0] < 5:
          stop()
     else:
          left_wheel.setVelocity(3)
          right_wheel.setVelocity(3)