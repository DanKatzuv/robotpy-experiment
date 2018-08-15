from commandbased import CommandBasedRobot
# from commands import AutonomousCommandGroup
from wpilib.command import Command

from subsystems.drive import Drive


class MyRobot(CommandBasedRobot):
    def RobotInit(self):
        Command.getRobot = lambda x=0: self

        drive = Drive()
