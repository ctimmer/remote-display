
from area_modules.remote_area import RemoteArea

#-------------------------------------------------------------------------------
# RemoteContainer
#-------------------------------------------------------------------------------
class RemoteContainer (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        self.text = None
        if "text" in area_config :
            self.text = area_config["text"]

    def reload (self, reload_all = True) :
        if not self.page_is_active() :
            return
        if reload_all :
            self.reload_border ()
        self.remote_display.rectangle_fill (x = self.xmin ,
                                            w = self.xlen ,
                                            y = self.ymin ,
                                            h = self.ylen ,
                                            color=self.backgroundcolor)
        if self.text is not None :
            self.remote_display.text (x = self.xmin ,
                                        y = self.ymin ,
                                        text = self.text ,
                                        font = self.font ,
                                        color = self.textcolor ,
                                        background = self.backgroundcolor)

        if reload_all :
            self.reload_areas ()

## end RemoteContainer ##
            