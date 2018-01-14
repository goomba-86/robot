import robohat, jsonpickle

class Robot:

    def __init__(self):
        self.speed = 60
        robohat.init()

    def move(self, request):

        if(request.find('"forward": true') != -1):
            robohat.forward(self.speed)
        elif(request.find('"reverse": true') != -1):
            robohat.reverse(self.speed)
        elif(request.find('"left": true') != -1):
            robohat.spinLeft(80)
        elif(request.find('"right": true') != -1):
            robohat.spinRight(80)
        else:
            robohat.stop()
            
#{"py/object": "request.Request", "forward": false, "right": false, "reverse": false, "left": false}
