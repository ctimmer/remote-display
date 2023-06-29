

import select as select
import socket as socket

#-------------------------------------------------------------------------------
# UpdateUDPServer
#-------------------------------------------------------------------------------
class UpdateUDPServer :
    def __init__ (self ,
                  update_display ,
                  update_queue ,
                  port = 5010
                  ) :
        self.update_display = update_display
        self.update_queue = update_queue
        self.port = port
        self.udp_socket = socket.socket (socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.setblocking (False)
        self.udp_socket.bind (('0.0.0.0', self.port))
        #self.udp_socket.close ()

    def start_server (self) :
        buf = ""
        p = select.poll()
        p.register(self.udp_socket, select.POLLIN)
        to =  5000 #self.polltimeout
        while True :
            events = p.poll (to)
            for s, flag in events:
                 print('socket: %s\tflag: %s' % (s, flag))
            if len (events) > 0 :
                (buf, addr) = self.udp_socket.recvfrom(1500)
                print (buf)

## UpdateUDPServer ##
