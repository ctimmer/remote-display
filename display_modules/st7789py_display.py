#

from st7789s3 import ST7789
from machine import Pin, SPI

#from xglcd_font import XglcdFont

class ST7789Display :
    def __init__ (self , **kwargs) :
        self.display = self.initialize_display (**kwargs)
        xy_params = {
                    "x" : "x" ,
                    "xpos" : "x" ,
                    "hpos" : "x" ,
                    "y" : "y" ,
                    "ypos" : "y" ,
                    "vpos" : "y"
                    }
        length_params = {
                        "h" : "h" ,
                        "vlen" : "h" ,
                        "height" : "h" ,
                        "w" : "w" ,
                        "hlen" : "w" ,
                        "width" : "w"
                        }
        self.screen_clear_params = {
                                    "color" : "color" ,
                                    "hlines" : "hlines"
                                    }
        self.pixel_params = {
                            "color" : "color"
                            }
        self.pixel_params.update (xy_params)
        self.text_params = {
                            "text" : "text" ,
                            "font" : "font" ,
                            "color" : "color" ,
                            "background" : "background" ,
                            "spacing" : "spacing"
                            }
        self.text_params.update (xy_params)
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
                                "color" : "color"
                                }
        self.rectangle_params.update (xy_params)
        self.rectangle_params.update (length_params)
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
        self.image_params = {
                            "path" : "path" ,
                            "file_name" : "path"
                            }
        self.image_params.update (xy_params)
        self.image_params.update (length_params)
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
        ignore_params = {
                        "trace_methods" : "Used by RemoteTrace"
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
            elif id in ignore_params :
                pass
            else :
                print ("__init__: Unknown parameter", id)
        if "display_object" in display_object_args :
            self.display = display_object_args ["display_object"]
            return self.display
        #
        # is this SPI
        if "id" in spi_args :
            # SPI pin objects
            for pin_arg in ["sck", "mosi", "miso"] :
                if pin_arg in spi_args :
                    spi_args [pin_arg] = Pin (spi_args [pin_arg])
            spi = SPI (**spi_args)
            # display pin objects
            for pin_arg in ["dc", "cs", "rst"] :
                if pin_arg in display_args :
                    display_args [pin_arg] = Pin (display_args [pin_arg])
            display = Display (spi, **display_args)
        #---- Handle other interfaces here
        else :
            pass # error

        return display

    def font_initialize (self, file_name, width, height) :
        return XglcdFont(file_name, width, height)
    '''
    def clear(self, color=0, hlines=8):
    '''
    def screen_clear (self, **kwargs) :
        named_args = {
                    "color" : None
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
                    "x" : None ,
                    "y" : None ,
                    "color" : None
                    }
        for id in kwargs :
            if id in self.text_params :
                named_args [self.text_params [id]] = kwargs [id]
        self.display.draw_pixel (named_arge["x"], named_arge["y"], named_arge["color"])

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
                    "font" : None ,
                    "color" : None ,
                    "background" : None
                    }
        #if self.font_default is not None :
            #named_args ["font"] = self.font_default
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
    def line(self, x0, y0, x1, y1, color):
    '''
    def line (self, **kwargs) :
        #print ("text kwargs:", kwargs)
        named_args = {
                    "x0" : None ,
                    "y0" : None ,
                    "x1" : None ,
                    "y1" : None ,
                    "color" : None
                    }
        for id in kwargs :
            if id in self.line_params :
                named_args [self.line_params [id]] = kwargs [id]
        #print ("text named_args:", named_args)
        self.display.line (named_args["x0"] ,
                           named_args["y0"] ,
                           named_args["x1"] ,
                           named_args["y1"] ,
                           named_args["color"]
                           )
    '''
    def rect(self, x, y, w, h, color):
    '''
    def rectangle (self, **kwargs) :
        named_args = {
                    "x" : None ,
                    "y" : None ,
                    "h" : None ,
                    "w" : None ,
                    "color" : None
                    }
        for id in kwargs :
            if id in self.rectangle_params :
                named_args [self.rectangle_params [id]] = kwargs [id]
        self.display.rect (named_args["x"] ,
                            named_args["y"] ,
                            named_args["w"] ,
                            named_args["h"] ,
                            named_args["color"]
                            )
    '''
    def fill_rect (self, x, y, w, h, color):
    '''
    def rectangle_fill (self, **kwargs) :
        named_args = {
                    "x" : None ,
                    "y" : None ,
                    "w" : None ,
                    "h" : None ,
                    "color" : None
                    }
        for id in kwargs :
            if id in self.rectangle_params :       # same as rectangle
                named_args [self.rectangle_params [id]] = kwargs [id]
        self.display.fill_rect (named_args["x"] ,
                                named_args["y"] ,
                                named_args["w"] ,
                                named_args["h"] ,
                                named_args["color"]
                                )

    '''
    def bitmap(self, bitmap, x, y, index=0):
    '''
    def image (self, **kwargs) :
        #print ("image kwargs:", kwargs)
        bitmap = None
        named_args = {
            "path" : None ,
            "x" : None ,
            "y" : None
            }
        for id in kwargs :
            if id in self.image_params :
                named_args [self.image_params [id]] = kwargs [id]
        #---- Need to create bitmap from path?
        self.display.draw_image(bitmap ,
                                named_args["x"] ,
                                named_args["y"]
                                )

    #-------------------------------------------------------------------------------        
    def convert_rgb (self, red, green, blue) :    # _16bit from below
        return ((red & 0b11111000) << 8) | ((green & 0b11111100) << 3) | (blue >> 3)
    def convert_rgb_8bit (self, red, green, blue) :
        return ((red & 0b11100000) << 5) | ((green & 0b11100000) << 2) | ((blue & 0b11000000) >> 6)
    def convert_rgb_16bit (self, red, green, blue) :
        return ((red & 0b11111000) << 8) | ((green & 0b11111100) << 3) | (blue >> 3)
    def convert_rgb_24bit (self, red, green, blue) :
        return (red << 15) | (green << 7) | blue
        
    def reverse_bits (self, bit_field, bits=8) :
        reversed_bits = 0x000000
        msd = bits - 1
        for bit_idx in range (0, bits) :
            reversed_bits |= ((bit_field >> bit_idx) & 0x01) << (msd - bit_idx)
        return reversed_bits

    def dummy_test (self, mess = "dummy_test") :
        print (mess)

## end ST7789Display ##
