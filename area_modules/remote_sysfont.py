
from area_modules.remote_area import RemoteArea

#-------------------------------------------------------------------------------
# RemoteTemplate
#-------------------------------------------------------------------------------
class RemoteSysFont (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        #self.scale = 3
        self.text_current = ""
        self.text_initial = ""
        self.len_max = 10
        self.horizontal = True
        if "horizontal" in area_config :
            self.horizontal = area_config["horizontal"]
        elif "vertical" in area_config :
            self.horizontal = not area_config["vertical"]
        if "scale" in area_config :
            self.scale = int (area_config["scale"])
        else :
            if self.horizontal :
                self.scale = self.ylen // 8
            else :
                self.scale = self.xlen // 5
        if self.scale < 1 :
            self.scale = 1
        elif self.scale > 10 :
            self.scale = 10
        if self.horizontal :
            self.len_max = (self.xlen + self.scale) // (self.scale * 6) # char width + 1
        else :
            self.len_max = (self.ylen + self.scale) // (self.scale * 9)
        if "text" in area_config :
            self.text_current = area_config ["text"]
            if len (self.text_current) > self.len_max :
                self.text_current = self.text_current[0:self.len_max]  # too long, trim
            #print (area_config ["text"],self.text_current, self.len_max)
        self.text_initial = self.text_current
        self.show_border_color = remote_display.get_color_name ("LIME")
    def update (self, **kwargs) :
        if "text" not in kwargs :
            return
        text = kwargs ["text"]
        if len (text) > self.len_max :
            text = text[0:self.len_max]  # too long, trim
        if text == self.text_current :
            return                    # No change, exit
        self.text_current = text
        self.reload (reload_all = False)
        #
    def reset (self) :
        #
        #---- Set area parameters to initial state
        #
        self.reload (reload_all = True)
        #
    def reload (self, reload_all = True) :
        if not self.page_is_active (self.page_id) :
            return
        if reload_all :
            self.reload_border ()
        #
        self.remote_display.rectangle_fill (x = self.xmin ,
                                            w = self.xlen ,
                                            y = self.ymin ,
                                            h = self.ylen ,
                                            color=self.backgroundcolor)
        self.text_sysfont (self.text_current ,
                           self.textcolor ,
                           self.scale ,
                           self.horizontal)
        #
        if reload_all :
            self.reload_areas ()

## end RemoteSysFont ##