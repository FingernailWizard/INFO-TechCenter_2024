print("\n***************************************************************************************")

print("Weather Branch\n")

#Import Libraries Here
import random
from time import sleep

def weather():
    weatherforcast = ["Snowing", "Blizzard", "Raining", "Foggy", "Windy", "Icy", "Sunny"]
    weatherConditions = random.choice(weatherforcast)
    return weatherConditions

# Variable to call the weather() once VRS(vehicle response system) is determined
weatherAlert = weather()

def vehicleRepsonseSystem():
    if weatherAlert == "Snowing":
        print("\nNational Weather Service has updated our alarm by 30 minutes because of the the forcast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 50mph")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service has updated our alarm by 45 minutes because of the the forcast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 40mph")
    elif weatherAlert == "raining":
        print("\nNational Weather Service has updated our alarm by 10 minutes because of the the forcast of",weatherAlert,
              "weather conditions.")
        print("VRS has been engaged only allowing you to drive 60mph")

vehicleRepsonseSystem()