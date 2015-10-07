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

## Enable les moteurs
GPIO.output(MotorGE, GPIO.LOW)
GPIO.output(MotorDE, GPIO.LOW)

