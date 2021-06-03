import serial
import serial.rs485
from crc import crc16


ser=serial.rs485.RS485(port='/dev/ttyAMA0',baudrate=9600)
ser.rs485_mode = serial.rs485.RS485Settings(False,True)

#    read_Tension_out (coef) = array_funcion = [0x01, 0x03, 0x10, 0x01, 0x00, 0x01] #leer tension
#    read_current_out (coef) = array_funcion = [0x01, 0x03, 0x10, 0x02, 0x00, 0x01] #leer corriente
#    read_speed_status_out (coef): array_funcion = [0x01, 0x03, 0x10, 0x05, 0x00, 0x01] #leer velocidad
#    read_percent_pair_out (coef): array_funcion = [0x01, 0x03, 0x10, 0x06, 0x00, 0x01] #leer par
#    read_Temp_out (coef): array_funcion = [0x01, 0x03, 0x10, 0x07, 0x00, 0x01] #leer 
    
   


def read_freq_out (coef):                                 #Array de launcion base leer frecuencia de salida    
    array_funcion = [0x01, 0x03, 0x10, 0x00, 0x00, 0x01]  #Introducion peticion de la palabra de frecuencia 
    CRC = crc16().createcrc(array_funcion)                #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final. 
    CRC_izq = (CRC >> 8)                                  #CRC bajo (el primero)
    CRC_der = (CRC & 0xff)                                #CRC alto (el segundo)   
    array_final = array_funcion                           #creamos array_final, a partir de array_datos
    array_final.append(CRC_izq)                           #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    array_final.append(CRC_der)                           #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.    
    ser.write(array_final)                                #Envio al drive del conjunto de la palabra entera con el CRC
    print('mensaje enviado al drive',array_final)
    x= ser.read(7)
    x= ser.read(4)
    print('mensaje devuelto del drive',x)
    z =[x[0],x[1],x[2],x[3],x[4]]
    array_funcion_v = z
    CRC = crc16().createcrc(array_funcion_v)              #Calculamos el CRC de array_datos y se le añade al final, convirtiendolo en array_final. 
    CRC_izq_v = (CRC >> 8)                                #CRC bajo (el primero)
    CRC_der_v = (CRC & 0xff)                              #CRC alto (el segundo)     
    y = array_funcion_v                                   #creamos array_final, a partir de array_datos
    y.append(CRC_izq_v)                                   #Aqui añadimos el CRC bajo, al array que acabamos de crear.
    y.append(CRC_der_v)                                   #Aqui añadimos el CRC alto, al array que acabamos de crear, completando el array y la palabra de control.    
    print('comprobacion mensaje devuelto',y)
    
    if [x[5],x[6]] == [y[5],y[6]]:
        print("mensaje ok")
        print("velocidad",50,"%")
    else:
        print("mensaje no ok")
    
   
      
    
  
    
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
    
