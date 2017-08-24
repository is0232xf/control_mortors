# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 18:11:55 2017

@author: Fujiichang
"""

# import module
import smbus            # use I2C
import csv
import time
import RPi.GPIO as GPIO
import matplotlib.pyplot as plt
from time import sleep  # time module
from tqdm import tqdm

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
# Sleep解除.
bus.write_byte_data(DEV_ADDR, PWR_MGMT_1, 0)

#
# Sub function
#
# 1byte read


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
# 温度
#
def get_temp():
    temp = read_word_sensor(TEMP_OUT)
    x = temp / 340 + 36.53      # data sheet(register map)記載の計算式.
    return x

#
# 角速度(full scale range ±250 deg/s
#        LSB sensitivity 131 LSB/deg/s
#        -> ±250 x 131 = ±32750 LSB[16bitで表現])
#   Gyroscope Configuration GYRO_CONFIG (reg=0x1B)
#   FS_SEL(Bit4-Bit3)でfull scale range/LSB sensitivityの変更可.
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
# 加速度(full scale range ±2g
#        LSB sensitivity 16384 LSB/g)
#        -> ±2 x 16384 = ±32768 LSB[16bitで表現])
#   Accelerometer Configuration ACCEL_CONFIG (reg=0x1C)
#   AFS_SEL(Bit4-Bit3)でfull scale range/LSB sensitivityの変更可.
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
    plt.plot(range(len(gy_data)), gy_data, "-", color="red")
    plt.plot(range(len(gz_data)), gz_data, "-", color="green")
    plt.savefig("gyro_data.png")


def save_acceleration_data(ax_data, ay_data, az_data):
    plt.xlabel("time")
    plt.ylabel("g")
    plt.ylim(-2.5, 2.5)
    plt.plot(range(len(ax_data)), ax_data, "-", color="blue")
    plt.plot(range(len(ay_data)), ay_data, "-", color="red")
    plt.plot(range(len(az_data)), az_data, "-", color="green")
    plt.savefig("acceleration_data.png")


if __name__ == "__main__":

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
    GPIO.output(gpio_pin5, 0)
    GPIO.output(gpio_pin6, 1)
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
    time.sleep(1)

    # print("stop")
    # GPIO.output(gpio_pin1, 0)
    # GPIO.output(gpio_pin2, 0)
    # GPIO.output(gpio_pin3,  0)
    # GPIO.output(gpio_pin4, 0)
    # GPIO.output(gpio_pin5, 0)
    # GPIO.output(gpio_pin6, 0)
    # GPIO.output(gpio_pin7,  0)
    # GPIO.output(gpio_pin8, 0)
    # time.sleep(3)

    # print("restart")
    # pwm1.ChangeDutyCycle(0)
    # GPIO.output(gpio_pin1, 0)
    # GPIO.output(gpio_pin2, 1)
    # pwm2.ChangeDutyCycle(0)
    # GPIO.output(gpio_pin3,  0)
    # GPIO.output(gpio_pin4, 1)
    # pwm3.ChangeDutyCycle(0)
    # GPIO.output(gpio_pin5, 0)
    # GPIO.output(gpio_pin6, 1)
    # pwm4.ChangeDutyCycle(0)
    # GPIO.output(gpio_pin7,  0)
    # GPIO.output(gpio_pin8, 1)

    # pwm1.ChangeDutyCycle(100)
    # pwm2.ChangeDutyCycle(100)
    # pwm3.ChangeDutyCycle(100)
    # pwm4.ChangeDutyCycle(100)
    # time.sleep(3)

    gx = []
    gy = []
    gz = []
    ax = []
    ay = []
    az = []

    write_fp = csv.writer(open("logfile.csv", "w"))

    for count in range(50):
        # 温度.
        temp = get_temp()
        # 小数点以下第1位まで表示.
        # print 'count: %d' % count,
        # print 'temperature[degrees C]:',
        # print '%04.1f' % temp,
        # print '||',
        # 角速度.
        gyro_x, gyro_y, gyro_z = get_gyro_data_deg()
        # 小数点以下第3位まで表示.
        # print 'gyro[deg/s]',
        # # print 'x: %08.3f' % gyro_x,
        # print 'y: %08.3f' % gyro_y,
        # print 'z: %08.3f' % gyro_z,
        # print '||',
        # 加速度
        accel_x, accel_y, accel_z = get_accel_data_g()
        # 小数点以下第3位まで表示.
        # print 'accel[g]',
        # print 'x: %06.3f' % accel_x,
        # print 'y: %06.3f' % accel_y,
        # print 'z: %06.3f' % accel_z,

        print "count: %d" % count

        # 各値をそれぞれの配列に格納する
        gx.append(gyro_x)
        gy.append(gyro_y)
        gz.append(gyro_z)
        ax.append(accel_x)
        ay.append(accel_y)
        az.append(accel_z)

        # csvファイルを作るための1行のリストを生成する
        list_data = [gyro_x, gyro_y, gyro_z, accel_x, accel_y, accel_z]

        # csvファイルへの書き込み
        write_fp.writerow(list_data)

        list_data = []

        sleep(1)

    save_gyro_data(gx, gy, gz)
    save_acceleration_data(ax, ay, az)
    print("finished saving gyroscope data")
    print("finished saving acceleration data")

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
