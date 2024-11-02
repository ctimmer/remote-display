
from area_modules.remote_area import RemoteArea

#-------------------------------------------------------------------------------
# RemoteImage
#-------------------------------------------------------------------------------
class RemoteImage (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        self.image_id = ""
        if "image_id" in area_config :
            self.image_id = area_config["image_id"]
        self.image_id_current = self.image_id
        self.show_border_color = remote_display.get_color_name ("YELLOW")

    def update (self, **kwargs) :
        #print (__class__, "update:", kwargs)
        if "image_id" not in kwargs :
            print ("image_id missing")
            return
        image_id = kwargs["image_id"]
        if image_id == self.image_id_current :
            return
        if image_id not in self.remote_display.images :
            print ("invalid image_id:", image_id)
            return
        self.image_id_current = image_id
        self.reload (reload_all = False)

    def reload (self, reload_all = True) :
        if not self.page_is_active (self.page_id) :
            return
        if reload_all :
            self.reload_border ()
        #image_id = self.image_id_current
        image_args = {
                    "hpos" : self.xmin ,
                    "vpos" : self.ymin
                    }
        image_dict = self.remote_display.get_image_object (self.image_id_current)
        image_args ["image_object"] = image_dict ["image_object"]
        #image_args.update (self.remote_display.images[self.image_id_current])
        self.remote_display.image (**image_args)
        if reload_all :
            self.reload_areas ()

## end RemoteImage ##
