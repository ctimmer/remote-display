#-------------------------------------------------------------------------------
# RemoteArea
#-------------------------------------------------------------------------------
class RemoteArea :

    def __init__ (self ,
                  remote_display ,
                  area) :
        super().__init__ ()
        self.remote_display = remote_display
        self.page = remote_display.get_configuration_page ()
        parent_hpos = 0
        parent_vpos = 0
        self.area_id = None
        self.active = False
        self.hpos = 0
        self.hlen = None
        self.vpos = 0
        self.vlen = None
        self.borderwidth = 0
        self.bordercolor = 0
        self.paddingwidth = 0
        #self.backgroundcolor = remote_display.get_background_default()
        self.backgroundwidth = 0
        self.backgroundcolor = remote_display.get_background_color_default ()
        self.font = remote_display.get_font_default()
        self.textcolor = remote_display.get_font_color_default()
        self.show_border_color = self.remote_display.get_color_name ("WHITE")
        self.areas = []
        if "area_id" in area :
            self.area_id = area["area_id"]
        if "parent_hpos" in area :
            parent_hpos = area ["parent_hpos"]
        if "parent_vpos" in area :
            parent_vpos = area ["parent_vpos"]
        if "hpos" in area :
            self.hpos = area ["hpos"] + parent_hpos
        else :
            self.hpos = self.parent_hpos
        if "hlen" in area :
            self.hlen = area ["hlen"]
        if "vpos" in area :
            self.vpos = area ["vpos"] + parent_vpos
        else :
            self.vpos = self.parent_vpos
        if "vlen" in area :
            self.vlen = area ["vlen"]
            
        if "borderwidth" in area :
            self.borderwidth = area ["borderwidth"]
        if "bordercolorname" in area :
            self.bordercolor = remote_display.get_color_by_name (area ["bordercolorname"])
        if "bordercolorrbg" in area :
            self.bordercolor = remote_display.convert_rgb (*area["bordercolorrgb"])
        if "paddingwidth" in area :
            self.paddingwidth = area ["paddingwidth"]
        elif "backgroundcolorrgb" in area :
            self.backgroundcolor = remote_display.convert_rgb (*area["backgroundcolorrgb"])
        elif "backgroundcolorname" in area :
            self.backgroundcolor = remote_display.get_color_by_name (area["backgroundcolorname"])
        if "font" in area :
            self.font = remote_display.get_font (area ["font"])
        if "textcolor" in area :
            self.textcolor = area ["textcolor"]
        elif "textcolorrgb" in area :
            self.textcolor = remote_display.convert_rgb (*area["textcolorrgb"])
        elif "textcolorname" in area :
            self.textcolor = remote_display.get_color_by_name (area["textcolorname"])

        #---- Set field data position/lengths parameters
        offsets = self.borderwidth + self.paddingwidth
        self.xlen = self.hlen - (offsets * 2)
        self.ylen = self.vlen - (offsets * 2)
        self.xmin = self.hpos + offsets
        self.ymin = self.vpos + offsets
        self.xmax = (self.xmin + self.xlen) - 1
        self.ymax = (self.ymin + self.ylen) - 1
        self.xmid = self. xmin + round (self.xlen / 2)
        self.ymid = self. ymin + round (self.ylen / 2)

    def add_area (self, area) :
        if area is not None :
            self.areas.append (area)
    def page_is_active (self) :
        return self.page.page_is_active ()
    def set_page_active (self, state) :
        self.page.set_page_active (state)

    def reload_border (self) :
        if self.xmin == self.hpos :
            return          # No border or padding
        x = self.hpos
        xlen = self.hlen
        y = self.vpos
        ylen = self.vlen
        for i in range (self.borderwidth) :
            if self.bordercolor is not None :
                self.remote_display.rectangle (x = x ,
                                                y = y ,
                                                w = xlen ,
                                                h = ylen ,
                                                color = self.bordercolor)
            x += 1
            y += 1
            xlen -= 2
            ylen -= 2
        for i in range (self.paddingwidth) :
            if self.backgroundcolor is not None :
                self.remote_display.rectangle (x = x ,
                                                y = y ,
                                                w = xlen ,
                                                h = ylen ,
                                                color = self.backgroundcolor)
            x += 1
            y += 1
            xlen -= 2
            ylen -= 2
    def reload_background (self) :
        self.reload_border ()
        if self.backgroundwidth > 0 :
            if self.backgroundcolor is not None :
                pass # need
        if self.paddingwidth > 0 :
            pass # need
    def reload_areas (self) :
        for area in self.areas :
            area.reload ()

    def update (self) :
        pass
    def reload (self) :
        self.reload_background ()
        self.reload_areas ()

    def show_area (self, show_all = True) :
        #print (self.page)
        #color = self.remote_display.get_color_name ("WHITE")
        self.remote_display.rectangle (x = self.hpos ,
                                        y = self.vpos ,
                                        w = self.hlen ,
                                        h = self.vlen ,
                                        color = self.show_border_color)
        if show_all :
            for child_area in self.areas :
                child_area.show_area ()

## end RemoteArea ##
