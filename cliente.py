import socket

mi_socket = socket.socket()
mi_socket.connect(('localhost', 8000))

mensaje_enviar = 'Hola desde el cliente!'

mi_socket.send(mensaje_enviar.encode('utf-8'))

respuesta  = mi_socket.recv(1024)

print(respuesta.decode('utf-8'))
mi_socket.close()