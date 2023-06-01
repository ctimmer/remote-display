#

import sys
import time
import random

from ili9341 import Display, color565
from machine import Pin, SPI  # type: ignore

from xglcd_font import XglcdFont

import ujson

class ILI9341Display :
    def __init__ (self , **kwargs) :
        #print ("ILI9341Display:", kwargs)
        self.display = self.initialize_display (**kwargs)
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
        #self.font_default = XglcdFont('fonts/Unispace12x24.c', 12, 24)
        self.font_default = XglcdFont('fonts/Unispace12x24.c', 12, 24)
        self.color_default = self.color_names ["YELLOW"]
        self.background_default = self.color_names ["BLUE"]
        self.screen_clear_params = {
                                    "color" : "color" ,
                                    "hlines" : "hlines"
                                    }
        self.pixel_params = {
                            "x" : "x" ,
                            "xpos" : "x" ,
                            "y" : "y" ,
                            "ypos" : "y" ,
                            "color" : "color"
                            }
        self.text_params = {
                            "x" : "x" ,
                            "xpos" : "x" ,
                            "y" : "y" ,
                            "ypos" : "y" ,
                            "text" : "text" ,
                            "font" : "font" ,
                            "color" : "color" ,
                            "background" : "background" ,
                            "spacing" : "spacing"
                            }
        self.line_params = {
                            "x1" : "x1" ,
                            "x1pos" : "x1" ,
                            "y1" : "y1" ,
                            "y1pos" : "y1" ,
                            "x2" : "x2" ,
                            "x2pos" : "x2" ,
                            "y2" : "y2" ,
                            "y2pos" : "y2" ,
                            "color" : "color"
                            }
        self.rectangle_params = {
                                "x" : "x" ,
                                "xpos" : "x" ,
                                "y" : "y" ,
                                "ypos" : "y" ,
                                "h" : "h" ,
                                "vlen" : "h" ,
                                "height" : "h" ,
                                "w" : "w" ,
                                "hlen" : "w" ,
                                "width" : "w" ,
                                "color" : "color"
                                }
        self.circle_params = {
                                "x" : "x0" ,
                                "x0" : "x0" ,
                                "xpos" : "x0" ,
                                "y" : "y0" ,
                                "y0" : "y0" ,
                                "ypos" : "y0" ,
                                "r" : "r" ,
                                "radius" : "r" ,
                                "color" : "color"
                                }
        # draw_polygon(self, sides, x0, y0, r, color, rotate=0):
        self.polygon_params = {
                                "sides" : "sides" ,
                                "x0" : "x0" ,
                                "xcenter" : "x0" ,
                                "y0" : "y0" ,
                                "ycenter" : "y0" ,
                                "r" : "r" ,
                                "radius" : "r" ,
                                "color" : "color" ,
                                "rotate" : "rotate"
                                }
    def initialize_display (self, **kwargs) :
        display = None
        display_object_params = {
                                "display" : "display_object" ,
                                "display_object" : "display_object"
                                }
        spi_params = {
                        "id" : "id" ,
                        "spi_id" : "id" ,
                        "baudrate" : "baudrate" ,
                        "spi_baudrate" : "baudrate" ,
                        "polarity" : "polarity" ,
                        "spi_polarity" : "polarity" ,
                        "phase" : "phase" ,
                        "spi_phase" : "phase" ,
                        "bits" : "bits" ,
                        "spi_bits" : "bits" ,
                        #"firstbit" : "firstbit" ,
                        #"spi_firstbit" : "firstbit" ,
                        "sck" : "sck" ,
                        "spi_sck" : "sck" ,
                        "mosi" : "mosi" ,
                        "spi_mosi" : "mosi" ,
                        "miso" : "miso" ,
                        "spi_miso" : "miso"
                        }
        display_params = {
                            "width" : "width" ,
                            "display_width" : "width" ,
                            "height" : "height" ,
                            "display_height" : "height" ,
                            "rotation" : "rotation" ,
                            "display_rotation" : "rotation" ,
                            "dc" : "dc" ,
                            "display_dc" : "dc" ,
                            "cs" : "cs" ,
                            "display_cs" : "cs" ,
                            "rst" : "rst" ,
                            "display_rst" : "rst"
                            }
        display_object_args = {}
        spi_args = {}
        display_args = {}
        #
        # if display is already set up, store it and exit
        for id in kwargs :
            if id in display_object_params :
                arg_id = display_object_params [id]
                display_object_args [arg_id] = kwargs [id]
            elif id in spi_params :
                arg_id = spi_params [id]
                spi_args [arg_id] = kwargs [id]
            elif id in display_params :
                arg_id = display_params [id]
                display_args [arg_id] = kwargs [id]
            else :
                print ("__init__: Unknown parameter", id)
        if "display_object" in display_object_args :
            self.display = display_object_args ["display_object"]
            return self.display
        #
        # is this SPI
