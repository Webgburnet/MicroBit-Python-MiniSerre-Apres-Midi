from microbit import *
import utime
import machine

def distance_cm():
    pin0.write_digital(0)
    utime.sleep_us(2)
    pin0.write_digital(1) #Emission d'une impulsion US
    utime.sleep_us(5)
    pin0.write_digital(0)
    pin0.read_digital() #Ecoute de l'echo
    temps=machine.time_pulse_us(pin0,1,1000000) #Mesure du temps de la reception de l'écho
    return temps*0.0169+0.55    #Calcul de la distance de l'obstacle 
                                #avec prise en compte de l'aller retour de l'onde
while True:
    display.scroll(distance_cm())
    sleep(500)
