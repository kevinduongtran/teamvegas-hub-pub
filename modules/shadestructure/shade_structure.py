# Servo Control
import time
import wiringpi
import sys 


wiringpi.wiringPiSetupGpio()
wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)
wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

THREE_POS = 1
TWELVE_POS = 130

def open():
	wiringpi.pwmWrite(18, TWELVE_POS)
	off()
	
def close():
	wiringpi.pwmWrite(18, THREE_POS)
	off()

def off():
	time.sleep(1)
	wiringpi.pwmWrite(18, 0)

def main():
	if sys.argv:
		if str(sys.argv[1]) == 'close':
			open()
		if str(sys.argv[1]) == 'open':
			close()
	
if __name__ == '__main__':
	main()

