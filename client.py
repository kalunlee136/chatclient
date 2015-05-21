#####VIEW####
from network import Handler, poll
import sys
from threading import Thread
from time import sleep

class Client(Handler):
    
    def on_close(self):
        pass
    
    def on_msg(self, msg):
        print msg
    
def periodic_poll():
    while 1:
        poll()
        sleep(0.05)  # seconds

      