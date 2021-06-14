import time
import RPi.GPIO as GPIO
from time import sleep
import funciones
from listaDeComandos import listaDeComandos

#funciones.write_temp_acc (10, 3.6)

while True:
    for comando in listaDeComandos:
        respuesta = funciones.read_parametro(comando)
        if not respuesta:
            time.sleep(10) # si hay un error agregar tiempo de espera de 10 segundos
            break # interrumpir el lazo de lectura de parametros
        time.sleep(1)
    time.sleep(15)
  


# Valor real x100
#funciones.read_current_out (1)         # Valor real x100
#funciones.read_Tension_out (1)         # Valor real x1
#funciones.read_speed_status_out (1)    # Valor real x100
#funciones.read_percent_pair_out (1) 
#funciones.read_Temp_out (1)            # Valor real x10


  