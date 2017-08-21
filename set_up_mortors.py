# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:15:08 2017

@author: Fujiichang
"""

import RPi.GPIO as GPIO


def set_up():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    gpio_pin1 = 19
    gpio_pin2 = 21
    pwm_pin1 = 23

    gpio_pin3 = 11
    gpio_pin4 = 13
    pwm_pin2 = 15

    gpio_pin5 = 8
    gpio_pin6 = 10
    pwm_pin3 = 12

    gpio_pin7 = 22
    gpio_pin8 = 24
    pwm_pin4 = 26

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
