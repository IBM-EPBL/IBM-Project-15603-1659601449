import RPi.GPIO as GPIO
import time
  
try:
  def lightTraffic(led1, led2, led3, delay ):
    GPIO.output(led1, 1)
    time.sleep(delay)
    GPIO.output(led1, 0)
    GPIO.output(led2, 1)
    time.sleep(delay)
    GPIO.output(led2, 0)
    GPIO.output(led3, 1)  
    time.sleep(delay)
    GPIO.output(led3, 0)  
  GPIO.setmode(GPIO.BCM)
  button = 19
  GPIO.setup(button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
  Green = 7
  Yellow = 11
  Red = 13
  GPIO.setup(Green, GPIO.OUT)
  GPIO.setup(Yellow, GPIO.OUT)
  GPIO.setup(Red, GPIO.OUT)
  while True:
    input_state = GPIO.input(button)
    if input_state == False:
      print('Button ON')
      lightTraffic(Green, Yellow, Red, 1)
    else: 
      GPIO.output(Green, 0)
      GPIO.output(Yellow, 0)
      GPIO.output(Red, 0)
except KeyboardInterrupt:
  print "Program ends"
finally:
  GPIO.cleanup()
