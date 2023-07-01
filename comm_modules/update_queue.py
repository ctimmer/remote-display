#
#-------------------------------------------------------------------------------
# UpdateQueue
#-------------------------------------------------------------------------------
class UpdateQueue :
    push_count = 0
    pop_count = 0
    def __init__ (self, size = 20) :
        self.queue_size = size
        queue_entry = {
            "active" : False ,
            "next" : None ,
            "data" : None
            }
        #---- Initialize queue entries
        first_entry = queue_entry.copy ()       # save first entry
        prev_entry = first_entry
        for idx in range (0, (size - 1)) :
            last_entry = queue_entry.copy ()    # new q entry
            prev_entry ["next"] = last_entry    # forward link
            prev_entry = last_entry
        last_entry["next"] = first_entry        # link last to first
        #---- initialize push/pop entries
        self.push_entry = first_entry
        self.pop_entry = first_entry

    def push_queue (self, data) :
        if self.push_entry ["active"] == True :
            return True                           # full q
        self.push_entry ["data"] = data           # data to q
        self.push_entry ["active"] = True         # in use
        self.push_entry = self.push_entry ["next"] # move to next entry
        self.push_count += 1
        return False                              # good return
    def pop_queue (self, empty_return = None) :
        if self.pop_entry ["active"] != True :
            return empty_return                   # empty q
        data = self.pop_entry ["data"]            # returned data
        self.pop_entry ["data"] = None            # clear data
        self.pop_entry ["active"] = False         # make available
        self.pop_entry = self.pop_entry ["next"]  # move to next entry
        self.pop_count += 1
        return data
    def empty_queue (self) :
        return not self.pop_entry ["active"]
    def full_queue (self) :
        return self.push_entry ["active"]
    def __str__ (self) :
        print ("push count: ", self.push_count)
        print (" pop count: ", self.pop_count)

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

str (q)
'''

