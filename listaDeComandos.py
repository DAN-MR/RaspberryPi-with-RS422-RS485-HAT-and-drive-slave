
listaDeComandos = {          #dir  #leer #cmdh #cmdl #rech #recl
    "frecuencia":   {"array": [0x01, 0x03, 0x10, 0x00, 0x00, 0x01], "factor": 100}, #leer frecuencia de salida
    "tension":      {"array": [0x01, 0x03, 0x10, 0x01, 0x00, 0x01], "factor": 1},   #leer tensión de salida
    "corriente":    {"array": [0x01, 0x03, 0x10, 0x02, 0x00, 0x01], "factor": 100}, #leer corriente de salida
    "numero polos": {"array": [0x01, 0x03, 0x10, 0x03, 0x00, 0x01], "factor": 100}, #leer nuemro de polos/modo control
    "tension bus":  {"array": [0x01, 0x03, 0x10, 0x04, 0x00, 0x01], "factor": 100}, #leer tensión del Bus
    "velocidad":    {"array": [0x01, 0x03, 0x10, 0x05, 0x00, 0x01], "factor": 100}, #leer velocidad de salida (media de las fases)
    "par":          {"array": [0x01, 0x03, 0x10, 0x06, 0x00, 0x01], "factor": 1},   #leer el porcentage del par de salida
    "temperatura":  {"array": [0x01, 0x03, 0x10, 0x07, 0x00, 0x01], "factor": 1},   #leer la temperatura del radiador del drive
    "valor PID":    {"array": [0x01, 0x03, 0x10, 0x08, 0x00, 0x01], "factor": 1},   #leer valor proporcionado del PID
    "velocidad act."{"array": [0x01, 0x03, 0x10, 0x17, 0x00, 0x01], "factor": 1}    #leer coontrol de la velocidad actual
    
    }