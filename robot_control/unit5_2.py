from robot_control_class import RobotControl

class MoveRobot:
    def __init__(self, motion, clockwise, speed, time):
        self.rc = RobotControl()
        self.motion = motion 
        self.clockwise = clockwise
        self.speed = speed
        self.time = time
        self.time_turn = 7.0
    
    def move_straight(self):
        self.rc.move_straight_time(self.motion, self.speed, self.time)
    
    def turn(self):
        self.rc.turn(self.clockwise, self.speed, self.time_turn)

    def doSquare(self):
        i = 0
        while (i < 4):
            self.move_straight()
            self.turn()
            i = i + 1


t1 = MoveRobot('forward', 'clockwise', 0.3, 2)
t2 = MoveRobot('forward', 'clockwise', 0.3, 4)

print("T1 time")
t1.doSquare()
print("T2 time")
t2.doSquare()

#added a single space