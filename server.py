from network import Listener, Handler, poll
from controller import MyHandler
 
handlers = {}  # map client handler to user name
 
port = 8888
server = Listener(port, MyHandler)
while 1:
    poll(timeout=0.05) # in seconds