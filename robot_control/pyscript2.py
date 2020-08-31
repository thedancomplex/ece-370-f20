from robot_control_class import RobotControl
import time as t

rc = RobotControl()

# Now we are ready to go

# Robot starts stopped
rc.stop_robot()

while True:
  d = rc.get_laser(360)
  # Is there a wall < 1m from the robot
  if(d < 1.0):
    # Stop Robot
    rc.stop_robot()
  else:
    # Move forward
    rc.move_straight()
  print("dist = ", d)

