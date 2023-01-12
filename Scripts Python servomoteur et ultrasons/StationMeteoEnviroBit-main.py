from microbit import *
import bme280
bme=bme280.bme280()

import log
log.set_labels('temperature', 'pressure', 'humidity', timestamp=log.MINUTES)

def blink(): #fonction pour faire clignoter le pixel central
    display.set_pixel(2,2,6)
    sleep(200)
    display.set_pixel(2,2,0)
    sleep(200)


def log_data():
    log.add({
      'temperature': bme.temperature(),
      'pressure': bme.pressure(),
      'humidity': bme.humidity()
   })
    
while True:
    blink()               #On visualise l'enregistrement d'une donnée à chaque cycle
    log_data()            #Enregistrement des 3 données d'environnement du module envirobit
    sleep(5000)           #Pause de 5s entre chaque enregistrement
    
    
