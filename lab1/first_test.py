# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 01:26:59 2024

@author: Erica
"""

import robot


robot.init()
## 1: the initial position of 3 boxes, red, green, blue
## 2: the position of the robot

"""
First want to swap red to green and green to red we need:
    Assume the robot started at position 0, and the gripper is closed
    Open gripper
    Close gripper to pick the red box
    lift red up
    Drive to one right 
    lift red down
    Open gripper
    Drive to one right to green
    Close gripper to pick the green box
    lift green up
    Drive to two left
    lift green down
    Open gripper
    Drive to one right to red
    Close gripper to pick the red box
    lift red up
    Drive to one right 
    lift red down
    Open gripper
"""
"""
def swap_left_and_middle():
    robot.gripper_to_open()
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_open()
    robot.drive_right()
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_left()
    robot.drive_left()
    robot.lift_down()
    robot.gripper_to_open()
    robot.drive_right()
    robot.gripper_to_closed()
    robot.lift_up()
    robot.drive_right()
    robot.lift_down()
    robot.gripper_to_open()
    
    
swap_left_and_middle
"""


robot.lift_up()
robot.gripper_to_folded()

