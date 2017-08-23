# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:18:23 2017

@author: Fujiichang
"""

# import module
import os
import smbus            # use I2C
import csv
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from time import sleep  # time module
import datetime

#
# define
#
# slave address
DEV_ADDR = 0x68         # device address
# register address
ACCEL_XOUT = 0x3b
ACCEL_YOUT = 0x3d
ACCEL_ZOUT = 0x3f
TEMP_OUT = 0x41
GYRO_XOUT = 0x43
GYRO_YOUT = 0x45
GYRO_ZOUT = 0x47
PWR_MGMT_1 = 0x6b       # PWR_MGMT_1
PWR_MGMT_2 = 0x6c       # PWR_MGMT_2

bus = smbus.SMBus(1)
# Sleepè§£é¤.
bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)

#
# Sub function
#
# 1byte read

"""
def setup_gpio(gpio_pin1, gpio_pin2, pwm_pin):
    GPIO.setup(gpio_pin1, GPIO.OUT)
    GPIO.setup(gpio_pin2, GPIO.OUT)
    GPIO.setup(pwm_pin, GPIO.OUT)


def rotate_mortor(gpio_pin1, gpio_pin2, pwm_pin):
    pwm = GPIO.PWM(pwm_pin, 50)
    pwm.start(0)
    pwm.ChangeDutyCycle(0)
    GPIO.output(gpio_pin1, 1)
    GPIO.output(gpio_pin2, 0)
    pwm.ChangeDutyCycle(100)


def stop_mortor(gpio_pin1, gpio_pin2, pwm_pin):
    GPIO.output(gpio_pin1, 0)
    GPIO.output(gpio_pin2, 0)
    pwm_pin.stop()
    GPIO.cleanup()
    pwm = GPIO.PWM(pwm_pin, 0)
    pwm.stop()
"""


def read_byte(adr):
    return bus.read_byte_data(DEV_ADDR, adr)


# 2byte read
def read_word(adr):
    high = bus.read_byte_data(DEV_ADDR, adr)
    low = bus.read_byte_data(DEV_ADDR, adr+1)
    val = (high << 8) + low
    return val


# Sensor data read
def read_word_sensor(adr):
    val = read_word(adr)
    if (val >= 0x8000):         # minus
        return -((65535 - val) + 1)
    else:                       # plus
        return val


#
# æ¸©åº¦
#
def get_temp():
    temp = read_word_sensor(TEMP_OUT)
    x = temp / 340 + 36.53      # data sheet(register map)è¨è¼ãEè¨ç®å¼E
    return x

#
# è§éåº¦(full scale range Â±250 deg/s
#        LSB sensitivity 131 LSB/deg/s
#        -> Â±250 x 131 = Â±32750 LSB[16bitã§è¡¨ç¾])
#   Gyroscope Configuration GYRO_CONFIG (reg=0x1B)
#   FS_SEL(Bit4-Bit3)ã§full scale range/LSB sensitivityã®å¤æ´å¯.
#
# get gyro data


def get_gyro_data_lsb():
    x = read_word_sensor(GYRO_XOUT)
    y = read_word_sensor(GYRO_YOUT)
    z = read_word_sensor(GYRO_ZOUT)
    return [x, y, z]


def get_gyro_data_deg():
    x, y, z = get_gyro_data_lsb()
    x = x / 131.0
    y = y / 131.0
    z = z / 131.0
    return [x, y, z]

#
# å éåº¦(full scale range Â±2g
#        LSB sensitivity 16384 LSB/g)
#        -> Â±2 x 16384 = Â±32768 LSB[16bitã§è¡¨ç¾])
#   Accelerometer Configuration ACCEL_CONFIG (reg=0x1C)
#   AFS_SEL(Bit4-Bit3)ã§full scale range/LSB sensitivityã®å¤æ´å¯.
#
# get accel data


def get_accel_data_lsb():
    x = read_word_sensor(ACCEL_XOUT)
    y = read_word_sensor(ACCEL_YOUT)
    z = read_word_sensor(ACCEL_ZOUT)
    return [x, y, z]
# get accel data


def get_accel_data_g():
    x, y, z = get_accel_data_lsb()
    x = x / 16384.0
    y = y / 16384.0
    z = z / 16384.0
    return [x, y, z]


def save_gyro_data(gx_data, gy_data, gz_data):
    plt.xlabel("time")
    plt.ylabel("deg/s")
    plt.ylim(-200, 200)
    plt.plot(range(len(gx_data)), gx_data, "-", color="blue")
    plt.plot(range(len(gy_data)), gy_data,  "-", color="red")
    plt.plot(range(len(gz_data)), gz_data,  "-", color="green")
    # plt.show()
    plt.savefig("gyro_data.png")
    os.rename("gyro_data.png", "{0:%Y%m%d_%H%M%S}gyro_data.png".format(d))


def save_acceleration_data(ax_data, ay_data, az_data):
    plt.xlabel("time")
    plt.ylabel("g")
    plt.ylim(-2.5, 2.5)
    plt.plot(range(len(ax_data)), ax_data, "-", color="blue")
    plt.plot(range(len(ay_data)), ay_data, "-", color="red")
    plt.plot(range(len(az_data)), az_data, "-", color="green")
    # plt.show()
    plt.savefig("acceleration_data.png")
    os.rename("acceleration_data.png", "{0:%Y%m%d_%H%M%S}acceleration_data.png".format(d))


gpio_pin1 = 8
gpio_pin2 = 10
pwm_pin = 12


if __name__ == "__main__":
    gx = []
    gy = []
    gz = []
    ax = []
    ay = []
    az = []

    # モータピンのセットアップ
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(gpio_pin1, GPIO.OUT)
    GPIO.setup(gpio_pin2, GPIO.OUT)
    GPIO.setup(pwm_pin, GPIO.OUT)
    pwm = GPIO.PWM(pwm_pin, 50)
    pwm.start(0)
    pwm.ChangeDutyCycle(0)
    GPIO.output(gpio_pin1, 1)
    GPIO.output(gpio_pin2, 0)
    pwm.ChangeDutyCycle(100)

    d = datetime.datetime.now()
    write_fp = csv.writer(open('logfile.csv', "w"))

    for count in range(10):

        # æ¸©åº¦.
        temp = get_temp()
        # è§éåº¦.
        gyro_x, gyro_y, gyro_z = get_gyro_data_deg()
        # å éåº¦
        accel_x, accel_y, accel_z = get_accel_data_g()

        gx.append(gyro_x)
        gy.append(gyro_y)
        gz.append(gyro_z)
        ax.append(accel_x)
        ay.append(accel_y)
        az.append(accel_z)

        list_data = [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z]
        write_fp.writerow(list_data)

        list_data = []

        sleep(1)

    GPIO.output(gpio_pin1, 0)
    GPIO.output(gpio_pin2, 0)
    pwm.stop()
    GPIO.cleanup()

    save_gyro_data(gx, gy, gz)
    save_acceleration_data(ax, ay, az)
