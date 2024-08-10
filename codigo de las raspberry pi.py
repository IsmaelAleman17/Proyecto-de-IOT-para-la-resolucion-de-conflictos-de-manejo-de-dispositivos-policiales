import socket
import RPi.GPIO as GPIO
import time

# Configuración de los pines GPIO para los LEDs
# Supongamos que el LED para conexión está en el pin 17 y el LED para dato entrante en el pin 23
LED_CONEXION = 17
LED_DATO_ENTRANTE = 23

# Configuramos los pines GPIO como salida
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_CONEXION, GPIO.OUT)
GPIO.setup(LED_DATO_ENTRANTE, GPIO.OUT)

# Inicialmente los LEDs están apagados
GPIO.output(LED_CONEXION, GPIO.LOW)
GPIO.output(LED_DATO_ENTRANTE, GPIO.LOW)

# Creamos un socket para recibir el dato
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Conectamos al socket con la IP y puerto que utilizamos en el código anterior
sock.bind(("192.168.0.12", 8080))

# Escuchamos conexiones
sock.listen(1)

print("Esperando conexiones...")

# Creamos una lista para almacenar los datos recibidos
datos_recibidos = []

while True:
    # Aceptamos la conexión
    conn, addr = sock.accept()
    print("Conexión establecida con", addr)
    
    # Encendemos el LED de conexión
    GPIO.output(LED_CONEXION, GPIO.HIGH)
    
    while True:
        # Recibimos el dato
        data = conn.recv(1024)
        if not data:
            break
        print("Dato recibido:", data.decode())
        
        # Encendemos el LED de dato entrante durante un breve período
        GPIO.output(LED_DATO_ENTRANTE, GPIO.HIGH)
        time.sleep(0.5)  # Pausa de medio segundo
        GPIO.output(LED_DATO_ENTRANTE, GPIO.LOW)
        
        # Agregamos el dato a la lista
        datos_recibidos.append(data.decode())

        # Procesamos los datos recibidos (por ejemplo, imprimimos la lista)
        print("Datos recibidos hasta ahora:", datos_recibidos)

    # Cerramos la conexión (opcional, pero recomendado para liberar recursos)
    # conn.close()
    
    # Apagamos el LED de conexión
    GPIO.output(LED_CONEXION, GPIO.LOW)

# Limpieza de los pines GPIO al finalizar (importante para evitar daños)
GPIO.cleanup()