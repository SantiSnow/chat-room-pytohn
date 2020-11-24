import threading
import socket

host = '127.0.0.1'  # locahost
port = 55555

# creacion del socket server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('127.0.0.1', 55555))
server.listen()

clients = []
nicks = []


def broadcast(mensaje):
    for i in clients:
        i.send(mensaje)


def manejoclientes(client):
    while True:
        try:
            mensaje = client.recv(2048)
            broadcast(mensaje)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicks[index]
            nicks.remove(nickname)
            broadcast(f'{nickname} ha abandonado la sala'.encode('ascii'))
            break


def receive():
    while True:
        client, address = server.accept()
        print(f"Se ha conectado correctamente con direccion {str(address)}")

        client.send('NICK'.encode('ascii'))
        nickname = client.recv(2048).decode('ascii')

        nicks.append(nickname)
        clients.append(client)

        print(f"El nick del cliente es {nickname}")
        broadcast(f"{nickname} se ha unido a la sala de chat!".encode('ascii'))
        client.send("Conectado correctamente a la sala de chat!".encode('ascii'))

        thread1 = threading.Thread(target=manejoclientes, args=(client,))
        thread1.start()


print("El servidor ya esta activo")
receive()

