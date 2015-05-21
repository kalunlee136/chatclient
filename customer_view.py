'''Customer View'''

from network import Handler, poll
import sys
from threading import Thread
from time import sleep
from client import Client, periodic_poll

myname = raw_input('What is your name? ')

host, port = 'localhost', 8888
client = Client(host, port)
client.do_send({'join': myname})
                            
thread = Thread(target=periodic_poll)
thread.daemon = True  # die when the main thread dies 
thread.start()

while 1:
    mytxt = sys.stdin.readline().rstrip()
    client.do_send({'speak': myname, 'txt': mytxt})
