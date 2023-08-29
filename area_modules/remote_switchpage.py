

#-------------------------------------------------------------------------------
# RemoteSwitchPage
#-------------------------------------------------------------------------------
class RemoteSwitchPage () :
    def __init__ (self, remote_display) :
        self.remote_display = remote_display
    def update (self, **kwargs) :
        if "page_id" in kwargs :
            self.remote_display.change_active_page_id (kwargs["page_id"])
        elif "page_index" in kwargs :
            self.remote_display.change_active_page_index (kwargs["page_index"])

## end RemoteSwitchPage ##