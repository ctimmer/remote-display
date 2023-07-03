#
################################################################################
# The MIT License (MIT)
#
# Copyright (c) 2023 Curt Timmerman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
################################################################################

import sys
import gc
import time
import random
import re

from machine import Pin, SPI

#from xglcd_font import XglcdFont

import ujson as json

#from xglcd_font import XglcdFont
#from ili9341 import Display
from ili9341_display import ILI9341Display
#from trace_display import TraceDisplay

from area_modules.remote_area import RemoteArea

from area_modules.remote_container import RemoteContainer
from area_modules.remote_text import RemoteText
from area_modules.remote_image import RemoteImage
from area_modules.remote_lamp import RemoteLamp
from area_modules.remote_7segment import Remote7Segment
from area_modules.remote_switchpage import RemoteSwitchPage
from area_modules.remote_template import RemoteTemplate

#-------------------------------------------------------------------------------
# RemotePage
#-------------------------------------------------------------------------------
class RemotePage :
    def __init__ (self, base_area = None) :
        self.active = False
        self.base = base_area
    def set_base (self, base_area) :
        self.base = base_area
    def get_base (self) :
        return self.base
    def page_is_active (self) :
        return self.active
    def set_page_active (self, state = False) :
        self.active = state

DEVICE_DISPLAY = ILI9341Display
#DEVICE_DISPLAY = TraceDisplay

