import socket, robot


class Server:

    def __init__(self, port):
        self.host = 'localhost'
        self.port = port
        self.robo = robot.Robot()
        
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
                data = connection.recv(buffer_size)
                if not data:
                    break
                print("Reiceived data", data)
                connection.send(data) #echo
                robo.move(data)

            connection.close()
            
x = Server(5000)
x.run()
