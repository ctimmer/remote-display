#

import time
from array import array

if not hasattr (time, "ticks_ms") :
    from types import MethodType
    import time as time
    def ticks_ms(self):
        return int (round (time.time () * 1000))
    def ticks_add(self, ms_1, ms_2):
        return ms_1 + ms_2
    def ticks_diff(self, ms_1, ms_2):
        return ms_1 - ms_2
    def sleep_ms (self, ms_1) :
        return time.sleep (ms_1 / 1000)
    time.ticks_ms = MethodType (ticks_ms, time)
    time.ticks_add = MethodType (ticks_add, time)
    time.ticks_diff = MethodType (ticks_diff, time)
    time.sleep_ms = MethodType (sleep_ms, time)

try :
    import ntptime
except :
    class ntptime () :
        def __init__ (self) :
            pass

import display_config

SYSFONT = {"Width": 5,
           "Height": 8,
           "Start": 0,
           "End": 254,
           "Data": bytearray([
  0x00, 0x00, 0x00, 0x00, 0x00,
  0x3E, 0x5B, 0x4F, 0x5B, 0x3E,
  0x3E, 0x6B, 0x4F, 0x6B, 0x3E,
  0x1C, 0x3E, 0x7C, 0x3E, 0x1C,
  0x18, 0x3C, 0x7E, 0x3C, 0x18,
  0x1C, 0x57, 0x7D, 0x57, 0x1C,
  0x1C, 0x5E, 0x7F, 0x5E, 0x1C,
  0x00, 0x18, 0x3C, 0x18, 0x00,
  0xFF, 0xE7, 0xC3, 0xE7, 0xFF,
  0x00, 0x18, 0x24, 0x18, 0x00,
  0xFF, 0xE7, 0xDB, 0xE7, 0xFF,
  0x30, 0x48, 0x3A, 0x06, 0x0E,
  0x26, 0x29, 0x79, 0x29, 0x26,
  0x40, 0x7F, 0x05, 0x05, 0x07,
  0x40, 0x7F, 0x05, 0x25, 0x3F,
  0x5A, 0x3C, 0xE7, 0x3C, 0x5A,
  0x7F, 0x3E, 0x1C, 0x1C, 0x08,
  0x08, 0x1C, 0x1C, 0x3E, 0x7F,
  0x14, 0x22, 0x7F, 0x22, 0x14,
  0x5F, 0x5F, 0x00, 0x5F, 0x5F,
  0x06, 0x09, 0x7F, 0x01, 0x7F,
  0x00, 0x66, 0x89, 0x95, 0x6A,
  0x60, 0x60, 0x60, 0x60, 0x60,
  0x94, 0xA2, 0xFF, 0xA2, 0x94,
  0x08, 0x04, 0x7E, 0x04, 0x08,
  0x10, 0x20, 0x7E, 0x20, 0x10,
  0x08, 0x08, 0x2A, 0x1C, 0x08,
  0x08, 0x1C, 0x2A, 0x08, 0x08,
  0x1E, 0x10, 0x10, 0x10, 0x10,
  0x0C, 0x1E, 0x0C, 0x1E, 0x0C,
  0x30, 0x38, 0x3E, 0x38, 0x30,
  0x06, 0x0E, 0x3E, 0x0E, 0x06,
  0x00, 0x00, 0x00, 0x00, 0x00,
  0x00, 0x00, 0x5F, 0x00, 0x00,
  0x00, 0x07, 0x00, 0x07, 0x00,
  0x14, 0x7F, 0x14, 0x7F, 0x14,
  0x24, 0x2A, 0x7F, 0x2A, 0x12,
  0x23, 0x13, 0x08, 0x64, 0x62,
  0x36, 0x49, 0x56, 0x20, 0x50,
  0x00, 0x08, 0x07, 0x03, 0x00,
  0x00, 0x1C, 0x22, 0x41, 0x00,
  0x00, 0x41, 0x22, 0x1C, 0x00,
  0x2A, 0x1C, 0x7F, 0x1C, 0x2A,
  0x08, 0x08, 0x3E, 0x08, 0x08,
  0x00, 0x80, 0x70, 0x30, 0x00,
  0x08, 0x08, 0x08, 0x08, 0x08,
  0x00, 0x00, 0x60, 0x60, 0x00,
  0x20, 0x10, 0x08, 0x04, 0x02,
  0x3E, 0x51, 0x49, 0x45, 0x3E,
  0x00, 0x42, 0x7F, 0x40, 0x00,
  0x72, 0x49, 0x49, 0x49, 0x46,
  0x21, 0x41, 0x49, 0x4D, 0x33,
  0x18, 0x14, 0x12, 0x7F, 0x10,
  0x27, 0x45, 0x45, 0x45, 0x39,
  0x3C, 0x4A, 0x49, 0x49, 0x31,
  0x41, 0x21, 0x11, 0x09, 0x07,
  0x36, 0x49, 0x49, 0x49, 0x36,
  0x46, 0x49, 0x49, 0x29, 0x1E,
  0x00, 0x00, 0x14, 0x00, 0x00,
  0x00, 0x40, 0x34, 0x00, 0x00,
  0x00, 0x08, 0x14, 0x22, 0x41,
  0x14, 0x14, 0x14, 0x14, 0x14,
  0x00, 0x41, 0x22, 0x14, 0x08,
  0x02, 0x01, 0x59, 0x09, 0x06,
  0x3E, 0x41, 0x5D, 0x59, 0x4E,
  0x7C, 0x12, 0x11, 0x12, 0x7C,
  0x7F, 0x49, 0x49, 0x49, 0x36,
  0x3E, 0x41, 0x41, 0x41, 0x22,
  0x7F, 0x41, 0x41, 0x41, 0x3E,
  0x7F, 0x49, 0x49, 0x49, 0x41,
  0x7F, 0x09, 0x09, 0x09, 0x01,
  0x3E, 0x41, 0x41, 0x51, 0x73,
  0x7F, 0x08, 0x08, 0x08, 0x7F,
  0x00, 0x41, 0x7F, 0x41, 0x00,
  0x20, 0x40, 0x41, 0x3F, 0x01,
  0x7F, 0x08, 0x14, 0x22, 0x41,
  0x7F, 0x40, 0x40, 0x40, 0x40,
  0x7F, 0x02, 0x1C, 0x02, 0x7F,
  0x7F, 0x04, 0x08, 0x10, 0x7F,
  0x3E, 0x41, 0x41, 0x41, 0x3E,
  0x7F, 0x09, 0x09, 0x09, 0x06,
  0x3E, 0x41, 0x51, 0x21, 0x5E,
  0x7F, 0x09, 0x19, 0x29, 0x46,
  0x26, 0x49, 0x49, 0x49, 0x32,
  0x03, 0x01, 0x7F, 0x01, 0x03,
  0x3F, 0x40, 0x40, 0x40, 0x3F,
  0x1F, 0x20, 0x40, 0x20, 0x1F,
  0x3F, 0x40, 0x38, 0x40, 0x3F,
  0x63, 0x14, 0x08, 0x14, 0x63,
  0x03, 0x04, 0x78, 0x04, 0x03,
  0x61, 0x59, 0x49, 0x4D, 0x43,
  0x00, 0x7F, 0x41, 0x41, 0x41,
  0x02, 0x04, 0x08, 0x10, 0x20,
  0x00, 0x41, 0x41, 0x41, 0x7F,
  0x04, 0x02, 0x01, 0x02, 0x04,
  0x40, 0x40, 0x40, 0x40, 0x40,
  0x00, 0x03, 0x07, 0x08, 0x00,
  0x20, 0x54, 0x54, 0x78, 0x40,
  0x7F, 0x28, 0x44, 0x44, 0x38,
  0x38, 0x44, 0x44, 0x44, 0x28,
  0x38, 0x44, 0x44, 0x28, 0x7F,
  0x38, 0x54, 0x54, 0x54, 0x18,
  0x00, 0x08, 0x7E, 0x09, 0x02,
  0x18, 0xA4, 0xA4, 0x9C, 0x78,
  0x7F, 0x08, 0x04, 0x04, 0x78,
  0x00, 0x44, 0x7D, 0x40, 0x00,
  0x20, 0x40, 0x40, 0x3D, 0x00,
  0x7F, 0x10, 0x28, 0x44, 0x00,
  0x00, 0x41, 0x7F, 0x40, 0x00,
  0x7C, 0x04, 0x78, 0x04, 0x78,
  0x7C, 0x08, 0x04, 0x04, 0x78,
  0x38, 0x44, 0x44, 0x44, 0x38,
  0xFC, 0x18, 0x24, 0x24, 0x18,
  0x18, 0x24, 0x24, 0x18, 0xFC,
  0x7C, 0x08, 0x04, 0x04, 0x08,
  0x48, 0x54, 0x54, 0x54, 0x24,
  0x04, 0x04, 0x3F, 0x44, 0x24,
  0x3C, 0x40, 0x40, 0x20, 0x7C,
  0x1C, 0x20, 0x40, 0x20, 0x1C,
  0x3C, 0x40, 0x30, 0x40, 0x3C,
  0x44, 0x28, 0x10, 0x28, 0x44,
  0x4C, 0x90, 0x90, 0x90, 0x7C,
  0x44, 0x64, 0x54, 0x4C, 0x44,
  0x00, 0x08, 0x36, 0x41, 0x00,
  0x00, 0x00, 0x77, 0x00, 0x00,
  0x00, 0x41, 0x36, 0x08, 0x00,
  0x02, 0x01, 0x02, 0x04, 0x02,
  0x3C, 0x26, 0x23, 0x26, 0x3C,
  0x1E, 0xA1, 0xA1, 0x61, 0x12,
  0x3A, 0x40, 0x40, 0x20, 0x7A,
  0x38, 0x54, 0x54, 0x55, 0x59,
  0x21, 0x55, 0x55, 0x79, 0x41,
  0x21, 0x54, 0x54, 0x78, 0x41,
  0x21, 0x55, 0x54, 0x78, 0x40,
  0x20, 0x54, 0x55, 0x79, 0x40,
  0x0C, 0x1E, 0x52, 0x72, 0x12,
  0x39, 0x55, 0x55, 0x55, 0x59,
  0x39, 0x54, 0x54, 0x54, 0x59,
  0x39, 0x55, 0x54, 0x54, 0x58,
  0x00, 0x00, 0x45, 0x7C, 0x41,
  0x00, 0x02, 0x45, 0x7D, 0x42,
  0x00, 0x01, 0x45, 0x7C, 0x40,
  0xF0, 0x29, 0x24, 0x29, 0xF0,
  0xF0, 0x28, 0x25, 0x28, 0xF0,
  0x7C, 0x54, 0x55, 0x45, 0x00,
  0x20, 0x54, 0x54, 0x7C, 0x54,
  0x7C, 0x0A, 0x09, 0x7F, 0x49,
  0x32, 0x49, 0x49, 0x49, 0x32,
  0x32, 0x48, 0x48, 0x48, 0x32,
  0x32, 0x4A, 0x48, 0x48, 0x30,
  0x3A, 0x41, 0x41, 0x21, 0x7A,
  0x3A, 0x42, 0x40, 0x20, 0x78,
  0x00, 0x9D, 0xA0, 0xA0, 0x7D,
  0x39, 0x44, 0x44, 0x44, 0x39,
  0x3D, 0x40, 0x40, 0x40, 0x3D,
  0x3C, 0x24, 0xFF, 0x24, 0x24,
  0x48, 0x7E, 0x49, 0x43, 0x66,
  0x2B, 0x2F, 0xFC, 0x2F, 0x2B,
  0xFF, 0x09, 0x29, 0xF6, 0x20,
  0xC0, 0x88, 0x7E, 0x09, 0x03,
  0x20, 0x54, 0x54, 0x79, 0x41,
  0x00, 0x00, 0x44, 0x7D, 0x41,
  0x30, 0x48, 0x48, 0x4A, 0x32,
  0x38, 0x40, 0x40, 0x22, 0x7A,
  0x00, 0x7A, 0x0A, 0x0A, 0x72,
  0x7D, 0x0D, 0x19, 0x31, 0x7D,
  0x26, 0x29, 0x29, 0x2F, 0x28,
  0x26, 0x29, 0x29, 0x29, 0x26,
  0x30, 0x48, 0x4D, 0x40, 0x20,
  0x38, 0x08, 0x08, 0x08, 0x08,
  0x08, 0x08, 0x08, 0x08, 0x38,
  0x2F, 0x10, 0xC8, 0xAC, 0xBA,
  0x2F, 0x10, 0x28, 0x34, 0xFA,
  0x00, 0x00, 0x7B, 0x00, 0x00,
  0x08, 0x14, 0x2A, 0x14, 0x22,
  0x22, 0x14, 0x2A, 0x14, 0x08,
  0xAA, 0x00, 0x55, 0x00, 0xAA,
  0xAA, 0x55, 0xAA, 0x55, 0xAA,
  0x00, 0x00, 0x00, 0xFF, 0x00,
  0x10, 0x10, 0x10, 0xFF, 0x00,
  0x14, 0x14, 0x14, 0xFF, 0x00,
  0x10, 0x10, 0xFF, 0x00, 0xFF,
  0x10, 0x10, 0xF0, 0x10, 0xF0,
  0x14, 0x14, 0x14, 0xFC, 0x00,
  0x14, 0x14, 0xF7, 0x00, 0xFF,
  0x00, 0x00, 0xFF, 0x00, 0xFF,
  0x14, 0x14, 0xF4, 0x04, 0xFC,
  0x14, 0x14, 0x17, 0x10, 0x1F,
  0x10, 0x10, 0x1F, 0x10, 0x1F,
  0x14, 0x14, 0x14, 0x1F, 0x00,
  0x10, 0x10, 0x10, 0xF0, 0x00,
  0x00, 0x00, 0x00, 0x1F, 0x10,
  0x10, 0x10, 0x10, 0x1F, 0x10,
  0x10, 0x10, 0x10, 0xF0, 0x10,
  0x00, 0x00, 0x00, 0xFF, 0x10,
  0x10, 0x10, 0x10, 0x10, 0x10,
  0x10, 0x10, 0x10, 0xFF, 0x10,
  0x00, 0x00, 0x00, 0xFF, 0x14,
  0x00, 0x00, 0xFF, 0x00, 0xFF,
  0x00, 0x00, 0x1F, 0x10, 0x17,
  0x00, 0x00, 0xFC, 0x04, 0xF4,
  0x14, 0x14, 0x17, 0x10, 0x17,
  0x14, 0x14, 0xF4, 0x04, 0xF4,
  0x00, 0x00, 0xFF, 0x00, 0xF7,
  0x14, 0x14, 0x14, 0x14, 0x14,
  0x14, 0x14, 0xF7, 0x00, 0xF7,
  0x14, 0x14, 0x14, 0x17, 0x14,
  0x10, 0x10, 0x1F, 0x10, 0x1F,
  0x14, 0x14, 0x14, 0xF4, 0x14,
  0x10, 0x10, 0xF0, 0x10, 0xF0,
  0x00, 0x00, 0x1F, 0x10, 0x1F,
  0x00, 0x00, 0x00, 0x1F, 0x14,
  0x00, 0x00, 0x00, 0xFC, 0x14,
  0x00, 0x00, 0xF0, 0x10, 0xF0,
  0x10, 0x10, 0xFF, 0x10, 0xFF,
  0x14, 0x14, 0x14, 0xFF, 0x14,
  0x10, 0x10, 0x10, 0x1F, 0x00,
  0x00, 0x00, 0x00, 0xF0, 0x10,
  0xFF, 0xFF, 0xFF, 0xFF, 0xFF,
  0xF0, 0xF0, 0xF0, 0xF0, 0xF0,
  0xFF, 0xFF, 0xFF, 0x00, 0x00,
  0x00, 0x00, 0x00, 0xFF, 0xFF,
  0x0F, 0x0F, 0x0F, 0x0F, 0x0F,
  0x38, 0x44, 0x44, 0x38, 0x44,
  0x7C, 0x2A, 0x2A, 0x3E, 0x14,
  0x7E, 0x02, 0x02, 0x06, 0x06,
  0x02, 0x7E, 0x02, 0x7E, 0x02,
  0x63, 0x55, 0x49, 0x41, 0x63,
  0x38, 0x44, 0x44, 0x3C, 0x04,
  0x40, 0x7E, 0x20, 0x1E, 0x20,
  0x06, 0x02, 0x7E, 0x02, 0x02,
  0x99, 0xA5, 0xE7, 0xA5, 0x99,
  0x1C, 0x2A, 0x49, 0x2A, 0x1C,
  0x4C, 0x72, 0x01, 0x72, 0x4C,
  0x30, 0x4A, 0x4D, 0x4D, 0x30,
  0x30, 0x48, 0x78, 0x48, 0x30,
  0xBC, 0x62, 0x5A, 0x46, 0x3D,
  0x3E, 0x49, 0x49, 0x49, 0x00,
  0x7E, 0x01, 0x01, 0x01, 0x7E,
  0x2A, 0x2A, 0x2A, 0x2A, 0x2A,
  0x44, 0x44, 0x5F, 0x44, 0x44,
  0x40, 0x51, 0x4A, 0x44, 0x40,
  0x40, 0x44, 0x4A, 0x51, 0x40,
  0x00, 0x00, 0xFF, 0x01, 0x03,
  0xE0, 0x80, 0xFF, 0x00, 0x00,
  0x08, 0x08, 0x6B, 0x6B, 0x08,
  0x36, 0x12, 0x36, 0x24, 0x36,
  0x06, 0x0F, 0x09, 0x0F, 0x06,
  0x00, 0x00, 0x18, 0x18, 0x00,
  0x00, 0x00, 0x10, 0x10, 0x00,
  0x30, 0x40, 0xFF, 0x01, 0x01,
  0x00, 0x1F, 0x01, 0x01, 0x1E,
  0x00, 0x19, 0x1D, 0x17, 0x12,
  0x00, 0x3C, 0x3C, 0x3C, 0x3C
])}

