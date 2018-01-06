class Request:
            
    def __init__(self, keyboard_status):
        self.forward = keyboard_status.up_pressed
        self.reverse = keyboard_status.down_pressed
        self.left = keyboard_status.left_pressed
        self.right = keyboard_status.right_pressed
