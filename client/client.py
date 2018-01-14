import socket
import time
import keyboardstatus
import request
import jsonpickle

class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.keyboard_status = keyboardstatus.KeyboardStatus()
            

    def create_socket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def update_keyboard_status(self):
        self.keyboard_status.update_key_statuses()

    def create_message(self):
        request_message = request.Request(self.keyboard_status)
        return jsonpickle.encode(request_message)

    def run(self):
        BUFFER_SIZE = 1024

        while True:
            s = self.create_socket()
            s.connect((self.host, self.port))
            self.update_keyboard_status()
            s.send(self.create_message().encode())
            data = s.recv(BUFFER_SIZE)
            s.close()
            time.sleep(1)

x = Client('192.168.1.11', 5000)
x.run()
