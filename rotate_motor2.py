# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:51:21 2017

@author: Fujiichang
"""

import time
import RPi.GPIO as GPIO

time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)


gpio_pin3 = 11
gpio_pin4 = 13
pwm_pin2 = 15

GPIO.setup(gpio_pin3, GPIO.OUT)
GPIO.setup(gpio_pin4, GPIO.OUT)
GPIO.setup(pwm_pin2, GPIO.OUT)

pwm2 = GPIO.PWM(pwm_pin2, 50)
pwm2.start(0)

print("start")
pwm2.ChangeDutyCycle(0)
GPIO.output(gpio_pin3, 1)
GPIO.output(gpio_pin4, 0)
time.sleep(3)

print("change")
pwm2.ChangeDutyCycle(100)
time.sleep(3)


print("change")
pwm2.ChangeDutyCycle(30)
time.sleep(3)


print("change")
pwm2.ChangeDutyCycle(50)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin3,  0)
GPIO.output(gpio_pin4, 0)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin3, 1)
GPIO.output(gpio_pin4, 1)
time.sleep(1)

GPIO.output(gpio_pin3, 0)
GPIO.output(gpio_pin4, 0)
pwm2.stop()

GPIO.cleanup()
time.sleep(1)
