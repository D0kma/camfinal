#!/usr/bin/env python3

import rospy
import tty
import sys
import cv2
import numpy as np
import termios
from std_msgs.msg import String
from geometry_msgs.msg import Twist

def turtle_bot_teleop_letra():

	pub = rospy.Publisher('robot_lectura', String, queue_size=10) #declaramos la variable que publicará las velocidades
	rospy.init_node('turtle_bot_teleop_letra', anonymous=True)  #inicializamos el nodo
	rate = rospy.Rate(10) #definimos la frecuencia de actualización

	filedescriptors = termios.tcgetattr(sys.stdin) 
	tty.setcbreak(sys.stdin)
	
	menssage="Esperando color"
	X=str(input("Ingresa palabra a buscar: "))
	print(X)
	pub.publish(X)  
		

if __name__ == '__main__':
	try:

		turtle_bot_teleop_letra()
	except rospy.ROSInterruptException:
		pass
