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
#
import sys
import time

#from ili9341_display import ILI9341Display
from display_config import *

class DummyDisplay () :
    def __init__ (self, **kwargs) :
        self.fonts = {}
        self.images = {}
        self.color_names = {
                        "BLACK" : "BLACK" ,
                        "WHITE" : "WHITE" ,
                        "RED" : "RED" ,
                        "LIME" : "LIME" ,
                        "BLUE" : "BLUE" ,
                        "YELLOW" : "YELLOW" ,
                        "CYAN" : "CYAN" ,
                        "MAGENTA" : "MAGENTA" ,
                        "SILVER" : "SILVER" ,
                        "GRAY" : "GRAY" ,
                        "MAROON" : "MAROON" ,
                        "OLIVE" : "OLIVE" ,
                        "GREEN" : "GREEN" ,
                        "PURPLE" : "PURPLE" ,
                        "TEAL" : "TEAL" ,
                        "NAVY" : "NAVY"
                        }
    def font_initialize (self, *argv) :
        return None
    def add_font (self, *argv) :
        self.fonts [argv[0]] = argv[1]
    def image_initialize (self, *argv) :
        return None
    def add_image (self, *argv) :
        self.images [argv[0]] = argv[1]
    #
    def screen_clear (self, **kwargs) :
        return None
    def screen_on (self, **kwargs) :
        return None
    def screen_off (self, **kwargs) :
        return None
    #
    def polygon (self, **kwargs) :
        pass
    def pixel (self, **kwargs) :
        pass
    def text (self, **kwargs) :
        pass
    def line (self, **kwargs) :
        pass
    def rectangle (self, **kwargs) :
        pass
    def rectangle_fill (self, **kwargs) :
        pass
    def circle (self, **kwargs) :
        pass
    def circle_fill (self, **kwargs) :
        pass
    def image (self, **kwargs) :
        pass
    #
    def convert_rgb (self, r, g, b) :
        return "rbg({:.d},{:.d},{:,d})".format (r, b, g)
    #def get_color_name (self, color_name):
        #return color_name
    def get_font_default (self):
        return None
    def get_color_default (self):
        return None
    def get_background_default (self):
        return None

## end DummyDisplay ##

#-------------------------------------------------------------------------------
# TraceDisplay
#-------------------------------------------------------------------------------
#class TraceDisplay (DummyDisplay) :
class TraceDisplay (TRACE_DISPLAY) :
    def __init__ (self, **kwargs) :
        print ("TraceDisplay running")
        print ("__init__:", kwargs)
        #self.output_enabled = True

        self.trace_stats = {}
        #if "trace_output" in kwargs :
            #self.set_trace_output (kwargs ["trace_output"])
        '''
        if not self.output_enabled :
            self.color_names = {
                        "BLACK" : "BLACK" ,
                        "WHITE" : "WHITE" ,
                        "RED" : "RED" ,
                        "LIME" : "LIME" ,
                        "BLUE" : "BLUE" ,
                        "YELLOW" : "YELLOW" ,
                        "CYAN" : "CYAN" ,
                        "MAGENTA" : "MAGENTA" ,
                        "SILVER" : "SILVER" ,
                        "GRAY" : "GRAY" ,
                        "MAROON" : "MAROON" ,
                        "OLIVE" : "OLIVE" ,
                        "GREEN" : "GREEN" ,
                        "PURPLE" : "PURPLE" ,
                        "TEAL" : "TEAL" ,
                        "NAVY" : "NAVY"
                        #
                        #"BLACK" : self.convert_rgb (0, 0, 0) ,
                        #"WHITE" : self.convert_rgb (255, 255, 255) ,
                        #"RED" : self.convert_rgb (255, 0, 0) ,
                        #"LIME" : self.convert_rgb (0, 255, 0) ,
                        #"BLUE" : self.convert_rgb (0, 0, 255) ,
                        #"YELLOW" : self.convert_rgb (255, 255, 0) ,
                        #"CYAN" : self.convert_rgb (0, 255, 255) ,
                        #"MAGENTA" : self.convert_rgb (255, 0, 255) ,
                        #"SILVER" : self.convert_rgb (192, 192, 192) ,
                        #"GRAY" : self.convert_rgb (128, 128, 128) ,
                        #"MAROON" : self.convert_rgb (128, 0, 0) ,
                        #"OLIVE" : self.convert_rgb (128, 128, 0) ,
                        #"GREEN" : self.convert_rgb (0, 128, 0) ,
                        #"PURPLE" : self.convert_rgb (80, 0, 80) ,
                        #"TEAL" : self.convert_rgb (0, 128, 128) ,
                        #"NAVY" : self.convert_rgb (0, 0, 128)
                        }
            '''
            #self.font_default = None
            #self.background_default = self.color_names ["BLUE"]
            #self.color_default = self.color_names ["YELLOW"]
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
                            "circle_fill" ,
                            "image"
                            ]
        if "trace_methods" in kwargs :
            self.set_trace_methods (kwargs ["trace_methods"])
        #if self.output_enabled :
        super ().__init__ (**kwargs)
    def set_trace_methods (self, trace_methods) :
        self.trace_methods = trace_methods
    '''
    def set_trace_output (self, val) :
        if val :
            self.output_enabled = True
        else :
            self.output_enabled = False
        print("Trace output to Display:", self.output_enabled)
    '''
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
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().screen_clear (**kwargs)
        self.set_trace_out (method)
    def screen_on (self, **kwargs) :
        method = "screen_on"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().screen_on (**kwargs)
        self.set_trace_out (method)
    def screen_off (self, **kwargs) :
        method = "screen_off"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().screen_off (**kwargs)
        self.set_trace_out (method)

    def polygon (self, **kwargs) :
        method = "polygon"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().polygon (**kwargs)
        self.set_trace_out (method)
    def pixel (self, **kwargs) :
        method = "pixel"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().pixel (**kwargs)
        self.set_trace_out (method)
    def text (self, **kwargs) :
        method = "text"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().text (**kwargs)
        self.set_trace_out (method)
    def line (self, **kwargs) :
        method = "line"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().line (**kwargs)
        self.set_trace_out (method)
    def rectangle (self, **kwargs) :
        method = "rectangle"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().rectangle (**kwargs)
        self.set_trace_out (method)
    def rectangle_fill (self, **kwargs) :
        method = "rectangle_fill"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().rectangle_fill (**kwargs)
        self.set_trace_out (method)
    def circle (self, **kwargs) :
        method = "circle"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().circle (**kwargs)
        self.set_trace_out (method)
    def circle_fill (self, **kwargs) :
        method = "circle_fill"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().circle_fill (**kwargs)
        self.set_trace_out (method)
    def image (self, **kwargs) :
        method = "image"
        if method in self.trace_methods :
            print (method, kwargs)
        #if self.output_enabled :
        self.set_trace_in (method)
        super ().image (**kwargs)
        self.set_trace_out (method)
    #
    def get_font_default (self):
        #if self.output_enabled :
        return super().get_font_default ()
        #return self.font_default
    def get_color_default (self):
        #if self.output_enabled :
        return super().get_color_default ()
        #return self.color_default
    def get_background_default (self):
        #if self.output_enabled :
        return super().get_background_default ()
        #return self.background_default

## end TraceDisplay ##

