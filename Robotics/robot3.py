import RPi.GPIO as gpio
import time
import Tkinter as tk
import sys

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
    gpio.output(7,True)
    gpio.output(11, False)
    gpio.output(13,False)
    gpio.output(15,True)
    time.sleep(tf)
    gpio.cleanup()

def left(tf):
    init()
    gpio.output(7,False)
    gpio.output(11,False)
    gpio.output(13,False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def right(tf):
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
    gpio.output(13, False)
    gpio.output(15, True)
    time.sleep(tf)
    gpio.cleanup()

def pivot_left(tf):
    init()
    gpio.output(7,True)
    gpio.output(11,False)
    gpio.output(13, True)
    gpio.output(15, False)
    time.sleep(tf)
    gpio.cleanup()


def key_input(event):
    init()
    key_press=event.char
    print('Key: '+ key_press)
    
    sleep_time=0.40
    sleep_time2=0.50    

    if key_press.lower()=='w':
        forward(sleep_time2)
    elif key_press.lower()=='s':
        reverse(sleep_time2)
    elif key_press.lower()=='a':
        left(sleep_time)
    elif key_press.lower()=='d':
        right(sleep_time)
    elif key_press.lower()=='q':
        pivot_left(sleep_time2)
    elif key_press.lower()=='e':
        pivot_right(sleep_time2)
    else:
        pass
        

command=tk.Tk()
command.bind('<KeyPress>',key_input)
command.mainloop()



#forward(1)

#left(5)
#pivot_left(20)
#pivot_right(20)
#pivot_right(20)
#forward(2)
#left(4)
#forward(2)
#left(4)
#forward(2)
#right(4)
