import socket
import time
import keyboardstatus
import request
import jsonpickle
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from threading import Thread

class CommandSender:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.keyboard_status = keyboardstatus.KeyboardStatus()

    def create_socket(self):
        return socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def update_keyboard_status(self):
        self.keyboard_status.update_key_statuses()

    def create_message(self):
        request_message = request.Request(self.keyboard_status)
        return jsonpickle.encode(request_message)

    def run(self):
        s = self.create_socket()
        while True:
            self.update_keyboard_status()
            s.sendto(self.create_message().encode(), (self.host, self.port))
            time.sleep(0.2)

class PictureShower:
    def __init__(self, port):
        self.host = '192.168.1.11'
        self.port = port
        self.image_name = 'image.jpg'
        plt.ion()
        plt.show()
            
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
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.host, self.port))
        BUFFER_SIZE = 1024
        while True:
            data = ''
            while True:
                temp, addr = s.recvfrom(BUFFER_SIZE)
                data += temp
                if len(temp) < BUFFER_SIZE:
                    break
            
            print('Received ' + str(len(data)) + ' bytes from server.')
            self.write_image(data)
            self.show_image()

def start_command_sender():
    x = CommandSender('192.168.1.9', 5000)
    x.run()

def start_picture_shower():
    y = PictureShower(5001)
    y.run()
    

thread1 = Thread(target = start_command_sender)
thread1.daemon = True
thread1.start()
thread2 = Thread(target = start_picture_shower)
thread2.daemon = True
thread2.start()

while True:
    time.sleep(1)

