import socket
import time
import keyboardstatus
import request
import jsonpickle
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class Client:

    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.image_name = 'image.jpg'
        self.keyboard_status = keyboardstatus.KeyboardStatus()
        plt.ion()
        plt.show()
            

    def create_socket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def update_keyboard_status(self):
        self.keyboard_status.update_key_statuses()

    def create_message(self):
        request_message = request.Request(self.keyboard_status)
        return jsonpickle.encode(request_message)

    def write_image(self, bytes):
        image_file = open(self.image_name, 'wb')
        image_file.write(bytes)
        image_file.close()

    def show_image(self):
        try:
            img = mpimg.imread(self.image_name)
            imgplot = plt.imshow(img)
            plt.pause(0.001)
        except IOError:
            print('Unable to plot the image')
    
    def run(self):
        BUFFER_SIZE = 1024

        while True:
            s = self.create_socket()
            s.connect((self.host, self.port))
            self.update_keyboard_status()
            s.send(self.create_message().encode())

            data = ''
            while True:
                temp = s.recv(BUFFER_SIZE)
                data += temp
                if len(temp) < BUFFER_SIZE:
                    break
                time.sleep(0.01)
            
            print('Received ' + str(len(data)) + ' bytes from server.')
            self.write_image(data)
            self.show_image()
            s.close()
            time.sleep(0.5)

x = Client('192.168.1.9', 5000)
x.run()
