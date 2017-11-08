# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 15:16:00 2017

@author: Fujiichang
"""

import time
import RPi.GPIO as GPIO

time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

gpio_pin5 = 11
gpio_pin6 = 13
pwm_pin3 = 15
gpio_pin7 = 22
gpio_pin8 = 24
pwm_pin4 = 26


GPIO.setup(gpio_pin5, GPIO.OUT)
GPIO.setup(gpio_pin6, GPIO.OUT)
GPIO.setup(pwm_pin3, GPIO.OUT)
GPIO.setup(gpio_pin7, GPIO.OUT)
GPIO.setup(gpio_pin8, GPIO.OUT)
GPIO.setup(pwm_pin4, GPIO.OUT)


pwm3 = GPIO.PWM(pwm_pin3, 50)
pwm3.start(0)
pwm4 = GPIO.PWM(pwm_pin4, 50)
pwm4.start(0)

pwm3.ChangeDutyCycle(0)
GPIO.output(gpio_pin5, 1)
GPIO.output(gpio_pin6, 0)
pwm4.ChangeDutyCycle(0)
GPIO.output(gpio_pin7, 1)
GPIO.output(gpio_pin8, 0)

print("change")
pwm3.ChangeDutyCycle(100)
pwm4.ChangeDutyCycle(100)
time.sleep(10)

print("stop")
pwm3.stop()
pwm4.stop()
GPIO.output(gpio_pin7, 0)
GPIO.output(gpio_pin8, 0)
GPIO.output(gpio_pin7, 0)
GPIO.output(gpio_pin8, 0)
time.sleep(1)

GPIO.cleanup()
time.sleep(1)
