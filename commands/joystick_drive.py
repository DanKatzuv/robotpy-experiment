from wpilib.command import Command


class JoystickDrive(Command):
    """Command for driving the robot with joysticks."""

    def __init__(self):
        super().__init__('Joystick Drive')
        self.requires(self.get_robot().drive)

    def execute(self):
        left_value = self.get_robot().left.getY()
        right_value = self.get_robot().right.getY()
        self.get_robot().drive.set(left_value, right_value)
