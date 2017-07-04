# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 12:09:18 2017

@author: Fujiichang
"""

if __name__ == "__main__":

import time
import RPi.GPIO as GPIO

time.sleep(2)

print 'start'

# set up GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

GPIO.setup(16,  GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)

pwmR = GPIO.PWM(12, 50)
pwmR.start(0)

print 'rotation'
pwmR.ChangeDutyCycle(0)
GPIO.output(16,  1)
GPIO.output(18, 0)

print ' 30'
pwmR.ChangeDutyCycle(30)
time.sleep(2)
print ' 60'
pwmR.ChangeDutyCycle(60)
time.sleep(2)
print ' 100'
pwmR.ChangeDutyCycle(100)
time.sleep(2)

print 'stop'
GPIO.output(16,  0)
GPIO.output(18, 0)
time.sleep(2)

print 'reverse'
pwmR.ChangeDutyCycle(0)
GPIO.output(16,  0)
GPIO.output(18, 1)

print ' 30'
pwmR.ChangeDutyCycle(30)
time.sleep(2)
print ' 60'
pwmR.ChangeDutyCycle(60)
time.sleep(2)
print ' 100'
pwmR.ChangeDutyCycle(100)
time.sleep(2)

print 'break'
GPIO.output(16, 1)
GPIO.output(18, 1)
time.sleep(1)

# GPIO post-processing
GPIO.output(16, 0)
GPIO.output(18, 0)
pwmR.stop()

GPIO.cleanup()
time.sleep(1)

print 'finish'
