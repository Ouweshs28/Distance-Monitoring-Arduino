#CCE 1000 Coursework 2 By Ouwesh & Yusra
#!/usr/bin/env python
from nanpy import (ArduinoApi, SerialManager, Ultrasonic, Tone) 
#Importing Libraries 
#ArduinoApi to control the arduino
#SerialManaager to connect via serial port
#Ultrasonic to use the sensor
#Tone to control the buzzer
import time
from time import sleep
import sys
#Simulator leds
import opc
from random import randint
import random
#Pins connected to the Ultrasonar sensor
trigPin = 2
echoPin = 3
#LED Pins
greenLed = 9
yellowLed = 8
redLed = 7
#Buzzer Alarm
alarm = 11
#Setting LEDs
client = opc.Client('localhost:7890')

    
my_led=[(0,0,0)]*360
#GreenAnimation
def GreenLED():

    greenRange1 = randint(1,256)
    greenRange2 = randint(1,256)
    greenRange3 = randint(1,256)
    greenRange4 = randint(1,256)
    greenRange5 = randint(1,256)
    greenRange6 = randint(1,256)
    red=0
    blue=0


    for i in range (0,60) :
        my_led[i] = (red,greenRange1,blue)
        my_led[i+60] = (red,greenRange2,blue)
        my_led[i+120] = (red,greenRange3,blue)
        my_led[i+180] = (red,greenRange4,blue)
        my_led[i+240] = (red,greenRange5,blue)
        my_led[i+300] = (red,greenRange6,blue)
        client.put_pixels(my_led)
        time.sleep(0.01)

    greenRange1 = randint(1,256)
    greenRange2 = randint(1,256)
    greenRange3 = randint(1,256)
    greenRange4 = randint(1,256)
    greenRange5 = randint(1,256)
    greenRange6 = randint(1,256)		

    for i in reversed(range(0,60)) :
        my_led[i] = (red,greenRange1,blue)
        my_led[i+60] = (red,greenRange2,blue)
        my_led[i+120] = (red,greenRange3,blue)
        my_led[i+180] = (red,greenRange4,blue)
        my_led[i+240] = (red,greenRange5,blue)
        my_led[i+300] = (red,greenRange6,blue)
        client.put_pixels(my_led)
        time.sleep(0.01)

