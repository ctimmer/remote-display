#

import sys
import time
import random

from machine import Pin, SPI  # type: ignore

#from xglcd_font import XglcdFont

import ujson

#from ili9341 import Display
from ili9341_display import ILI9341Display
#from trace_display import TraceDisplay

#-------------------------------------------------------------------------------
# RemoteDisplay
#-------------------------------------------------------------------------------
#class RemoteDisplay (TraceDisplay) :
class RemoteDisplay (ILI9341Display) :
    def __init__ (self, **kwargs) :
        #print ("RemoteDisplay __init__:", kwargs)
        super ().__init__ (**kwargs)
        self.active_default = True
        self.page = None
        self.page_count = 0
        self.page_names = {}
        self.page_index = []
        self.areas = {}

        # Check for configuration file
        if "config_file" in kwargs :
            self.setup_config_file (kwargs["config_file"])

    def setup_config_file (self, file_name) :
        config_dict = None
        try :
            with open(file_name, 'r') as config_file:
                config_dict = ujson.loads(config_file.read())
        except Exception :
            print ("Configuration file error:", file_name)
            return
        self.setup_config_dict (config_dict)
    def setup_config_dict (self, config_dict) :
        if config_dict is None :
            return
        if "page_id" not in config_dict :
            config_dict["page_id"] = "_PAGE_{:2d}".format (self.page_count)
        config_dict["globals"] = {
                              "active" : False ,    # No active pages
                              "font" : super().get_font_default() ,
                              "color" : super().get_color_default() ,
                              "background" : super().get_background_default()
                              }
        self.configure (None, config_dict)
        self.page_names[config_dict["page_id"]] = config_dict
        self.page_index.append (config_dict)
        self.area_reload (config_dict)
        if self.page_count <= 0 :
            self.page = config_dict
        self.page_count += 1
    def configure (self, parent, area) :
        #print ("area:", area)
        self.initialize_area (parent, area)
        if "areas" not in area :
            area ["areas"] = []
        if "id" in area :
            #print (area["id"])
            self.areas [area["id"]] = area
        for child in area["areas"] :
            self.configure (area, child)
    def initialize_area (self, parent, area) :
        if parent is None :
            parent_hpos = 0
            parent_vpos = 0
            if "vpos" not in area :
                area ["vpos"] = 0
            if "hpos" not in area :
                area ["hpos"] = 0
            if "border" not in area :
                area ["border"] = 0
            if "padding" not in area :
                area ["padding"] = 0
        else :
            area["globals"] = parent ["globals"]
            if "hpos" not in area :
                area ["hpos"] = parent ["hpos"]
            else :
                area ["hpos"] += parent ["hpos"]
            if "vpos" not in area :
                area ["vpos"] = parent ["vpos"]
            else :
                area ["vpos"] += parent ["vpos"]
            if "border" not in area :
                area ["border"] = parent ["border"]
            if "padding" not in area :
                area ["padding"] = parent ["padding"]
        if "vlen" not in area :
            area ["vlen"] = 20
        if "hlen" not in area :
            area ["hlen"] = 20

        offsets = area ["border"] + area ["padding"]
        area ["xlen"] = area ["hlen"] - (offsets * 2)
        area ["ylen"] = area ["vlen"] - (offsets * 2)
        area ["xmin"] = area ["hpos"] + offsets
        area ["ymin"] = area ["vpos"] + offsets
        area ["xmax"] = (area ["xmin"] + area ["xlen"]) - 1
        area ["ymax"] = (area ["ymin"] + area ["ylen"]) - 1
        if "type" not in area :
            area ["type"] = "container"
        #print ("type:", area["type"])
        if "backgroundcolor" not in area :
            area["backgroundcolor"] = super().get_background_default ()
        if area ["type"] == "text" :
            self.setup_text_area (area)
        elif area ["type"] == "lamp" :
            self.setup_lamp_area (area)
        if "value" not in area :
            area ["value"] = ""
        area["current_value"] = area ["value"]
    def setup_text_area (self, area) :
        if "value" not in area :
            area ["value"] = ""
        area ["current_value"] = area ["value"]
    def setup_lamp_area (self, area) :
        color_by_idx = []
        color_by_name = {}
        for color in area['lampcolors'] :
            #print ("====> in ", color)
            if "lampcolorrgb" in color :
                color["lampcolor"] = super().convert_rgb (*color["lampcolorrgb"])
            elif "lampcolorname" in color :
                color["lampcolor"] = self.get_color_name (color["lampcolorname"])
            else :
                pass #print ("setup:",area)
            if "textcolorrgb" in color :
                color["textcolor"] = super().convert_rgb (*color["textcolorrgb"])
            elif "textcolorname" in color :
                color["textcolor"] = self.get_color_name (color["textcolorname"])
            else :
                pass # print ("setup:",area)
            #print ("====> out", color)
            color_by_idx.append (color)
            color_by_name [color['name']] = color
        area['color_by_idx'] = color_by_idx
        area['color_by_name'] = color_by_name
        area["backgroundcolor"] = color_by_idx[0]["lampcolor"]
        if "value" not in area :
            area ["value"] = ""
        area ["current_value"] = area ["value"]
    def setup_container_area (self, area) :
        if "value" not in area :
            area ["value"] = ""
        area ["current_value"] = area ["value"]

    def area_reload (self, area) :
        if not area["globals"]["active"] :
            return
        super().rectangle_fill (x = area["hpos"] ,
                                    y = area["vpos"] ,
                                    w = area["hlen"] ,
                                    h = area["vlen"] ,
                                    color = area["backgroundcolor"])
        super().text (x = area["xmin"] ,
                      y = area["ymin"] ,
                      text = area["current_value"] ,
                      backgroundcolor = area["backgroundcolor"])
        for child_area in area["areas"] :
            self.area_reload (child_area)

    def screen_reload (self) :
        self.screen_clear ()
        self.area_reload (self.page)

    def update_text_area (self, **kwargs) :
        #print ("uta:", kwargs)
        if "area" not in kwargs :
            print ("area missing")
            return
        area_id = kwargs ["area"]
        if area_id not in self.areas :
            print ("area_id invalid")
            return
        area = self.areas[area_id]
        #print ("ta area", area)
        if "value" not in kwargs :
            return
        area ["current_value"] = kwargs ["value"]
        if area["globals"]["active"] :
            super().rectangle_fill (x = area["xmin"],
                                    w=area["xlen"],
                                    y = area["ymin"],
                                    h=area["ylen"]) 
            super().text (x = area["xmin"],
                          y = area["ymin"],
                          text = kwargs["value"])

    def update_lamp_area (self, **kwargs) :
        #print ("Update Lamp:",kwargs)
        if "area" not in kwargs :
            return
        area_id = kwargs ["area"]
        if area_id not in self.areas :
            return
        area = self.areas[area_id]
        if area["type"] != "lamp" :
            return
        #print ("Lamp:", area)
        #print ("kwargs", kwargs)
        lamp = None
        lamp_color = None
        text_color = None
        if "statename" in kwargs :
            lamp = area["color_by_name"][kwargs["color_name"]]["color"]
        elif "stateidx" in kwargs :
            #print (area["color_by_idx"])
            lamp = area["color_by_idx"][kwargs["stateidx"]]
        else :
            print ("update_lamp_area: Missing color arg")
            return

        if "value" in kwargs :
            area["value"] = kwargs["value"]
        elif "value" in lamp :
            area["value"] = lamp["value"]

        #area ["backgroundcolor"] = lamp_color
        if area["globals"]["active"] :
            super().rectangle_fill (x = area["xmin"],
                                    w = area["xlen"],
                                    y = area["ymin"],
                                    h = area["ylen"],
                                    color = lamp["lampcolor"]) 
            super().text (x = area["xmin"],
                          y = area["ymin"],
                          text = area["value"],
                          color = lamp["textcolor"] ,
                          backgroundcolor = lamp["lampcolor"])            

    def show_areas (self, parent_area=None, first_time=True) :
        #print (self.page)
        area = parent_area
        color = super().get_color_name ("WHITE")
        if first_time :
            super().screen_clear (color = super().get_color_name ("BLACK"))
        if area is None :
            area = self.page
        #print (area["type"])
        if area["type"] == "text" :
            color = super().get_color_name ("GREEN")
        elif area["type"] == "lamp" :
            color = super().get_color_name ("RED")
        super().rectangle (x = area["hpos"] ,
                            y = area["vpos"] ,
                            w = area["hlen"] ,
                            h = area["vlen"] ,
                            color = color)
        for child_area in area["areas"] :
            self.show_areas (parent_area=child_area, first_time=False)
            
    def show_area (self, area_id) :
        if area_id not in self.areas :
            print ("Unknown Label:", area_id)
            return
        self.show_areas (self.areas [area_id])

    def page_by_name (self, page_name) :
        if page_name not in self.page_names :
            return
        self.page["globals"]["active"] = False
        self.page = self.page_names[page_name]
        self.page["globals"]["active"] = True
        self.screen_reload ()
    def page_by_index (self, page_index) :
        if page_index < 0 \
        or page_index >= len (self.page_index) :
            return
        self.page["globals"]["active"] = False
        self.page = self.page_index[page_index]
        self.page["globals"]["active"] = True
        self.screen_reload ()

