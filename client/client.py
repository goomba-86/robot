import socket
import time

class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
    
    def run(self):
        BUFFER_SIZE = 1024
        MESSAGE = 'Hello, World!'
        
        while True:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((self.host, self.port))
            s.send(MESSAGE.encode())
            data = s.recv(BUFFER_SIZE)
            s.close()
            print("Received data: ", data)
            time.sleep(1)

x = Client('127.0.0.1', 5000)
x.run()