#DANGER RED 
def Danger():
        strobecount = 5
        flashDelay = 0.03
        Pause = 0.3
        red=255
        blue=0
        green=0
        for x in range(0, strobecount):
            my_led=[(32,32,32)]*360
            client.put_pixels(my_led)
            time.sleep(flashDelay)
            my_led[6] = (red, blue, green)
            my_led[7] = (red, blue, green)
            my_led[8] = (red, blue, green)
            my_led[66] = (red, blue, green)
            my_led[126] = (red, blue, green)
            my_led[186] = (red, blue, green)
            my_led[246] = (red, blue, green)
            my_led[306] = (red, blue, green)
            my_led[69] = (red, blue, green)
            my_led[130] = (red, blue, green)
            my_led[190] = (red, blue, green)
            my_led[249] = (red, blue, green)
            my_led[308] = (red, blue, green)
            my_led[307] = (red, blue, green)
            my_led[14] = (red, blue, green)
            my_led[74] = (red, blue, green)
            my_led[134] = (red, blue, green)
            my_led[194] = (red, blue, green)
            my_led[254] = (red, blue, green)
            my_led[314] = (red, blue, green)
            my_led[15] = (red, blue, green)
            my_led[16] = (red, blue, green)
            my_led[17] = (red, blue, green)
            my_led[77] = (red, blue, green)
            my_led[137] = (red, blue, green)
            my_led[197] = (red, blue, green)
            my_led[257] = (red, blue, green)
            my_led[317] = (red, blue, green)
            my_led[134] = (red, blue, green)
            my_led[135] = (red, blue, green)
            my_led[136] = (red, blue, green)
            my_led[137] = (red, blue, green)
            my_led[21] = (red, blue, green)
            my_led[25] = (red, blue, green)
            my_led[81] = (red, blue, green)
            my_led[142] = (red, blue, green)
            my_led[201] = (red, blue, green)
            my_led[261] = (red, blue, green)
            my_led[321] = (red, blue, green)
            my_led[145] = (red, blue, green)
            my_led[205] = (red, blue, green)
            my_led[264] = (red, blue, green)
            my_led[265] = (red, blue, green)
            my_led[203] = (red, blue, green)
            my_led[325] = (red, blue, green)
            my_led[142] = (red, blue, green)
            my_led[43] = (red, blue, green)
            my_led[85] = (red, blue, green)
            my_led[141] = (red, blue, green)
            my_led[30] = (red, blue, green)
            my_led[31] = (red, blue, green)
            my_led[32] = (red, blue, green)
            my_led[88] = (red, blue, green)
            my_led[148] = (red, blue, green)
            my_led[208] = (red, blue, green)
            my_led[268] = (red, blue, green)
            my_led[329] = (red, blue, green)
            my_led[330] = (red, blue, green)
            my_led[272] = (red, blue, green)
            my_led[212] = (red, blue, green)
            my_led[152] = (red, blue, green)
            my_led[151] = (red, blue, green)
            my_led[150] = (red, blue, green)
            my_led[210] = (red, blue, green)
            my_led[35] = (red, blue, green)
            my_led[36] = (red, blue, green)
            my_led[37] = (red, blue, green)
            my_led[38] = (red, blue, green)
            my_led[39] = (red, blue, green)
            my_led[95] = (red, blue, green)
            my_led[155] = (red, blue, green)
            my_led[215] = (red, blue, green)
            my_led[275] = (red, blue, green)
            my_led[335] = (red, blue, green)
            my_led[336] = (red, blue, green)
            my_led[337] = (red, blue, green)
            my_led[338] = (red, blue, green)
            my_led[156] = (red, blue, green)
            my_led[157] = (red, blue, green)
            my_led[158] = (red, blue, green)
            my_led[159] = (red, blue, green)
            my_led[338] = (red, blue, green)
            my_led[339] = (red, blue, green)
            my_led[43] = (red, blue, green)
            my_led[102] = (red, blue, green)
            my_led[162] = (red, blue, green)
            my_led[222] = (red, blue, green)
            my_led[282] = (red, blue, green)
            my_led[342] = (red, blue, green)
            my_led[44] = (red, blue, green)
            my_led[45] = (red, blue, green)
            my_led[105] = (red, blue, green)
            my_led[165] = (red, blue, green)
            my_led[224] = (red, blue, green)
            my_led[346] = (red, blue, green)
            my_led[285] = (red, blue, green)
            my_led[223] = (red, blue, green)
            client.put_pixels(my_led)

        time.sleep(flashDelay)
        time.sleep(Pause)

def YellowAnimation ():
    redyellow=randint(1,256)
    my_led = [(redyellow, redyellow, 0)]*360
    random.shuffle(my_led)
    client.put_pixels(my_led)
    time.sleep(0.3)

#END ANIMATION
def EndlineAnim (x) :
    my_led[x]= (255, 255, 255)
    time.sleep(0.05)
    client.put_pixels(my_led)

