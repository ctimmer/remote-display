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
import os
from machine import Pin, SPI
import time

import display_modules.st7789py as st7789
#import tti_config # not used
from display_modules.remote_display import RemoteDisplay
from area_modules.remote_sysfont import RemoteSysFont
from area_modules.remote_7segment import Remote7Segment

import display_screen               # display configuration

FREQ = const (240000000)           # 300000000 doesn't work (Pico 2)
#FREQ = const (0)                  # No freq change

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
## text_split - split text into string array at word boundries
def text_split (text_in, max_len = 30) :
    #print (text_in)
    text_return = []
    text_words = text_in.split ()
    word_idx = 0
    #print (text_words)
    text_line = ""
    while word_idx < len (text_words) :
        #print (text_words [word_idx])
        append_len = max_len
        if len (text_words [word_idx]) > max_len :
            if len (text_line) > 0 :
                len_left = max_len - len (text_line)
                if len_left >= 4 :
                    append_len -= len_left
                    len_left -= 1
                    text_line += " " + (text_words [word_idx][0:len_left])
                    text_words [word_idx] = text_words [word_idx][len_left:]
                text_return.append (text_line)
                text_line = ""
            #text_return.append (text_words [word_idx][0:append_len])
            #text_words [word_idx] = text_words [word_idx][append_len:]
            continue
        if len (text_line) + len (text_words [word_idx]) + 1 > max_len :
            if len (text_line) > 0 :
                text_return.append (text_line)
                text_line = ""
        if len (text_line) > 0 :
            #text_line += " "
            text_line += " "
        text_line += text_words [word_idx]
        word_idx += 1
    if len (text_line) > 0 :
        text_return.append (text_line)
    #print (text_return)
    return text_return          # return array of text lines

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

display.setup_config_dict (display_screen.DEMO_SCREEN)

'''
display.screen_clear ()
display.show_area ()
sys.exit ()
'''

time.sleep (2)
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
