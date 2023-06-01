# import usocket as socket
import socket

# Agregar nport de donde está el servidor TCP, en el ejemplo: 3000
serverAddressPort = socket.getaddrinfo('0.0.0.0', 3000)[0][-1]
# Cantidad de bytes a recibir
bufferSize  = 128

# Descomentar si el esp32 será una estación
# from wifiSTA import connectSTA as connect

# Descomentar si el esp32 estará en modo de acceso AP
from wifiAP import apConfig as connect

# poner acá el nombre de red ssid y password para conectarse
connect("miRed", "87654321")

# Esta función es de ejemplo,
# Lo que se plantea acá es saber qué hacer con el dato recibido
# En el ejemplo solo se está imprimiendo por terminal
def exec(data):
    print(data)
    if data == b'A':
        print("Arriba")
    elif data == b'B':
        print("Abajo")
    elif data == b'C':
        print("Izquierda")
    elif data == b'D':
        print("Derecha")
    elif data == b'E':
        print("Detener")
    else:
        print("Otra opcion")

sk = socket.socket()
sk.bind(serverAddressPort)
sk.listen(1)
print("Listening on: ", serverAddressPort)

while True:
    conn, addr = sk.accept()
    while True:
        data = conn.recv(bufferSize)
        # Si dato fue recibido, se decide que hacer con el.
        if data:
            exec(data)
            # Con la siguiente instruccion se pueden enviar datos al
            # dispositivo conectado
            conn.sendall("ok")
            # conn.send("ok")
    conn.close()

