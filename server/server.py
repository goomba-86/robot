import socket, robot, camera, time
from threading import Thread

class CommandListener:
    def __init__(self, port):
        self.host = '192.168.1.9'
        self.port = port
        self.robo = robot.Robot()
        
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.bind((self.host, self.port))

        while True:
            print('Ready to receive data')
            data, addr = s.recvfrom(1024)
            self.robo.move(data)

class PictureSender:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.camera = camera.Camera()
        
    def run(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        buf = 1024
        while True:
            self.camera.take_new_picture()
            picture = self.camera.get_picture()
            data = picture.read(buf)
            while (data):
                if(s.sendto(data, (self.host, self.port))):
                    data = picture.read(buf)
            print 'Sent picture'
            time.sleep(1.5)
            
def start_command_listener():
    print 'Starting command listener'
    x = CommandListener(5000)
    x.run()
    
def start_picture_sender():
    print 'Starting picture sender'
    y = PictureSender('192.168.1.11', 5001) 
    y.run()

thread1 = Thread(target = start_command_listener)
thread1.daemon = True
thread1.start()
thread2 = Thread(target = start_picture_sender)
thread2.daemon = True
thread2.start()

while True:
    time.sleep(1)
