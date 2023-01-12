from microbit import *
pin1.set_analog_period(20)   # MLI avec période de 20ms

def servo(angle):
    rapport_cyclique = ((118-28)/180) * angle + 28  # calcul du rapport cyclique entre 28 et 118 (2,7-11,5%) 
    #display.scroll(rapport_cyclique)
    pin1.write_analog(rapport_cyclique)             # écriture du rapport cyclique sur la broche P1

while True:
    pot = pin0.read_analog()
    #display.scroll(pot)
    angle = pot /1023 * 180
    print ('angle = ',angle , 'deg')
    servo(angle)                                    # appel de la fonction angle
    sleep(500)