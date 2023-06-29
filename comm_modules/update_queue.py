#
#-------------------------------------------------------------------------------
# UpdateQueue
#-------------------------------------------------------------------------------
class UpdateQueue :
    def __init__ (self, size = 20) :
        self.queue_size = size
        queue_entry = {
            "active" : False ,
            "next" : None ,
            "data" : None
            }
        self.circ_queue = [None for element in range(size)]
        print (len (self.circ_queue))
        #---- Initialize queue entries
        for idx in range (0, size) :
            self.circ_queue[idx] = queue_entry.copy ()
            if idx > 0 :
                self.circ_queue [idx - 1]["next"] = self.circ_queue [idx]
        self.circ_queue [size - 1]["next"] = self.circ_queue [0] # fix last
        self.current_entry = self.circ_queue [0]
        self.data_entry = self.circ_queue [0]
    def push_queue (self, data) :
        if self.current_entry ["active"] == True :
            return True
        self.current_entry ["active"] = True
        self.current_entry ["data"] = data
        self.current_entry = self.current_entry ["next"]
        return False
    def pop_queue (self, empty_return = None) :
        if self.data_entry ["active"] != True :
            return empty_return
        data = self.data_entry ["data"]
        self.data_entry ["active"] = False
        self.data_entry = self.data_entry ["next"]
        return data
    def empty_queue (self) :
        return not self.data_entry ["active"]
    def full_queue (self) :
        return self.current_entry ["active"]

## end UpdateQueue ##

'''
q = UpdateQueue (size=3)
print ("queue empty:", q.empty_queue ())
print (q.push_queue ({"first" : "curt"}))
print ("queue empty:", q.empty_queue ())
print (q.push_queue ({"last" : "timm"}))
print ("queue empty:", q.empty_queue ())
print (q.push_queue ({"age" : "old"}))
print ("queue empty:", q.empty_queue ())
print (q.push_queue ({"state" : "Alaska"}))
print ("queue empty:", q.empty_queue ())
print (q.push_queue ({"fail" : "toomany"}))
print ("queue empty:", q.empty_queue ())
print (q.pop_queue ())
print ("queue empty:", q.empty_queue ())
print (q.pop_queue ())
print ("queue empty:", q.empty_queue ())
print (q.pop_queue ())
print ("queue empty:", q.empty_queue ())
print (q.pop_queue ())
print ("queue empty:", q.empty_queue ())
print (q.pop_queue ())
print ("queue empty:", q.empty_queue ())
print (q.pop_queue ())
print ("queue empty:", q.empty_queue ())
print (q.push_queue ({"state" : "Alaska"}))
print ("queue empty:", q.empty_queue ())
print (q.pop_queue ())
print ("queue empty:", q.empty_queue ())
print (q.pop_queue ())
print ("queue empty:", q.empty_queue ())
'''
