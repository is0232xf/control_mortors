# -*- coding: utf-8 -*-
"""
Created on Tue Jul 04 12:53:08 2017

@author: Fujiichang
"""

import time
import RPi.GPIO as GPIO


# モーターを2秒間回転させる
def rotate_motor(mortor_channel):
    print 'rotation'
    GPIO.output(mortor_channel[0], 1)
    GPIO.output(mortor_channel[1], 0)

    time.sleep(2)


# モーターの回転を止める
def break_rotation(mortor_channel):
    print 'break'
    GPIO.output(mortor_channel[0], 1)
    GPIO.output(mortor_channel[1], 1)
    time.sleep(1)


def cleanup_GPIO(mortor_channel):
    GPIO.output(mortor_channel[0], 0)
    GPIO.output(mortor_channel[1], 0)

    time.sleep(1)


if __name__ == "__main__":

    print 'start'

    # set up GPIO
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    # 1つ目のモーターのチャンネル設定
    out_channel1 = 16
    out_channel2 = 18
    # pwm_channel1 = 12
    mortor_channels1 = [out_channel1, out_channel2]

    # 2つ目のモーターのチャンネル設定
    out_channel3 = 24
    out_channel4 = 26
    pwm_channel2 = 22
    mortor_channels2 = [out_channel3, out_channel4]

    # 3つ目のモーターのチャンネル設定
    out_channel5 = 7
    out_channel6 = 11
    pwm_channel3 = 3
    mortor_channels3 = [out_channel5, out_channel6]

    # 4つ目のモーターのチャンネル設定
    out_channel7 = 33
    out_channel8 = 37
    pwm_channel4 = 12
    mortor_channels4 = [out_channel7, out_channel8]

    # 各ピンのGPIO設定
    GPIO.setup(mortor_channels1, GPIO.OUT)

    GPIO.setup(mortor_channels2, GPIO.OUT)

    GPIO.setup(mortor_channels3, GPIO.OUT)

    GPIO.setup(mortor_channels4, GPIO.OUT)

    # モータの回転と停止（制御部分）
    rotate_motor(mortor_channels1)
    rotate_motor(mortor_channels2)
    rotate_motor(mortor_channels3)
    rotate_motor(mortor_channels4)

    break_rotation(mortor_channels1)
    cleanup_GPIO(mortor_channels1)
    break_rotation(mortor_channels2)
    cleanup_GPIO(mortor_channels2)
    break_rotation(mortor_channels3)
    cleanup_GPIO(mortor_channels3)
    break_rotation(mortor_channels4)
    cleanup_GPIO(mortor_channels4)

    GPIO.cleanup()

    print 'finish'
