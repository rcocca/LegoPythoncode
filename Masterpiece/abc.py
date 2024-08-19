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

ev3.speaker.beep()
# lift_motor.run_target(1000, -1500)
# gripper_motor.run_target(1000, 1000)

# Mission 1 3D CINEMA move robot, move arm down, then move arm up
move(my_robot, 275)
# lift down
lift_motor.run_target(1000, -2500)
# lift up
lift_motor.run_target(1000, 1000)

# Moving to Mission 2
move(my_robot,-100)
my_robot.turn(-64)
move(my_robot, 235)
my_robot.turn(65)
gripper_motor.run_target(1000, 700)
move(my_robot,250)
my_robot.turn(25)


# Mission 2 THEATER SCENE CHANGE move robot around mission 1 then onto mission 2, moving arm down
# lift down
lift_motor.run_target(1000, -2500)
move(my_robot, -30)
# lift up
lift_motor.run_target(1000, 1000)
my_robot.turn(-70)

# Mission 3 IMMERSIVE EXPERIENCE move robot arond mission 2 then onto mission 3, moving arm down
move(my_robot, 200)
my_robot.turn(-22)
move(my_robot, 180)
# lift down
lift_motor.run_target(1000, -2500)
# lift up
lift_motor.run_target(1000, 1000) 