import socket

HOST = '127.0.0.1'
PORT = 5000
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

connection, address = s.accept()
print('Connection address: ', address)

while True:
    data = connection.recv(BUFFER_SIZE)
    if not data:
        break
    print("Reiceived data", data)
    connection.send(data) #echo

connection.close()