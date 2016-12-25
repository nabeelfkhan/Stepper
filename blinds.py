from flask import Flask
from flask_ask import Ask, statement, convert_errors
import wiringpi
import logging
from stepfcn import *

initializePins()

setMotor1Dir(0) #1=CCW, 0=CW

setMotor2Dir(0)


app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('StepIntent', mapping={'status': 'status', 'motor': 'motor'})
def motor_control(status, motor):

	if status in ['open']:   
		enableMotor1()
		enableMotor2()
		setMotor1Dir(0)
		setMotor2Dir(0) 
		step(650,0)#number of steps(motor1,motor2)
		

   	if status in ['close']:    
		enableMotor1()
		enableMotor2()
		setMotor1Dir(1)
		setMotor2Dir(1) 
		step(650,0)#number of steps

	
	disableMotor1()
	disableMotor2()
	return statement('I got you homie')


if __name__ == '__main__':

		port = 5000 #the custom port you want
	
		app.run(host='0.0.0.0', port=port)
		
