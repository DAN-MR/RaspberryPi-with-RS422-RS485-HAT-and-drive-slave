import serial
import serial.rs485

from crc import crc16


ser=serial.rs485.RS485(port='/dev/ttyAMA0',baudrate=9600)
ser.rs485_mode = serial.rs485.RS485Settings(False,True)


def read_freq_out (coef): 
    
    #Array de launcion base leer frecuencia de salida
    
    array_funcion = [0x01, 0x03, 0x10, 0x00, 0x00, 0x01]
       
    #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final.
    
    CRC = crc16().createcrc(array_funcion)
    
    CRC_izq = (CRC >> 8)   #CRC bajo (el primero)
    CRC_der = (CRC & 0xff) #CRC alto (el segundo
        
    
    print(hex(CRC_izq)) 
    print(hex(CRC_der)) 
    
    array_final = array_funcion   #creamos array_final, a partir de array_datos
    array_final.append(CRC_izq)   #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    array_final.append(CRC_der)   #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.
    
    print(array_final)
    ser.write(array_final)
    respuesta_drive = ser.read(7)
    print(respuesta_drive)
    
    #comprovación de la respuesta
    #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final.
def read_freq_out_drive (coef):

    CRC = crc16().createcrc(respuesta_drive)
    
    CRC_izq_d = (CRC >> 8)   #CRC bajo (el primero)
    CRC_der_d = (CRC & 0xff) #CRC alto (el segundo
    
    print(hex(CRC_izq_d)) 
    print(hex(CRC_der))
    
    array_drive = respuesta_drive
    array_drive.append(CRC_izq_d)   #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    array_drive.append(CRC_der_d)   #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.
    
    print(array_drive)
    #ser.write(array_drive)
    #respuesta_drive = ser.read(7)
    print(respuesta_drive)
    
    
    
    
    
def read_Tension_out (coef): 
    
    #Array de launcion base (en este caso cambiar el tiempo de acceleracion)
    
    array_funcion = [0x01, 0x03, 0x10, 0x01, 0x00, 0x01]
       
    #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final.
    
    CRC = crc16().createcrc(array_funcion)
    
    CRC_izq = (CRC >> 8)   #CRC bajo (el primero)
    CRC_der = (CRC & 0xff) #CRC alto (el segundo
        
   # print(hex(CRC_izq)) 
   # print(hex(CRC_der)) 
    
    array_final = array_funcion   #creamos array_final, a partir de array_datos
    array_final.append(CRC_izq) #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    array_final.append(CRC_der) #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.
    
    
    #print(array_final)
    ser.write(array_final)
    respuesta = ser.read(7)
    print(respuesta)

def read_current_out (coef): 
    
    #Array de launcion base (en este caso cambiar el tiempo de acceleracion)
    
    array_funcion = [0x01, 0x03, 0x10, 0x02, 0x00, 0x01]
       
    #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final.
    
    CRC = crc16().createcrc(array_funcion)
    
    CRC_izq = (CRC >> 8)   #CRC bajo (el primero)
    CRC_der = (CRC & 0xff) #CRC alto (el segundo
        
    #print(hex(CRC_izq)) 
    #print(hex(CRC_der)) 
    
    array_final = array_funcion   #creamos array_final, a partir de array_datos
    array_final.append(CRC_izq) #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    array_final.append(CRC_der) #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.
    
    
    #print(array_final)
    ser.write(array_final)
    respuesta = ser.read(7)
    print(respuesta)

def read_speed_status_out (coef): 
    
    #Array de launcion base (en este caso cambiar el tiempo de acceleracion)
    
    array_funcion = [0x01, 0x03, 0x10, 0x05, 0x00, 0x01]
       
    #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final.
    
    CRC = crc16().createcrc(array_funcion)
    
    CRC_izq = (CRC >> 8)   #CRC bajo (el primero)
    CRC_der = (CRC & 0xff) #CRC alto (el segundo
        
    print(hex(CRC_izq)) 
    print(hex(CRC_der)) 
    
    array_final = array_funcion   #creamos array_final, a partir de array_datos
    array_final.append(CRC_izq) #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    array_final.append(CRC_der) #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.
    
    
    print(array_final)
    ser.write(array_final)
    respuesta = ser.read(7)
    print(respuesta)
    
def read_percent_pair_out (coef): 
    
    #Array de launcion base (en este caso cambiar el tiempo de acceleracion)
    
    array_funcion = [0x01, 0x03, 0x10, 0x06, 0x00, 0x01]
       
    #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final.
    
    CRC = crc16().createcrc(array_funcion)
    
    CRC_izq = (CRC >> 8)   #CRC bajo (el primero)
    CRC_der = (CRC & 0xff) #CRC alto (el segundo
        
    print(hex(CRC_izq)) 
    print(hex(CRC_der)) 
    
    array_final = array_funcion   #creamos array_final, a partir de array_datos
    array_final.append(CRC_izq) #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    array_final.append(CRC_der) #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.
    
    
    print(array_final)
    ser.write(array_final)
    respuesta = ser.read(7)
    print(respuesta)
    
def read_Temp_out (coef): 
    
    #Array de launcion base (en este caso cambiar el tiempo de acceleracion)
    
    array_funcion = [0x01, 0x03, 0x10, 0x07, 0x00, 0x01]
       
    #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final.
    
    CRC = crc16().createcrc(array_funcion)
    
    CRC_izq = (CRC >> 8)   #CRC bajo (el primero)
    CRC_der = (CRC & 0xff) #CRC alto (el segundo
        
    print(hex(CRC_izq)) 
    print(hex(CRC_der)) 
    
    array_final = array_funcion   #creamos array_final, a partir de array_datos
    array_final.append(CRC_izq) #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    array_final.append(CRC_der) #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.
    
    
    print(array_final)
    ser.write(array_final)
    respuesta = ser.read(7)
    print(respuesta)
    
    
    #Parametros de escritura 
    
    
def write_temp_acc (coef, tiempo_acc):
    
    #Array de la f  uncion base (en este caso cambiar el tiempo de acceleracion)
    
    array_funcion = [0x01, 0x06, 0x01, 0x0E]
    
    #Calculamos los datos de "acceleracion" y se añade al array_funcion, conviertendolo en array_datos.

    dato=int(tiempo_acc * coef) 
    dato_izq = (dato >> 8)   #dato bajo (el primero)
    dato_der = (dato & 0xff) #dato alto (el segundo)
      
    array_datos = array_funcion  #creamos array_datos, a partir de array_funcion
    array_datos.append(dato_izq) #Aqui añadimos el dato bajo, al array que acabamos de crear.
    array_datos.append(dato_der) #Aqui añadimos el dato alto, al array que acabamos de crear, completando el array.
   
    #print(array_datos)
   
    #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final.
    
    CRC = crc16().createcrc(array_datos)
    
    CRC_izq = (CRC >> 8)   #CRC bajo (el primero)
    CRC_der = (CRC & 0xff) #CRC alto (el segundo
        
    #print(CRC_izq) 
    #print(CRC_der) 
    
    array_final = array_datos   #creamos array_final, a partir de array_datos
    array_final.append(CRC_izq) #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    array_final.append(CRC_der) #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.
    
    
    #print(array_final)
    ser.write(array_final)
    respuesta = ser.read(8)
    