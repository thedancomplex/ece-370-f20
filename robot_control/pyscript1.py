from robot_control_class import RobotControl
import time as t
# import robot_control_class

rc = RobotControl()
# rc2 = robot_control_class.RobotControl()

a = rc.get_laser(360)

print("the dist measured = ", a)

i = 225
while True:
    d = rc.get_laser_full()
    for i in range(0,719):
        dd = d[i]
        print("i = ", i, " d = ", dd)
        t.sleep(0.1)
    i = i+1
    if( i > 719):
        i = 0
    
