#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

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

## Enable les moteurs
GPIO.output(MotorGE, GPIO.HIGH)
GPIO.output(MotorDE, GPIO.HIGH)

# Main
## Boucle infinie
while 1:
	if (GPIO.input(CapteurG) == False or GPIO.input(CapteurD) == False):
		GPIO.output(MotorDA, GPIO.LOW)
		GPIO.output(MotorDB, GPIO.LOW)
		GPIO.output(MotorGA, GPIO.LOW)
		GPIO.output(MotorGB, GPIO.LOW)
	else:
		GPIO.output(MotorDA, GPIO.LOW)
		GPIO.output(MotorDB, GPIO.HIGH)
		GPIO.output(MotorGA, GPIO.LOW)
		GPIO.output(MotorGB, GPIO.HIGH)
