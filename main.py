from machine import Pin
import time

# set ABCD pins of the K155ID1 chip as outputs connected to the GPIO pins
A = Pin(3, Pin.OUT)  # GP3
B = Pin(1, Pin.OUT)  # GP2
C = Pin(2, Pin.OUT)  # GP1
D = Pin(0, Pin.OUT)  # GP0

# function for binary decoding
# the decoder works this:
# set D C B D in binary, e.g. D = 0 V, C = 0 V, B = 1 V, A = 0 V
# interprets as 0010 = 2 in decimal --> chip pulls nixie two to GND
def show_digit(n):
    # A is the least significant bit of the input number
    # say n = 5 which is in binary n = 0101 for which we need to turn on A nd C
    
    # & means bit wise and
    # e.g 0 1 0 1
    # &   0 0 0 1
    # =   0 0 0 1
    # which is 1 so turn A on
    A.value(n & 0b0001)
    
    # >> shifts the binary number to the right and adds a 0 in front
    # so n = 0101 >> 1 gives 0010
    #     0 0 1 0
    # &   0 0 0 1
    # =   0 0 0 0
    # = 0 so turn B off
    B.value((n >> 1) & 0b0001)
    
    C.value((n >> 2) & 0b0001)
    
    D.value((n >> 3) & 0b0001)

# start main loop
while True:
    for i in range(10):
        show_digit(i)
        time.sleep(0.4)
