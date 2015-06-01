'''chat agent view'''

from network import Handler, poll, periodic_poll, Client, get_my_ip
import sys
from threading import Thread
from time import sleep
import asyncore


#replace host with ip address
#192.168.1.105
host, port = get_my_ip(), 8888
client = Client(host, port)
                         
thread = Thread(target=asyncore.loop)
thread.daemon = True  # die when the main thread dies 
thread.start()

client.do_send({'speak': 'agent', 'txt': 'Chat agent has connected'})
client.do_send({'Info': 'Model'})
while 1:
    mytxt = sys.stdin.readline().rstrip()
    client.do_send({'speak': 'agent', 'txt': mytxt})
