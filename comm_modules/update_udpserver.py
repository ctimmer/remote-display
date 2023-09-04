

import select as select
import socket as socket
import utime as time

from comm_modules.update_queue import UpdateQueue

#-------------------------------------------------------------------------------
# UpdateUDPServer
#-------------------------------------------------------------------------------
class UpdateUDPServer :
    def __init__ (self ,
                  update_display ,
                  port = 5010 ,
                  queue_length = 20
                  ) :
        self.update_display = update_display
        self.update_queue = UpdateQueue (queue_length)
        self.port = port

    def start_server (self) :
        buf = ""
        self.udp_socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind (('0.0.0.0', self.port))
        #p = select.poll()
        #p.register(self.udp_socket, select.POLLIN)
        to =  5000 #self.polltimeout
        while True :
            print ("poll:", to)
            #self.udp_socket.setblocking (True)
            #events = p.poll (to)
            #print (events)
            #for s, flag in events:
                 #print('socket: %s\tflag: %s' % (s, flag))
            #if len (events) > 0 :
                #self.udp_socket.setblocking (False)
            (buf, addr) = self.udp_socket.recvfrom (1000)
            print (buf)

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
