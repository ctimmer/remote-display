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
import time
import random
import re

from machine import Pin, SPI  # type: ignore

#from xglcd_font import XglcdFont

import ujson

#from xglcd_font import XglcdFont
#from ili9341 import Display
#from ili9341_display import ILI9341Display
from trace_display import TraceDisplay

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
        #print ("init:", self.page)
        #self.area = area
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
        self.fontcolor = remote_display.get_font_color_default()
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
        if "bordercolor" in area :
            self.bordercolor = area ["bordercolor"]
        if "paddingwidth" in area :
            self.paddingwidth = area ["paddingwidth"]
        if "backgroundcolor" in area :
            self.backgroundcolor = area ["backgroundcolor"]
        if "font_id" in area :
            self.font = remote_display.get_font (area ["font_id"])
        if "fontcolor" in area :
            self.fontcolor = area ["fontcolor"]

        #---- Set field data position/lengths parameters
        offsets = self.borderwidth + self.paddingwidth
        self.xlen = self.hlen - (offsets * 2)
        self.ylen = self.vlen - (offsets * 2)
        self.xmin = self.hpos + offsets
        self.ymin = self.vpos + offsets
        self.xmax = (self.xmin + self.xlen) - 1
        self.ymax = (self.ymin + self.ylen) - 1

    def add_area (self, area) :
        if area is not None :
            self.areas.append (area)
    def page_is_active (self) :
        return self.page.page_is_active ()
    def set_page_active (self, state) :
        self.page.set_page_active (state)

    def reload_border (self) :
        pass # need
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
        if not self.page_is_active() :
            return
        if reload_all :
            self.reload_background ()
        #image_id = self.image_id_current
        image_args = {
                    "hpos" : self.xmin ,
                    "vpos" : self.ymin
                    }
        image_args.update (self.remote_display.images[self.image_id_current])
        self.remote_display.image (**image_args)
        if reload_all :
            self.reload_areas ()

## end RemoteImage ##

