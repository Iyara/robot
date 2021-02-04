# move the robot around
# beth@carrigandesigns

import time
import crickit_robot
from adafruit_crickit import crickit

LEFT_TRIM = 0
RIGHT_TRIM = 0

robot = crickit_robot.Robot(left_trim=LEFT_TRIM, right_trim=RIGHT_TRIM)
#crickit.continuous_servo_1.set_pulse_width_range(min_pulse=1000, max_pulse=2000)
#crickit.continuous_servo_2.set_pulse_width_range(min_pulse=1000, max_pulse=2000)

robot.forward(1, 3)
robot.left(0.5, 1)
robot.right(0.5, 0.2)
time.sleep(3)
print("stop")
robot.stop()

"""
print("now testing for trim")
print("fwd 0.1")
robot.forward(0.1, 3)
print("zero")
robot.stop()
print("fwd -0.1")
robot.forward(-0.1, 3)
print("sleep 3")
time.sleep(3)
"""

