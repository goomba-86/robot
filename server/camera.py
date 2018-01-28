import picamera

class Camera:

    def __init__(self):
        self.camera = picamera.PiCamera()
        self.camera.resolution = (640,480)
        self.camera.rotation = 90
        self.image_name = 'image.jpg'

    def take_new_picture(self):
        self.camera.capture(self.image_name)

    def get_picture_bytes(self):
        image_file = open(self.image_name, 'rb')
        return image_file.read()
        
