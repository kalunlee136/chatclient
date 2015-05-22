#Controller
'''Reasoning behind design:''' 
'''The Client, MyHandler classes and periodic_poll function control the flow 
in the chat system. The Client class directs to the m sends messages to the server or prints them
on the view (this is the definition of what a controller should do). MyHandler class 
does the exact same thing but with the Server/Listener. '''

from network import Listener, Handler, poll
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


#if __name__ == '__main__':
    #treats it like the server
    #port = 8888
    #server = Listener(port, MyHandler)
    #while 1:
        #poll(timeout=0.05) # in seconds