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
        print("\nNational Weather Service Has Updated Our Alarm By 30 Minutes Because Of The Forcast Of",weatherAlert,
              "Weather Conditions.")
        sleep(1.5)
        print("VRS Has Been Engaged Only Allowing You To Drive 50mph")
    elif weatherAlert == "Blizzard":
        print("\nNational Weather Service Has Updated Our Alarm By 45 Minutes Because Of The Forcast Of",weatherAlert,
              "Weather Conditions.")
        sleep(1.5)
        print("VRS Has Been Engaged Only Allowing You To Drive 40mph")
    elif weatherAlert == "Raining":
        print("\nNational Weather Service Has Updated Our Alarm By 10 Minutes Because Of The Forcast Of",weatherAlert,
              "Weather Conditions.")
        sleep(1.5)
        print("VRS Has Been Engaged Only Allowing You To Drive 60mph")
    elif weatherAlert == "Foggy":
        print("\nNational Weather Service Has Updated Our Alarm By 10 Minutes Because Of The Forcast Of",weatherAlert,
              "Weather Conditions.")
        sleep(1.5)
        print("VRS Has Been Engaged Only Allowing You To Drive 60mph")
    elif weatherAlert == "Windy":
        print("\nNational Weather Service Has Updated Our Alarm By 5 Minutes Because Of The Forcast Of",weatherAlert,
              "Weather Conditions.")
        sleep(1.5)
        print("VRS Has Been Engaged Only Allowing You To Drive 80mph")
    elif weatherAlert == "Icy":
        print("\nNational Weather Service Has Updated Our Alarm By 60 Minutes Because Of The Forcast Of",weatherAlert,
              "Weather Conditions.")
        sleep(1.5)
        print("VRS Has Been Engaged Only Allowing You To Drive 30mph")
    else:
        print("\nNational Weather Service Has Updated Our Alarm By 0 Minutes Because Of The Forcast Of",weatherAlert,
              "Weather Conditions.")
        sleep(1.5)
        print("VRS Has Been Engaged Only Allowing You To Drive MAXmph")


vehicleRepsonseSystem()