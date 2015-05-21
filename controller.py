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


handlers = {}  # map client handler to user name
 
class MyHandler(Handler):
     
    def on_open(self):
        pass
         
    def on_close(self):
        pass
     
    def on_msg(self, msg):
        print msg
        #self.do_send(msg)


port = 8888
server = Listener(port, MyHandler)
while 1:
    poll(timeout=0.05) # in seconds