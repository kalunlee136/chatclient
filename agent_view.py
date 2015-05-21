'''chat agent view'''

from network import Handler, poll
import sys
import controller
from threading import Thread
from time import sleep
from controller import Client, periodic_poll


#filler sentence
print("Customer stuff")
host, port = 'localhost', 8888
client = Client(host, port)
                         
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()

while 1:
    mytxt = sys.stdin.readline().rstrip()
    client.do_send({'speak': "Chat Agent", 'txt': mytxt})
