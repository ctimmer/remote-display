
from area_modules.remote_area import RemoteArea

#-------------------------------------------------------------------------------
# RemoteText
#-------------------------------------------------------------------------------
class RemoteText (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        self.text = ""
        if "text" in area_config :
            self.text = area_config ["text"]
        self.text_current = self.text
        self.show_border_color = remote_display.get_color_name ("LIME")
    def update (self, **kwargs) :
        if "text" not in kwargs :
            return
        self.text_current = kwargs ["text"]
        self.reload (reload_all = False)
    def reload (self, reload_all = True) :
        if not self.page_is_active(self.page_id) :
            return
        #print ("active")
        if reload_all :
            self.reload_border ()
        self.remote_display.rectangle_fill (x = self.xmin ,
                                            w = self.xlen ,
                                            y = self.ymin ,
                                            h = self.ylen,
                                            color=self.backgroundcolor) 
        self.remote_display.text (x = self.xmin ,
                                  y = self.ymin ,
                                  text = self.text_current,
                                  font = self.font ,
                                  color = self.textcolor ,
                                  background = self.backgroundcolor)
        if reload_all :
            self.reload_areas ()

## end RemoteText ##
