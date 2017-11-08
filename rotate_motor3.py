# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:46:02 2017

@author: Fujiichang
"""

import time
import RPi.GPIO as GPIO

time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

gpio_pin5 = 29
gpio_pin6 = 31
pwm_pin3 = 33

GPIO.setup(gpio_pin5, GPIO.OUT)
GPIO.setup(gpio_pin6, GPIO.OUT)
GPIO.setup(pwm_pin3, GPIO.OUT)

pwm3 = GPIO.PWM(pwm_pin3, 50)
pwm3.start(0)

print("start")
pwm3.ChangeDutyCycle(0)
GPIO.output(gpio_pin5, 1)
GPIO.output(gpio_pin6, 0)

pwm3.ChangeDutyCycle(100)
time.sleep(3)


print("change")
pwm3.ChangeDutyCycle(30)
time.sleep(3)


print("change")
pwm3.ChangeDutyCycle(50)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin5, 0)
GPIO.output(gpio_pin6, 0)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin5, 1)
GPIO.output(gpio_pin6, 1)
time.sleep(1)

GPIO.output(gpio_pin5, 0)
GPIO.output(gpio_pin6, 0)
pwm3.stop()

GPIO.cleanup()
time.sleep(1)
