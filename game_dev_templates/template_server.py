from _thread import *
from template_player import Player
import socket
import pickle


server = "xxx.xxx.xx.xxx"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)

s.listen(2)
print("Waiting for a connection, Server Started")


players = [Player(0, 0, 50, 50, (255, 0, 0)), Player(100, 100, 50, 50, (0, 0, 255))]


def threaded_client(connection, player):
    connection.send(pickle.dumps(players[player]))
    while True:
        try:
            data = pickle.loads(connection.recv(2048))
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]

                print("Received: ", data)
                print("Sending : ", reply)

            connection.sendall(pickle.dumps(reply))
        except socket.error as new_error:
            print(new_error)

    print("Lost connection")
    connection.close()


currentPlayer = 0
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
