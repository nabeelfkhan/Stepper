#Code to interface with DRV8821 and two stepper motors

import wiringpi


#Pin number listing

PWMA = 7  #Pin 7
PWMB = 0  #Pin 11
ABRST = 2 #Pin 13
ABDIR = 3 #Pin 15
CDRST = 4 #Pin 16
CDDIR = 5 #Pin 18

# Static Variables
OUTPUT = 1
HIGH = 1
LOW = 0

#Global variable init
pwmacount = 0
pwmbcount = 0

def initializePins():
	wiringpi.wiringPiSetup()
	wiringpi.pinMode(PWMA,OUTPUT)
	wiringpi.pinMode(PWMB,OUTPUT)
	wiringpi.pinMode(ABRST,OUTPUT)
	wiringpi.pinMode(ABDIR,OUTPUT)
	wiringpi.pinMode(CDRST,OUTPUT)
	wiringpi.pinMode(CDDIR,OUTPUT)

#initializePins()

#for time in range(0,4):
#	for brightness in range(0,100): # Going from 0 to 100 will give us full off to full on
#		wiringpi.softPwmWrite(PIN_TO_PWM,brightness) # Change PWM duty cycle
#		wiringpi.delay(10) # Delay for 0.2 seconds
#	for brightness in reversed(range(0,100)):
#		wiringpi.softPwmWrite(PIN_TO_PWM,brightness)
#		wiringpi.delay(10)

#Init vars


def requestInput():
	global pwmacount
	global pwmbcount
	pwmacount= int(raw_input("Enter number of pulses for Motor 1:\n"))
	pwmbcount= int(raw_input("Enter number of pulses for Motor 2:\n"))

#requestInput()

#Inputs for later
MotorABDir = 1
MotorCDDir = 0

def enableMotor1():
	wiringpi.digitalWrite(ABRST,HIGH) #Enable motor 1

#enableMotor1()

def enableMotor2():
	wiringpi.digitalWrite(CDRST,HIGH) #Enable motor 2

#enableMotor2()

def setMotor1Dir(MotorABDir):
	wiringpi.digitalWrite(ABDIR,MotorABDir) #Set Dir to 0 for CW, 1 for CCW

#setMotor1Dir(MotorABDir)

def setMotor2Dir(MotorCDDir):
	wiringpi.digitalWrite(CDDIR,MotorCDDir) 

#setMotor2Dir(MotorCDDir)


def step(pwmacount,pwmbcount):

	while (pwmacount != 0 or pwmbcount != 0):

		if pwmacount > 0 and pwmbcount > 0:
			wiringpi.digitalWrite(PWMA,HIGH)
			wiringpi.digitalWrite(PWMB,HIGH)
			wiringpi.delayMicroseconds(1000)
			wiringpi.digitalWrite(PWMA,LOW)
			wiringpi.digitalWrite(PWMB,LOW)
			wiringpi.delayMicroseconds(1000)
		
			pwmacount = pwmacount -1
			pwmbcount = pwmbcount -1

		elif pwmacount > 0 and pwmbcount == 0:
			wiringpi.digitalWrite(PWMA,HIGH)
			wiringpi.delayMicroseconds(1000) #f = 900Hz (pulses per second). T = 1/f. Delay = T/2 = 555.56us> Modified based on scope
			wiringpi.digitalWrite(PWMA,LOW)
			wiringpi.delayMicroseconds(1000) #f = 900Hz (pulses per second). T = 1/f. Delay = T/2 = 555.56us> Modified based on scope
		
			pwmacount = pwmacount - 1
	
		elif pwmbcount > 0 and pwmacount == 0:
			wiringpi.digitalWrite(PWMB,HIGH)
			wiringpi.delayMicroseconds(1000) #f = 900Hz (pulses per second). T = 1/f. Delay = T/2 = 555.56us> Modified based on scope
			wiringpi.digitalWrite(PWMB,LOW)
			wiringpi.delayMicroseconds(1000)
		
			pwmbcount = pwmbcount - 1 

#step(pwmacount,pwmbcount)

def disableMotor1():
	wiringpi.digitalWrite(ABRST,LOW) #Disable motor 1

#disableMotor1()

def disableMotor2():
	wiringpi.digitalWrite(CDRST,LOW) #Disable motor 2

#disableMotor2()
