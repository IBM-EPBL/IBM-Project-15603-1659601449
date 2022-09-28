import random

while True:

   temperature=random.uniform(0.0,70.0)

   humidity=random.uniform(0,50)

   print("Temperature sensed:",temperature)

   print("Humidity sensed:",humidity)

   if (temperature>40 and humidity<50):

     print("Alarm Rings")

   else:

     print("Normal state")
