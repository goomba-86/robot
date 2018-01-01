import robohat
import time
import tty
import sys

def readchar():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    if ch == '0x03':
        raise KeyboardInterrupt
    return ch

def readkey(getchar_fn=None):
    getchar = getchar_fn or readchar
    c1 = getchar()
    if ord(c1) != 0x1b:
        return c1
    c2 = getchar()
    if ord(c2) != 0x5b:
        return c1
    c3 = getchar()
    return chr(0x10 + ord(c3) - 65)  # 16=Up, 17=Down, 18=Right, 19=Left arrows

class KeyboardStatus:

    def __init__(self):
        reset()

    def reset(self):
        self.forward_pressed = False
        self.reverse_pressed = False
        self.left_pressed = False
        self.right_pressed = False
    
class Robot:

    def __init__(self):
        self.speed = 60
        self.keyboard_status = KeyboardStatus()
        robohat.init()

    def run(self):
        try:
            while True:
                keyp = readKey()
                
                if keyboard.is_pressed('up'):
                    robohat.forward(speed)
                elif keyboard.is_pressed('down'):
                    robohat.reverse(speed)
                elif keyboard.is_pressed('left'):
                    robohat.spinLeft(speed)
                elif keyboard.is_pressed('right'):
                    robohat.spinRight(speed)
                else:
                    robohat.stop()                
                time.sleep(0.1)
                
        except KeyboardInterrupt:
            print

        finally:
            robohat.cleanup()
     
# rob = Robot()
#robot.run()
