import RPi.GPIO as gpio
import time

def init():
    gpio.setmode(gpio.BOARD)
    gpio.setup(7, gpio.OUT)
    gpio.setup(11, gpio.OUT)
    gpio.setup(13, gpio.OUT)
    gpio.setup(15, gpio.OUT)

def reverse(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,True)
    gpio.output(13,True)
    gpio.output(15,False)
    time.sleep(tf)
    gpio.cleanup()

def forward(tf):
    init()
    gpio.output(7, True)
    gpio.output(11, False)
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def right(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13, True)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_right(tf):
    init()
    gpio.output(7, False)
    gpio.output(11, True)
    gpio.output(13, True)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,True)
    gpio.output(13, True)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()


#time.sleep(1)
#gpio.cleanup()
forward(3)

left(3)
#pivot_left(5)
#pivot_right(5)
pivot_right(4)
#forward(2)
#left(4)
#forward(2)
#left(4)
#forward(2)
right(3)
reverse(3)
