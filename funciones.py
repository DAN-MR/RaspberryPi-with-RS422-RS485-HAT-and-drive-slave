import serial
import serial.rs485
from crc import crc16
from listaDeComandos import listaDeComandos
from datetime import datetime


ser=serial.rs485.RS485(port='/dev/ttyAMA0',baudrate=9600,timeout=1)
ser.rs485_mode = serial.rs485.RS485Settings(False,True)


def read_parametro(comando):                              #Array de launcion base leer frecuencia de salida
    array_final = listaDeComandos[comando]["array"]       #creamos array_final, a partir de array_datos
    CRC = crc16().createcrc(array_final)                  #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final. 
    CRC_izq = (CRC >> 8)                                  #CRC bajo (el primero)
    CRC_der = (CRC & 0xff)                                #CRC alto (el segundo)   
    array_final.append(CRC_izq)                           #Añadimos CRC bajo, al array que acabamos de crear.
    array_final.append(CRC_der)                           #Añadimos CRC alto, al array que acabamos de crear, completando el array y la palabra de control.    
 
    ser.write(array_final)                                #Envio pregunta al Drive

    x = ser.read(7)                                       # x = datos recibidos
    if len(x) < 7:                                        #verificación de los datos de lectura recibidos
        print('error de comunicacion')
        return False

    array_funcion_v = x[0:5]                                                        #Los datos recibidos del drive, calculamos generando nuevamente el CRC. 
    CRC = crc16().createcrc(array_funcion_v)                                        #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final. 
    CRC_izq_v = (CRC >> 8)                                                          #CRC bajo (el primero)
    CRC_der_v = (CRC & 0xff)                                                        #CRC alto (el segundo)     
    y = array_funcion_v + CRC_izq_v.to_bytes(1,"big") + CRC_der_v.to_bytes(1,"big") # y = array_final, a partir de array_datos
                                                                                    #CRC bajo, al array que acabamos de crear.
                                                                                    #CRC alto, al array que acabamos de crear, completando el array y la palabra de control.    
    print(f'comprobacion mensaje devuelto:\n{x}\n{y}')
    
    if x[5] == y[5] and x[6] == y[6]: print("mensaje ok")
    parametro = (x[3]*256+x[4]) / listaDeComandos[comando]["factor"]
    
    print(f"Variador: {x[0]} - {comando}: {parametro} ")
    
    now = datetime.now()  #date and time format: dd/mm/YYYY H:M:S
    format = "%d/%m/%Y %H:%M:%S"   #format datetime using strftime() 
    time1 = now.strftime(format)
    with open("variador.log", "a") as file:
        file.write(f"{time1} - Variador: {x[0]} - {comando}: {parametro}\n")
    
    return True
   
    