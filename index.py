import time
import RPi.GPIO as GPIO
from time import sleep
import funciones


#while True:

#funciones.write_temp_acc (10, 3.6)

def cuenta():
    cuenta.numero += 1
    return cuenta.numero
cuenta.numero = 0

for i in range(50):
  
    
    funciones.read_freq_out(1)

   
    print(cuenta())

             # Valor real x100
#funciones.read_current_out (1)         # Valor real x100
#funciones.read_Tension_out (1)         # Valor real x1
#funciones.read_speed_status_out (1)    # Valor real x100
#funciones.read_percent_pair_out (1) 
#funciones.read_Temp_out (1)            # Valor real x10


  