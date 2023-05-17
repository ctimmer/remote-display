#

from time import sleep
from ili9341 import Display, color565
from machine import Pin, SPI  # type: ignore

class ILI9341Display :
    def __init__ (self ,
                  width = 320 ,
                  height = 240 ,
                  rotation = 270 ,
                  spi_id = 0 ,
                  sck = 18 ,
                  mosi = 19 ,
                  miso = 16 ,
                  baudrate = 10000000 ,
                  polarity = 1 ,
                  phase = 1 ,
                  bits = 8 ,
                  firstbit = SPI.MSB ,
                  dc = 15 ,
                  cs = 17 ,
                  rst = 14
                  ) :
        spi = SPI(spi_id,
                  baudrate = baudrate ,
                  #baudrate=40000000 ,
                  polarity = polarity ,
                  phase = phase ,
                  bits = bits ,
                  firstbit = firstbit,
                  sck = Pin(sck),
                  mosi = Pin(mosi),
                  miso = Pin(miso))
        self.display = Display(spi,
                                width = width ,
                                height = height ,
                                rotation = rotation ,
                                dc = Pin(dc),
                                cs = Pin(cs),
                                rst = Pin(rst))
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
        self.color_default = self.color_names ["WHITE"]
        self.background_default = self.color_names ["BLUE"]
    '''
    def clear(self, color=0, hlines=8):
    '''
    def screen_clear (self, **kwargs) :
        color = self.background_default
        hlines = 8
        if "color" in kwargs :
            color = kwargs ['color']
        if "hlines" in kwargs :
            hlines = kwargs ["hlines"]
        self.display.clear (color = color ,
                            hlines = hlines
                            )
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
        x = 0
        y = 0
        color = self.color_default
        if "x" in kwargs :
            x = kwargs ['x']
        if "y" in kwargs :
            y = kwargs ['y']
        if "color" in kwargs :
            color = kwargs ['color']
        self.display.draw_pixel (x, y, color)

    '''
    def draw_text(self, x, y, text, font, color,  background=0,
                  landscape=False, spacing=1):
    def draw_text8x8(self, x, y, text, color,  background=0,
                     rotate=0):
    '''
    def text (self, **kwargs) :
        x = 0
        y = 0
        text = "NotSet"
        font = self.font_default
        color = self.color_default
        background = self.background_default
        landscape = False
        spacing = 1
        for id in kwargs :
            if id == "x" :
                x = kwargs['x']
            elif id == "y" :
                y = kwargs['y']
            elif id == "text" :
                text = kwargs['text']
            elif id == "color" :
                color = kwargs['color']
            elif id == "background" :
                background = kwargs ['background']
        if font is not None :
            self.display.draw_text (x ,
                              y ,
                              text ,
                              font ,
                              color ,
                              background = background ,
                              landscape = landscape ,
                              spacing = spacing)
        else :
            self.display.draw_text8x8 (x ,
                                        y ,
                                        text, 
                                        color ,
                                        background = background)
                     #rotate=0):
    '''
    def draw_line(self, x1, y1, x2, y2, color):
    '''
    def line (self, **kwargs) :
        x1 = 0
        y1 = 0
        x2 = 0
        y2 = 0
        color = self.color_default
        for id in kwargs :
            if id == "x1" :
                x1 = kwargs ["x1"]
            elif id == "y1" :
                y1 = kwargs ["y1"]
            elif id == "x2" :
                x2 = kwargs ["x2"]
            elif id == "y2" :
                y2 = kwargs ["y2"]
            elif id == "color" :
                color = kwargs['color']
        self.display.draw_line (x1, y1, x2, y2, color)
    '''
    def draw_rectangle(self, x, y, w, h, color):
    '''
    def rectangle (self, **kwargs) :
        x = 0
        y = 0
        width = 0
        height = 0
        color = self.color_default
        for id in kwargs :
            if id == "x" :
                x = kwargs['x']
            elif id == "y" :
                y = kwargs['y']
            elif id == "width" :
                width = kwargs['width']
            elif id == "height" :
                height = kwargs['height']
            elif id == "color" :
                color = kwargs['color']
        self.display.draw_rectangle(x, y, width, height, color)
    #------
    def convert_rgb (self, red, green, blue) :    # _16bit from below
        return ((red & 0x1f) << 11) | ((green & 0x3f) << 5) | (blue & 0x1f)
    '''
    def convert_rgb_8bit (self, red, green, blue) :
        return ((red & 0x07) << 5) | ((green & 0x07) << 2) | (blue & 0x03)
    def convert_rgb_16bit (self, red, green, blue) :
        return ((red & 0x1f) << 11) | ((green & 0x3f) << 5) | (blue & 0x1f)
    def convert_rgb_24bit (self, red, green, blue) :
        return (red << 15) | (green << 7) | blue
    '''
    
#-------------------------------------------------------------------------------
# TestDisplay
#-------------------------------------------------------------------------------
class TestDisplay :
    def __init__ (self) :
        pass
    def pixel (self, **kwargs) :
        print (kwargs)

#class RemoteDisplay (TestDisplay) :
class RemoteDisplay (ILI9341Display) :
    def __init__ (self) :
        super ().__init__ ()
    #def pixel (self, **kwargs) :
    #    arguments = {"id" : "value"}
    #    super().d_pixel (**arguments)

################################################################################
# main
################################################################################
#

disp = RemoteDisplay ()

disp.pixel (val=0, test=True)

disp.screen_clear ()
disp.text (x = 20, y = 112, text="Hello, World!")
for x in range (20,40) :
    disp.pixel (x = x, y = 10, color = disp.color_names ["RED"])

disp.line (x1 = 30, y1 = 30, x2 = 90, y2 = 90, color = disp.color_names ["WHITE"])

disp.rectangle (x = 50, y = 150, width = 100, height = 20, color = disp.color_names ["TEAL"])
print (disp.convert_rgb (0,0,255))

