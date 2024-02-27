import serial
from serial.tools import list_ports
import time
import survey

def askSerialDevice():
	serialDevices = []
	for port in list_ports.comports():
		serialDevices.append(port.device)
	index = survey.routines.select('Select the serial device connected to the MR26 AP: ', options = serialDevices)
	return serialDevices[index]

def waitForMerakiBoot(ser):
	state = None
	with survey.graphics.SpinProgress(prefix = 'Please connect and reboot the MR26 AP...', epilogue = 'MR26 detected!') as progress:
		time.sleep(1)
		buf = ""
		while("Using GMAC1" not in buf):
			ser.write("xyzzy".encode())
			buf = str(ser.read(256))

	for x in range(100):
		ser.write("xyzzy".encode())

def confirmUboot(ser):
	state = None
	with survey.graphics.SpinProgress(prefix = 'Waiting for U-Boot shell..', epilogue = 'U-Boot shell detected!') as progress:
		time.sleep(1)
		buf = ""
		while("u-boot" not in buf):
			buf = str(ser.read(256))
		
		
devicePath = askSerialDevice()
ser = serial.Serial(devicePath, 115200)
waitForMerakiBoot(ser)
confirmUboot(ser)

ser.write("\n".encode())
ser.read(256)
ser.write("help\n".encode())
ser.read(256)
print(f'To access the U-Boot shell via serial: screen {devicePath} 115200')