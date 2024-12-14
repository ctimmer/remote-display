#

import webcolors
#from tkinter import font

class TKINTERDisplay :
    def __init__ (self , **kwargs) :
        self.convert_rgb = self.convert_rgb_16bit
        self.display_scale = 1
        self.display_width = 128
        self.display_height = 32
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
                                    "color" : "fill" ,
                                    "hlines" : "hlines"
                                    }
        self.pixel_params = {
                            "color" : "fill"
                            }
        self.pixel_params.update (xy_params)
        self.text_params = {
                            "text" : "text" ,
                            "font" : "font" ,
                            "color" : "fill"
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
                            "color" : "fill"
                            }
        self.rectangle_params = {
                                "color" : "fill"
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
                                "color" : "fill"
                                }
        self.polygon_params = {
                                "sides" : "sides" ,
                                "x0" : "x0" ,
                                "xcenter" : "x0" ,
                                "y0" : "y0" ,
                                "ycenter" : "y0" ,
                                "r" : "r" ,
                                "radius" : "r" ,
                                "color" : "fill" ,
                                "rotate" : "rotate"
                                }
        self.image_params = {
                            "image_object" : "image_object"
                            }
        self.image_params.update (xy_params)
        self.image_params.update (length_params)
        self.image_counter = 0
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
                            "display_scale" : "display_scale"
                            }
        ignore_params = {
                        "trace_methods" : "Used by RemoteTrace"
                        }
        display_object_args = {}
        display_args = {}
        #
        # if display is already set up, store it and exit
        for id in kwargs :
            if id in display_object_params :
                arg_id = display_object_params [id]
                display_object_args [arg_id] = kwargs [id]
            elif id in display_params :
                arg_id = display_params [id]
                display_args [arg_id] = kwargs [id]
            elif id in ignore_params :
                pass
            else :
                print ("__init__: Unknown parameter", id)
        #
        if "width" in display_args :
            self.display_width = display_args["width"]
        if "height" in display_args :
            self.display_height = display_args["height"]
        if "display_scale" in display_args :
            self.display_scale = display_args ["display_scale"]
            if self.display_scale < 1 :
                self.display_scale = 1
            elif self.display_scale > 10 :
                self.display_scale = 10
        if "display_object" in display_object_args :
            display = display_object_args ["display_object"]
        #---- Handle other interfaces here
        else :
            pass # error

        return display

    def font_initialize (self, file_name, width, height) :
        return XglcdFont(file_name, width, height)
    '''
    def clear(self, color=0, hlines=8):
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "h" : 0 ,
                    "w" : 0 ,
                    "outline" : "black"
                    }
    '''
    def screen_clear (self, **kwargs) :
        named_args = {
                    "width" : 0 ,
                    "fill" : "BLACK"
                    }
        pos_args = [
            0 ,
            0 ,
            self.display_width ,
            self.display_height
            ]
        for id in kwargs :
            if id in self.screen_clear_params :
                named_args [self.screen_clear_params [id]] = kwargs [id]
        named_args ["fill"] = self.get_canvas_color (named_args["fill"])
        #print (pos_args, named_args)
        self.display.delete ("all")
        self.display.create_rectangle (*pos_args, **named_args)
        '''
        self.display.create_rectangle ((0, 0),
                                      (self.display_width * self.display_scale,
                                           self.display_height * self.display_scale),
                                       fill = self.get_canvas_color (named_args["color"]) ,
                                       width = 0)
                                      #fill = named_args["color"])
        '''
    def screen_off (self) :
        """Turn display off."""
        #self.display.write_cmd (self.display.DISPLAY_OFF)
        pass

    def screen_on (self) :
        """Turn display on."""
        #self.display.write_cmd (self.display.DISPLAY_ON)
        pass
    '''
    def draw_pixel(self, x, y, color):
    '''
    def pixel (self, **kwargs) :
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "color" : "black"
                    }
        for id in kwargs :
            if id in self.text_params :
                named_args [self.text_params [id]] = kwargs [id]
        pos_args = [(named_args["x"], named_args["y"]),
                    (named_args["x"], named_args["y"])]
        option_args = {
            }
        for id in named_args :
            if id in ["fill"] :
                option_args [id] = named_args [id]
        if "fill" in option_args :
            option_args ["fill"] = self.get_canvas_color (option_args["fill"])
        #self.display.draw_pixel (**named_args)
        self.display.create_line (*pos_args, **option_args)

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
                    "text" : "" ,
                    "color" : "black"
                    }
        #if self.font_default is not None :
            #named_args ["font"] = self.font_default
        for id in kwargs :
            if id in self.text_params :
                named_args [self.text_params [id]] = kwargs [id]
        #print ("text named_args:", named_args)
        pos_args = [(named_args["x"], named_args["y"])]
        option_args =  {
            "text" : "" ,
            "anchor" : "nw" ,
            "fill" : "black"
            }
        for id in named_args :
            if id in ["text", "fill", "font"] :
                option_args [id] = named_args [id]
        if "fill" in option_args :
            option_args ["fill"] = self.get_canvas_color (option_args["fill"])
        self.display.create_text (*pos_args, **option_args)

    '''
    canvas.create_line((50, 50), (100, 100), width=4, fill='red')
    '''
    def line (self, **kwargs) :
        #print ("text kwargs:", kwargs)
        named_args = {
                    "x1" : 0 ,
                    "y1" : 0 ,
                    "x2" : 0 ,
                    "y2" : 0 ,
                    "color" : "black"
                    }
        for id in kwargs :
            if id in self.line_params :
                named_args [self.line_params [id]] = kwargs [id]
        if "fill" in option_args :
            option_args ["fill"] = self.get_canvas_color (option_args["fill"])
        #print ("text named_args:", named_args)
        self.display.create_line ((named_args["x1"], named_args["y1"]),
                                  (named_args["x2"], named_args["y2"]),
                                  fill = self.get_canvas_color (named_args["fill"]))
    '''
    def draw_rectangle(self, x, y, w, h, color):
    '''
    def rectangle (self, **kwargs) :
        #print ("rectangle kwargs:", kwargs)
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "h" : 0 ,
                    "w" : 0 ,
                    "outline" : "black"
                    }
        for id in kwargs :
            if id in self.rectangle_params :
                named_args [self.rectangle_params [id]] = kwargs [id]
        #print ("rectangle named_args:", named_args)
        x2 = named_args ["x"] + (named_args ["w"])
        y2 = named_args ["y"] + (named_args ["h"])
        #pos_args = [named_args["x"], named_args["y"], x2, y2]
        pos_args = [named_args["x"] + 1, named_args["y"] + 1, x2, y2]
        option_args = {
            "width" : 1
            }
        for id in named_args :
            if id in ["fill"] :
                option_args ["outline"] = named_args [id]
        if "outline" in option_args :
            option_args ["outline"] = self.get_canvas_color (option_args["outline"])
        self.display.create_rectangle (*pos_args, **option_args)
        #print ("create_rectangle:", pos_args, option_args)

    '''
    def fill_rectangle(self, x, y, w, h, color):
    '''
    def rectangle_fill (self, **kwargs) :
        #print ("rec_fill:", kwargs)
        named_args = {
                    "x" : 0 ,
                    "y" : 0 ,
                    "w" : 0 ,
                    "h" : 0 ,
                    "color" : "black"
                    }
        for id in kwargs :
            if id in self.rectangle_params :       # same as rectangle
                named_args [self.rectangle_params [id]] = kwargs [id]
        #print ("rec_fill:", named_args)
        #self.display.fill_rectangle(**named_args)
        x2 = named_args ["x"] + (named_args ["w"])
        y2 = named_args ["y"] + (named_args ["h"])
        #pos_args = [named_args["x"], named_args["y"], x2, y2]
        pos_args = [named_args["x"] + 1, named_args["y"] + 1, x2 + 1, y2 + 1]
        option_args = {
            "width" : 0
            }
        for id in named_args :
            if id in ["fill"] :
                option_args [id] = named_args [id]
        if "fill" in option_args :
            option_args ["fill"] = self.get_canvas_color (option_args["fill"])
        self.display.create_rectangle (*pos_args, **option_args)
        #print ("create_rectangle:", pos_args, option_args)

    '''
    def draw_image(self, path, x=0, y=0, w=320, h=240):
    '''
    def image_attribute (self) :
        if self.image_counter > 1000 :
            self.image_counter = 1
        else :
            self.image_counter += 1
        return "RemImage_" + str (self.image_counter)
    #--------------------------
    def image (self, **kwargs) :
        #print ("## image kwargs:", kwargs)
        from PIL import ImageTk, Image
        named_args = {
            "x" : 0 ,
            "y" : 0
            }
        for id in kwargs :
            if id in self.image_params :
                named_args [self.image_params [id]] = kwargs [id]
        image_attr = self.image_attribute ()
        python_image = kwargs ["image_object"]
        setattr (self.display, image_attr, ImageTk.PhotoImage(python_image))
        option_args = {
            "image" : getattr (self.display, image_attr) ,
            "anchor" : "nw"
            }
        pos_args = (
            named_args["x"],
            named_args ["y"]
            )
        #print ("## TK display: image", pos_args, option_args)
        self.display.create_image (*pos_args,
                                    **option_args)

    #---------------------------------------------------------------------------
    ''' defined in __INIT__
    def convert_rgb (self, red, green, blue) :    # _16bit from below
    '''
    def convert_rgb_8bit (self, red, green, blue) :
        return ((red & 0b11100000) << 5) \
                | ((green & 0b11100000) << 2) \
                | ((blue & 0b11000000) >> 6)
    def convert_rgb_16bit (self, red, green, blue) :
        return ((red & 0b11111000) << 8) \
                | ((green & 0b11111100) << 3) \
                | (blue >> 3)
    def convert_rgb_24bit (self, red, green, blue) :
        return (red << 15) | (green << 7) | blue

    def get_color_name (self, color_name):
        return self.color_names[color_name]
        
    def reverse_bits (self, bit_field, bits=8) :
        reversed_bits = 0x000000
        msd = bits - 1
        for bit_idx in range (0, bits) :
            reversed_bits |= ((bit_field >> bit_idx) & 0x01) << (msd - bit_idx)
        return reversed_bits

    def dummy_test (self, mess = "dummy_test") :
        print (mess)

    # rgb16 5,6,5
    #    0brrrrrggggggbbbbb
    #    0brrrrr000gggggg00bbbbb000
    #
    def breakout_rgb16_REMOVE (self, rgb16) :
        return (rgb16 & 0b1111100000000000) >> 8 , \
               (rgb16 & 0b0000011111100000) >> 3 , \
               (rgb16 & 0b0000000000011111) << 3
    def rgb16_to_rgb24 (self, rgb16) :
        r = (rgb16 & 0b1111100000000000) >> 11
        g = (rgb16 & 0b0000011111100000) >> 5
        b = (rgb16 & 0b0000000000011111)
        #print (f"===================> RGb16 input: r={r}, g={g}, b={b}")
        r = int ((r / 0b11111) * 255.0)
        g = int ((g / 0b111111) * 255.0)
        b = int ((b / 0b11111) * 255.0)
        #print (f"RGB24 output: r={r}, g={g}, b={b}")
        return (r, g, b)

    def get_closest_color (self, rgb_in):
        #print ("####### get_closest_color:", rgb_in)
        closest_color = "black"
        rgb_color = (0,0,0)
        if type (rgb_in) is tuple \
        or type (rgb_in) is list :
            rgb_color = rgb_in
        elif type (rgb_in) is int :
            rgb_color = self.rgb16_to_rgb24 (rgb_in)
            #rgb_color = self.breakout_rgb16 (rgb_in)
        else :
            print ("get_closest_color: Invalid rgb_in", rgb_in)
        try:
            closest_color = webcolors.rgb_to_name(rgb_color)
        except ValueError:
            closest_value = 0xffffff
            # pre python 3.10:
            #for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
            for name in webcolors.names("css3") :
                r_c, g_c, b_c = webcolors.name_to_rgb (name)
                # pre python 3.10:
                #r_c, g_c, b_c = webcolors.hex_to_rgb(key)
                val = ((r_c - rgb_color[0]) ** 2) \
                        + ((g_c - rgb_color[1]) ** 2) \
                        + ((b_c - rgb_color[2]) ** 2)
                if val < closest_value :
                    closest_value = val
                    closest_color = name
        return closest_color

    def get_canvas_color (self, rgb16_color) :
        """translates an rgb tuple of int to a tkinter friendly color code
        """
        #print ("get_canvas_color:", rgb16_color)
        canvas_color = "blue"
        if type (rgb16_color) is str :
            #print ("get_canvas_color: str") 
            canvas_color = rgb16_color.lower ()
        elif type (rgb16_color) is int :
            #print ("get_canvas_color: int")
            canvas_color = self.get_closest_color \
                                (self.rgb16_to_rgb24 (rgb16_color))
                                #(self.breakout_rgb16 (rgb16_color))
        #print ("get_canvas_color:", canvas_color)
        return canvas_color

## end TKINTERDisplay ##
