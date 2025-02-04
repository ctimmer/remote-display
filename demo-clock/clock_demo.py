#
################################################################################
# The MIT License (MIT)
#
# Copyright (c) 2025 Curt Timmerman
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
#import os
from machine import Pin, SPI
import time
import requests
import json

try :
    import local_settings
except :
    print ("local_settings module missing")

import display_modules.st7789py as st7789
#import tti_config # not used
from display_modules.remote_display import RemoteDisplay
from area_modules.remote_sysfont import RemoteSysFont
from area_modules.remote_7segment import Remote7Segment
from area_modules.remote_datetime import RemoteDateTime
from comm_modules.update_queue import UpdateQueue
from comm_modules.update_udpserver import UpdateUDPServer
import clock_screens

from PimDisplayPack28 import PimoroniGPIO
from open_weather import OpenWeather

FREQ = const (240000000)           # 300000000 doesn't work

SPI_ID = const (0)
BAUDRATE = const (40000000)
SCK_PIN = const (18)
MOSI_PIN = const (19)
MISO_PIN = None
RESET_PIN = const (11)
CS_PIN = const (17)
DC_PIN = const (16)
BACKLIGHT_PIN = const (20)
HEIGHT = const (320)
WIDTH = const (240)
ROTATION = const (3)    # landscape 1 or 3

#-------------------------------------------------------------------------------
## text_split - split text into lines with length <= max_len at word boundries
def text_split (text_in,
                max_len = 30) :
    new_lines = []
    tokens = []
    for token in text_in.split () :
        while len (token) > max_len :
            # split tokens with length > max_len
            tokens.append (token [0:max_len])
            token = token [max_len:]
        tokens.append (token)
    ## build lines from tokens
    curr_line = ""
    for token in tokens :
        if len (curr_line) + len (token) + 1 > max_len :
            if len (curr_line) > 0 :
                new_lines.append (curr_line)
            curr_line = token
        else :
            if len (curr_line) > 0 :
                curr_line += " "
            curr_line += token
    if len (curr_line) > 0 :
        new_lines.append (curr_line)
    return new_lines

class TextScroller :
    def __init__ (self, **kwargs) :
        self.display = kwargs ["display"]
        self.line_area_ids = kwargs ["line_area_ids"]
        self.line_len_max = 30
        if "line_len_max" in kwargs :
            self.line_len_max = kwargs ["line_len_max"]
        self.text_queue = UpdateQueue (size = 25)
        self.text_lines = []
        for area_id in self.line_area_ids :
            self.text_lines.append ("")    # initialize blank scroll lines

    def add_queue_message (self, message) :
        self.text_queue.push_queue (message)
    def process_queue_message (self) :
        if not self.text_queue.empty_queue () :
            self.add_message (self.text_queue.pop_queue ())
    def process_queue_all (self) :
        while not self.text_queue.empty_queue () :
            self.add_message (self.text_queue.pop_queue ())
    def add_message (self,
                     message = None ,
                     clear = False ,
                     scroll_to_top = False) :
        if clear :
            for line_idx in range (0, len (self.text_lines)) :
                self.text_lines [line_idx] = ""
        if message is not None :
            new_lines = text_split (message, self.line_len_max)
            new_lines_len = len (new_lines)
            if new_lines_len <= 0 :
                new_lines.append ("")        # Add blank line
                new_lines_len = 1
            if new_lines_len > len (self.text_lines) :
                new_lines = new_lines [new_lines_len - len (self.text_lines)::]
            for text_lines_idx in range (0, (len (self.text_lines) - new_lines_len)) :
                self.text_lines [text_lines_idx] = self.text_lines [text_lines_idx + new_lines_len]
            text_lines_idx = len (self.text_lines) - new_lines_len
            for text_idx in range (0, new_lines_len) :
                self.text_lines [text_lines_idx] = new_lines [text_idx]
                text_lines_idx += 1
            #print ("new:", self.text_lines)
        if scroll_to_top :
            line_idx = None
            for line_idx in range (0, len (self.text_lines)) :
                if self.text_lines [line_idx] != "" :
                    break
            for scroll_idx in range (0, (len (self.text_lines) - line_idx)) :
                self.text_lines [scroll_idx] = self.text_lines [(scroll_idx + line_idx)]
            for line_idx in range ((scroll_idx + 1), len (self.text_lines)) :
                self.text_lines [line_idx] = ""
        self.update_scroll_lines ()

    def update_scroll_lines (self) :
        #print ("update_scroll_lines:", self.text_lines)
        for text_idx, text_area_id in enumerate (self.line_area_ids) :
            self.display.update_area (area_id = text_area_id ,
                                      text = self.text_lines [text_idx])

