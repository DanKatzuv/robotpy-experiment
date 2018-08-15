import ctre
import wpilib
from wpilib.command.subsystem import Subsystem

from commands.joystick_drive import JoystickDrive
from robot_map import drive


class Drive(Subsystem):
    def __init__(self):
        """Instantiates the motor object."""

        super().__init__('Drive')

        self.left_front = ctre.WPI_VictorSPX(drive['left_front'])
        self.left_back = ctre.WPI_VictorSPX(drive['left_back'])
        self.right_front = ctre.WPI_VictorSPX(drive['right_front'])
        self.right_back = ctre.WPI_VictorSPX(drive['right_back'])

        self.left = wpilib.SpeedControllerGroup(self.left_front, self.left_back)
        self.right = wpilib.SpeedControllerGroup(self.right_front, self.right_back)

    def initDefaultCommand(self):
        self.setDefaultCommand(JoystickDrive())

    def set(self, left, right):
        self.left.set(left)
        self.right.set(right)
