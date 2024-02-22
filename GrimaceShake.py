<<<<<<< HEAD

#Import Libraries Here
import time
import sys
import random
from time import sleep

#Welcome branch starts here
timeToSleep = 1

print("\n\nWelcome to Info Tech center version 1.0\n")
time.sleep(timeToSleep)

#Code to have the ellipsis add a dot every .5 seconds
x = 0
ellipsis = 0

while x != 20:
    x += 1
    message = ("Info Tech Center Operating System Grimacing" + "." * ellipsis)
    ellipsis = ellipsis + 1
    sys.stdout.write("\r" + message) # \r prints a carriage return first
    time.sleep(.5)
    if ellipsis == 4:
        ellipsis = 0
    if x == 20:
        print("\n\nOperating System Has Grimaced Up- Retina Scanned - Access Grimaced\n")

#gasoline branch starts here
print("*******************************************************************\n")
print("Gasoline Branch\n\n")

def gasLevelGauge():
    gasLevelList = ["Empty", "Low", "Quarter Tank", "Half Tank","Three Quarter Tank", "Full Tank"]
    currentGasLevel = random.choice(gasLevelList)
    return currentGasLevel

#Funtion that lists gas stations, randomly choosing one and returning its value

def listOfGasStations():
    gasStations = ["Shell", "Speedway", "Kum And Go", "Circle K", "Moble", "Costco", "meijor", "7Eleven"]
    gasStationsNearby = random.choice(gasStations)
    return gasStationsNearby

def gasLevelAlert():
    milesToGasStationLow = round(random.uniform(1,25),1)
    milesToGasStationQuarterTank = round(random.uniform(25.1,50),1)
    gasLevelIndicator = gasLevelGauge()
    if gasLevelIndicator == "Empty":
        print("***WARNING - YOU ARE ON EMPTY***")
        sleep(1.25)
        print("Calling Triple AAA")
    elif gasLevelIndicator == "Low":
        print("Your Gas Tank Is Exremely Low, Checking Google Maps For The Nearest Gas Station")
        sleep(2.5)
        print("The Closest Gas Station Is",listOfGasStations(),"which Is",milesToGasStationLow,"Miles Away." )
    elif gasLevelIndicator == "Quarter Tank":
        print("Your Gas Tank Is On A Quarter Tank, Checking Google Maps For The Nearest Gas Station")
        sleep(2.5)
        print("The Closest Gas Station Is",listOfGasStations(),"which Is",milesToGasStationLow,"Miles Away." )
    elif gasLevelIndicator == "Half Tank":
        print("Your Gas Tank Is Halfway Full Which Is Plenty To Get Were You Need To Go.")
    elif gasLevelIndicator == "Three Quarter Tank":
         print("Your Gas Tank Is 3 Quarters Full.")
    else:
        print("Full Tank, Nice.")

gasLevelAlert()

