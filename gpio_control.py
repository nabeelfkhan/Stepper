from flask import Flask
from flask_ask import Ask, statement, convert_errors
import wiringpi
import logging
from stepfcn import *
#GPIO.setmode(GPIO.BCM)

initializePins()

setMotor1Dir(1)

setMotor2Dir(1)

enableMotor1()
enableMotor2()

app = Flask(__name__)
ask = Ask(app, '/')

logging.getLogger("flask_ask").setLevel(logging.DEBUG)

@ask.intent('StepIntent', mapping={'status': 'status', 'motor': 'motor'})
def motor_control(status, motor):

#	try:
#        motorNum = int(motor)
 #   except Exception as e:
  #      return statement('Motor number not valid.')

#	if status in ['clockwise', 'right']:   
		setMotor1Dir(1)
		setMotor2Dir(1) 
		step(600,600)#number of steps
#		disableMotor1()

#    	if status in ['counterclockwise', 'left']:    
#		setMotor1Dir(0)
#		setMotor2Dir(0) 
#		step(600,600)#number of steps
#		disableMotor2()

#
#return statement('Turning pin {} {}'.format(pin, status))

		return statement('I got you homie')


if __name__ == '__main__':

		port = 5000 #the custom port you want
	
		app.run(host='0.0.0.0', port=port)
