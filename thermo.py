# pretends there is an oven, and a thermostat.
import time
import random

temperature = 40.0

print("start the oven")
while temperature < 100.0:
    print("temperature is: " + str(temperature) + " celcius")
    print("raising temperature")
    time.sleep(1)
    temperature += 10.0 * random.random()
print("the pot is boiling")
print("temperature is: " + str(temperature) + " celcius")
print("stop the oven")