#-------------------------------------------------------------------------------
# RemoteDisplay
#-------------------------------------------------------------------------------
#class RemoteDisplay (TraceDisplay) :
#class RemoteDisplay (ILI9341Display) :
class RemoteDisplay (DEVICE_DISPLAY) :
    def __init__ (self, **kwargs) :
        #print ("RemoteDisplay __init__:", kwargs)
        super ().__init__ (**kwargs)
        self.page = None
        self.page_count = 0
        self.page_names = {}
        self.page_index = []
        self.areas = {}
        self.area_types = {   # Predefined types
                        "container" : RemoteContainer ,
                        "text" : RemoteText ,
                        "lamp" : RemoteLamp ,
                        "image" : RemoteImage
                        }
        self.color_names = {
                        "BLACK" : self.convert_rgb (0, 0, 0) ,
                        "WHITE" : self.convert_rgb (255, 255, 255) ,
                        "RED" : self.convert_rgb (255, 0, 0) ,
                        "LIME" : self.convert_rgb (0, 255, 0) ,
                        "BLUE" : self.convert_rgb (0, 0, 255) ,
                        "YELLOW" : self.convert_rgb (255, 255, 0) ,
                        "CYAN" : self.convert_rgb (0, 255, 255) ,
                        "MAGENTA" : self.convert_rgb (255, 0, 255) ,
                        "SILVER" : self.convert_rgb (192, 192, 192) ,
                        "GRAY" : self.convert_rgb (128, 128, 128) ,
                        "MAROON" : self.convert_rgb (128, 0, 0) ,
                        "OLIVE" : self.convert_rgb (128, 128, 0) ,
                        "GREEN" : self.convert_rgb (0, 128, 0) ,
                        "PURPLE" : self.convert_rgb (80, 0, 80) ,
                        "TEAL" : self.convert_rgb (0, 128, 128) ,
                        "NAVY" : self.convert_rgb (0, 0, 128)
                        }
        self.fonts = {}
        self.images = {}
        self.font_default = None
        self.font_color_default = self.color_names ["WHITE"]
        self.background_color_default = self.color_names ["BLUE"]
        self.border_color_default = self.color_names ["BLUE"]
        self.border_width_default = 0
        self.padding_width_default = 0
        self.configuration_page = None

        # Check for configuration file
        if "config_file" in kwargs :
            self.setup_config_file (kwargs["config_file"])

    def get_configuration_page (self) :
        return self.configuration_page

    def setup_config_file (self, file_name) :
        config_dict = None
        try :
        #if True :
            with open(file_name, 'r') as config_file:
                config_dict = json.loads(config_file.read())
        except :
        #else :
            print ("Configuration file error:", file_name)
            return
        self.setup_config_dict (config_dict)
    def setup_config_dict (self, config_dict) :
        if config_dict is None :
            return
        if "page_id" not in config_dict :
            config_dict["page_id"] = "_PAGE_{:2d}".format (self.page_count)
        self.configuration_page = RemotePage ()
        page_obj = self.configure (config_dict)
        #print ("page_obj:", page_obj)
        #page_obj.active = False
        self.page_names[config_dict["page_id"]] = page_obj
        self.page_index.append (page_obj)
        self.area_reload (page_obj)
        if self.page_count <= 0 :
            self.page = self.configuration_page
        self.page_count += 1
        gc.collect ()
    def configure (self, area_config) :
        if "areas" not in area_config :
            area_config ["areas"] = []
        area_obj = None
        if "type" not in area_config :
            area_config ["type"] = "container"
        if area_config ["type"] not in self.area_types :
            print ("Unknown area type:", area["type"])
            area_config ["type"] = "container"
        area_obj = self.area_types [area_config ["type"]] (self, area_config)
        if area_obj is None :
            return None
        if "area_id" in area_config :
            self.areas [area_config ["area_id"]] = area_obj
        for child in area_config ["areas"] :
            child ["parent_hpos"] = area_obj.xmin
            child ["parent_vpos"] = area_obj.ymin
            area_obj.add_area (self.configure (child))
        return area_obj

    def get_color_name (self, color_name) :
        if color_name in self.color_names :
            return self.color_names [color_name]
        return 0         # black

    #---- Load command (eg. switch page)
    def add_update (self, update_id, update_class) :
        self.areas [update_id] = update_class (self)
    #---- User defined area type
    def add_area_type (self, area_type, area_class) :
        self.area_types [area_type] = area_class
    #---- Load font
    def add_font (self, font_id, file_name, width, height) :
        self.fonts [font_id] = super().font_initialize (file_name, width, height)
        if self.font_default == None :
            self.font_default = self.fonts [font_id]    # first font
    #---- Load image
    def add_image (self, image_id, file_name, width, height, ramdisk_file_name = None) :
        image_file = file_name
        #
        if ramdisk_file_name is not None :
            try :
            #if True :
                with open (file_name, "rb") as disk_file :
                    with open (ramdisk_file_name, "wb") as ramdisk_file :
                        ramdisk_file.write (disk_file.read())
                image_file = ramdisk_file_name
            #else :
            except Exception :
                print ("copy to ramdisk failed:", file_name)
        #
        self.images [image_id] = {"file_name" : image_file ,
                                  "width" : width ,
                                  "height" : height}
            
    def area_reload (self, area) :
        if not area.page_is_active () :
            return
        area.reload ()

    def screen_reload (self) :
        self.screen_clear (color = self.background_color_default)
        self.area_reload (self.page)

    def update_area (self, **kwargs) :
        if "area" not in kwargs :
            print ("area parameter missing", kwargs)
            return
        area_id = kwargs ["area"]
        if area_id not in self.areas :
            print ("area_id invalid:", area_id)
            return
        area = self.areas[area_id]
        area.update (**kwargs)
            
    def show_area (self, area_id = None, show_all = True) :
        area = None
        if area_id is None :
            area = self.page
        elif area_id in self.areas :
            area = self.areas [area_id]
        else :
            print ("Unknown area id:", area_id)
            return
        area.show_area (show_all = show_all)

    def page_by_name (self, page_name) :
        #print ("page_by_name:",self.page_names)
        if page_name not in self.page_names :
            return
        #print ("page_by_name:",self.page)
        self.page.set_page_active(False)
        self.page = self.page_names[page_name]
        #self.page["globals"]["active"] = True
        self.page.set_page_active(True)
        self.screen_reload ()
    def page_by_index (self, page_index) :
        if page_index < 0 \
        or page_index >= len (self.page_index) :
            return
        self.page.set_page_active(False)
        #self.page["globals"]["active"] = False
        self.page = self.page_index[page_index]
        self.page.set_page_active(True)
        #self.page["globals"]["active"] = True
        self.screen_reload ()

    def get_child_list (self, parent_id) :
        if parent_id not in self.areas :
            print ("Unknown area id:", parent_id)
            #print (self.areas)
            return
        parent_area = self.areas [parent_id]
        child_list = []
        for area in parent_area.areas :
            #print (area)
            if area.area_id is not None :
                child_list.append (area.area_id)
        return child_list

    def number_justify (self, num, rlen=10, pad=" ") :
        formatted = re.sub ("[^0-9.-]", "", num)
        if "-" in formatted :
            formatted = str ("-" + re.sub ("[^0-9.]", "", formatted))
        flen = len (formatted)
        if flen < rlen :
            formatted = (pad * (rlen - flen)) + formatted
        elif flen > rlen :
            formatted = formatted [(flen - rlen)]
        return formatted

    def get_font (self, font_id) :
        return self.fonts[font_id]
    def get_font_default (self) :
        return self.font_default
    def get_font_color_default (self) :
        return self.font_color_default
    def get_background_color_default (self) :
        return self.background_color_default
    def get_color_by_name (self, color_name) :
        return self.color_names[color_name]

    def dump_area (self, area, level=0) :
        if area.area_id is not None :
            area_id = area.area_id
        else :
            area_id = "anon"
        if level <= 0 :
            indent = ""
        else :
            indent = "." * level + " "
        print (indent + area_id)
        for child in area.areas :
            self.dump_area (child, level + 1)
    def dump (self) :
        for area in self.page_index :
            #print (area.area_id)
            self.dump_area (area)
            
    
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
                        trace_methods = ["image"] ,
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