def about_screen_setup () :
    import os
    import gc
    about_scroller = TextScroller (display = display ,
                                    line_len_max = 50 ,
                                    line_area_ids = clock_screens.ABOUT_CONFIG["line_area_ids"])

    os_info = os.uname ()
    about_scroller.add_message ("Copyright (c) 2025 Curt Timmerman")
    about_scroller.add_message ("")
    
    #about_scroller.add_message ("")
    about_scroller.add_message ("**** OS")
    about_scroller.add_message ("SYSNAME: " + os_info.sysname)
    about_scroller.add_message ("NODENAME: " + os_info.nodename)
    about_scroller.add_message ("RELEASE: " + os_info.release)
    about_scroller.add_message ("VERSION: " + os_info.version)
    about_scroller.add_message ("MACHINE: " + os_info.machine)

    #about_scroller.add_message ("")
    about_scroller.add_message ("**** MEMORY")
    gc.collect ()
    about_scroller.add_message ("ALLOCATED: " + str (gc.mem_alloc()))
    about_scroller.add_message ("FREE: " + str (gc.mem_free()))
    
    about_scroller.add_message ("**** SYS")
    about_scroller.add_message ("BYTE ORDER: " + sys.byteorder)
    max_size = "<= 32"
    bits = 0
    v = sys.maxsize
    while v:
        bits += 1
        v >>= 1
    if bits > 32:
        max_size = ">= 64"
    about_scroller.add_message ("INT SIZE: " + max_size)

    about_scroller.add_message (scroll_to_top = True)

#-------------------------------------------------------------------------------
# main
#-------------------------------------------------------------------------------

if FREQ > 0 :
    machine.freq (FREQ)

st_display = st7789.ST7789 (
        SPI (SPI_ID ,
             baudrate = BAUDRATE ,
             sck = SCK_PIN ,
             mosi = MOSI_PIN ,
             miso = MISO_PIN) ,
        WIDTH ,
        HEIGHT ,
        reset = Pin (RESET_PIN, Pin.OUT) ,
        cs = Pin (CS_PIN, Pin.OUT) ,
        dc = Pin (DC_PIN, Pin.OUT) ,
        backlight = Pin (BACKLIGHT_PIN, Pin.OUT) ,
        rotation = ROTATION)

display = RemoteDisplay (display_object = st_display)
display.add_area_type ("sysfont", RemoteSysFont)
display.add_area_type ("7seg", Remote7Segment)
display.add_area_type ("datetime", RemoteDateTime)

display.setup_config_dict (clock_screens.CLOCK_SCREEN)
display.setup_config_dict (clock_screens.WEATHER_SCREEN)
display.setup_config_dict (clock_screens.MESSAGE_SCREEN)
display.setup_config_dict (clock_screens.ABOUT_SCREEN)
current_page_idx = 0
current_page_idx_max = 3

#display.screen_clear ()
#display.show_area ()
#sys.exit ()
open_weather = OpenWeather (display,
                            latitude = 61.54175 ,           # Big Lake
                              longitude = -149.83036 ,
                              appid = local_settings.OPEN_WEATHER_APPID)
