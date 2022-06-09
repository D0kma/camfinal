#!/usr/bin/env python3

import rospy
import tty
import sys
import cv2
import numpy as np
import termios
from std_msgs.msg import String
from geometry_msgs.msg import Twist
def callback(msg):
	pub = rospy.Publisher('arm_color', String, queue_size=10) #declaramos la variable que publicará las velocidades
	X=str(msg)
	X=X.replace('data: ','')
	X=X.replace('"','')
	cap = cv2.VideoCapture(0)
	#Azul
	azBa = np.array([50,103,138],np.uint8)
	azAl = np.array([100,255,255],np.uint8)
	#amarillo
	amBa = np.array([15,179,160],np.uint8)
	amAl = np.array([45,255,255],np.uint8)
	#rojo 
	reBa1 = np.array([0,100,20],np.uint8)
	reAl1 = np.array([5,255,255],np.uint8)
	reBa2 = np.array([175,100,20],np.uint8)
	reAl2 = np.array([179,255,255],np.uint8)

	#Abrir cámara    
	cap=cv2.VideoCapture(2)
	#Tomar imagen
	ret,frame=cap.read()
	if ret== True:
		cv2.imwrite("/home/juand/Proyecto/src/taller3_pkg/Resultados/foto2.png",frame)
		print("Ya se tomo foto")
	else:
		print("No se tomo foto")
	
	cap.release()
	if X=="blue":
		im=cv2.imread("/home/juand/Proyecto/src/taller3_pkg/Resultados/foto2.png")
		if ret==True:
			frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
			mask = cv2.inRange(frameHSV,azBa,azAl)
			contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			x=0
			y=0
			for c in contornos:
				area = cv2.contourArea(c)
				if area > 3000:
					M = cv2.moments(c)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					cv2.circle(frame, (x,y), 7, (0,255,0), -1)
					font = cv2.FONT_HERSHEY_SIMPLEX
					cv2.putText(im, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
					nuevoContorno = cv2.convexHull(c)
					cv2.drawContours(im, [nuevoContorno], 0, (255,0,0), 3)
			cv2.imwrite("/home/juand/Proyecto/src/taller3_pkg/Resultados/foto3.png",im)
			if x != 0:
				print(x)
				print(y)
				x_real=((x*0.16)/600)-0.08
				y_real=((y*0.11)/465)-0.07
				message=str(x_real)+str(y_real)
				print(message)
				pub.publish(message)
				
			else:
				print("No se encontro color")
		
	if X=="yellow":
		im=cv2.imread("/home/juand/Proyecto/src/taller3_pkg/Resultados/foto2.png")
		if ret==True:
			frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
			mask = cv2.inRange(frameHSV,amBa,amAl)
			contornos,_ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			x=0
			y=0
			for c in contornos:
				area = cv2.contourArea(c)
				if area > 3000:
					M = cv2.moments(c)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					cv2.circle(frame, (x,y), 7, (0,255,0), -1)
					font = cv2.FONT_HERSHEY_SIMPLEX
					cv2.putText(im, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
					nuevoContorno = cv2.convexHull(c)
					cv2.drawContours(im, [nuevoContorno], 0, (255,0,0), 3)
			cv2.imwrite("/home/juand/Proyecto/src/taller3_pkg/Resultados/foto3.png",im)
			if x != 0:
				print(x)
				print(y)
				x_real=((x*0.16)/600)-0.08
				y_real=((y*0.11)/465)-0.07
				message=str(x_real)+str(y_real)
				print(message)
				pub.publish(message)
				
			else:
				print("No se encontro color")
			
		
	if X=="red":	
		im=cv2.imread("/home/juand/Proyecto/src/taller3_pkg/Resultados/foto2.png")
		if ret==True:
			frameHSV = cv2.cvtColor(im,cv2.COLOR_BGR2HSV)
			maskRed1 = cv2.inRange(frameHSV, reBa1, reAl1)
			maskRed2 = cv2.inRange(frameHSV, reBa2, reAl2)
			maskRed = cv2.add(maskRed1, maskRed2)
			contornos,_ = cv2.findContours(maskRed, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
			x=0
			y=0
			for c in contornos:
				area = cv2.contourArea(c)
				if area > 3000:
					M = cv2.moments(c)
					if (M["m00"]==0): M["m00"]=1
					x = int(M["m10"]/M["m00"])
					y = int(M['m01']/M['m00'])
					cv2.circle(frame, (x,y), 7, (0,255,0), -1)
					font = cv2.FONT_HERSHEY_SIMPLEX
					cv2.putText(im, '{},{}'.format(x,y),(x+10,y), font, 0.75,(0,255,0),1,cv2.LINE_AA)
					nuevoContorno = cv2.convexHull(c)
					cv2.drawContours(im, [nuevoContorno], 0, (255,0,0), 3)
			cv2.imwrite("/home/juand/Proyecto/src/taller3_pkg/Resultados/foto3.png",im)
			
			if x != 0:
				print(x)
				print(y)
				x_real=((x*0.16)/600)-0.08
				y_real=((y*0.11)/465)-0.07
				message=str(x_real)+str(y_real)
				print(message)
				pub.publish(message)
				
			else:
				print("No se encontro color")
def robot_manipulador_camara():
	
	rospy.init_node('robot_manipulador_camara', anonymous=True)  #inicializamos el nodo
	rospy.Subscriber('robot_manipulador', String, callback)
	rate = rospy.Rate(28)  # 10hz
	rospy.spin()         


# Ejecuta función turtle_bot
if __name__ == '__main__':
    try:
        robot_manipulador_camara()
    except rospy.ROSInterruptException:
        pass

