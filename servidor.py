import socket

mi_socket = socket.socket()
mi_socket.bind(('localhost', 8000))
mi_socket.listen(5)

while True:
    conexion, addr = mi_socket.accept()
    print ("Nueva conexión establecida")
    print(addr)

    peticion = conexion.recv(1024)
    print (peticion.decode('utf-8'))

    mensaje_envio = 'Hola, te saludo desde el servidor'

    conexion.send(mensaje_envio.encode('utf-8'))
    conexion.close()