disp.add_area_type ("template", RemoteTemplate)
disp.add_area_type ("7segment", Remote7Segment)
disp.add_update ("switchpage", RemoteSwitchPage)


#
iwidth = 15
iheight = 25
hpos = 0
hlen = 15
vpos = 0
vlen = 25

disp.add_font ('default', 'fonts/Unispace12x24.c', 12, 24)
disp.add_font ('bally7x9', 'fonts/Bally7x9.c', 7, 9)


disp.add_image ('nixie0', 'images/nixie0.raw', iwidth, iheight)
disp.add_image ('nixie1', 'images/nixie1.raw', iwidth, iheight)
disp.add_image ('nixie2', 'images/nixie2.raw', iwidth, iheight)
disp.add_image ('nixie3', 'images/nixie3.raw', iwidth, iheight)
disp.add_image ('nixie4', 'images/nixie4.raw', iwidth, iheight)
disp.add_image ('nixie5', 'images/nixie5.raw', iwidth, iheight)
disp.add_image ('nixie6', 'images/nixie6.raw', iwidth, iheight)
disp.add_image ('nixie7', 'images/nixie7.raw', iwidth, iheight)
disp.add_image ('nixie8', 'images/nixie8.raw', iwidth, iheight)
disp.add_image ('nixie9', 'images/nixie9.raw', iwidth, iheight)
disp.add_image ('nixieoff', 'images/nixieoff.raw', iwidth, iheight)
disp.add_image ('nixieminus', 'images/nixieminus.raw', iwidth, iheight)
'''
disp.add_image ('nixie0', 'images/nixie0.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie0.raw")
disp.add_image ('nixie1', 'images/nixie1.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie1.raw")
disp.add_image ('nixie2', 'images/nixie2.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie2.raw")
disp.add_image ('nixie3', 'images/nixie3.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie3.raw")
disp.add_image ('nixie4', 'images/nixie4.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie4.raw")
disp.add_image ('nixie5', 'images/nixie5.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie5.raw")
disp.add_image ('nixie6', 'images/nixie6.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie6.raw")
disp.add_image ('nixie7', 'images/nixie7.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie7.raw")
disp.add_image ('nixie8', 'images/nixie8.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie8.raw")
disp.add_image ('nixie9', 'images/nixie9.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixie9.raw")
disp.add_image ('nixieoff', 'images/nixieoff.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixieoff.raw")
disp.add_image ('nixieminus', 'images/nixieminus.raw', iwidth, iheight, ramdisk_file_name="ramdisk/nixieminus.raw")
'''

# nixie with decimal point
disp.add_image ('nixie0dp', 'images/nixie0dp.raw', iwidth, iheight)
disp.add_image ('nixie1dp', 'images/nixie1dp.raw', iwidth, iheight)
disp.add_image ('nixie2dp', 'images/nixie2dp.raw', iwidth, iheight)
disp.add_image ('nixie3dp', 'images/nixie3dp.raw', iwidth, iheight)
disp.add_image ('nixie4dp', 'images/nixie4dp.raw', iwidth, iheight)
disp.add_image ('nixie5dp', 'images/nixie5dp.raw', iwidth, iheight)
disp.add_image ('nixie6dp', 'images/nixie6dp.raw', iwidth, iheight)
disp.add_image ('nixie7dp', 'images/nixie7dp.raw', iwidth, iheight)
disp.add_image ('nixie8dp', 'images/nixie8dp.raw', iwidth, iheight)
disp.add_image ('nixie9dp', 'images/nixie9dp.raw', iwidth, iheight)
disp.add_image ('nixieoffdp', 'images/nixieoffdp.raw', iwidth, iheight)
disp.add_image ('nixieminusdp', 'images/nixieminusdp.raw', iwidth, iheight)

