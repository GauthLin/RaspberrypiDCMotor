#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
from threading import Thread

GPIO.setmode(GPIO.BCM)

# Variables
## Moteur gauche
MotorGA = 23
MotorGB = 24
MotorGE = 4

## Moteur droit
MotorDA = 27
MotorDB = 22
MotorDE = 17

## Capteur gauche
CapteurG = 18

## Capteur droit
CapteurD = 25

## Encodeur
EncodeurD = 7
EncodeurG = 8

previousEncodeurG = 0
previousEncodeurD = 0
compteurEncodeurG = 0 
compteurEncodeurD = 0

# Configuration des GPIOs
## Moteur gauche
GPIO.setup(MotorGA, GPIO.OUT)
GPIO.setup(MotorGB, GPIO.OUT)
GPIO.setup(MotorGE, GPIO.OUT)

## Moteur droit
GPIO.setup(MotorDA, GPIO.OUT)
GPIO.setup(MotorDB, GPIO.OUT)
GPIO.setup(MotorDE, GPIO.OUT)

## Capteurs
GPIO.setup(CapteurD, GPIO.IN)
GPIO.setup(CapteurG, GPIO.IN)

## Encoder
GPIO.setup(EncodeurD, GPIO.IN)
GPIO.setup(EncodeurG, GPIO.IN)

## Enable les moteurs
GPIO.output(MotorGE, GPIO.HIGH)
GPIO.output(MotorDE, GPIO.HIGH)

# Definitions de fonction
def forward():
        GPIO.output(MotorDA, GPIO.HIGH)
        GPIO.output(MotorDB, GPIO.LOW)
        GPIO.output(MotorGA, GPIO.HIGH)
        GPIO.output(MotorGB, GPIO.LOW)

def stopMotor():
        GPIO.output(MotorDA, GPIO.LOW)
        GPIO.output(MotorDB, GPIO.LOW)
        GPIO.output(MotorGA, GPIO.LOW)
        GPIO.output(MotorGB, GPIO.LOW)

def backward():
        GPIO.output(MotorDA, GPIO.LOW)
        GPIO.output(MotorDB, GPIO.HIGH)
        GPIO.output(MotorGA, GPIO.LOW)
        GPIO.output(MotorGB, GPIO.HIGH)
	
def turnLeft():
	GPIO.output(MotorDA, GPIO.HIGH)
        GPIO.output(MotorDB, GPIO.LOW)
        GPIO.output(MotorGA, GPIO.HIGH)
        GPIO.output(MotorGB, GPIO.HIGH)

def turnRight():
	GPIO.output(MotorDA, GPIO.LOW)
        GPIO.output(MotorDB, GPIO.LOW)
        GPIO.output(MotorGA, GPIO.HIGH)
        GPIO.output(MotorGB, GPIO.LOW)

def updateCodeurs():
	global previousEncodeurG, previousEncodeurD, compteurEncodeurG, compteurEncodeurD
	
	outputEncodeurG = GPIO.input(EncodeurG)
	outputEncodeurD = GPIO.input(EncodeurD)

	if (previousEncodeurG != outputEncodeurG):
		compteurEncodeurG = compteurEncodeurG + 1
		previousEncodeurG = outputEncodeurG

	if (previousEncodeurD != outputEncodeurD):
		compteurEncodeurD = compteurEncodeurD + 1
		previousEncodeurD = outputEncodeurD

class EncodersThread(Thread):
	def __init__(self):
		Thread.__init__(self)

	def run(self):
		 while True:
 			updateCodeurs()
			sleep(0.001)

# Main
## Boucle infinie
if __name__ == '__main__':
	try:
        	myThread = EncodersThread()
		myThread.start()

	        while 1:
			if: (compteurEncodeurD < compteurEncodeurG):
				turnLeft()
			elif (compteurEncodeurD > compteurEncodeurG):
				turnRight()
			else:
				forward()
	except KeyboardInterrupt:
		stopMotor()
