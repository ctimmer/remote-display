
import sys
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
        self.byte_buffer = bytearray (1500)

    def start_server (self) :
        self.udp_socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind (('0.0.0.0', self.port))
        #self.udp_socket.setblocking (False)
        poller = select.poll()
        poller.register(self.udp_socket, select.POLLIN)  # only event
        timeout = 5000
        while self.running :
            input_processed = False
            events = poller.poll (timeout)
            for event in events :
                #print (event)
                if event[1] == select.POLLIN :
                    self.udp_input (event[0])
                    input_processed = True
                else :
                    poller.unregister (event[0])
            if not input_processed :
                if not self.update_queue.empty_queue () :
                    self.update_display.process_update_queue (self.update_queue)
                timeout = 5000
            else :
                if self.update_queue.full_queue () :
                    self.update_display.process_update_queue (self.update_queue)
                timeout = 10

    #-----------------------------------------------------------------------
    # udp_input
    #-----------------------------------------------------------------------
    def udp_input (self, udp_socket) :
        udp_socket.setblocking (False)
        while True :
            buffer = None
            try :
                '''
                #print ("recvfrom")
                (buffer, address_ip) = udp_socket.recvfrom (1500)
                buffer = json.loads (buffer.decode("utf-8"))
                '''
                #print ("readinto:", time.ticks_ms ())
                buffer_length = 0
                buffer_length = udp_socket.readinto(self.byte_buffer)
                if buffer_length == 0 :
                    print ("buff == 0")
                    break
                buffer = json.loads (str (memoryview(self.byte_buffer[0:buffer_length]), 'utf8'))
                #
                #print (buffer)
                if "method" not in buffer :
                    print ("no method")
                    continue
                if buffer["method"] == "shutdown" :
                    self.running = False                     # All done
                    continue
                if "params" not in buffer :
                    print ("no params")
                    continue
                #queue_entry = {
                #    "method" : buffer["method"] ,
                #    "params" : buffer["params"]
                #    }
                #print (queue_entry)
                self.update_queue.push_queue ({
                    "method" : buffer["method"] ,
                    "params" : buffer["params"]
                    })
                if self.update_queue.full_queue () :         # is q full
                    break
                break ### TEST ###
            except :
                #print ("recvfrom: exception")
                #time.sleep_ms (100)
                break
        #if not self.update_queue.empty_queue () :
            #self.update_display.process_update_queue (self.update_queue)

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

