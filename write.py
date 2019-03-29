#!/usr/bin/env python

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import time

ledb= 3
ledr= 5
buz= 7

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(ledb,GPIO.OUT)
GPIO.setup(ledr,GPIO.OUT)
GPIO.setup(buz,GPIO.OUT)
reader = SimpleMFRC522()

try:
        GPIO.output(ledb,1)
        GPIO.output(ledr,0)
        GPIO.output(buz,0)
        reg_no = raw_input('Registration Number:')
        GPIO.output(ledb,1)
        GPIO.output(ledr,1)
        GPIO.output(buz,0)
        print("Now place your tag to write")
        reader.write(reg_no)
        print("Written")
        GPIO.output(ledb,0)
        GPIO.output(ledr,0)
        GPIO.output(buz,1)
        time.sleep(0.5)
        GPIO.output(ledb,0)
        GPIO.output(ledr,0)
        GPIO.output(buz,0)

finally:
        GPIO.cleanup()

