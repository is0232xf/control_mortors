# -*- coding: utf-8 -*-
"""
Created on Wed Aug 09 16:48:56 2017

@author: Fujiichang
"""

import time
import RPi.GPIO as GPIO

time.sleep(3)

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)

gpio_pin1 = 11
gpio_pin2 = 13
pwm_pin1 = 15

gpio_pin3 = 19
gpio_pin4 = 21
pwm_pin2 = 23

gpio_pin5 = 8
gpio_pin6 = 10
pwm_pin3 = 12

gpio_pin7 = 22
gpio_pin8 = 24
pwm_pin4 = 26

# pwm用のピンは12と32
GPIO.setup(gpio_pin1, GPIO.OUT)
GPIO.setup(gpio_pin2, GPIO.OUT)
GPIO.setup(pwm_pin1, GPIO.OUT)

GPIO.setup(gpio_pin3, GPIO.OUT)
GPIO.setup(gpio_pin4, GPIO.OUT)
GPIO.setup(pwm_pin2, GPIO.OUT)

GPIO.setup(gpio_pin5, GPIO.OUT)
GPIO.setup(gpio_pin6, GPIO.OUT)
GPIO.setup(pwm_pin3, GPIO.OUT)

GPIO.setup(gpio_pin7, GPIO.OUT)
GPIO.setup(gpio_pin8, GPIO.OUT)
GPIO.setup(pwm_pin4, GPIO.OUT)


pwm1 = GPIO.PWM(pwm_pin1, 50)
pwm1.start(0)
pwm2 = GPIO.PWM(pwm_pin2, 50)
pwm2.start(0)
pwm3 = GPIO.PWM(pwm_pin3, 50)
pwm3.start(0)
pwm4 = GPIO.PWM(pwm_pin4, 50)
pwm4.start(0)

print("start")
pwm1.ChangeDutyCycle(0)
GPIO.output(gpio_pin1, 1)
GPIO.output(gpio_pin2, 0)
pwm2.ChangeDutyCycle(0)
GPIO.output(gpio_pin3, 1)
GPIO.output(gpio_pin4, 0)
pwm3.ChangeDutyCycle(0)
GPIO.output(gpio_pin5, 1)
GPIO.output(gpio_pin6, 0)
pwm4.ChangeDutyCycle(0)
GPIO.output(gpio_pin7, 1)
GPIO.output(gpio_pin8, 0)

print("change")
pwm1.ChangeDutyCycle(100)
pwm2.ChangeDutyCycle(100)
pwm3.ChangeDutyCycle(100)
pwm4.ChangeDutyCycle(100)
time.sleep(3)


print("change")
pwm1.ChangeDutyCycle(30)
pwm2.ChangeDutyCycle(30)
pwm3.ChangeDutyCycle(30)
pwm4.ChangeDutyCycle(30)
time.sleep(3)


print("change")
pwm1.ChangeDutyCycle(50)
pwm2.ChangeDutyCycle(50)
pwm3.ChangeDutyCycle(50)
pwm4.ChangeDutyCycle(50)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin1, 0)
GPIO.output(gpio_pin2, 0)
GPIO.output(gpio_pin3,  0)
GPIO.output(gpio_pin4, 0)
GPIO.output(gpio_pin5, 0)
GPIO.output(gpio_pin6, 0)
GPIO.output(gpio_pin7,  0)
GPIO.output(gpio_pin8, 0)
time.sleep(3)

print("restart")
pwm1.ChangeDutyCycle(0)
GPIO.output(gpio_pin1, 0)
GPIO.output(gpio_pin2, 1)
pwm2.ChangeDutyCycle(0)
GPIO.output(gpio_pin3,  0)
GPIO.output(gpio_pin4, 1)
pwm3.ChangeDutyCycle(0)
GPIO.output(gpio_pin5, 0)
GPIO.output(gpio_pin6, 1)
pwm4.ChangeDutyCycle(0)
GPIO.output(gpio_pin7,  0)
GPIO.output(gpio_pin8, 1)

pwm1.ChangeDutyCycle(100)
pwm2.ChangeDutyCycle(100)
pwm3.ChangeDutyCycle(100)
pwm4.ChangeDutyCycle(100)
time.sleep(3)

print("stop")
GPIO.output(gpio_pin1, 1)
GPIO.output(gpio_pin2, 1)
GPIO.output(gpio_pin3, 1)
GPIO.output(gpio_pin4, 1)
GPIO.output(gpio_pin5, 1)
GPIO.output(gpio_pin6, 1)
GPIO.output(gpio_pin7, 1)
GPIO.output(gpio_pin8, 1)
time.sleep(3)

GPIO.output(gpio_pin1, 0)
GPIO.output(gpio_pin2, 0)
GPIO.output(gpio_pin3, 0)
GPIO.output(gpio_pin4, 0)
GPIO.output(gpio_pin5, 0)
GPIO.output(gpio_pin6, 0)
GPIO.output(gpio_pin7, 0)
GPIO.output(gpio_pin8, 0)
pwm1.stop()
pwm2.stop()
pwm3.stop()
pwm4.stop()

GPIO.cleanup()
time.sleep(1)
