import time
import re
from array import *

try :
    import ntptime
except :
    class NTPTime :
        def __init__ (self) :
            print ("Set up dummy ntptime")
        def settime (self) :
            pass # Doesn't do anything - not needed
    ntptime = NTPTime ()

from area_modules.remote_area import RemoteArea

class CurrentDateTime () :
    def __init__ (self,
                  utc_offset = -8) :
        self.utc_offset = utc_offset
        self.time_offset = self.utc_offset * 3600
        self.next_ntptime_ms = time.ticks_ms ()

    def get_now_DELETE (self ,
                 format_type = "t"):
        curr_ms = time.ticks_ms ()
        if time.ticks_diff (curr_ms, self.next_ntptime_ms) >= 0 :
            print ("getting ntptime")
            self.next_ntptime_ms = time.ticks_add (curr_ms, (6 * 3600))
            try:
                ntptime.settime()
            except:
                pass
            self.next_ntptime_ms = time.ticks_add (time.ticks_ms (), 60000)
        return array ("i", time.gmtime(time.time() + (self.time_offset)))

#-------------------------------------------------------------------------------
# RemoteDateTime
#-------------------------------------------------------------------------------
class RemoteDateTime (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        self.next_ntptime_ms = time.ticks_ms ()
        self.utc_offset = -8     # Alaska
        self.time_offset = self.utc_offset * 3600
        #self.current_time = CurrentDateTime (-8)
        self.format_types = {
            "d" : "%Y-%m-%d" ,
            "t" : "%H:%M" ,
            "dt" : "%Y-%m-%d %H:%M"
            }
        self.codes = {
            "%Y" : "{0:04d}" ,
            "%m" : "{1:02d}" ,
            "%d" : "{2:02d}" ,
            "%H" : "{3:02d}" ,
            "%M" : "{4:02d}" ,
            "%S" : "{5:02d}" ,
            "%%" : "%"
            }
        #self.format_type = "ts"
        self.format_str = "%Y%m%d%H%M%S"
        if "formatstr" in area_config :
            self.format_str = area_config ["formatstr"]
        elif "formattype" in area_config :
            format_type = area_config["formattype"].lower ()
            if format_type in self.format_types :
                self.format_str = self.format_types [format_type]
        self.format_regex = re.compile ("%Y|%m|%d|%H|%M|%S|%%")
        #if "font" not in area_config :
            #self.font = None
            #self.setup_sysfont ()
        self.text_current = ""
        self.show_border_color = remote_display.get_color_name ("LIME")

    def sub_codes (self, match) :
        code = match.group(0)
        if code in self.codes :
            return self.codes [code]
        return code

    def update (self, **kwargs) :
        #print ("RemoteDateTime: update")
        now = self.get_now ()
        format_text = re.sub (self.format_regex, self.sub_codes, self.format_str)
        text = format_text.format (*now)
        if text != self.text_current :
            #print (text, self.text_current)
            self.text_current = text
            self.reload (reload_all = False)

    def reload (self, reload_all = True) :
        if not self.page_is_active (self.page_id) :
            return
        #print ("active")
        if reload_all :
            self.reload_border ()

        self.remote_display.rectangle_fill (x = self.xmin ,
                                            w = self.xlen ,
                                            y = self.ymin ,
                                            h = self.ylen,
                                            color=self.backgroundcolor)
        if self.font is not None :
            self.remote_display.text (x = self.xmin ,
                                      y = self.ymin ,
                                      text = self.text_current,
                                      font = self.font ,
                                      color = self.textcolor ,
                                      background = self.backgroundcolor)
        else :
            text = self.text_current
            if len (text) > self.text_length_max :
                text = text [0:self.text_length_max]
            self.text_sysfont (text ,
                               self.textcolor)
                               #self.scale ,
                               #self.horizontal)
        if reload_all :
            self.reload_areas ()

## end RemoteDateTime ##
