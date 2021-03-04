import serial
import serial.tools.list_ports
import time
import os

usbInUse = []
manufact = ["Silicon Labs"]

def FindESPports():

	del usbInUse[:]
	comlist = serial.tools.list_ports.comports()
	for element in comlist:
		usbInUse.append(element.manufacturer)
		if element.manufacturer == manufact[0]:
			ESP_port = element.device
	if any(x in usbInUse for x in manufact):
		print "ESP Find in: " + element.device
		return element.device
		
	else:
		return "Esp Not Connected"
		


ESP_Port_Find = FindESPports()

while ESP_Port_Find == "Esp Not Connected":
	ESP_Port_Find = FindESPports()
	print "ESP Disconnected"
	time.sleep(1)

readOut = 0   #chars waiting from laser range finder
ser = serial.Serial()
ser.baudrate = 9600
ser.port = ESP_Port_Find
ser.timeout = 1


print ("Starting up")
connected = False
commandToSend = ["<SAFETYOFFSHAKED>", "<SAFETYOFFTURNOFFOK>"]
state = 0

while True:
	try:
		if ser.is_open:
			if connected == False:
				print ("Attempt to Read")
				readOut = ser.readline().decode('ascii')
				time.sleep(0.5)
				if readOut != "":
					print ("Received: " + readOut)
					if readOut == "<SAFETYOFFSHAKE>":
						connected = True 
					if readOut == "<SAFETYOFFTURNOFF>":
						connected = True
						state = 1 
					ser.flush() #flush the buffer
			
			if connected == True:
				if state == 0:
					print ("Writing: ",  commandToSend[0])
					ser.write(str(commandToSend[0]).encode('ascii'))
					time.sleep(0.5)
					connected = False
					ser.flush() #flush the buffer
					
				if state == 1:
					print ("Writing: ",  commandToSend[1])
					ser.write(str(commandToSend[1]).encode('ascii'))
					time.sleep(0.5)
					connected = False
					state = 0
					ser.flush() #flush the buffer
					ser.close()
					os.system('shutdown -h now')
		else:	
			ser.open()
	except:
		ser.close()
		print "ESP Disconnected"
		time.sleep(1)
		if ESP_Port_Find == "Esp Not Connected":
			ESP_Port_Find = FindESPports()
			print "ESP Disconnected"

		
