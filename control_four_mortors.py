# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 12:53:08 2017

@author: Fujiichang
"""

import time
import RPi.GPIO as GPIO


def rotate_motor(mortor_channel):
    pwm = GPIO.PWM(mortor_channel[2], 50)
    pwm.start(0)

    print 'rotation'
    pwm.ChangeDutyCycle(0)
    GPIO.output(mortor_channel[0], 1)
    GPIO.output(mortor_channel[1], 0)

    print 'Duty Cycle is 30'
    pwm.ChangeDutyCycle(30)
    time.sleep(2)


if __name__ == "__main__":

    print 'start'

    # set up GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    out_channel1 = 16
    out_channel2 = 18
    pwm_channel1 = 12

    mortor_channels1 = [out_channel1, out_channel2, pwm_channel1]

    GPIO.setup(mortor_channels1, GPIO.OUT)
