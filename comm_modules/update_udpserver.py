

import select
import socket
import json
import time

import display_config
from comm_modules.update_queue import UpdateQueue

PORT = 5010
QUEUE_LENGTH = 20
if "PORT" in display_config.PARAMETERS :
    PORT = display_config.PARAMETERS ["PORT"]
if "QUEUE_LENGTH" in display_config.PARAMETERS :
    QUEUE_LENGTH = display_config.PARAMETERS ["QUEUE_LENGTH"]

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
        self.running = True
        self.udp_socket = None
        self.port = port
        self.ip_stats = {}               # for debugging

    def start_server (self, timeout = 5000) :
        buf = ""
        self.udp_socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind (('0.0.0.0', self.port))
        poller = select.poll()
        poller.register(self.udp_socket, select.POLLIN)  # event 1
        while self.running :
            #print ("poll:", timeout)
            #self.udp_socket.setblocking (True)
            events = poller.poll (timeout)
            for event in events :
                if event[1] == 1 :
                    self.udp_input (event[0])
                #print (self.ip_stats)

    def udp_input (self, udp_socket) :
        address_ip = None
        udp_socket.setblocking (False)
        while True :
            buffer = None
            try :
                (buffer, address_ip) = udp_socket.recvfrom (1500)
                address = address_ip [0]
                if address not in self.ip_stats :
                    self.ip_stats [address] = {
                                                "input" : 0 ,
                                                "valid" : 0
                                                }
                self.ip_stats [address]["input"] += 1       # stats
                buffer = json.loads (buffer.decode())
                #print (buffer)
                if "method" not in buffer :
                    continue
                if buffer["method"] == "shutdown" :
                    self.running = False                     # All done
                    continue
                if "params" not in buffer :
                    continue
                args = buffer["params"]
                args.update ({"method" : buffer["method"]})  # add method
                #print (args)
                self.update_queue.push_queue (args)
                self.ip_stats [address]["valid"] += 1       # more stats
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

    def get_stats (self) :
        return self.ip_stats

## UpdateUDPServer ##
