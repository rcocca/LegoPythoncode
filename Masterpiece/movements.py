from pybricks.ev3devices import Motor
from pybricks.robotics import DriveBase
from pybricks.parameters import Port, Stop, Direction


def initialize_robot():
    # Initialize the motors.
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)

    # Initialize the drive base.
    robot = DriveBase(left_motor, right_motor, wheel_diameter=55, axle_track=109)
    
    return robot

def move(robot, distance):
    # Go forward for the specified distance.
    robot.straight(distance)

def initialize_robot_arm():
    Lift_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE, [16, 24])

    return Lift_motor

def lift_arm_up(Lift_arm, distance):
    lift_motor.run_target(60, -40)
    gripper_motor.run_target(100, 100)

def initialize_gripper():
    gripper_motor = Motor(Port.A)

    return gripper_motor

def close_gripper():
    gripper_motor = Motor(Port.A)
    gripper_motor.run_until_stalled(-1000, then=Stop.HOLD, duty_limit=50)
    
def open_gripper():
    gripper_motor = Motor(Port.A)
    gripper_motor.run_target(800, 1000)


