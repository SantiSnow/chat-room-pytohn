import socket
import threading

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect(('127.0.0.1', 55555))

nickname = input("Elija un nick para que los usuarios del chat lo vean como su nombre: ")


def recibir():
    while True:
        try:
            mensaje = cliente.recv(2048).decode('ascii')
            if mensaje == 'NICK':
                cliente.send(nickname.encode('ascii'))
            else:
                print(mensaje)
        except:
            print("Ha ocurrido un error inesperado y la conexion va a cerrarse.")
            cliente.close()
            break


def chatear():
    while True:
        mensaje = f'{nickname}: {input("")}'
        cliente.send(mensaje.encode('ascii'))


hiloRecibir = threading.Thread(target=recibir)
hiloEnviar = threading.Thread(target=chatear)

hiloRecibir.start()
hiloEnviar.start()

