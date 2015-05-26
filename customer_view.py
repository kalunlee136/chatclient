'''Customer View'''

import controller
from network import Handler, poll, Client, periodic_poll
import sys
from threading import Thread
from time import sleep


myname = raw_input('What is your name? ')

host, port = 'localhost', 8888
client = Client(host, port)
client.do_send({'join': myname})


########## sending prompt to chat agent. #########
myoptions = raw_input('What brings you here?(choose a number) 1. Complaint, 2. Question, 3. Other ')
if myoptions == '1':
	myoptions = 'Complaint'
elif myoptions == '2':
	myoptions = 'Question'
elif myoptions == '3': 
	myoptions ='Other'
	
#while (myoptions != '1' or myoptions != '2' or myoptions != '3'):  
#	myoptions = raw_input('What brings you here?(choose a number) 1. Complaint, 2. Question, 3. Other ')
#	print myoptions

myoptions += ', topic: '
myoptions += raw_input('What is your topic regarding this prompt?')
client.do_send({'prompt': myoptions})
#########################################

#print 'Connecting you with an agent'

thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()

while 1:
    mytxt = sys.stdin.readline().rstrip()

    #customer console options
    if mytxt == ':q':
    	client.on_close()
    elif mytxt == ':s':
    	pass
    	#TO DO: save a copy of the chat
    elif mytxt == ':e':
    	print "Trivia: Did you know cats have 9 lives?" 
    else: 	 
    	client.do_send({'speak': 'client', 'txt': mytxt})
