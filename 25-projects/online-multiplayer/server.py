import socket
import pickle
from _thread import start_new_thread

server = "0.0.0.0"
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((server, port))
s.listen(2)

print("Server started. Waiting for connections...")

positions = [(100, 100), (300, 100)]  # Initial positions for Player 1 and 2


def threaded_client(conn, player):
    conn.send(pickle.dumps(positions[player]))

    while True:
        try:
            data = pickle.loads(conn.recv(2048))
            positions[player] = data

            if not data:
                break

            conn.sendall(pickle.dumps(positions))
        except:
            break

    print("Lost connection to player", player)
    conn.close()


currentPlayer = 0

while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currentPlayer))
    currentPlayer += 1
