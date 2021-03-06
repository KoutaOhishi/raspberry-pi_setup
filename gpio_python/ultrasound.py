#! /usr/bin/env python
# coding:utf-8

import os
import time
import wiringpi as pi
 
TRIG_PIN = 23
ECHO_PIN = 24

pi.wiringPiSetupGpio()
 
pi.pinMode( TRIG_PIN, pi.OUTPUT )
pi.pinMode( ECHO_PIN, pi.INPUT )
pi.digitalWrite( TRIG_PIN, pi.LOW )
time.sleep( 1 )
 
def mesure():
    pi.digitalWrite( TRIG_PIN, pi.HIGH )
    time.sleep(0.00001)
    pi.digitalWrite( TRIG_PIN, pi.LOW )
    while ( pi.digitalRead( ECHO_PIN ) == pi.LOW ):
        sigoff = time.time()
    while ( pi.digitalRead( ECHO_PIN ) == 1 ):
        sigon = time.time()
    return (( sigon - sigoff ) * 34000) / 2
    
if __name__ == "__main__":
  while True:
      try:
        distance = mesure()
        print ("Distance:", distance )
        time.sleep(0.1)
      except KeyboardInterrupt:
        break
