#
from area_modules.remote_area import RemoteArea

#-------------------------------------------------------------------------------
# RemoteLinearGuage
#-------------------------------------------------------------------------------
class RemoteLinearGuage (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        self.vertical_guage = True
        self.range_min = 0
        self.range_max = 100
        self.backgroundcolor = remote_display.get_color_name ("BLACK")
        self.valuecolor = remote_display.get_color_name ("WHITE")
        self.current_value = 0
        self.current_level = None
        #
        if "verticalguage" in area_config :
            self.vertical_guage = area_config ["verticalguage"]   # True/False
        if "horizontalguage" in area_config :
            self.vertical_guage = not area_config ["horizontalguage"]   # True/False
        if "rangemin" in area_config :
            self.range_min = area_config ["rangemin"]
            self.current_value = self.range_min
        if "rangemax" in area_config :
            self.range_max = area_config ["rangemax"]
        if "backgroundcolorname" in area_config :
            self.backgroundcolor = remote_display.get_color_name (area_config["backgroundcolorname"])
        elif "backgroundcolorrgb" in area_config :
            self.backgroundcolor = remote_display.convert_rgb (*area_config["backgroundcolorrgb"])
        if "valuecolorname" in area_config :
            self.valuecolor = remote_display.get_color_name (area_config["valuecolorname"])
        elif "valuecolorrgb" in area_config :
            self.valuecolor = remote_display.convert_rgb (*area_config["valuecolorrgb"])
        if "value" in area_config :
            self.current_value = area_config["value"]
        #
        self.previous_value = self.current_value
        self.show_border_color = remote_display.get_color_name ("YELLOW")
        self.range_len = (self.range_max - self.range_min)
    def update (self, **kwargs) :
        if "value" not in kwargs :
            #print ("b_update: no value")
            return
        if kwargs["value"] == self.current_value :
            #print ("b_update: no change")
            return
        #
        #---- Make changes to area parameters
        #
        self.current_value = kwargs["value"]
        if self.current_value > self.range_max :
            self.current_value = self.range_max
        elif self.current_value < self.range_min :
            self.current_value = self.range_min
        RemoteLinearGuage.reload (self, reload_all = False)
        #
    def reset (self) :
        #
        #---- Set area parameters to initial state
        #
        self.current_value = self.range_min
        RemoteLinearGuage.reload (self, reload_all = True)
        #
    def reload (self, reload_all = True) :
        if not self.page_is_active(self.page_id) :
            print ("b_reload: not active")
            return
        if reload_all :
            self.current_level = None
            self.reload_border ()
        #
        #---- Output to display here
        level = None
        bg_w = 0
        bg_h = 0
        lv_w = 0
        lv_h = 0
        if self.vertical_guage :
            level = self.ymax - round((self.current_value / self.range_len) * (self.ylen - 1))
            if self.current_level is not None :
                if level == self.current_level :
                    #print ("no change")
                    pass
                elif level < self.current_level :
                    #print ("extend level")
                    lv_x = self.xmin
                    lv_w = self.xlen
                    lv_y = level
                    lv_h = (self.current_level - level) + 1
                else :
                    #print ("extend background")
                    bg_x = self.xmin
                    bg_w = self.xlen
                    bg_y = self.current_level # self.ymin
                    bg_h = level - self.current_level # self.ymin #+ 1
            else :
                bg_x = self.xmin
                bg_w = self.xlen
                bg_y = self.ymin
                bg_h = level - self.ymin #+ 1
                lv_x = self.xmin
                lv_w = self.xlen
                lv_y = level
                lv_h = (self.ymax - level) + 1
            self.current_level = level
        else :
            level = self.xmin + round((self.current_value / self.range_len) * (self.xlen - 1))
            if self.current_level is not None :
                if level == self.current_level :
                    #print ("h no change")
                    #bg_w = 0                     # No change
                    #lv_w = 0
                    pass
                elif level > self.current_level :
                    #print ("h extend level")
                    #bg_w = 0
                    lv_x = self.current_level + 1
                    lv_w = level - self.current_level
                    lv_y = self.ymin
                    lv_h = self.ylen
                else :
                    #print ("h extend bg")
                    #lv_w = 0
                    bg_x = level + 1
                    bg_w = self.current_level - level
                    bg_y = self.ymin
                    bg_h = self.ylen
            else :
                bg_x = level + 1
                bg_w = (self.xmax - level) #+ 1
                bg_y = self.ymin
                bg_h = self.ylen
                lv_x = self.xmin
                lv_w = (level - self.xmin) + 1
                lv_y = self.ymin
                lv_h = self.ylen

        self.current_level = level
        if bg_w > 0 \
        and bg_h > 0 :
            self.remote_display.rectangle_fill (x = bg_x ,
                                            w = bg_w ,
                                            y = bg_y ,
                                            h = bg_h,
                                            color = self.backgroundcolor)
        if lv_w > 0 \
        and lv_h > 0 :
            self.remote_display.rectangle_fill (x = lv_x ,
                                            w = lv_w ,
                                            y = lv_y ,
                                            h = lv_h,
                                            color = self.valuecolor)
        #
        if reload_all :
            self.reload_areas ()

## end RemoteLinearGuage ##


