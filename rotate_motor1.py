# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 14:54:50 2017

@author: Fujiichang
"""

import time
import RPi.GPIO as GPIO

time.sleep(1)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

gpio_pin1 = 19
gpio_pin2 = 21
pwm_pin1 = 23


# pwm用のピンは12と32
GPIO.setup(gpio_pin1, GPIO.OUT)
GPIO.setup(gpio_pin2, GPIO.OUT)
GPIO.setup(pwm_pin1, GPIO.OUT)


pwm1 = GPIO.PWM(pwm_pin1, 50)
pwm1.start(0)

print("start")
pwm1.ChangeDutyCycle(0)
GPIO.output(gpio_pin1, 1)
GPIO.output(gpio_pin2, 0)

print("change")
pwm1.ChangeDutyCycle(100)
time.sleep(3)


print("change")
pwm1.ChangeDutyCycle(30)
time.sleep(3)


print("change")
pwm1.ChangeDutyCycle(50)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin1, 0)
GPIO.output(gpio_pin2, 0)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin1, 1)
GPIO.output(gpio_pin2, 1)
time.sleep(1)

GPIO.output(gpio_pin1, 0)
GPIO.output(gpio_pin2, 0)
pwm1.stop()

GPIO.cleanup()
time.sleep(1)