#open_weather = OpenWeather (latitude = 39.099724 ,          # KC
#                              longitude = -94.578331 ,
#                              appid = local_settings.OPEN_WEATHER_APPID)
#open_weather = OpenWeather (latitude = 37.69224000 ,          # Wichita
#                              longitude = -97.33754000 ,
#                              appid = local_settings.OPEN_WEATHER_APPID)
#open_weather = OpenWeather (latitude = 34.05223000 ,          # LA
#                              longitude = -118.24368000 ,
#                              appid = local_settings.OPEN_WEATHER_APPID)
#print (open_weather.get_current_weather ())
#sys.exit ()
udp_input = UpdateUDPServer ()
udp_input.open_udp_port ()
udp_input.read_udp_port ()

pimoroni_input = PimoroniGPIO ()
pimoroni_input.set_alias ("HOME", "A")
pimoroni_input.set_alias ("NEXT_PAGE", "Y")
pimoroni_input.set_alias ("PREVIOUS_PAGE", "X")

message_scroller = TextScroller (display = display ,
                                   line_len_max = 25 ,
                                   line_area_ids = clock_screens.MESSAGE_CONFIG["line_area_ids"])

about_screen_setup ()

#open_weather.update ()
display.update_area (area_id = "status", text = "Starting...")
#display.change_active_page_id ("weather")
#display.change_active_page_id ("messages")
#message_scroller.add_message ("1234567890123456789012345678901234567890")
#sys.exit ()
for idx in range (0, 20000) :
    display.update_area (area_id = "c_time")
    udp_input.read_udp_port ()
    while True :
        udp_message = udp_input.get_udp_message ()
        if udp_message is None :
            break
        print ("Proceessing:", udp_message)
    if idx % 1800 == 0 :
        print ("w upd", idx)
        open_weather.update ()
    if idx % 20 == 0 :
        message_scroller.add_message ("The value of the interation index: idx =" + str (idx))
        display.update_area (area_id = clock_screens.MESSAGE_CONFIG["update_area_id"])
    pim_buttons = pimoroni_input.read_buttons (("HOME", "NEXT_PAGE", "PREVIOUS_PAGE", "B"))
    if pim_buttons ["HOME"] :
        current_page_idx = 0
        display.change_active_page_index (current_page_idx)
    elif pim_buttons ["NEXT_PAGE"] :
        current_page_idx += 1
        if current_page_idx > current_page_idx_max :
            current_page_idx = 0
        display.change_active_page_index (current_page_idx)
    elif pim_buttons ["PREVIOUS_PAGE"] :
        current_page_idx -= 1
        if current_page_idx < 0 :
            current_page_idx = current_page_idx_max
        display.change_active_page_index (current_page_idx)
    time.sleep (0.5)

display.update_area (area_id = "status", text = "That's All Folks")

'''
## Scrolling text
os_info = os.uname ()
os_text = ["OS INFORMATION"]

MAX_TEXT_LEN = 25
os_text += text_split ("SYSNAME: " + os_info.sysname, max_len = MAX_TEXT_LEN)
os_text += text_split ("RELEASE: " + os_info.release, max_len = MAX_TEXT_LEN)
os_text += text_split ("VERSION: " + os_info.version, max_len = MAX_TEXT_LEN)
os_text += text_split ("MACHINE: " + os_info.machine, max_len = MAX_TEXT_LEN)
#print (os_text)

scroll_area_ids = display_screen.SCROLL_AREA_IDS
scroll_text = display_screen.scroll_text
for os_text_idx in range (0, len (os_text)) :
    scroll_idx = 1
    for scroll_idx in range (scroll_idx, len (scroll_text)) :
        scroll_text [scroll_idx - 1] = scroll_text [scroll_idx]
    scroll_text [scroll_idx] = os_text [os_text_idx]
    scroll_idx = 0
    for area_id in scroll_area_ids :
        display.update_area (area_id = area_id, text = scroll_text [scroll_idx])
        scroll_idx += 1
    time.sleep (2.0)

#time.sleep (2)
display.update_area (area_id = "text_output" ,
                     text = "End of Demonstration")

print ("End of Demonstration")
'''