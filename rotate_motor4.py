# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:58:34 2017

@author: Fujiichang
"""

import time
import RPi.GPIO as GPIO

time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

gpio_pin7 = 22
gpio_pin8 = 24
pwm_pin4 = 26

# pwm用のピンは12と32

GPIO.setup(gpio_pin7, GPIO.OUT)
GPIO.setup(gpio_pin8, GPIO.OUT)
GPIO.setup(pwm_pin4, GPIO.OUT)


pwm4 = GPIO.PWM(pwm_pin4, 50)
pwm4.start(0)

pwm4.ChangeDutyCycle(0)
GPIO.output(gpio_pin7, 1)
GPIO.output(gpio_pin8, 0)

print("change")
pwm4.ChangeDutyCycle(100)
time.sleep(3)


print("change")
pwm4.ChangeDutyCycle(30)
time.sleep(3)


print("change")
pwm4.ChangeDutyCycle(50)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin7, 0)
GPIO.output(gpio_pin8, 0)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin7, 1)
GPIO.output(gpio_pin8, 1)
time.sleep(1)


GPIO.output(gpio_pin7, 0)
GPIO.output(gpio_pin8, 0)

pwm4.stop()

GPIO.cleanup()
time.sleep(1)
