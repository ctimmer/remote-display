
from area_modules.remote_area import RemoteArea

#-------------------------------------------------------------------------------
# RemoteLamp
#-------------------------------------------------------------------------------
class RemoteLamp (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        self.lamp_by_idx = []
        self.lamp_by_name = {}
        self.lampcolor = 0
        self.textcolor = 0xff
        self.text = ""
        self.lamp_id_current = ""
        #print (area_config['lampcolors'])
        for color in area_config['lampcolors'] :
            #print ("====> in ", color)
            lamp = {
                    "name" : color["name"] ,
                    "lampcolor" : self.remote_display.get_color_name ("BLACK") ,
                    "textcolor" : self.remote_display.get_color_name ("WHITE") ,
                    "text" : ""
                    }
            if "lampcolorrgb" in color :
                lamp["lampcolor"] = self.remote_display.convert_rgb (*color["lampcolorrgb"])
            elif "lampcolorname" in color :
                lamp["lampcolor"] = self.remote_display.get_color_name (color["lampcolorname"])
            if "textcolorrgb" in color :
                lamp["textcolor"] = super().convert_rgb (*color["textcolorrgb"])
            elif "textcolorname" in color :
                lamp["textcolor"] = self.remote_display.get_color_name (color["textcolorname"])
            if "text" in color :
                lamp["text"] = color ["text"]
            #print ("====> out", color)
            self.lamp_by_idx.append (lamp)
            #print (color)
            #print (lamp)
            self.lamp_by_name [color['name']] = lamp
        #print (self.lamp_by_idx[0]["name"])
        self.lamp_id = self.lamp_by_idx[0]["name"]
        self.lamp_id_current = self.lamp_id
        self.lampcolor = self.lamp_by_name[self.lamp_id_current]["lampcolor"]
        self.textcolor = self.lamp_by_name[self.lamp_id_current]["textcolor"]
        self.text = self.lamp_by_name[self.lamp_id_current]["text"]
        self.show_border_color = remote_display.get_color_name ("RED")
    def update (self, **kwargs) :
        #print (__class__, "Update", kwargs)
        lamp_id = ""
        if "lamp_id" in kwargs :
            lamp_id = kwargs["lamp_id"]
            if lamp_id not in self.lamp_by_name :
                print ("Unknown lamp_id:", lamp_id)
                return
        elif "lamp_index" in kwargs :
            lamp_index = kwargs["lamp_index"]
            if lamp_index < 0 \
            or lamp_index >= len (self.lamp_by_idx) :
                print ("Invalid lamp_index:", lamp_index)
                return
            lamp_id = self.lamp_by_idx[lamp_index]["name"]
        else:
            return
        if lamp_id == self.lamp_id_current :
            return
        self.lamp_id_current = lamp_id
        lamp = self.lamp_by_name [lamp_id]
        self.lampcolor = lamp["lampcolor"]
        self.textcolor = lamp["textcolor"]
        self.text = lamp["text"]
        self.reload (reload_all = False)
    def reload (self, reload_all = True) :
        if self.page_is_active() :
            if reload_all :
                self.reload_background ()
            #print ("lamp color:", self.lampcolor)
            #print ("text color:", self.textcolor)
            #print ("text:", self.text)
            #print ("lamp: reload#####################")
            #print ("lamp: clear")
            self.remote_display.rectangle_fill (x = self.xmin ,
                                                w = self.xlen ,
                                                y = self.ymin ,
                                                h = self.ylen ,
                                                color = self.lampcolor)
            #print ("lamp: text")
            self.remote_display.text (x = self.xmin ,
                                      y = self.ymin ,
                                      text = self.text ,
                                      font = self.font ,
                                      color = self.textcolor ,
                                      background = self.lampcolor)
            if reload_all :
                self.reload_areas ()   

## end RemoteLamp ##
