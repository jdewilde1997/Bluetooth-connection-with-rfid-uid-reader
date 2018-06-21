import RPi.GPIO as GPIO
import MFRC522
from bluetooth import *
import sys
import signal

continue_reading = True

reader = MFRC522.MFRC522()

addr = None

if len(sys.argv) < 2:
	print("no device specified.  Searching all nearby bluetooth devices for")
	print("the SampleServer service")
else:
	addr = sys.argv[1]
	print("Searching for SampleServer on %s" % addr)

# search for the SampleServer service
uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
	print("couldn't find the SampleServer service =(")
	sys.exit(0)

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s" % (name, host))

# Create the client socket
sock=BluetoothSocket( RFCOMM )
sock.connect((host, port))

print("Connection successful! RFID ready!")

while True:
	(status,TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)

	if status == reader.MI_OK:	#If card found
        	print("Card detected")

	(status,uid) = reader.MFRC522_Anticoll()	#Get UID

	if status == reader.MI_OK:	#If UID is obtained
		data = str(format(uid[0], '02X') + ":"  + format(uid[1], '02X')+ ":" + format(uid[2], '02X') + ":" + format(uid[3], '02X'))
		sock.send(data)	#Send data


sock.close()