TIME_OFFSET = -8     # Alaska

if "time_offset" in display_config.PARAMETERS :
    TIME_OFFSET = display_config.PARAMETERS

#-------------------------------------------------------------------------------
# RemoteArea
#-------------------------------------------------------------------------------
class RemoteArea :
    utc_offset = TIME_OFFSET
    local_second_offset = 0
    ntptime_interval_minutes = 60
    next_ntptime_ms = 0

    def __init__ (self ,
                  remote_display ,
                  area) :
        super().__init__ ()
        self.remote_display = remote_display
        RemoteArea.local_second_offset = RemoteArea.utc_offset * 3600
        RemoteArea.next_ntptime_ms = time.ticks_add (time.ticks_ms (),
                                               (RemoteArea.ntptime_interval_minutes * 3600))
        #self.page = area.page ()  # REMOVE
        self.page_id = area["page_id"]
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
        self.font = None # remote_display.get_font_default()
        self.textcolor = remote_display.get_font_color_default()
        self.scale = 2               # for sysfont 
        self.text_length_max = 10    # for sysfont
        self.horizontal = True       # for sysfont
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
        #
        if "borderwidth" in area :
            self.borderwidth = area ["borderwidth"]
        if "bordercolorrgb" in area :
            self.bordercolor = remote_display.convert_rgb (*area["bordercolorrgb"])
        elif "bordercolorname" in area :
            self.bordercolor = remote_display.get_color_by_name (area ["bordercolorname"])
        #
        if "paddingwidth" in area :
            self.paddingwidth = area ["paddingwidth"]
        if "backgroundcolorrgb" in area :
            self.backgroundcolor = remote_display.convert_rgb (*area["backgroundcolorrgb"])
        elif "backgroundcolorname" in area :
            self.backgroundcolor = remote_display.get_color_by_name (area["backgroundcolorname"])

        if "font" in area :
            self.font = remote_display.get_font (area ["font"])
        if "textcolorrgb" in area :
            self.textcolor = remote_display.convert_rgb (*area["textcolorrgb"])
        elif "textcolorname" in area :
            self.textcolor = remote_display.get_color_by_name (area["textcolorname"])
        if "horizontal" in area :
            self.horizontal = area  ["horizontal"]
        elif "vertical" in area :
            self.horizontal = not area ["vertical"]
        if "scale" in area :
            self.scale = area ["scale"]

        #---- Set field data position/lengths parameters
        offsets = self.borderwidth + self.paddingwidth
        self.xlen = self.hlen - (offsets * 2)
        self.ylen = self.vlen - (offsets * 2)
        self.xmin = self.hpos + offsets
        self.ymin = self.vpos + offsets
        self.xmax = (self.xmin + self.xlen) - 1
        self.ymax = (self.ymin + self.ylen) - 1
        self.xmid = self. xmin + round (self.xlen / 2)
        self.ymid = self. ymin + round (self.ylen / 2)
    #----
    #---- Called after the displays are initialized
    #---- may not be implemented
    #----
    def post_init (self) :
        pass

    def add_area (self, area) :
        if area is not None :
            self.areas.append (area)
    def page_is_active (self, page_id) :
        #return self.page.page_is_active ()
        return self.remote_display.page_id_is_active (page_id)
    def set_page_active (self, page_id) :
        #self.page.set_page_active (state)
        self.remote_display.change_active_page_id (page_id)

    def reload_border (self) :
        if self.xmin == self.hpos :
            return          # No border or padding
        x = self.hpos
        xlen = self.hlen
        y = self.vpos
        ylen = self.vlen
        #---- Border
        for i in range (self.borderwidth) :
            if self.bordercolor is not None :
                self.remote_display.rectangle (x = x ,
                                                y = y ,
                                                w = xlen ,
                                                h = ylen ,
                                                color = self.bordercolor)
            x += 1
            y += 1
            xlen -= 2
            ylen -= 2
        #---- Padding
        #print ("Padding: start")
        for i in range (self.paddingwidth) :
            if self.backgroundcolor is not None :
                self.remote_display.rectangle (x = x ,
                                                y = y ,
                                                w = xlen ,
                                                h = ylen ,
                                                color = self.backgroundcolor)
            x += 1
            y += 1
            xlen -= 2
            ylen -= 2
        #print ("Padding: end")

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

    def get_now (self ,
                 format_type = "t"):
        curr_ms = time.ticks_ms ()
        #print ("get_now:",curr_ms, RemoteArea.next_ntptime_ms)
        if time.ticks_diff (curr_ms, RemoteArea.next_ntptime_ms) >= 0 :
            #print ("get_now: getting ntptime")
            try:
                ntptime.settime()
            except:
                pass
            RemoteArea.next_ntptime_ms = time.ticks_add (curr_ms,
                                                   (RemoteArea.ntptime_interval_minutes * 3600))
        return array ("i", time.gmtime(time.time() + (RemoteArea.local_second_offset)))

    def setup_sysfont (self ,
                       scale = None ,
                       horizontal = None) :
        #print ("scale:", scale)
        self.font = None
        if horizontal is not None :
            self.horizontal = horizontal
        if scale is not None :
            self.scale = scale
        if self.scale is None :
            if self.horizontal :
                self.scale = self.ylen // 8
            else :
                self.scale = self.xlen // 5
        if self.scale < 1 :
            self.scale = 1
        elif self.scale > 10 :
            self.scale = 10
        #print (self.scale)
        if self.horizontal :
            self.text_length_max = (self.xlen + self.scale) // (self.scale * 6) # char width + 1
        else :
            self.text_length_max = (self.ylen + self.scale) // (self.scale * 9)
        
    def text_sysfont (self ,
                     text ,
                     text_color = 0 ,
                     scale_in = None ,
                     horizontal_in = True ,
                     ) :
        x_char = self.xmin                   # first char position
        y_char = self.ymin
        scale = self.scale
        horizontal = self.horizontal
        if scale_in is not None :
            scale = scale_in
        if horizontal_in is not None :
            horizontal = horizontal_in
        for char in text :
            if ord (char) > SYSFONT["End"] :
                char = "?"                   # invalid
            sysfont_idx = ord (char) * 5     # first col bits
            x_dot = x_char
            for byte_idx in range (0,5) :    # font columns
                col_bits = SYSFONT["Data"] [sysfont_idx + byte_idx] # col bits
                y_dot = y_char
                for col_idx in range (0,8) : # font rows
                    if col_bits == 0 :
                        break                # no more dots
                    if col_bits & 0x01 != 0 :
                        self.remote_display.rectangle_fill (x = x_dot ,
                                                            w = scale ,
                                                            y = y_dot ,
                                                            h = scale ,
                                                            color = self.textcolor)
                    col_bits >>= 1           # next col bit
                    y_dot += scale      # next row
                x_dot += scale          # next col
            if horizontal :
                x_char += (scale * 6)       # next character position
            else :
                y_char += (scale * 9)       # next character position

## end RemoteArea ##
