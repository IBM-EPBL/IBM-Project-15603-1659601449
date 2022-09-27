import time
import random
while True:
    temperature = random.randint(1,100)
    humidity = random.randint(1,100)
    print("Current temperature:",temperature)
    print("Current Humidity:",humidity)
    if (temperature > 37 and humidity < 37):        
        print("Alarm Rings")
        time.sleep(2)
    else:
        print("normal state")
        time.sleep(2)
