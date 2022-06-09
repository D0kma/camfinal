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
	texto=''
	j=str(msg)
	j=j.replace('data: ','')
	j=j.replace('"','')
	while texto != j:

		#Abrir cámara    
		cap=cv2.VideoCapture(2)
		#Tomar imagen
		leido,frame=cap.read()
		if leido == True:
			cv2.imwrite("/home/juand/Proyecto/src/taller3_pkg/Resultados/foto.png",frame)
			print("Ya se tomo foto")
		else:
			print("No se tomo foto")
		#Liberar cámara
		cap.release()
		im="/home/juand/Proyecto/src/taller3_pkg/Resultados/foto.png"
		texto=str(((pytesseract.image_to_string(Image.open(im)))))
		print(len(texto))
		print(texto)
		print(j)
		
		if j in texto:
			texto=j
			print("Se encontro la palabra: ", j,"En la foto")
def robot_lectura_camara():

	rospy.init_node('robot_lectura_camara', anonymous=True)
	rospy.Subscriber('robot_lectura', String, callback)
	rate = rospy.Rate(28)  # 10hz
	rospy.spin()         


# Ejecuta función turtle_bot
if __name__ == '__main__':
    try:
        robot_lectura_camara()
    except rospy.ROSInterruptException:
        pass

