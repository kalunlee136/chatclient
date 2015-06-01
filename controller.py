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
    
    #check if agent and user are connected
    def __init__(self):
        self.conv_type = None
        self.topic = None
        self.handlers = {}
        self.q = Queue.Queue()
        self.copy = ''

    #topic of the chat
    def set_topic(self,topic):
        self.topic = topic
        
    def set_conv_type(self, conv_type):
        self.conv_type = conv_type
    


model = Model


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
        
        a = model.q.get()
        
        model.handlers['client'] = a
        #self.log.close()
        self.close()
    
    #server shoots the message back to the clients
    def on_msg(self, msg):
        
        print ("SENDING Back")
        
        with open('log.txt', 'a') as outfile:
            if self in model.handlers.values():
                with open('log.txt', 'a') as outfile:
                    for c in model.handlers:
                        if 'Conversation Type' in msg:
                            model.set_conv_type(msg['Conversation Type'])
                        elif 'Topic' in msg:
                            model.set_topic(msg['Topic'])
                        elif 'Info' in msg:
                                model.handlers['agent'].do_send(msg['Info']+' \n'+ 'Conversation Type: ' + model.conv_type + '\nTopic: ' + model.topic)
                                outfile.write('\n'+ msg['Info']+' \n'+ 'Conversation Type: ' + model.conv_type + ' \n Topic: ' + model.topic)  
                        if model.handlers[c] != self:
                            
                            if 'speak' in msg:
                                model.handlers[c].do_send(msg['speak']+':'+' '+msg['txt'])
                                outfile.write('\n'+msg['speak']+':'+' '+msg['txt'])
                            
                        
                                
                        
                            
class Controller(Listener):
    
    #add new connections to our handlers dict
    def on_accept(self, host):
        #don't accept multiple agent/viewers
        if len(model.handlers) < 2:
            self.active = True
            if 'client' in model.handlers.keys():
                model.handlers['agent'] = host
            else:
                model.handlers['client'] = host 
        else:
            host.do_send("Chat is full, wait for a bit")
            model.q.put(host)
            
        


###########################################

if __name__ == '__main__':
    print("Server running")
    port = 8888
    model = Model()
    controller = Controller(port, ControllerHandler) #uses Listener parameters
    asyncore.loop()