## end RemoteDisplay ##

################################################################################
# main
################################################################################
#

SPI_ID = 0
SCK = 18
MOSI = 19
MISO = 16
BAUDRATE = 10000000
POLARITY = 1
PHASE = 1
BITS = 8
#FIRSTBIT = SPI.MSB ,    # not implemented
#---- Display parameters
DISPLAY_WIDTH = 320
DISPLAY_HEIGHT = 240
ROTATION = 270
DC = 15
CS = 17
RST = 14

machine.freq(270000000)

if True :
    disp = RemoteDisplay (
                        #trace_output = False ,
                        #trace_methods = [] ,
                        #config_file = "testtitle.json" ,
                        #---- SPI parameters
                        spi_id = SPI_ID ,
                        sck = SCK ,
                        mosi = MOSI ,
                        miso = MISO ,
                        baudrate = BAUDRATE ,
                        polarity = POLARITY ,
                        phase = PHASE ,
                        bits = BITS ,
                        #firstbit = SPI.MSB ,    # not implemented
                        #---- Display parameters
                        display_width = DISPLAY_WIDTH ,
                        display_height = DISPLAY_HEIGHT ,
                        rotation = ROTATION ,
                        dc = DC ,
                        cs = CS ,
                        rst = RST
                        )
else :
    spi = SPI (
                SPI_ID,
                baudrate = BAUDRATE ,
                polarity = POLARITY ,
                phase = PHASE ,
                bits = BITS ,
                sck = Pin (SCK) ,
                mosi = Pin (MOSI) ,
                miso = Pin (MISO)
                )
    display = Display (spi,
                        width = DISPLAY_WIDTH ,
                        height = DISPLAY_HEIGHT ,
                        rotation = ROTATION ,
                        dc = Pin (DC),
                        cs = Pin (CS) ,
                        rst = Pin (RST)
                       )
    disp = RemoteDisplay (display_object = display)
