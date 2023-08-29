#
#from display_config import *

class DummyDisplay () :
    def __init__ (self, **kwargs) :
        self.fonts = {}
        self.images = {}
        '''
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
    '''
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