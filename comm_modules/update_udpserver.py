

import select
import socket
import json
import time

import display_config
from comm_modules.update_queue import UpdateQueue

PORT = 5010
QUEUE_LENGTH = 20

#-------------------------------------------------------------------------------
# UpdateUDPServer
#-------------------------------------------------------------------------------
class UpdateUDPServer :
    def __init__ (self ,
                  update_display ,
                  port = PORT ,
                  queue_length = QUEUE_LENGTH
                  ) :
        self.update_display = update_display
        self.update_queue = UpdateQueue (queue_length)
        self.udp_socket = None
        self.port = port
        #self.buffer = ""

    def start_server (self, timeout = 5000) :
        buf = ""
        self.udp_socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind (('0.0.0.0', self.port))
        poller = select.poll()
        poller.register(self.udp_socket, select.POLLIN)  # event 1
        while True :
            #print ("poll:", timeout)
            #self.udp_socket.setblocking (True)
            events = poller.poll (timeout)
            for event in events :
                if event[1] == 1 :
                    self.udp_input (event[0])

    def udp_input (self, udp_socket) :
        address = None
        udp_socket.setblocking (False)
        while True :
            buffer = None
            try :
                (buffer, address) = udp_socket.recvfrom (1500)
                buffer = json.loads (buffer.decode())
                #print (buffer)
                if "method" not in buffer :
                    continue
                if "args" not in buffer :
                    continue
                args = buffer["args"]
                args.update ({"method" : buffer["method"]})  # add method
                #print (args)
                self.update_queue.push_queue (args)
                if self.update_queue.full_queue () :         # is q full
                    break ;
            except :
                break
        if not self.update_queue.empty_queue () :
            self.update_display.process_update_queue (self.update_queue)

    def start_test (self,
                    test_data,
                    repeat = 1 ,
                    delay = 5) :
        for repeat_count in range (0, repeat) :
            print ("start_test repeat:", repeat_count)
            for queue_messages in test_data :
                for json_message in queue_messages :
                    self.update_queue.push_queue (json_message)
                self.update_display.process_update_queue (self.update_queue)
                time.sleep (delay)
                
## UpdateUDPServer ##
