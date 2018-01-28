import socket, robot, camera


class Server:

    def __init__(self, port):
        self.host = '192.168.1.9'
        self.port = port
        self.robo = robot.Robot()
        self.camera = camera.Camera()
        
    def run(self):
        buffer_size = 1024
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(1)

        while True:
            print('Waiting for connection...')
            connection, address = s.accept()
            print('Connection address: ', address)

            while True:
                print('Receiving data')
                data = connection.recv(buffer_size)
                if not data:                    
                    break
                print("Received data. Sending image back...")
                self.camera.take_new_picture()
                picture_bytes = self.camera.get_picture_bytes()
                connection.send(picture_bytes)
                print("Sent image back. Bytes: ", str(len(picture_bytes)))
                self.robo.move(data)

            connection.close()
            
x = Server(5000)
x.run()
