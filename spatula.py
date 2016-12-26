from flask import Flask
from flask_ask import Ask, statement, convert_errors
import wiringpi
import logging
from stepfcn import *

initializePins()

setMotor1Dir(0) #1=CCW, 0=CW

setMotor2Dir(0)


#app = Flask(__name__)
#ask = Ask(app, '/')

#logging.getLogger("flask_ask").setLevel(logging.DEBUG)

#@ask.intent('StepIntent', mapping={'status': 'status', 'motor': 'motor'})


 
enableMotor2()		#Motor 1 = spoon
#enableMotor2()		#Motor 2 = spatula
#wiringpi.delay(1000)	#Initial Delay
					
					#Spoon code
for x in range(0, 5):					
	setMotor2Dir(1) 	#set direction down --Utencil Up is CCW or 1. Down is 0 or CW
	step(0,80)
	#disableMotor1()
		#step spoon down to crack egg *** step(motor1,motor2)
	wiringpi.delay(200)	#Delay
	setMotor2Dir(0) 	#Set direction up
		#Delay
	step(0,80)		#step spoon up slightly to reset position
	wiringpi.delay(150)
	#Set direction up	
#	wiringpi.delay(1000)	#Delay
#	setMotor2Dir(1) 	#Set direction up
#	step(0,100)
	
disableMotor2()
disableMotor1()
#		setMotor1Dir(0)		#set direction down 
#		wiringpi.delay(1000)	#Delay
#		step(50,0)		#step spoon down to crack egg again***
#		setMotor1Dir(1) 	#Set direction up
#		wiringpi.delay(1000)	#Delay
#		step(50,0)		#step spoon up slightly to reset position
#		setMotor1Dir(0)		#set direction down 
#		wiringpi.delay(1000)	#Delay
#		step(50,0)		#step spoon down to crack egg again***
#		setMotor1Dir(1) 	#set direction up
#		wiringpi.delay(1000)	#Delay
#		step(100,0)		#step spoon up to starting position
#	
#					#Spatula Code
#
#		wiringpi.delay(2000)	#Initial Delay
#		setMotor2Dir(0) 	#set direction down --Utencil Up is CCW or 1. Down is 0 or CW
#		step(0,100)		#step spatula down
#		wiringpi.delay(100)	#Delay
#		setMotor2Dir(1) 	#Set direction up
#		step(0,100)		#step spatula up
#		wiringpi.delay(100)	#Delay
#		setMotor2Dir(0) 	#Set direction down
#		step(0,100)		#
#		wiringpi.delay(100)	#Delay
#		setMotor2Dir(1) 	#Set direction up
#		step(0,100)		#
#		wiringpi.delay(100)	#Delay
#		setMotor2Dir(0) 	#Set direction down
#		step(0,100)		#
#		wiringpi.delay(100)	#Delay
#		setMotor2Dir(1) 	#Set direction up
#		step(0,100)		#
#		wiringpi.delay(100)	#Delay
#		setMotor2Dir(0) 	#Set direction down
#		step(0,100)		#
#		wiringpi.delay(100)	#Delay
#		setMotor2Dir(1) 	#Set direction up
#		step(0,100)		#

				

#	disableMotor1() #Want to keep utencil position fixed. Keep Motors enabled
#	disableMotor2()
#		return statement('I got you homie')


#if __name__ == '__main__':

#		port = 5000 #the custom port you want
	
#		app.run(host='0.0.0.0', port=port)
		
