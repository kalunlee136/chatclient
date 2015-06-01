#Contains Model and Controller
#Run this file to start the server.
from network import Listener, Handler, poll, Client, get_my_ip
import sys
from threading import Thread
import asyncore
import Queue
import os

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


handlers = {} # map client handler to user name
q = Queue.Queue()
copy = ''


####### server logic/functionality #########
class ControllerHandler(Handler):

    #append client to our list of clients.
    def on_open(self):
        pass
        # for key, value in handlers.items():
        #     if value == self:
        #         host = handlers[key]
        #         if key == 'agent':
        #             value.do_send('WOOOOOOOOOOOOOO')
        #self.copy = True

    def on_close(self):
        print "ControllerHandler on_close"
        a = q.get()
        handlers['client'] = a
        #self.log.close()
        self.close()
    
    #server shoots the message back to the clients
    def on_msg(self, msg):
        print ("SENDING Back")
        with open('log.txt', 'a') as outfile:
            if self in handlers.values():
                with open('log.txt', 'a') as outfile:
                    for c in handlers:
                        if handlers[c] != self:
                            if 'prompt' in msg:
                                handlers[c].do_send('Customer is asking about: '+ msg['prompt'])
                                outfile.write('Customer is asking about: '+ msg['prompt'])

                            if 'speak' in msg:
                                handlers[c].do_send(msg['speak']+':'+' '+msg['txt'])
                                outfile.write('\n'+msg['speak']+':'+' '+msg['txt'])

class Controller(Listener, Model):
    
    #add new connections to our handlers dict
    def on_accept(self, host):
        #don't accept multiple agent/viewers
        if len(handlers) < 2:
            if 'client' in handlers.keys():
                handlers['agent'] = host
            else:
                handlers['client'] = host   
        else:
            host.do_send("Chat is full, wait for a bit")
            q.put(host)


###########################################

if __name__ == '__main__':
    print("Server running")
    port = 8888
    model = Model()
    controller = Controller(port, ControllerHandler,model) #uses Listener parameters
    asyncore.loop()

