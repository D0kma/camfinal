#!/usr/bin/env python3


from pynput import keyboard
# Librerías Nuevas
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String
import numpy as np
import pytesseract
import cv2
from PIL import Image
import sys

def callback(msg):
	print(msg)
def turtle_bot_listener_manipulador():
	rospy.init_node('turtle_bot_listener_manipulador', anonymous=True)
	rospy.Subscriber('arm_color', String, callback)
	rate = rospy.Rate(28)  # 10hz
	rospy.spin()         


# Ejecuta función turtle_bot
if __name__ == '__main__':
    try:
        turtle_bot_listener_manipulador()
    except rospy.ROSInterruptException:
        pass
