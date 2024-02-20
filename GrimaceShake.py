print("********************************************")
print("Gasoline Branch\n\n")

#import libraries here
import random

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
    milesToGasStationLow = random.uniform(1,25)
    milesToGasStationQuarterTank = random.uniform(25.1,50)

    print(milesToGasStationLow)
    print(milesToGasStationQuarterTank)


print(gasLevelGauge())
print(listOfGasStations())