#-------------------------------------------------------------------------------
# RemoteText
#-------------------------------------------------------------------------------
class RemoteText (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        self.text = ""
        if "value" in area_config :
            self.text = area_config ["value"]
        self.text_current = self.text
    def update (self, **kwargs) :
        if "value" not in kwargs :
            return
        self.text_current = kwargs ["value"]
        self.reload (reload_all = False)
    def reload (self, reload_all = True) :
        if not self.page_is_active() :
            return
        #print ("active")
        if reload_all :
            self.reload_background ()
        self.remote_display.rectangle_fill (x = self.xmin ,
                                            w = self.xlen ,
                                            y = self.ymin ,
                                            h = self.ylen,
                                            color=self.backgroundcolor) 
        self.remote_display.text (x = self.xmin ,
                                    y = self.ymin ,
                                    text = self.text_current,
                                  font = self.font ,
                                  color = self.fontcolor ,
                                  background = self.backgroundcolor)
        if reload_all :
            self.reload_areas ()

## end RemoteText ##

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
            if "value" in color :
                lamp["text"] = color ["value"]
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

#-------------------------------------------------------------------------------
class RemoteContainer (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)

## end RemoteLamp ##

#-------------------------------------------------------------------------------
class RemoteTemplate (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
    def update (self, **kwargs) :
        #
        #---- Make changes to area parameters
        #
        self.reload (reload_all = False)
        #
    def reset (self) :
        #
        #---- Set area parameters to initial state
        #
        self.reload ()
        #
    def reload (self, reload_all = True) :
        if not self.page_is_active() :
            return
        if reload_all :
            self.reload_background ()
        #
        #---- Output to display here
        #
        if reload_all :
            self.reload_areas ()

## end RemoteLamp ##

#-------------------------------------------------------------------------------
# RemoteDisplay
#-------------------------------------------------------------------------------
class RemoteSwitchPage () :
    def __init__ (self, remote_display) :
        self.remote_display = remote_display
    def update (self, **kwargs) :
        if "page_id" in kwargs :
            self.remote_display.page_by_name (kwargs["page_id"])
        elif "page_index" in kwargs :
            self.remote_display.page_by_index (kwargs["page_index"])

## end RemoteSwitch_page ##

#-------------------------------------------------------------------------------
# RemoteDisplay
#-------------------------------------------------------------------------------
class RemoteDisplay (TraceDisplay) :
#class RemoteDisplay (ILI9341Display) :
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
        #try :
        if True :
            with open(file_name, 'r') as config_file:
                config_dict = ujson.loads(config_file.read())
        #except Exception :
        else :
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
    def configure (self, area) :
        #print ("area:", area)
        #self.initialize_area (parent, area)
        if "areas" not in area :
            area ["areas"] = []
        area_obj = None
        if "type" not in area :
            area ["type"] = "container"
        if area ["type"] in self.area_types :
            area_obj = self.area_types [area ["type"]] (self, area)
        else :
            print ("Unknown area type:", area["type"])
            area_obj = RemoteContainer (self, area)
        if area_obj is None :
            return None
        if "area_id" in area :
            #print (area["area_id"])
            self.areas [area["area_id"]] = area_obj
        for child in area["areas"] :
            child ["parent_hpos"] = area_obj.hpos
            child ["parent_vpos"] = area_obj.vpos
            #print ("child:", child)
            area_obj.add_area (self.configure (child))
        return area_obj

    def get_color_name (self, color_name) :
        return self.color_names [color_name]

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
                with open (file_name, "r") as disk_file :
                    with open (ramdisk_file_name, "w") as ramdisk_file :
                        ramdisk_file.write (disk_file.read())
                image_file = ramdisk_file_name
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

    def get_font_default (self) :
        return self.font_default
    def get_font_color_default (self) :
        return self.font_color_default
    def get_background_color_default (self) :
        return self.background_color_default
    
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

#machine.freq(270000000)

if True :
    disp = RemoteDisplay (
                        trace_output = False ,
                        #trace_methods = ["image"] ,
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
disp.show_area ("screen")
sys.exit()

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

#print ("call dummy_test ##############")
#disp.dummy_test ()
#sys.exit()

#print ("screen_reload")
#disp.screen_reload ()
#disp.circle_fill (xpos=50, ypos=50, r=25, color=disp.color_names ["RED"])
#time.sleep (5)

#disp.update_lamp_area (area = "WarpDrive", color_name = "ok")
#sys.exit ()



#disp.screen_reload ()

disp.update_area (area = "UpperRight", value = "Test")
disp.update_area (area = "UpperLeft", value = "Upper Left")

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

disp.update_area (area = "switchpage", page_id = "testtitle")
time.sleep (2)
disp.update_area (area = "switchpage", page_id = "testconfig")
#time.sleep (2)
print ("show_areas ####################")
#disp.show_area (area_id = "LampRow", show_all = False)
disp.show_area ()
#time.sleep (5)
#sys.exit()

start_ms = time.ticks_ms ()
for i in range (0,10) :
    time.sleep (2)
    print ("iteration #################################################")
    ticks = disp.number_justify (str(time.ticks_diff (time.ticks_ms(), start_ms)))
    disp.update_area (area = "UpperRight", value = ticks)
                      #value = disp.number_justify (str(time.ticks_diff (time.ticks_ms(), start_ms))))
    display_nixie (round (float (ticks) / 1000, 1), "nix")
    disp.update_area (area = "Fortune",
                      value = fortunes [random.randrange (0,len(fortunes))])
    disp.update_area (area = "Lamp1",
                      lamp_index = (i % 2))
    disp.update_area (area = "WarpDrive",
                      lamp_index = (i % 3))
    disp.update_area (area = "StopLight",
                      lamp_index = (i % 3))
    #disp.page_by_index (i % 2)
#print (disp.get_trace_stats ())
time.sleep (5)
disp.update_area (area = "switchpage", page_id = "testeoj")
#disp.page_by_name ("testeoj")
#sys.exit()

time.sleep (2)
disp.screen_off ()
time.sleep (2)
disp.screen_on ()
#time.sleep (2)

#print (disp.get_trace_stats ())
