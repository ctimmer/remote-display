#
################################################################################
# The MIT License (MIT)
#
# Copyright (c) 2024 Curt Timmerman
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
        return f"rbg({r:d},{g:d},{b:d})"
    #def get_color_name (self, color_name):
        #return color_name
    def get_font_default (self):
        return None
    def get_color_default (self):
        return None
    def get_background_default (self):
        return None

## end DummyDisplay ##
