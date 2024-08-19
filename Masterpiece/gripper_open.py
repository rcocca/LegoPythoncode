#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick

from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from movements import *

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.
""" 
    Medium motor is Port A - Arms
    Large Motor Left is Port B
    Large Motor Right is Port C
"""

# Create your objects here.
ev3 = EV3Brick()

my_robot = initialize_robot()

robot_arm = initialize_robot_arm()

gripper_motor = Motor(Port.A)
 
lift_motor = Motor(Port.D)

gripper_motor = Motor(Port.A)
gripper_motor.run_target(1000, -800)