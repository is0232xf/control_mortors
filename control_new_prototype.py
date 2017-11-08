# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 13:44:34 2017

@author: Fujiichang
"""

# import module
import sys
import RPi.GPIO as GPIO
from time import sleep  # time module

if __name__ == "__main__":

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # モータ1
    gpio_pin1 = 19
    gpio_pin2 = 21
    pwm_pin1 = 23

    # モータ2
    gpio_pin3 = 11
    gpio_pin4 = 13
    pwm_pin2 = 15

    # モータ3
    gpio_pin5 = 29
    gpio_pin6 = 31
    pwm_pin3 = 33

    # モータ4
    gpio_pin7 = 22
    gpio_pin8 = 24
    pwm_pin4 = 26

    pwm_value1 = 0
    pwm_value2 = 0
    pwm_value3 = 0
    pwm_value4 = 0
    case = sys.argv

    # モータピンのセットアップ
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

    if case[1] == '0':
        pwm_value1 = 0
        pwm_value2 = 100
        pwm_value3 = 0
        pwm_value4 = 100
    elif case[1] == '30':
        pwm_value1 = 100
        pwm_value2 = 0
        pwm_value3 = 0
        pwm_value4 = 50
    elif case[1] == '45':
        pwm_value1 = 100
        pwm_value2 = 0
        pwm_value3 = 100
        pwm_value4 = 0
    elif case[1] == '60':
        pwm_value1 = 100
        pwm_value2 = 50
        pwm_value3 = 0
        pwm_value4 = 0
    elif case[1] == '90':
        pwm_value1 = 100
        pwm_value2 = 100
        pwm_value3 = 0
        GPIO.output(gpio_pin5, 0)
        GPIO.output(gpio_pin6, 0)
        pwm_value4 = 0

    print("change angle: " + case[1])
    pwm1.ChangeDutyCycle(pwm_value1)
    pwm2.ChangeDutyCycle(pwm_value2)
    pwm3.ChangeDutyCycle(pwm_value3)
    pwm4.ChangeDutyCycle(pwm_value4)
    sleep(5)

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
    print("stop")
