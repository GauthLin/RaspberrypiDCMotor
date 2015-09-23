import RPi.GPIO as GPIO
import time

def blink(pin, n=50):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        for i in xrange(n):
                GPIO.output(pin, GPIO.HIGH)
                time.sleep(1)
                GPIO.output(pin, GPIO.LOW)
                time.sleep(1)

if __name__ == "__main__":
        blink(4)
