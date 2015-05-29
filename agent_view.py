'''chat agent view'''

from controller import Client
from network import Handler, poll, periodic_poll, Client
import sys
from threading import Thread
from time import sleep
import asyncore


#replace host with ip address
#192.168.1.105
host, port = 'localhost', 8888
client = Client(host, port)
                         
thread = Thread(target=asyncore.loop)
thread.daemon = True  # die when the main thread dies 
thread.start()

client.do_send({'speak': 'agent', 'txt': 'Chat agent has connected'})

while 1:
    mytxt = sys.stdin.readline().rstrip()
    client.do_send({'speak': 'agent', 'txt': mytxt})
