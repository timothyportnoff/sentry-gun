#Remote control support
#!/usr/bin/env python3
import RPi.GPIO as GPIO
from config import *
from time import sleep
from time import *

count = 0

CODES = {
    0xffa25d: "ON/OFF",
    0xff629d: "MODE",
    0xffe21d: "MUTE",
    0xff22dd: "PLAY/PAUSE",
    0xff02fd: "PREVIOUS",
    0xffc23d: "NEXT",
    0xffe01f: "EQ",
    0xffa857: "MINUS",
    0xff906f: "PLUS",
    0xff6897: "0",
    0xff9867: "SHUFFLE",
    0xffb04f: "U/SD",
    0xff30cf: "1",
    0xff18e7: "2",
    0xff7a85: "3",
    0xff10ef: "4",
    0xff38c7: "5",
    0xff5aa5: "6",
    0xff42bd: "7",
    0xff4ab5: "8",
    0xff52ad: "9",
}

def setup():
	#GPIO.setmode(GPIO.BOARD)       # Numbers GPIOs by physical location
	GPIO.setup(IR, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def cnt(ev=None):
	global count
	count += 1
	print ('Received infrared. cnt = ', count)

def loop():
	GPIO.add_event_detect(IR, GPIO.FALLING, callback=cnt) # wait for falling
	while True:
		pass   # Don't do anything

def binary_aquire(pin, duration):
    # aquires data as quickly as possible
    t0 = time()
    results = []
    while (time() - t0) < duration:
        results.append(GPIO.input(pin))
    return results


def on_ir_receive(pinNo, bouncetime=150):
    # when edge detect is called (which requires less CPU than constant
    # data acquisition), we acquire data as quickly as possible
    data = binary_aquire(pinNo, bouncetime/1000.0)
    if len(data) < bouncetime:
        return
    rate = len(data) / (bouncetime / 1000.0)
    pulses = []
    i_break = 0
    # detect run lengths using the acquisition rate to turn the times in to microseconds
    for i in range(1, len(data)):
        if (data[i] != data[i-1]) or (i == len(data)-1):
            pulses.append((data[i-1], int((i-i_break)/rate*1e6)))
            i_break = i
    # decode ( < 1 ms "1" pulse is a 1, > 1 ms "1" pulse is a 1, longer than 2 ms pulse is something else)
    # does not decode channel, which may be a piece of the information after the long 1 pulse in the middle
    outbin = ""
    for val, us in pulses:
        if val != 1:
            continue
        if outbin and us > 2000:
            break
        elif us < 1000:
            outbin += "0"
        elif 1000 < us < 2000:
            outbin += "1"
    try:
        return int(outbin, 2)
    except ValueError:
        # probably an empty code
        return None

def destroy():
	GPIO.cleanup()                     # Release resource
        exit()

if __name__ == '__main__':     # Program start from here
	setup()
	try:
            print("Starting IR Listener")
            while True:
                print("Waiting for signal")
                GPIO.wait_for_edge(IR, GPIO.FALLING)
                code = on_ir_receive(IR)
                if code:
                    print(str(hex(code)))
                else:
                    print("Invalid code")
	except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
		destroy()
        except RuntimeError:
                # this gets thrown when control C gets pressed
                # because wait_for_edge doesn't properly pass this on
		destroy()
                #pass
