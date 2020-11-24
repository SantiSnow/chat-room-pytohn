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