#         for id in kwargs :
#             if id in spi_params :
#                 arg_id = spi_params [id]
#                 spi_args [arg_id] = kwargs [id]
#         for id in kwargs :
#             if id in display_params :
#                 #print (id)
#                 arg_id = display_params [id]
#                 display_args [arg_id] = kwargs [id]

        if "id" in spi_args :             # this is SPI
            for pin_arg in ["sck", "mosi", "miso"] :
                if pin_arg in spi_args :
                    spi_args [pin_arg] = Pin (spi_args [pin_arg])
            spi = SPI (**spi_args)
            for pin_arg in ["dc", "cs", "rst"] :
                if pin_arg in display_args :
                    display_args [pin_arg] = Pin (display_args [pin_arg])
            display = Display (spi, **display_args)
        #---- Handle other interfaces here
        else :
            pass # error

        return display

    '''
    def clear(self, color=0, hlines=8):
    '''
    def screen_clear (self, **kwargs) :
        named_args = {
                    "color" : self.background_default
                    }
        for id in kwargs :
            if id in self.screen_clear_params :
                named_args [self.screen_clear_params [id]] = kwargs [id]
        self.display.clear (**named_args)
    def screen_off (self) :
        """Turn display off."""
        self.display.write_cmd (self.display.DISPLAY_OFF)

    def screen_on (self) :
        """Turn display on."""
        self.display.write_cmd (self.display.DISPLAY_ON)
    '''
    def draw_pixel(self, x, y, color):
    '''
    def pixel (self, **kwargs) :
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "color" : self.color_default
                    }
        for id in kwargs :
            if id in self.text_params :
                named_args [self.text_params [id]] = kwargs [id]
        self.display.draw_pixel (**named_args)

    '''
        def draw_polygon(self, sides, x0, y0, r, color, rotate=0):
    '''
    def polygon (self, **kwargs) :
        #print ("text kwargs:", kwargs)
        named_args = {
                    "sides" : 6 ,
                    "x0" : 5 ,
                    "y0" : 5 ,
                    "r" : 4 ,
                    "color" : self.color_default
                    }
        for id in kwargs :
            if id in self.polygon_params :
                named_args [self.polygon_params [id]] = kwargs [id]
        self.display.draw_polygon (**named_args)

    '''
    def draw_text(self, x, y, text, font, color,  background=0,
                  landscape=False, spacing=1):
    def draw_text8x8(self, x, y, text, color,  background=0,
                     rotate=0):
    '''
    def text (self, **kwargs) :
        #print ("text kwargs:", kwargs)
        backgroundcolor = self.background_default
        if "backgroundcolor" in kwargs :
            backgroundcolor = kwargs["backgroundcolor"]
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "text" : "NotSet" ,
                    #"font" : self.font_default ,
                    "color" : self.color_default ,
                    "background" : backgroundcolor
                    }
        if self.font_default is not None :
            named_args ["font"] = self.font_default
        for id in kwargs :
            if id in self.text_params :
                named_args [self.text_params [id]] = kwargs [id]
        #print ("text named_args:", named_args)
        if "font" in named_args :
            named_args ["spacing"] = 1
            self.display.draw_text (**named_args)
        else :
            self.display.draw_text8x8 (**named_args)
    '''
    def draw_line(self, x1, y1, x2, y2, color):
    '''
    def line (self, **kwargs) :
        #print ("text kwargs:", kwargs)
        named_args = {
                    "x1" : 0 ,
                    "y1" : 0 ,
                    "x2" : 0 ,
                    "y2" : 0 ,
                    "color" : self.color_default
                    }
        for id in kwargs :
            if id in self.line_params :
                named_args [self.line_params [id]] = kwargs [id]
        #print ("text named_args:", named_args)
        self.display.draw_line (**named_args)
    '''
    def draw_rectangle(self, x, y, w, h, color):
    '''
    def rectangle (self, **kwargs) :
        #print ("text kwargs:", kwargs)
        color = self.color_default
        if "color" in kwargs :
            color = kwargs ["color"]
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "h" : 0 ,
                    "w" : 0 ,
                    "color" : color
                    }
        for id in kwargs :
            if id in self.rectangle_params :
                named_args [self.rectangle_params [id]] = kwargs [id]
        self.display.draw_rectangle(**named_args)
    '''
    def fill_rectangle(self, x, y, w, h, color):
    '''
    def rectangle_fill (self, **kwargs) :
        color = self.background_default
        if "color" in kwargs :
            color = kwargs ["color"]
            #print ("rf:",color)
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "w" : 0 ,
                    "h" : 0 ,
                    "color" : color
                    }
        for id in kwargs :
            if id in self.rectangle_params :       # same as rectangle
                named_args [self.rectangle_params [id]] = kwargs [id]
        #print (named_args)
        self.display.fill_rectangle(**named_args)
    '''
    def draw_circle(self, x0, y0, r, color):
    '''
    def circle (self, **kwargs) :
        color = self.color_default
        if "color" in kwargs :
            color = kwargs ["color"]
        named_args = {
                    "x0" : 10 ,
                    "y0" : 10 ,
                    "r" : 10 ,
                    "color" : color
                    }
        for id in kwargs :
            if id in self.circle_params :       # same as rectangle
                named_args [self.circle_params [id]] = kwargs [id]
        self.display.draw_circle(**named_args)
    '''
    def fill_circle(self, x0, y0, r, color):
    '''
    def circle_fill (self, **kwargs) :
        color = self.color_default
        if "color" in kwargs :
            color = kwargs ["color"]
        named_args = {
                    "x0" : 10 ,
                    "y0" : 10 ,
                    "r" : 10 ,
                    "color" : color
                    }
        for id in kwargs :
            if id in self.circle_params :       # same as rectangle
                named_args [self.circle_params [id]] = kwargs [id]
        self.display.fill_circle(**named_args)

    #-------------------------------------------------------------------------------        
    def convert_rgb (self, red, green, blue) :    # _16bit from below
        return ((red & 0b11111000) << 8) | ((green & 0b11111100) << 3) | (blue >> 3)
    def convert_rgb_8bit (self, red, green, blue) :
        return ((red & 0b11100000) << 5) | ((green & 0b11100000) << 2) | ((blue & 0b11000000) >> 6)
    def convert_rgb_16bit (self, red, green, blue) :
        return ((red & 0b11111000) << 8) | ((green & 0b11111100) << 3) | (blue >> 3)
    def convert_rgb_24bit (self, red, green, blue) :
        return (red << 15) | (green << 7) | blue

    def get_color_name (self, color_name):
        return self.color_names[color_name]

    def get_font_default (self) :
        return self.font_default
    def get_color_default (self) :
        return self.color_default
    def get_background_default (self) :
        return self.background_default
        
    def reverse_bits (self, bit_field, bits=8) :
        reversed_bits = 0x000000
        msd = bits - 1
        for bit_idx in range (0, bits) :
            reversed_bits |= ((bit_field >> bit_idx) & 0x01) << (msd - bit_idx)
        return reversed_bits

    def dummy_test (self, mess = "dummy_test") :
        print (mess)

