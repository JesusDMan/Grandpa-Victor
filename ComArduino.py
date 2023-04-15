startMarker = b'<'
endMarker = b'>'
ready_msg = 'Arduino is ready!'
minimum_time_between_presses = 1;

#=====================================

#  Function Definitions

#=====================================

def sendToArduino(sendStr):
  ser.write(sendStr)

#======================================

def recvFromArduino():
  ck = ""
  x = "" # any value that is not an end- or startMarker
  
  # wait for the start character
  while x != startMarker: 
    x = ser.read()

  # save data until the end marker is found
  while x != endMarker:
    if x != startMarker:
      ck = ck + x.decode('UTF-8') 
    x = ser.read()
  
  return(ck)


#============================

def waitForArduino():

   # wait until the Arduino sends 'Arduino Ready' - allows time for Arduino reset
   # it also ensures that any bytes left over from a previous message are discarded
   
    global startMarker, endMarker
    
    msg = ""
    while msg != ready_msg:
      msg = recvFromArduino()

    print(f'{msg}\n')


def yes():
    p = subprocess.Popen(f'python "{os.getcwd()}\yes.py"')
    time.sleep(5)
    p.kill()

def no():
    p = subprocess.Popen(f'python "{os.getcwd()}\script.py"')
    time.sleep(5)
    p.kill()



     
#======================================

# THE DEMO PROGRAM STARTS HERE

#======================================

import serial
import time
import subprocess
import os
    
print('\n\n')

# NOTE the user must ensure that the serial port and baudrate are correct
serPort = "COM7"
baudRate = 9600
ser = serial.Serial(serPort, baudRate)
print("Serial port " + serPort + " opened  Baudrate " + str(baudRate))

waitForArduino()
msg = ''
time_from_lest_yes = 0
time_from_lest_no = 0

while True:
    
    msg = recvFromArduino()
    if (msg == 'Yes' and time.time() - time_from_lest_yes > minimum_time_between_presses):
        yes()
        time_from_lest_yes = time.time()
    elif (msg == 'No' and time.time() - time_from_lest_no > minimum_time_between_presses):
        no()
        time_from_lest_no = time.time()

ser.close

