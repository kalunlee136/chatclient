#Contains Model and Controller
#Run this file to start the server.
from network import Listener, Handler, poll, Client
import sys
from threading import Thread
import asyncore


#handlers = {}  # map client handler to user name
connections = [] # real map client handler to user name

#stores the amount of users connected.
class Model():
    type = ''
    connections = []
    #check if agent and user are connected
    def __init__(self):
        self.agent = False
        self.user = False

    #topic of the chat
    def set_type(self,type):
        self.type = type
        
    def set_agent(self, bool):
        self.agent = bool
        
    def set_user(self, bool):
        self.user = bool
    
####### server logic/functionality #########
class ControllerHandler(Handler):

    def on_open(self):
        print "ControllerHandler Open Handler"

    def on_close(self):
        #Client.on_close()
        print "ControllerHandler on_close"

    #server shoots the message back to the clients
    def on_msg(self, msg):
        print ("SENDING Back")
        
        #//To Do: 
        #    Exclude yourself and make it echo back ONLY to the other client. 
        #    

        #//Currently functionality: 
        # echos back messages to all clients connected (including yourself)
        # Does multiple checks with multiple different callbacks:
            #if it's a prompt: shoot back what the customer's prompt is
            #if it's normal convo ('speak') it echo messages in this format: "name: text"  
                          
        for c in connections:
            #c.do_send(msg)

            if 'prompt' in msg: 
                c.do_send('Customer is asking about: '+ msg['prompt'])

            if 'speak' in msg:
                c.do_send(msg['speak']+':'+' '+msg['txt'])
            #if 'speak' in msg:
            #    self.copy += msg['speak']+':'+' '+msg['txt']+ '\t\n'
            #    print self.copy
                 
class Controller(Listener, Model):
        
    def on_accept(self, h):
        print "Controller on_accept"
        #self.model exists in the Listener class
        #Does not allow more than 2 people connected.
        #Checks if there are less than 2 clients connected
        #if yes, adds that client to our list
        #if no, does not connect and tells the user the room is full.

        if len(connections) < 2:
            #self.model.connections.append(h.addr)
            connections.append(h)
            
        else:
            print "Chat room exceeded amount of connections"
        
        #don't accept multiple agent/viewers

###########################################

if __name__ == '__main__':
    print("Testing")
    port = 8888
    model = Model()
    controller = Controller(port, ControllerHandler,model) #uses Listener parameters
    asyncore.loop()
#     while 1:
#         poll(timeout=0.05) # in seconds
#        server.handler_class.collect_incoming_data()

#if __name__ == '__main__':
    #treats it like the server
    #port = 8888
    #server = Listener(port, MyHandler)
    #while 1:
        #poll(timeout=0.05) # in seconds
