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
import gc
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
from text_scroller import TextScroller

FREQ = const (240000000)           # Pico 2 W, 300000000 doesn't work

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

class DisplayIO () :
    def __init__ (self ,
                  display) :
        self.display = display
        self.running = True
        ## page data
        self.page_ids = None
        self.current_page_idx = None
        self.current_page_idx_max = None
        self.set_page_ids ()
        ## button IO
        self.pimoroni_input = PimoroniGPIO ()
        self.pimoroni_input.set_alias ("HOME", "A")
        self.pimoroni_input.set_alias ("SHUT_DOWN", "B")
        self.pimoroni_input.set_alias ("NEXT_PAGE", "Y")
        self.pimoroni_input.set_alias ("PREVIOUS_PAGE", "X")

    def set_page_ids (self) :
        self.page_ids = display.get_page_ids ()
        self.current_page_idx = 0
        self.current_page_idx_max = len (self.page_ids) - 1

    def read_buttons (self) :
        pim_buttons = self.pimoroni_input.read_buttons (("HOME", "SHUT_DOWN", "NEXT_PAGE", "PREVIOUS_PAGE"))
        if pim_buttons ["SHUT_DOWN"] :
            self.running = False
            return
        if pim_buttons ["HOME"] :
            self.current_page_idx = 0
            self.display.change_active_page_index (self.current_page_idx)
        elif pim_buttons ["NEXT_PAGE"] :
            self.current_page_idx += 1
            if self.current_page_idx > self.current_page_idx_max :
                self.current_page_idx = 0
            self.display.change_active_page_index (self.current_page_idx)
        elif pim_buttons ["PREVIOUS_PAGE"] :
            self.current_page_idx -= 1
            if self.current_page_idx < 0 :
                self.current_page_idx = self.current_page_idx_max
            self.display.change_active_page_index (self.current_page_idx)

    def is_running (self) :
        return self.running

## end DisplayIO ##

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
#                            longitude = -94.578331 ,
#                            appid = local_settings.OPEN_WEATHER_APPID)
#open_weather = OpenWeather (latitude = 37.69224000 ,          # Wichita
#                            longitude = -97.33754000 ,
#                            appid = local_settings.OPEN_WEATHER_APPID)
#open_weather = OpenWeather (latitude = 34.05223000 ,          # LA
#                            longitude = -118.24368000 ,
#                            appid = local_settings.OPEN_WEATHER_APPID)
#print (open_weather.get_current_weather ())
#sys.exit ()
udp_input = UpdateUDPServer ()
udp_input.open_udp_port ()
udp_input.read_udp_port ()

#pimoroni_input = PimoroniGPIO ()
#pimoroni_input.set_alias ("HOME", "A")
#pimoroni_input.set_alias ("NEXT_PAGE", "Y")
#pimoroni_input.set_alias ("PREVIOUS_PAGE", "X")

display_io = DisplayIO (display)

message_scroller = TextScroller (display = display ,
                                   line_len_max = 25 ,
                                   line_area_ids = clock_screens.MESSAGE_CONFIG["line_area_ids"])

about_screen_setup ()

display.update_area (area_id = "status", text = "Starting...")
idx = 0
while display_io.is_running () :
    display.update_area (area_id = "c_time")
    #display_io.read_buttons ()
    udp_input.read_udp_port ()
    while True :
        udp_message = udp_input.get_udp_message ()
        if udp_message is None :
            break
        print ("Proceessing:", udp_message)
    if idx % 3600 == 0 :
        print ("w upd", idx)
        open_weather.update ()
    if idx % 20 == 0 :
        message_scroller.add_message ("The value of the interation index: idx =" + str (idx))
        display.update_area (area_id = clock_screens.MESSAGE_CONFIG["update_area_id"])
    #
    idx += 1
    time.sleep (0.25)
    display_io.read_buttons ()

display.update_area (area_id = "status", text = "That's All Folks")
