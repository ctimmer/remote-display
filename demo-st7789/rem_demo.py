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

from machine import Pin, SPI
import time

import display_modules.st7789py as st7789
#import tti_config # not used
from display_modules.remote_display import RemoteDisplay
from area_modules.remote_sysfont import RemoteSysFont
from area_modules.remote_7segment import Remote7Segment

import display_screen

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

display.setup_config_dict (display_screen.DEMO_SCREEN)

time.sleep (5)
display.update_area (area_id = "text_output" ,
                     text = "Now is the time")

time.sleep (2)
display.update_area (area_id = "text_output" ,
                     text = "for all good people")

time.sleep (2)
display.update_area (area_id = "text_output" ,
                     text = "to come to the aid")

time.sleep (2)
display.update_area (area_id = "text_output" ,
                     text = "of their country")

time.sleep (2)
display.update_area (area_id = "text_end" ,
                     text = "End of Demonstration")

print ("End of Demonstration")
