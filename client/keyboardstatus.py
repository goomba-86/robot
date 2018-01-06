import keyboard

class KeyboardStatus:

    def __init__(self):
        self.up_pressed = False
        self.down_pressed = False
        self.right_pressed = False
        self.left_pressed = False

    def update_key_statuses(self):
        self.up_pressed = keyboard.is_pressed('up')
        self.down_pressed = keyboard.is_pressed('down')
        self.left_pressed = keyboard.is_pressed('left')
        self.right_pressed = keyboard.is_pressed('right')
        
    def to_string(self):
        "Up pressed: " + str(self.up_pressed) + "Down pressed: " + str(self.down_pressed)
