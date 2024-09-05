from pybricks.hubs import EV3Brick
from pybricks.ev3devices import TouchSensor, Motor
from pybricks.parameters import Port

# Initialize the EV3 Brick and the Touch Sensor
ev3 = EV3Brick()
touch_sensor = TouchSensor(Port.S1)
motor = Motor(Port.A)

# Wait for the Touch Sensor to be pressed
while True:
    if touch_sensor.pressed():
        motor.run_angle(180, 90)  # Rotate the motor for example
        ev3.speaker.beep()  # Play a beep sound 
        break  # Exit the loop