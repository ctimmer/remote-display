
from area_modules.remote_area import RemoteArea


#-------------------------------------------------------------------------------
# Remote7Segment
#-------------------------------------------------------------------------------
class Remote7Segment (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        #print (__class__)
        super().__init__ (remote_display, area_config)
        self.show_border_color = remote_display.get_color_name ("TEAL")
        self.digit_size = "S"
        self.v_segment_length = 4
        self.h_segment_length = 4 
        self.segment_width = 2
        self.spacing = 1
        #self.color = remote_display.color_by_name ("WHITE")
        self.bold = False
        self.text_current = ""
        if "text" in area_config :
            self.text_current = area_config ["text"]
        self.set_parameters (**area_config)
        #self.set_parameters  (digit_size="S" ,
                              #v_segment_length=v_segment_length ,
                              #h_segment_length=h_segment_length ,
                              #segment_width=segment_width ,
                              #spacing=spacing ,
                              #bold=bold ,
                              #color=color)
        #---- char/digit width
        self.char_wid = self.segment_wid \
                        + self.h_segment_len \
                        + self.segment_wid \
                        + self.spacing
        #---- char/digit height
        self.char_height = self.segment_wid \
                        + self.v_segment_len \
                        + self.segment_wid \
                        + self.v_segment_len \
                        + self.segment_wid \
                        + self.spacing
        self.width_mid = round ((self.char_wid - self.spacing) / 2)
        self.height_mid = round ((self.char_height - self.spacing) / 2)
        self.top_seg_bit = 0b00000001
        self.mid_seg_bit = 0b00000010
        self.bot_seg_bit = 0b00000100
        self.ul_seg_bit  = 0b00001000
        self.ur_seg_bit  = 0b00010000
        self.ll_seg_bit  = 0b00100000
        self.lr_seg_bit  = 0b01000000
        self.zero_segs = self.top_seg_bit | self.ul_seg_bit | self.ur_seg_bit|self.ll_seg_bit|self.lr_seg_bit|self.bot_seg_bit
        self.one_segs = self.ur_seg_bit | self.lr_seg_bit
        self.two_segs = self.top_seg_bit | self.ur_seg_bit | self.mid_seg_bit | self.ll_seg_bit | self.bot_seg_bit
        self.three_segs = self.top_seg_bit | self.ur_seg_bit | self.mid_seg_bit | self.lr_seg_bit | self.bot_seg_bit
        self.four_segs = self.ul_seg_bit | self.ur_seg_bit | self.mid_seg_bit | self.lr_seg_bit
        self.five_segs = self.top_seg_bit | self.ul_seg_bit | self.mid_seg_bit | self.lr_seg_bit | self.bot_seg_bit
        self.six_segs = self.top_seg_bit | self.ul_seg_bit | self.mid_seg_bit | self.ll_seg_bit | self.lr_seg_bit | self.bot_seg_bit
        self.seven_segs = self.top_seg_bit | self.ur_seg_bit | self.lr_seg_bit
        self.eight_segs = self.top_seg_bit | self.ul_seg_bit | self.ur_seg_bit|self.mid_seg_bit|self.ll_seg_bit|self.lr_seg_bit|self.bot_seg_bit
        self.nine_segs = self.top_seg_bit | self.ul_seg_bit | self.ur_seg_bit | self.mid_seg_bit | self.lr_seg_bit
        self.a_segs = self.top_seg_bit | self.ul_seg_bit | self.ur_seg_bit|self.ll_seg_bit|self.lr_seg_bit | self.mid_seg_bit
        self.b_segs = self.ul_seg_bit | self.ll_seg_bit|self.lr_seg_bit|self.mid_seg_bit |self.bot_seg_bit
        self.c_segs = self.top_seg_bit | self.ul_seg_bit | self.ll_seg_bit|self.bot_seg_bit
        self.d_segs = self.ur_seg_bit|self.ll_seg_bit|self.lr_seg_bit|self.mid_seg_bit|self.bot_seg_bit
        self.e_segs = self.top_seg_bit | self.ul_seg_bit |self.mid_seg_bit|self.ll_seg_bit|self.bot_seg_bit
        self.f_segs = self.top_seg_bit | self.ul_seg_bit | self.mid_seg_bit|self.ll_seg_bit
        self.question_segs = self.top_seg_bit | self.ur_seg_bit|self.mid_seg_bit|self.ll_seg_bit
        self.segment_chars = {
            "0" : {"handler" : self.build_segments, "args" : [self.zero_segs]} ,
            "1" : {"handler" : self.build_segments, "args" : [self.one_segs]} ,
            "2" : {"handler" : self.build_segments, "args" : [self.two_segs]} ,
            "3" : {"handler" : self.build_segments, "args" : [self.three_segs]} ,
            "4" : {"handler" : self.build_segments, "args" : [self.four_segs]} ,
            "5" : {"handler" : self.build_segments, "args" : [self.five_segs]} ,
            "6" : {"handler" : self.build_segments, "args" : [self.six_segs]} ,
            "7" : {"handler" : self.build_segments, "args" : [self.seven_segs]} ,
            "8" : {"handler" : self.build_segments, "args" : [self.eight_segs]} ,
            "9" : {"handler" : self.build_segments, "args" : [self.nine_segs]} ,
            "." : {"handler" : self.decimal_point_seg, "args" : []} ,
            "+" : {"handler" : self.plus_seg, "args" : []} ,
            "-" : {"handler" : self.minus_seg, "args" : []} ,
            ":" : {"handler" : self.colon_seg, "args" : []} ,
            "?" : {"handler" : self.build_segments, "args" : [self.question_segs]} ,
            " " : {"handler" : self.space_seg, "args" : []} ,
            "a" : {"handler" : self.build_segments, "args" : [self.a_segs]} ,
            "b" : {"handler" : self.build_segments, "args" : [self.b_segs]} ,
            "c" : {"handler" : self.build_segments, "args" : [self.c_segs]} ,
            "d" : {"handler" : self.build_segments, "args" : [self.d_segs]} ,
            "e" : {"handler" : self.build_segments, "args" : [self.e_segs]} ,
            "f" : {"handler" : self.build_segments, "args" : [self.f_segs]}
            }
    
    def set_parameters (self, **kwargs) :
        if "digit_size" in kwargs :
            #print ("digit_size:",kwargs ["digit_size"])
            digit_size = kwargs ["digit_size"].upper() + "  "
            if digit_size[0:1] == "S" :        # Small digits
                self.v_segment_len = 4
                if digit_size[1:2] == "N" :
                    self.h_segment_len = 3
                else :
                    self.h_segment_len = 4
                self.segment_wid = 2
            elif digit_size[0:1] == "M" :      # Medium digits
                self.v_segment_len = 10
                if digit_size[1:2] == "N" :
                    self.h_segment_len = 6
                    self.segment_wid = 3
                else :
                    self.h_segment_len = 10
                    self.segment_wid = 4
                self.spacing = 2
            elif digit_size[0:1] == "L" :      # Large digits
                self.v_segment_len = 20
                if digit_size[1:2] == "N" :
                    self.h_segment_len = 10
                    self.segment_wid = 4
                else :
                    self.h_segment_len = 20
                    self.segment_wid = 6
                self.spacing = 2
        if "bold" in kwargs :              # Bold (T/F)
            self.bold = kwargs ["bold"]

        #---- sign segment length
        self.sign_seg_len = max (self.v_segment_len,
                                self.h_segment_len)
        if self.sign_seg_len < 5 :
            self.sign_seg_len = 5
        elif self.sign_seg_len % 2 != 0 :
            self.sign_seg_len -= 1

    def update (self, **kwargs) :
        if "text" not in kwargs :
            return
        self.text_current = kwargs ["text"]
        self.reload (reload_all = False)
    def reload (self, reload_all = True) :
        if not self.page_is_active() :
            return
        #print ("active")
        #print ("reload text:", self.text_current)
        if reload_all :
            self.reload_background ()
        self.remote_display.rectangle_fill (x = self.xmin ,
                                            w = self.xlen ,
                                            y = self.ymin ,
                                            h = self.ylen,
                                            color=self.backgroundcolor)
        self.display_string (xpos = self.xmin ,
                             ypos = self.ymin ,
                             chars = self.text_current)
        if reload_all :
            self.reload_areas ()

    #----------------------------------------------------------------------------------
    # Segment identifiers:
    # bold=False    bold=True
    #  xxTOPxx      xxxTOPxxx
    # x       x     x       x
    # U       U     U       U
    # L       R     L       R
    # x       x     x       x
    #  xxMIDxx      xxxMIDxxx
    # x       x     x       x
    # L       L     L       L
    # L       R     L       R
    # x       x     x       x
    #  xxBOTxx      xxxBOTxxx
    #
    #------------------------------
    def TOP_seg (self, xpos_in, ypos_in) :
        if self.bold :
            xpos = xpos_in
            xlen = self.segment_wid + self.h_segment_len + self.segment_wid
        else :
            xpos = xpos_in + self.segment_wid
            xlen = self.h_segment_len
        ypos = ypos_in
        self.remote_display.rectangle_fill (hpos = xpos ,
                                            hlen = xlen ,
                                            vpos = ypos ,
                                            vlen = self.segment_wid ,
                                            color = self.textcolor)
    #------------------------------------
    def UL_seg (self, xpos_in, ypos_in) :
        xpos = xpos_in
        if self.bold :
            ypos = ypos_in
            ylen = self.segment_wid + self.v_segment_len + self.segment_wid
        else :
            ypos = ypos_in + self.segment_wid
            ylen = self.v_segment_len
        self.remote_display.rectangle_fill (hpos = xpos ,
                                            hlen = self.segment_wid ,
                                            vpos = ypos ,
                                            vlen = ylen ,
                                            color = self.textcolor)
    #------------------------------------
    def UR_seg (self, xpos_in, ypos_in) :
        xpos = xpos_in + self.segment_wid + self.h_segment_len
        if self.bold :
            ypos = ypos_in
            ylen = self.segment_wid + self.v_segment_len + self.segment_wid
        else :
            ypos = ypos_in + self.segment_wid
            ylen = self.v_segment_len
        self.remote_display.rectangle_fill (hpos = xpos ,
                                            hlen = self.segment_wid ,
                                            vpos = ypos ,
                                            vlen = ylen ,
                                            color = self.textcolor)
    #-------------------------------------
    def MID_seg (self, xpos_in, ypos_in) :
        if self.bold :
            xpos = xpos_in
            xlen = self.segment_wid + self.h_segment_len + self.segment_wid
        else :
            xpos = xpos_in + self.segment_wid
            xlen = self.h_segment_len
        ypos = ypos_in + self.segment_wid + self.v_segment_len
        self.remote_display.rectangle_fill (hpos = xpos ,
                                            hlen = xlen ,
                                            vpos = ypos ,
                                            vlen = self.segment_wid ,
                                            color = self.textcolor)
    def LL_seg (self, xpos_in, ypos_in) :
        xpos = xpos_in
        if self.bold :
            ypos = ypos_in + self.segment_wid + self.v_segment_len
            ylen = self.segment_wid + self.v_segment_len + self.segment_wid
        else :
            ypos = ypos_in + self.segment_wid + self.v_segment_len + self.segment_wid
            ylen = self.v_segment_len
        self.remote_display.rectangle_fill (hpos = xpos ,
                                            hlen = self.segment_wid ,
                                            vpos = ypos ,
                                            vlen = ylen ,
                                            color = self.textcolor)
    def LR_seg (self, xpos_in, ypos_in) :
        xpos = xpos_in + self.segment_wid + self.h_segment_len
        if self.bold :
            ypos = ypos_in + self.segment_wid + self.v_segment_len
            ylen = self.segment_wid + self.v_segment_len + self.segment_wid
        else :
            ypos = ypos_in + self.segment_wid + self.v_segment_len + self.segment_wid
            ylen = self.v_segment_len
        self.remote_display.rectangle_fill (hpos = xpos ,
                                            hlen = self.segment_wid ,
                                            vpos = ypos ,
                                            vlen = ylen ,
                                            color = self.textcolor)
    #-----------------------------------
    def BOT_seg (self, xpos_in, ypos_in) :
        if self.bold :
            xpos = xpos_in
            xlen = self.segment_wid + self.h_segment_len + self.segment_wid
        else :
            xpos = xpos_in + self.segment_wid
            xlen = self.h_segment_len
        ypos = ypos_in \
                + self.segment_wid \
                + self.v_segment_len \
                + self.segment_wid \
                + self.v_segment_len
        self.remote_display.rectangle_fill (hpos = xpos ,
                                            hlen = xlen ,
                                            vpos = ypos ,
                                            vlen = self.segment_wid ,
                                            color = self.textcolor)
    #-----------------------------
    def build_segments (self, seg_bits, xpos, ypos) :
        if (seg_bits & self.top_seg_bit) != 0 :
            self.TOP_seg (xpos, ypos)
        if (seg_bits & self.mid_seg_bit) != 0 :
            self.MID_seg (xpos, ypos)
        if (seg_bits & self.bot_seg_bit) != 0 :
            self.BOT_seg (xpos, ypos)
        if (seg_bits & self.ul_seg_bit) != 0 :
            self.UL_seg (xpos, ypos)
        if (seg_bits & self.ur_seg_bit) != 0 :
            self.UR_seg (xpos, ypos)
        if (seg_bits & self.ll_seg_bit) != 0 :
            self.LL_seg (xpos, ypos)
        if (seg_bits & self.lr_seg_bit) != 0 :
            self.LR_seg (xpos, ypos)
        return self.char_wid

    #---------------------------------------------------------------------------------
    def decimal_point_seg (self, xpos, ypos) :
        vxpos = xpos + (self.width_mid - (self.segment_wid // 2))
        vypos = ypos + self.v_segment_len \
                                    + self.v_segment_len \
                                    + self.segment_wid \
                                    + self.segment_wid
        self.remote_display.rectangle_fill (hpos = vxpos ,
                                            hlen = self.segment_wid ,
                                            vpos = vypos ,
                                            vlen = self.segment_wid ,
                                            color = self.textcolor)
        return self.char_wid
    #---------------------------------------------------------------------------------
    def colon_seg (self, xpos, ypos) :
        vxpos = xpos + (self.width_mid - (self.segment_wid // 2))
        vypos = ypos + self.v_segment_len \
                                    + self.segment_wid
        self.remote_display.rectangle_fill (hpos = vxpos ,
                                            hlen = self.segment_wid ,
                                            vpos = vypos ,
                                            vlen = self.segment_wid ,
                                            color = self.textcolor)
        vypos += + self.v_segment_len
        self.remote_display.rectangle_fill (hpos = vxpos ,
                                            hlen = self.segment_wid ,
                                            vpos = vypos ,
                                            vlen = self.segment_wid ,
                                            color = self.textcolor)
        return self.char_wid
    #---------------------------------------------------------------------------------
    def minus_seg (self, xpos_in, ypos_in) :
        xpos = xpos_in + self.segment_wid
        xlen = self.h_segment_len
        ypos = ypos_in + self.height_mid - (self.segment_wid // 2)
        self.remote_display.rectangle_fill (hpos = xpos ,
                                            hlen = xlen ,
                                            vpos = ypos ,
                                            vlen = self.segment_wid ,
                                            color = self.textcolor)
        return self.char_wid
    #---------------------------------------------------------------------------------
    def plus_seg (self, xpos, ypos) :
        self.minus_seg (xpos, ypos)
        vxpos = xpos + (self.width_mid - (self.segment_wid // 2))
        vypos = (ypos + self.height_mid) - (self.h_segment_len // 2)
        self.remote_display.rectangle_fill (hpos = vxpos ,
                                            hlen = self.segment_wid ,
                                            vpos = vypos ,
                                            vlen = self.h_segment_len ,
                                            color = self.textcolor)
        return self.char_wid

    #---------------------------------------------------------------------------------
    def space_seg (self, xpos, ypos) :
        return self.char_wid

    #---------------------------------------------------------------------------------
    def get_character_width (self) :
        return self.char_wid
    def get_character_height (self) :
        return self.char_height
    #-----------------------------
    def display_character (self, xpos, ypos, char) :
        #print ("'" + char + "'")
        disp_char = char.lower ()
        if disp_char in self.segment_chars :
            self.segment_chars[disp_char]["handler"] (*self.segment_chars[disp_char]["args"] ,
                                                      xpos, ypos)
        else :
            self.build_segments (self.question_segs, xpos, ypos)
        return self.char_wid
    def display_string (self, xpos, ypos, chars) :
        x_display = xpos
        for char in chars :
            x_display += self.display_character (x_display, ypos, char)
        return x_display

## end Remote7Segment ##