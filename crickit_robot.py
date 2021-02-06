# making class and functions for 2 continuous rotation servos with crickit
# beth@carrigandesigns.com
# crickit_robot.py
# left is motor1 and right is motor2

import time
import atexit
from adafruit_crickit import crickit

print("2 cont servos functions")


class Robot:
    def __init__(self, left_trim=0, right_trim=0, stop_at_exit=True):
        """Create an instance of the robot. Can specify these optional parameters:
        - left_trim/right_trim: amount to offset the speed of the left/right motor,
          can be positive or negative and useful for matching the speed of the motors.
          Default is 0.
        - stop_at_exit: Boolean to indicate if motors should stop on program exit.
          Default is True. Reccomended to prevent damage to robot on program crash.
        """

        self._left_trim = left_trim
        self._right_trim = right_trim
        if stop_at_exit:
            atexit.register(self.stop)

    def _left_speed(self, speed):
        print("left speed ", speed)
        assert -1 <= speed <= 1, "left Speed must be a value between -1 to 1 inclusive!"
        speed += self._left_trim
        speed = max(-1, min(1, speed)) #constrain speed to 0-255 after trimming
        print("left throttle ", speed)
        crickit.continuous_servo_2.throttle = speed

    def _right_speed(self, speed):
        speed = -1 * speed
        print("right speed ", speed)
        assert -1 <= speed <= 1, "right Speed must be a value between -1 to 1 inclusive!"
        speed += self._right_trim
        speed = max(-1, min(1, speed))
        print("right throttle ", speed)
        crickit.continuous_servo_1.throttle = speed

    @staticmethod
    def stop():
        print("called stop")
        crickit.continuous_servo_2.throttle = 0
        crickit.continuous_servo_1.throttle = 0

    def forward(self, speed, seconds=None):
        """move forward at the specified speed (0-255). will start moving forward and
        return unless a seconds value is specified, in which case the robot will move
        forward for that amount of time and then stop
        """
        self._left_speed(speed)
        self._right_speed(speed)
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def steer(self, speed, direction):
        """move forward at the specified speed (0 - 1). direction is +- 1.
        full left is -1, full right is +1
        """
        if (speed + direction / 2) > 1:
            speed = (speed - direction / 2) #calibrate so total motor output never goes above 1
        left = speed + direction / 2
        right = speed - direction / 2
        self._left_speed(left)
        self._right_speed(right)

    def backward(self, speed, seconds=None):
        self._left_speed(-1 * speed)
        self._right_speed(-1 * speed)
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def right(self, speed, seconds=None):
        """spin to the right at the specified speed. will start spinning and return unless a seconds
        value is specified, in which case the robot will spin for that amount of time and then stop.
        """
        self._left_speed(speed)
        self._right_speed(0)
        if seconds is not None:
            time.sleep(seconds)
            self.stop()

    def left(self, speed, seconds=None):
        self._left_speed(0)
        self._right_speed(speed)
        if seconds is not None:
            time.sleep(seconds)
            self.stop()


