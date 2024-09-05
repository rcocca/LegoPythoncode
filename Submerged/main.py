#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import Image, ImageFile, SoundFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
ev3.speaker.say("Bricks for Life!")

# Write code for wheels.
# Initialize the motors.
left_motor = Motor(Port.A)
right_motor = Motor(Port.D)

# Initialize the drive base.
robot = DriveBase(left_motor, right_motor, wheel_diameter=55.5, axle_track=104)

# Go forward and backwards for one meter.
Motor(Port.A, positive_direction=Direction.CLOCKWISE, gears=None)



# #right turn.
# robot.turn(90)

# ev3.speaker.beep()