def EndAnimation():
        #first row
        for x in (range(0,5)) :
                EndlineAnim (x)

        EndlineAnim (7)
        EndlineAnim (13)

        for x in (range(17,22)) :
                EndlineAnim (x)

        EndlineAnim (24)
        EndlineAnim (30)
        EndlineAnim (32)
        EndlineAnim (38)

        for x in (range(41,46)) :
                EndlineAnim (x)

        #second row
        EndlineAnim (62)
        EndlineAnim (67)
        EndlineAnim (73)
        EndlineAnim (77)
        EndlineAnim (81)
        EndlineAnim (84)
        EndlineAnim (86)
        EndlineAnim (90)
        EndlineAnim (96)
        EndlineAnim (92)
        EndlineAnim (100)

        #third row
        EndlineAnim (122)
        EndlineAnim (127)
        EndlineAnim (133)
        EndlineAnim (137)
        EndlineAnim (141)
        EndlineAnim (144)
        EndlineAnim (147)
        EndlineAnim (150)
        EndlineAnim (152)
        EndlineAnim (153)
        EndlineAnim (160)

        #forth row
        EndlineAnim (182)

        for x in (range(187,194)) :
                EndlineAnim (x)

        for x in (range(197, 202)) :
                EndlineAnim (x)

        EndlineAnim (204)
        EndlineAnim (210)
        EndlineAnim (212)
        EndlineAnim (215)

        for x in (range(221, 225)) :
                EndlineAnim (x)

        #fifth row
        EndlineAnim (247)
        EndlineAnim (242)
        EndlineAnim (253)
        EndlineAnim (197)
        EndlineAnim (261)
        EndlineAnim (208)
        EndlineAnim (257)
        EndlineAnim (264)
        EndlineAnim (272)
        EndlineAnim (264)
        EndlineAnim (277)
        EndlineAnim (269)
        EndlineAnim (285)

        #sixth row
        EndlineAnim (302)
        EndlineAnim (307)
        EndlineAnim (313)
        EndlineAnim (317)
        EndlineAnim (321)
        EndlineAnim (324)
        EndlineAnim (330)
        EndlineAnim (332)
        EndlineAnim (264)
        EndlineAnim (270)
        EndlineAnim (338)

        for x in (range(340, 345 )) :
                EndlineAnim (x)

#User Input for distance
def InputDistance():
  while True:
    try:
       distance = int(input("Enter the danger distance in inch: "))       
    except ValueError:
       print("Not a number try again: ")
       continue
    if distance<0:
        print("Invalid input!! PLEASE INPUT A POSTIVE NUMBER")
        continue
    elif distance>155:
        print("Excedes the range, PLEASE INPUT A VALUE BELOW 155 INCH")
        continue
    else:
       break
  return distance

distance=InputDistance()
#SETUP
try:
  connection = SerialManager('COM3')
  board = ArduinoApi(connection=connection)
except:
    print("Connection Failed")
    sys.exit(1)
my_led=[(0,0,0)]*360
#Start Animation
def lineAnim (b,x) :
    one= random.randint(0,256)
    two= random.randint(0,256)
    three= random.randint(0,256)
    my_led[b]=(0,0,0)
    my_led[b+x]= (one,two,three)
    time.sleep(0.01)
    client.put_pixels(my_led)
    time.sleep(0.01)
    client.put_pixels(my_led)

def lineAnimRev (b,x) :
    one= random.randint(0,256)
    two= random.randint(0,256)
    three= random.randint(0,256)
    my_led[b]=(0,0,0)
    my_led[b-x]= (one,two,three)
    time.sleep(0.01)
    client.put_pixels(my_led)
    time.sleep(0.01)
    client.put_pixels(my_led)

def ResetPixels():
    my_led=[(0,0,0)]*360
    return my_led


for b in range (0,15):
        for x in range (0,7) :
                lineAnim (b,x)

my_led=ResetPixels()
#Horizontal animation

#outer loop is range of animation
#inner loop is for length of the animation
for b in range (128,134):
        for x in range (0,7) :
                lineAnim (b,x)

my_led=ResetPixels()


for x in reversed(range(250,246)):
        for x in range (0,5) :
                lineAnimRev (b,x)

my_led=ResetPixels()


for b in range (306,315):
        for x in range (0,10) :
                lineAnim (b,x)

my_led=ResetPixels()


for b in range (76,83):
        for x in range (0,8) :
                lineAnim (b,x)

my_led=ResetPixels()


for b in reversed (range (202,200)):
        for x in range (0,7) :
                lineAnimRev (b,x)

