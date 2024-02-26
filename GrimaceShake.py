print("\n***************************************************************************************")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherforcast = ["Snowing", "Blizzards", "Raining", "Foggy", "Windy", "Icy", "Sunny"]
    weatherConditions = random.choice(weatherforcast)
    return weatherConditions

print(weather())