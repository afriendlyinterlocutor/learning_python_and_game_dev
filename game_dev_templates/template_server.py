import socket
from _thread import *
import sys

server = "xxx.xxx.xx.xxx"
port = 5555

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    socket.bind((server, port))
except socket.error as e:
    str(e)

socket.listen(2)
print("Waiting for a connection, Server Started")


def threaded_client(connection):
    reply = ""
    while True:
        try:
            data = connection.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print("Disconnected")
                break
            else:
                print("Received: ", reply)
                print("Sending: ", reply)

            connection.sendall(str(reply))
        except:
            break

    print("Lost connection")
    connection.close()


while True:
    conn, addr = socket.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
