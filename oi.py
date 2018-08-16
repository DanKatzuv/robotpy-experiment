from wpilib import Joystick


def get_joysticks():
    left = Joystick(0)
    right = Joystick(1)
    return left, right