#
disp.setup_config_file ("testtitle.json")
disp.setup_config_file ("testconfig.json")
disp.setup_config_file ("testeoj.json")

#disp.set_trace_methods (["text", "pixel"]
fortunes = [
    "      It is certain        " ,
    "  Reply hazy, try again    " ,
    "     Dont count on it      " ,
    "   It is decidedly so      " ,
    "     Ask again later       " ,
    "      My reply is no       " ,
    "      Without a doubt      " ,
    "  Better not tell you now  " ,
    "    My sources say no      " ,
    "      Yes definitely       " ,
    "    Cannot predict now     " ,
    "    Outlook not so good    " ,
    "     You may rely on it    " ,
    " Concentrate and ask again " ,
    "      Very doubtful        " ,
    "    As I see it, yes       " ,
    "       Most likely         " ,
    "       Outlook good        " ,
    "            Yes            " ,
    "    Signs point to yes     "
    ]

#print ("call dummy_test ##############")
#disp.dummy_test ()
#sys.exit()

print ("screen_reload")
#disp.screen_reload ()
#disp.circle_fill (xpos=50, ypos=50, r=25, color=disp.color_names ["RED"])
#time.sleep (5)

#disp.update_lamp_area (area = "WarpDrive", color_name = "ok")
#sys.exit ()

print ("show_areas ####################")
#disp.show_areas ()
#disp.show_areas ()
#time.sleep (5)
#sys.exit()

#disp.screen_reload ()
disp.update_text_area (area = "UpperRight", value = "Test")
disp.update_text_area (area = "UpperLeft", value = "Upper Left")

disp.page_by_name ("testtitle")
time.sleep (5)
start_ms = time.ticks_ms ()
disp.page_by_name ("testconfig")
for i in range (0,10) :
    #print ("iter#################################################")
    time.sleep (5)
    disp.update_text_area (area = "UpperRight",
                           value = str(time.ticks_diff (time.ticks_ms(), start_ms)))
    disp.update_text_area (area = "Fortune", value = fortunes [random.randrange (0,len(fortunes))])
    disp.update_lamp_area (area = "WarpDrive", stateidx = (i % 3))
    disp.update_lamp_area (area = "StopLight", stateidx = (i % 3))
    #disp.page_by_index (i % 2)
#print (disp.get_trace_stats ())
time.sleep (5)
disp.page_by_name ("testeoj")
sys.exit()

disp.text (x = 20, y = 112, text="Hello, World!")
for x in range (20,40) :
    disp.pixel (x = x, y = 10, color = disp.color_names ["RED"])

disp.line (x1 = 30, y1 = 30, x2 = 90, y2 = 90, color = disp.color_names ["WHITE"])

disp.rectangle (x = 50, y = 150, width = 100, height = 20, color = disp.color_names ["CYAN"])

disp.polygon (sides = 6, x0 = 50, y0 = 200, r = 10)

'''
disp.screen_off ()
time.sleep (2)
disp.screen_on ()
time.sleep (2)
'''
print (disp.get_trace_stats ())
