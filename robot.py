import wpilib
from commandbased import CommandBasedRobot
from wpilib.command import Command

import oi
from subsystems.drive import Drive


class MyRobot(CommandBasedRobot):
    def RobotInit(self):
        Command.get_robot = lambda x=0: self

        self.drive = Drive()

        self.left, right = oi.get_joysticks()


if __name__ == '__main__':
    wpilib.run(MyRobot)
