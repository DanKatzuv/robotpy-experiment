from wpilib.command import Command


class JoystickDrive(Command):
    """Command for driving the robot with joysticks."""

    def __init__(self):
        super().__init__('Joystick Drive')
        self.requires(self.getRobot())