## end ILI9341Display ##

#-------------------------------------------------------------------------------
# TraceDisplay
#-------------------------------------------------------------------------------
class TraceDisplay (ILI9341Display) :
    def __init__ (self, **kwargs) :
        print ("TraceDisplay running")
        print ("__init__:", kwargs)
        self.output_enabled = True

        self.trace_stats = {}
        if "trace_output" in kwargs :
            self.set_trace_output (kwargs ["trace_output"])
        if not self.output_enabled :
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
            self.font_default = None
            self.background_default = self.color_names ["BLUE"]
            self.color_default = self.color_names ["YELLOW"]
        self.trace_methods = [
                            "screen_clear" ,
                            "screen_on" ,
                            "screen_off" ,
                            "polygon" ,
                            "pixel" ,
                            "text" ,
                            "line" ,
                            "rectangle" ,
                            "rectangle_fill" ,
                            "circle" ,
                            "circle_fill"
                            ]
        if "trace_methods" in kwargs :
            self.set_trace_methods (kwargs ["trace_methods"])
        if self.output_enabled :
            super ().__init__ (**kwargs)
    def set_trace_methods (self, trace_methods) :
        self.trace_methods = trace_methods
    def set_trace_output (self, val) :
        if val :
            self.output_enabled = True
        else :
            self.output_enabled = False
        print("Trace output to Display:", self.output_enabled)
    def set_trace_in (self, method) :
        if method not in self.trace_stats :
            self.trace_stats [method] = {
                "count" : 0 ,
                "time_total" : 0 ,
                "time_in" : None ,
                "time_out" : None
                }
        method_stats = self.trace_stats[method]
        method_stats ["count"] += 1
        method_stats ["time_in"] = time.ticks_us ()
        method_stats ["time_out"] = None
    def set_trace_out (self, method) :
        if method not in self.trace_stats :
            return
        method_stats = self.trace_stats[method]
        if method_stats ["time_in"] is None :
            return
        method_stats ["time_out"] = time.ticks_us ()
        method_stats ["time_last"] \
            = time.ticks_diff (method_stats ["time_out"],
                                method_stats ["time_in"])
        method_stats ["time_total"] += method_stats ["time_last"]
        method_stats ["time_in"] = None
    def get_trace_stats (self) :
        return self.trace_stats

    def screen_clear (self, **kwargs) :
        method = "screen_clear"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().screen_clear (**kwargs)
            self.set_trace_out (method)
    def screen_on (self, **kwargs) :
        method = "screen_on"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().screen_on (**kwargs)
            self.set_trace_out (method)
    def screen_off (self, **kwargs) :
        method = "screen_off"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().screen_off (**kwargs)
            self.set_trace_out (method)

    def polygon (self, **kwargs) :
        method = "polygon"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().polygon (**kwargs)
            self.set_trace_out (method)
    def pixel (self, **kwargs) :
        method = "pixel"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().pixel (**kwargs)
            self.set_trace_out (method)
    def text (self, **kwargs) :
        method = "text"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().text (**kwargs)
            self.set_trace_out (method)
    def line (self, **kwargs) :
        method = "line"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().line (**kwargs)
            self.set_trace_out (method)
    def rectangle (self, **kwargs) :
        method = "rectangle"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().rectangle (**kwargs)
            self.set_trace_out (method)
    def rectangle_fill (self, **kwargs) :
        method = "rectangle_fill"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().rectangle_fill (**kwargs)
            self.set_trace_out (method)
    def circle (self, **kwargs) :
        method = "circle"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().circle (**kwargs)
            self.set_trace_out (method)
    def circle_fill (self, **kwargs) :
        method = "circle_fill"
        if method in self.trace_methods :
            print (method, kwargs)
        if self.output_enabled :
            self.set_trace_in (method)
            super ().circle_fill (**kwargs)
            self.set_trace_out (method)

    def get_color_name (self, color_name):
        if self.output_enabled :
            return super().get_color_name (color_name)
        return self.color_names[color_name]
    def get_font_default (self):
        if self.output_enabled :
            return super().get_font_default ()
        return self.font_default
    def get_color_default (self):
        if self.output_enabled :
            return super().get_color_default ()
        return self.color_default
    def get_background_default (self):
        if self.output_enabled :
            return super().get_background_default ()
        return self.background_default

## end TraceDisplay ##

#-------------------------------------------------------------------------------
# RemoteDisplay
#-------------------------------------------------------------------------------
#class RemoteDisplay (TraceDisplay) :
class RemoteDisplay (ILI9341Display) :
    def __init__ (self, **kwargs) :
        #print ("RD:", kwargs)
        super ().__init__ (**kwargs)
        self.active_default = True
        self.page = None
        self.page_count = 0
        self.page_names = {}
        self.page_index = []
        self.areas = {}

        if "config_file" in kwargs :
            #print ("config_file")
            self.setup_config_file (kwargs["config_file"])
            #self.setup_config_dict (config_dict)
        #print (self.areas)
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

if False :
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