my_led=ResetPixels()


for b in reversed (range (142,138)):
        for x in range (0,7) :
                lineAnimRev (b,x)

my_led=ResetPixels()


for b in range (100,114):
        for x in range (0,7) :
                lineAnim (b,x)

my_led=ResetPixels()



for b in reversed (range (360,350)):
        for x in range (0,7) :
                lineAnimRev (b,x)

my_led=ResetPixels()



for b in range (168,173):
        for x in range (0,7) :
                lineAnim (b,x)

my_led=ResetPixels()


for b in reversed (range (304,300)):
        for x in range (0,5) :
                lineAnimRev (b,x)

my_led=ResetPixels()


for b in reversed (range (330,338)):
        for x in range (0,8) :
                lineAnimRev (b,x)

my_led=ResetPixels()


for b in range (54,58):
        for x in range (0,4) :
                lineAnim (b,x)

my_led=ResetPixels()


for b in reversed (range (24,30)):
        for x in range (0,6) :
                lineAnimRev (b,x)

my_led=ResetPixels()


for b in reversed (range (260,266)):
        for x in range (0,6) :
                lineAnimRev (b,x)

my_led=ResetPixels()

for b in range (56,63) :
        for x in range (0,7) :
                lineAnim (b,x)

my_led=ResetPixels()

for b in reversed (range (295,303)):
        for x in range (0,8) :
                lineAnimRev (b,x)

my_led=ResetPixels()

#Taking reading on echo pin
#Initialise Sensor Pins
duration = Ultrasonic(echoPin, trigPin, True, connection=connection)
tone= Tone(alarm, connection=connection)
#Initialise the leds Pins
board.pinMode(greenLed,board.OUTPUT)
board.pinMode(redLed,board.OUTPUT)
board.pinMode(yellowLed,board.OUTPUT)
#Default LED
board.digitalWrite(greenLed, board.HIGH)
board.digitalWrite(yellowLed, board.LOW)
board.digitalWrite(redLed, board.LOW)
while True:
        try:

  #Converting the time to distance
          inches = duration.get_distance()
          print(inches, end='')
          print(" inch")
          if inches < distance:
                  print("DANGER, PLEASE REVERT BACK NOW!")
                  board.digitalWrite(greenLed, board.LOW)
                  board.digitalWrite(yellowLed, board.LOW)
                  board.digitalWrite(redLed, board.HIGH)
                  sleep(0.01)
                  board.digitalWrite(redLed, board.LOW)
                  sleep(0.01)
                  board.digitalWrite(redLed, board.HIGH)
                  Danger()
                  sleep(0.01)
                  tone.play(3000,1)
                  
          elif inches <(distance+10):
                  print("APPROACHING DANGER, PLEASE REVERT BACK")
                  board.digitalWrite(greenLed, board.LOW)
                  board.digitalWrite(redLed, board.LOW)
                  board.digitalWrite(yellowLed, board.HIGH)
                  YellowAnimation()
                  sleep(0.01)
                  board.digitalWrite(yellowLed, board.LOW)
                  sleep(0.01)
                  board.digitalWrite(yellowLed, board.HIGH)
                  tone.stop()
                  
          else:
                  print("GOOD, STAY SAFE")
                  board.digitalWrite(greenLed, board.HIGH)
                  board.digitalWrite(yellowLed, board.LOW)
                  board.digitalWrite(redLed, board.LOW)
                  GreenLED()
                  tone.stop()
                  
          sleep(0.002)
        except KeyboardInterrupt:
                print('\n',"        ********************Program terminated********************")
                board.digitalWrite(greenLed, board.LOW)
                board.digitalWrite(yellowLed, board.LOW)
                board.digitalWrite(redLed, board.LOW)
                tone.stop()
                my_led=[(0,0,0)]*360
                client.put_pixels(my_led)
                EndAnimation()
                my_led=[(0,0,0)]*360
                client.put_pixels(my_led)
                break
                
