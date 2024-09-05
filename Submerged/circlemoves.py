#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor
from pybricks.parameters import Port
from pybricks.robotics import DriveBase

#   Initialize EV3 Brick and motors
ev3 = EV3Brick()
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Create a Drivebase Object (measurements in mm)
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Set the desired radius for the circle (in mm)
# circle_radius = 100

# # Calculate the turn rate needed for the circle
# turn_rate = 180 * (robot.wheel_diameter / (2 * 3.14 * circle_radius))

# # Move in a circle
# robot.drive(speed=200, turn_rate=turn_rate)

# # Wait for user input to stop
# ev3.Button_left.wait()
# robot.stop()

# Set the radius of the circle and the angle to travel
radius = 50  # mm
angle = 180  # degrees

# Drive in a circle
robot.drive(speed=100, turn_rate=360/radius)

# Wait for the robot to complete the circle
while True:
    pass