import time
import serial
import serial.rs485
import RPi.GPIO as GPIO
from time import sleep
import crc


#GPIO.setwarning(false)
#GPIO.setmode(GPIO.BOARD) #Utilizar los pines de la tarjeta, es posible que el procesador tengo otros pines con otros nombres, por comodidad usaremos los de la tarjeta.
#GPIO.setup(7, GPIO.OUT, initial=GPIO.HIGH) #usamos el pin 7 (GPIO4) como Salida, empieza en High.
#GPIO.output(pin, GPIO.HIGH)


ser=serial.rs485.RS485(port='/dev/ttyAMA0',baudrate=9600)
ser.rs485_mode = serial.rs485.RS485Settings(False,True)

def temp_acc (tiempo_acc):
    array = array1
    CRC = hex(test.createcrc(array))
    print(CRC.upper(), "\n")
    array1 = test.createarray(array)
    
    #ser.write(array1)
    #respuesta = ser.read(8)
    ##respuesta =respuesta.replace("\x", ", 0x")
    ##print (respuesta)
    



#temp_acc (1)

#while True:
    #c = ser.read(1)
    #ser.write(c)
    #print(c, end='')