nixie_img = {
    "digit" : {
            "0" : 'nixie0' ,
            "1" : 'nixie1',
            "2" : 'nixie2', 
            "3" : 'nixie3',
            "4" : 'nixie4',
            "5" : 'nixie5',
            "6" : 'nixie6',
            "7" : 'nixie7',
            "8" : 'nixie8',
            "9" : 'nixie9',
            " " : 'nixieoff',
            "-" : 'nixieminus'
            } ,
    "digitdp" : {
            "0" : 'nixie0dp' ,
            "1" : 'nixie1dp',
            "2" : 'nixie2dp', 
            "3" : 'nixie3dp',
            "4" : 'nixie4dp',
            "5" : 'nixie5dp',
            "6" : 'nixie6dp',
            "7" : 'nixie7dp',
            "8" : 'nixie8dp',
            "9" : 'nixie9dp',
            " " : 'nixieoffdp',
            "-" : 'nixieminusdp'
            }
    }

disp.setup_config_file ("testtitle.json")
disp.setup_config_file ("testconfig.json")
disp.setup_config_file ("testeoj.json")
disp.dump ()
#sys.exit ()
#disp.show_area ("screen")
#sys.exit()

#sys.exit()

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

disp.screen_clear ()
disp.show_area ("screen")
time.sleep (5.0)

disp.update_area (area = "UpperRight", text = "Test")
disp.update_area (area = "UpperLeft", text = "Upper Left")

def display_nixie (num, nixie_container) :
    nixie_digits = disp.get_child_list (nixie_container)
    if nixie_digits is None :
        return
    formatted = disp.number_justify (str(num), rlen=len(nixie_digits))
    if "." in formatted :
        formatted = " " + formatted
    flen = len(formatted)
    area_idx = 0
    digit_idx = 0
    for nixie_area_id in nixie_digits :
        if formatted [digit_idx] == "." :
            digit_idx += 1                      # skip decimal point
        image_group = nixie_img["digit"]        # default No DP
        if digit_idx < (flen - 1) :
            if formatted [digit_idx + 1] == "." :
                image_group = nixie_img["digitdp"] # digit + DP
        disp.update_area (area = nixie_area_id ,
                        image_id = image_group [str(formatted[digit_idx])])
        digit_idx += 1

print ("mem_free:",gc.mem_free())
gc.collect()
print ("mem_free:",gc.mem_free())

disp.update_area (area = "switchpage", page_id = "testtitle")
#sys.exit()
time.sleep (5)
disp.update_area (area = "7seg", text = "  1024.48")
time.sleep (5)
disp.update_area (area = "7seg", text = "   -24.84")
#sys.exit()
time.sleep (2)
disp.update_area (area = "switchpage", page_id = "testconfig")
time.sleep (2)

start_ms = time.ticks_ms ()
for i in range (0,10) :
    time.sleep (5)
    print ("iteration #################################################")
    ticks = disp.number_justify (str(time.ticks_diff (time.ticks_ms(), start_ms)))
    disp.update_area (area = "UpperRight", text = ticks)
                      #text = disp.number_justify (str(time.ticks_diff (time.ticks_ms(), start_ms))))
    display_nixie (round (float (ticks) / 1000, 1), "nix")
    disp.update_area (area = "Fortune",
                      text = fortunes [random.randrange (0,len(fortunes))])
    disp.update_area (area = "Lamp1",
                      lamp_index = (i % 2))
    disp.update_area (area = "WarpDrive",
                      lamp_index = (i % 3))
    disp.update_area (area = "StopLight",
                      lamp_index = (i % 3))
    #disp.page_by_index (i % 2)
#print (disp.get_trace_stats ())
time.sleep (5)
print ("testeoj")
disp.update_area (area = "switchpage", page_id = "testeoj")
#disp.page_by_name ("testeoj")

time.sleep (2)
disp.screen_off ()
time.sleep (2)
disp.screen_on ()
#time.sleep (2)
try :
    print (disp.get_trace_stats ())
except :
    pass

