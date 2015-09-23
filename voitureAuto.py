#!usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

# Variables

Motor1A = 23
Motor1B = 24
Motor1E = 4

Motor2A = 27
Motor2B = 22
Motor2E = 17

Capteur1 = 

# Configuration des GPIOs
GPIO.setup(Motor1A, GPIO.OUT)
GPIO.setup(Motor1B, GPIO.OUT)
GPIO.setup(Motor1E, GPIO.OUT)

GPIO.setup(Motor2A, GPIO.OUT)
GPIO.setup(Motor2B, GPIO.OUT)
GPIO.setup(Motor2E, GPIO.OUT)
