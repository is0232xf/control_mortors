# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 12:53:08 2017

@author: Fujiichang
"""

import time
import RPi.GPIO as GPIO


# モーターを2秒間回転させる
def rotate_motor(mortor_channel, pwm):
    pwm.start(0)
    print 'rotation'
    pwm.ChangeDutyCycle(0)
    GPIO.output(mortor_channel[0], 1)
    GPIO.output(mortor_channel[1], 0)

    print 'Duty Cycle is 30'
    pwm.ChangeDutyCycle(30)
    time.sleep(2)


# モーターの回転を止める
def break_rotation(mortor_channel):
    print 'break'
    GPIO.output(mortor_channel[0], 1)
    GPIO.output(mortor_channel[1], 1)
    time.sleep(1)


# GPIOの設定をリセットする
def cleanup_GPIO(mortor_channel, pwm):
    GPIO.output(mortor_channel[0], 0)
    GPIO.output(mortor_channel[1], 0)
    pwm.stop()

    GPIO.cleanup()
    time.sleep(1)
    print 'finish'

if __name__ == "__main__":

    print 'start'

    # set up GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # 1つ目のモーターのチャンネル設定
    out_channel1 = 16
    out_channel2 = 18
    pwm_channel1 = 12
    mortor_channels1 = [out_channel1, out_channel2, pwm_channel1]

    GPIO.setup(mortor_channels1, GPIO.OUT)
    pwm1 = GPIO.PWM(mortor_channels1[2], 50)

    rotate_motor(mortor_channels1, pwm1)
    break_rotation(mortor_channels1, pwm1)
    cleanup_GPIO(mortor_channels1, pwm1)
