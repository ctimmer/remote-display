#

from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI  # type: ignore

from xglcd_font import XglcdFont

import ujson

class ILI9341Display :
    def __init__ (self , **kwargs) :
        #print (kwargs)
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
        named_args = {
                    "id" : 0
                    }
        for id in kwargs :
            if id in spi_params :
                arg_id = spi_params [id]
                if arg_id in ["sck", "mosi", "miso"] :
                    named_args [arg_id] = Pin (kwargs [id])
                else :
                    named_args [arg_id] = kwargs [id]
        #print ("spi:", named_args)
        spi = SPI (**named_args)
        #
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
        named_args = {}
        for id in kwargs :
            if id in display_params :
                #print (id)
                arg_id = display_params [id]
                if arg_id in ["dc", "cs", "rst"] :
                    named_args [arg_id] = Pin (kwargs [id])
                else :
                    named_args [arg_id] = kwargs [id]
        #print ("display:", named_args)
        self.display = Display(spi, **named_args)
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
        #print ("screen_clear:", named_args)
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
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "text" : "NotSet" ,
                    #"font" : self.font_default ,
                    "color" : self.color_default ,
                    "background" : self.background_default
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
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "h" : 0 ,
                    "w" : 0 ,
                    "color" : self.color_default
                    }
        for id in kwargs :
            if id in self.rectangle_params :
                named_args [self.rectangle_params [id]] = kwargs [id]
        self.display.draw_rectangle(**named_args)
    #------
    def convert_rgb (self, red, green, blue) :    # _16bit from below
        return ((red & 0x1f) << 11) | ((green & 0x3f) << 5) | (blue & 0x1f)
    def convert_rgb_8bit (self, red, green, blue) :
        return ((red & 0x07) << 5) | ((green & 0x07) << 2) | (blue & 0x03)
    def convert_rgb_16bit (self, red, green, blue) :
        return ((red & 0x1f) << 11) | ((green & 0x3f) << 5) | (blue & 0x1f)
    def convert_rgb_24bit (self, red, green, blue) :
        return (red << 15) | (green << 7) | blue
    
#-------------------------------------------------------------------------------
# TraceDisplay
#-------------------------------------------------------------------------------
class TraceDisplay (ILI9341Display) :
    def __init__ (self, **kwargs) :
        print ("TraceDisplay running")
        print ("__init__:", kwargs)
        super ().__init__ (**kwargs)
    def pixel (self, **kwargs) :
        print ("pixel", kwargs)
        super ().pixel (**kwargs)
    def line (self, **kwargs) :
        print ("line:", kwargs)
        super ().line (**kwargs)
    def rectangle (self, **kwargs) :
        print ("rectangle:", kwargs)
        super ().rectangle (**kwargs)

class RemoteDisplay (TraceDisplay) :
#class RemoteDisplay (ILI9341Display) :
    def __init__ (self, **kwargs) :
        super ().__init__ (**kwargs)

        with open('testconfig.json', 'r') as config_file:
            #data = config_file.read ()
            #print (data)
            self.config = ujson.loads(config_file.read())
            #print(self.config)
        self.areas = {}
        self.configure (None, self.config)
        #for id in self.areas :
            #print (id)
    def configure (self, parent, area) :
        #print ("area:", area)
        if parent is None :
            area["wpos"] = 0
            area["hpos"] = 0
        if "id" in area :
            #print (area['id'])
            self.areas [area["id"]] = area
        if "areas" in area :
            for child in area["areas"] :
                self.configure (area, child)
    #def pixel (self, **kwargs) :
    #    arguments = {"id" : "value"}
    #    super().d_pixel (**arguments)

################################################################################
# main
################################################################################
#

disp = RemoteDisplay (
                    config_file = "tesconfig.json" ,
                    #---- SPI parameters
                    spi_id = 0 ,
                    sck = 18 ,
                    mosi = 19 ,
                    miso = 16 ,
                    baudrate = 10000000 ,
                    polarity = 1 ,
                    phase = 1 ,
                    bits = 8 ,
                    #firstbit = SPI.MSB ,
                    #---- Display parameters
                    display_width = 320 ,
                    height = 240 ,
                    rotation = 270 ,
                    dc = 15 ,
                    cs = 17 ,
                    rst = 14
                    )
                    #

disp.screen_clear ()
disp.text (x = 20, y = 112, text="Hello, World!")
for x in range (20,40) :
    disp.pixel (x = x, y = 10, color = disp.color_names ["RED"])

disp.line (x1 = 30, y1 = 30, x2 = 90, y2 = 90, color = disp.color_names ["WHITE"])

disp.rectangle (x = 50, y = 150, width = 100, height = 20, color = disp.color_names ["CYAN"])

disp.polygon (sides = 6, x0 = 50, y0 = 200, r = 10)

#print (disp.convert_rgb (0,0,255))

