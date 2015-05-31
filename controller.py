#Contains Model and Controller
#Run this file to start the server.
from network import Listener, Handler, poll, Client, get_my_ip
import sys
from threading import Thread
import asyncore
import Queue

#stores the amount of users connected.
class Model():
    type = ''
    count = 0
    #check if agent and user are connected
    def __init__(self):
        self.agent = False
        self.user = False
        self.handlers = {}
        self.q = Queue.Queue()

    #topic of the chat
    def set_type(self,type):
        self.type = type
        
    def set_agent(self, bool):
        self.agent = bool
        
    def set_customer(self, bool):
        self.user = bool


handlers = []  # map client handler to user name
q = Queue.Queue()
####### server logic/functionality #########
class ControllerHandler(Handler):

    #append client to our list of clients.
    def on_open(self):
        print "ControllerHandler Open Handler"
        # if len(handlers) < 2:
        #     handlers.append(self)
        #     print '=================handlers================='
        #     print handlers
        # else:
        #     print "Chat is full, wait for a bit"
        #     q.put(self)
        # print len(handlers)
        # print q.qsize()

    def on_close(self):
        print "ControllerHandler on_close"
        open("log.txt", 'w').close()
        #handlers.remove(self)
        self.close()
        print handlers
        #self.do_send('You have disconnected from chat')
      
        

    #server shoots the message back to the clients
    def on_msg(self, msg):
        print ("SENDING Back")
        with open('log.txt', 'a') as outfile:
            for c in handlers:
                if c != self:
                    if 'prompt' in msg: 
                        c.do_send('Customer is asking about: '+ msg['prompt'])
                        outfile.write('Customer is asking about: '+ msg['prompt'])

                    if 'speak' in msg:
                        c.do_send(msg['speak']+':'+' '+msg['txt'])
                        outfile.write('\n'+msg['speak']+':'+' '+msg['txt'])
                 
class Controller(Listener, Model):
        
    def on_accept(self, h):
        print 'CONTROLLER ON ACCEPT'
        print len(self.model.handlers)
        print self.model.q.qsize()
        #don't accept multiple agent/viewers

###########################################

if __name__ == '__main__':
    print("Testing")
    port = 8888
    model = Model()
    controller = Controller(port, ControllerHandler,model) #uses Listener parameters
    asyncore.loop()

