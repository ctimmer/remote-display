#
import time
import random

import tkinter
from tkinter import font
#from PIL import Image     # Used by demo_5

USE_MODULE_DEMO_DISPLAYS = True
json_displays = None       # Used when USE_MODULE_DEMO_DISPLAYS is False

from display_modules.remote_display import RemoteDisplay
from area_modules.remote_sysfont import RemoteSysFont
from area_modules.remote_image import RemoteImage
from area_modules.remote_lamp import RemoteLamp
from area_modules.remote_7segment import Remote7Segment
from area_modules.remote_linear_gauge import RemoteLinearGauge
from area_modules.remote_linear_gauge_ticks import RemoteLinearGaugeTicks
from area_modules.remote_template import RemoteTemplate
from area_modules.remote_datetime import RemoteDateTime

################################################################################
# DEMO displays, initialize and update
################################################################################

## Determines which of the 9 demos are displayed
DEMO_LIST = {
    "demo_1" : {} ,
    "demo_2" : {} ,
    "demo_3" : {} ,
    "demo_4" : {} ,
    "demo_5" : {} ,
    "demo_6" : {} ,
    "demo_7" : {} ,
    "demo_8" : {} ,
    "demo_9" : {} ,
    "dummy" : {}
    }

## tkinter set up
#
DISPLAY_WIDTH = 320
DISPLAY_HEIGHT = 240

print ("tk_display setup")
tk_display = tkinter.Tk ()
tk_display.geometry ("{:04d}x{:04d}".format((DISPLAY_WIDTH * 3)  + 35 ,
                                            (DISPLAY_HEIGHT * 3) + 35))
#tk_display.tk.call('tk', 'scaling', 2.0)
tk_display.title ("Remote Display Demonstration")
tk_display.config(bg = "black") 

CANVAS_DEFAULT = {
    "width" : DISPLAY_WIDTH ,
    "height" : DISPLAY_HEIGHT
    }
CANVAS_BG = "black"
GRID_DEFAULT = {
    "padx" : 5 ,
    "pady" : 5
    }

## setup_display
#
def setup_display (display, display_name) :
    if USE_MODULE_DEMO_DISPLAYS :
        import rem_demo_displays
        display.setup_config_dict (getattr (rem_demo_displays, display_name, None))
    else :
        global json_displays
        if json_displays is None :
            with open("rem_demo_displays.py", 
                      mode="r",
                      encoding="utf-8") as display_fp :
                code = display_fp.read ()
            #print (code)
            exec (code)
            import json
            with open('rem_demo_displays.json') as fp :
                json_displays = json.load (fp)
        display.setup_config_dict (json_displays [display_name])

## end get_display_congig ##

#-------------------------------------------------------------------------------
def demo_1_init () :
    demo_id = "demo_1"
    demo_canvas = tkinter.Canvas(tk_display ,
                                **{**CANVAS_DEFAULT ,
                                    **{
                                    "bg" : CANVAS_BG
                                    }})
    demo_canvas.grid (column = 0 ,
                        row = 0 ,
                        **GRID_DEFAULT)

    if demo_id not in DEMO_LIST :
        return

    DEMO_LIST [demo_id]["canvas"] = demo_canvas

    display = RemoteDisplay (width = DISPLAY_WIDTH ,
                            height = DISPLAY_HEIGHT ,
                            display = demo_canvas)
    display.add_area_type ("sysfont", RemoteSysFont)
    display.add_font_specs ("courier", font.Font (family = 'Courier' ,
                                                    size = -24 ))
    display.add_font_specs ("helvetica", font.Font (family = 'Helvetica' ,
                                                size = -24 ,
                                                weight = 'bold'))
    display.add_font_specs ("times", font.Font (family = 'Times' ,
                                                size = -24 ,
                                                weight = 'bold'))
    display.add_font_specs ("sans", font.Font (family = 'Sans Display' ,
                                                size = -24 ,
                                                weight = 'bold'))
    setup_display (display, demo_id + "_display")
    DEMO_LIST [demo_id]["display"] = display
    return display

## end demo_1_init

def demo_1_loop () :
    demo_id = "demo_1"
    if demo_id not in DEMO_LIST :
        return

    display = DEMO_LIST [demo_id]["display"]

    display.screen_reload ()

## end demo_1_loop

#-------------------------------------------------------------------------------
def demo_2_init () :
    demo_id = "demo_2"
    demo_canvas = tkinter.Canvas(tk_display ,
                                **{**CANVAS_DEFAULT ,
                                    **{
                                    "bg" : CANVAS_BG
                                    }})
    demo_canvas.grid (column = 1 ,
                        row = 0 ,
                        **GRID_DEFAULT)

    if demo_id not in DEMO_LIST :
        return

    DEMO_LIST [demo_id]["canvas"] = demo_canvas

    display = RemoteDisplay (width = DISPLAY_WIDTH ,
                            height = DISPLAY_HEIGHT ,
                            display = demo_canvas)
    display.add_area_type ("sysfont", RemoteSysFont)
    display.add_area_type ("7segment", Remote7Segment)
    setup_display (display, demo_id + "_display")
    DEMO_LIST [demo_id]["display"] = display
    return display

## end demo_2_init

def demo_2_loop () :
    demo_id = "demo_2"
    if demo_id not in DEMO_LIST :
        return

    display = DEMO_LIST [demo_id]["display"]

    display.screen_reload ()

## end demo_2_loop

#-------------------------------------------------------------------------------

DEMO_3_COUNT = -1
DEMO_3_COMPASS_POINT_NAMES = (
    "compass_n" ,
    "compass_ne" ,
    "compass_e" ,
    "compass_se" ,
    "compass_s" ,
    "compass_sw" ,
    "compass_w" ,
    "compass_nw"
    )

def demo_3_init () :
    demo_id = "demo_3"
    demo_canvas = tkinter.Canvas(tk_display ,
                                **{**CANVAS_DEFAULT ,
                                    **{
                                    "bg" : CANVAS_BG
                                    }})
    demo_canvas.grid (column = 2 ,
                        row = 0 ,
                        **GRID_DEFAULT)

    if demo_id not in DEMO_LIST :
        return

    DEMO_LIST [demo_id]["canvas"] = demo_canvas

    display = RemoteDisplay (width = DISPLAY_WIDTH ,
                            height = DISPLAY_HEIGHT ,
                            display = demo_canvas)
    display.add_area_type ("sysfont", RemoteSysFont)
    display.add_area_type ("lamp", RemoteLamp)
    setup_display (display, demo_id + "_display")
    DEMO_LIST [demo_id]["display"] = display
    return display

## end demo_3_init

def demo_3_loop () :
    global DEMO_3_COUNT
    demo_id = "demo_3"
    if demo_id not in DEMO_LIST :
        return

    display = DEMO_LIST [demo_id]["display"]
    direction_list = ("north", "east", "south", "west")

    DEMO_3_COUNT += 1
    display.update_area (area = "onoff" ,
                        lamp_index = (DEMO_3_COUNT % 2))
    display.update_area (area = "status" ,
                        lamp_index = (DEMO_3_COUNT % 3))
    display.update_area (area = "direction" ,
                        lamp_id = direction_list [(DEMO_3_COUNT % 4)])

    for compass_point in DEMO_3_COMPASS_POINT_NAMES :
        display.update_area (area = compass_point ,
                            lamp_id = "off")
    display.update_area (area = DEMO_3_COMPASS_POINT_NAMES [DEMO_3_COUNT % 8] ,
                        lamp_id = "on")

    display.screen_reload ()

## end demo_3_loop

#-------------------------------------------------------------------------------
DEMO_4_TRIG_LEN = 20
DEMO_4_TRIG_AREA_IDS = [None] * DEMO_4_TRIG_LEN
DEMO_4_TRIG_VALUES = [None] * DEMO_4_TRIG_LEN

def demo_4_init () :
    demo_id = "demo_4"
    demo_canvas = tkinter.Canvas(tk_display ,
                                **{**CANVAS_DEFAULT ,
                                    **{
                                    "bg" : CANVAS_BG
                                    }})
    demo_canvas.grid (column = 0 ,
                        row = 1 ,
                        **GRID_DEFAULT)

    if demo_id not in DEMO_LIST :
        return

    import math
    DEMO_LIST [demo_id]["canvas"] = demo_canvas

    display = RemoteDisplay (width = DISPLAY_WIDTH ,
                            height = DISPLAY_HEIGHT ,
                            display = demo_canvas)
    display.add_area_type ("sysfont", RemoteSysFont)
    display.add_area_type ("lineargauge", RemoteLinearGauge)
    display.add_area_type ("lineargaugeticks", RemoteLinearGaugeTicks)
    setup_display (display, demo_id + "_display")
    trig_in_value = 0.0
    trig_increment = (2.0 * math.pi) / 20.0
    for trig_idx in range (0, DEMO_4_TRIG_LEN) :
        DEMO_4_TRIG_AREA_IDS [trig_idx] = "trig_" + str (trig_idx)
        DEMO_4_TRIG_VALUES [trig_idx] = math.cos (trig_in_value)
        trig_in_value += trig_increment
    # print (DEMO_4_TRIG_VALUES)

    DEMO_LIST [demo_id]["display"] = display
    return display

## end demo_4_init

DEMO_4_TRIG_COUNT = -1
def demo_4_loop () :
    global DEMO_4_TRIG_COUNT
    global DEMO_4_TRIG_AREA_IDS
    global DEMO_4_TRIG_VALUES
    demo_id = "demo_4"
    if demo_id not in DEMO_LIST :
        return

    display = DEMO_LIST [demo_id]["display"]

    ftemp = random.randint (-60, 260) 
    ctemp = int ((5 / 9) * (ftemp - 32))
    ktemp = ctemp + 273
    
    display.update_area (area = "Ftext",
                            text = "{: 4}F".format (ftemp))
    display.update_area (area = "Fdisplay",
                            value = ftemp)
    display.update_area (area = "Ctext",
                            text = "{: 4}C".format (ctemp))
    display.update_area (area = "Cdisplay",
                            value = ctemp)
    display.update_area (area = "Ktext",
                            text = "{: 4}K".format (ktemp))
    display.update_area (area = "Kdisplay",
                            value = ktemp)

    DEMO_4_TRIG_COUNT += 1
    if DEMO_4_TRIG_COUNT >= DEMO_4_TRIG_LEN :
        DEMO_4_TRIG_COUNT = 0
    trig_idx = DEMO_4_TRIG_COUNT
    for area_idx in range (0, DEMO_4_TRIG_LEN) :
        display.update_area (area = DEMO_4_TRIG_AREA_IDS [area_idx] ,
                            value = DEMO_4_TRIG_VALUES [trig_idx])
        trig_idx += 1
        if trig_idx >= DEMO_4_TRIG_LEN :
            trig_idx = 0

    display.screen_reload ()

## end demo_4_loop

#-------------------------------------------------------------------------------
def demo_5_init () :
    demo_id = "demo_5"
    demo_canvas = tkinter.Canvas(tk_display ,
                                **{**CANVAS_DEFAULT ,
                                    **{
                                    "bg" : CANVAS_BG
                                    }})
    demo_canvas.grid (column = 1 ,
                        row = 1 ,
                        **GRID_DEFAULT)

    if demo_id not in DEMO_LIST :
        return

    from PIL import Image

    DEMO_LIST [demo_id]["canvas"] = demo_canvas

    display = RemoteDisplay (width = DISPLAY_WIDTH ,
                            height = DISPLAY_HEIGHT ,
                            display = demo_canvas)
    DEMO_LIST [demo_id]["display"] = display

    display.add_area_type ("sysfont", RemoteSysFont)
    display.add_area_type ("image", RemoteImage)

    python_image = Image.open('images/curt.jpg')
    display.add_image_object ("me", python_image)
    python_image = Image.open('images/mecold.jpg')
    display.add_image_object ("mecold", python_image)
    python_image = Image.open('images/heart.jpg')
    display.add_image_object ("heart", python_image)

    setup_display (display, demo_id + "_display")

    return display

## end demo_5_init

def demo_5_loop () :
    demo_id = "demo_5"
    if demo_id not in DEMO_LIST :
        return

    display = DEMO_LIST [demo_id]["display"]
    demo_canvas = DEMO_LIST [demo_id]["canvas"]

    #display.screen_reload ()   # Nothing changes

## end demo_5_loop

#-------------------------------------------------------------------------------
def demo_6_init () :
    demo_id = "demo_6"
    demo_canvas = tkinter.Canvas(tk_display ,
                                **{**CANVAS_DEFAULT ,
                                    **{
                                    "bg" : CANVAS_BG
                                    }})
    demo_canvas.grid (column = 2 ,
                        row = 1 ,
                        **GRID_DEFAULT)

    if demo_id not in DEMO_LIST :
        return

    DEMO_LIST [demo_id]["canvas"] = demo_canvas

    display = RemoteDisplay (width = DISPLAY_WIDTH ,
                            height = DISPLAY_HEIGHT ,
                            display = demo_canvas)
    display.add_area_type ("sysfont", RemoteSysFont)
    display.add_area_type ("datetime", RemoteDateTime)
    setup_display (display, demo_id + "_display")
    DEMO_LIST [demo_id]["display"] = display
    return display

## end demo_6_init

def demo_6_loop () :
    demo_id = "demo_6"
    if demo_id not in DEMO_LIST :
        return

    display = DEMO_LIST [demo_id]["display"]

    display.update_area (area = "date_1")
    display.update_area (area = "date_2")
    display.update_area (area = "date_3")
    display.update_area (area = "date_4")
    display.update_area (area = "date_5")
    display.update_area (area = "date_6")
    display.update_area (area = "date_7")
    display.update_area (area = "date_8")
    #display.update_area (area = "date_9")

    display.screen_reload ()

## end demo_6_loop

DEMO_7_DISPLAY = "demo_4"

#-------------------------------------------------------------------------------
def demo_7_init () :
    demo_id = "demo_7"
    demo_canvas = tkinter.Canvas(tk_display ,
                                **{**CANVAS_DEFAULT ,
                                    **{
                                    "bg" : CANVAS_BG
                                    }})
    demo_canvas.grid (column = 0 ,
                        row = 2 ,
                        **GRID_DEFAULT)

    if demo_id not in DEMO_LIST :
        return

    DEMO_LIST [demo_id]["canvas"] = demo_canvas

    display = RemoteDisplay (width = DISPLAY_WIDTH ,
                            height = DISPLAY_HEIGHT ,
                            display = demo_canvas)
    display.add_area_type ("sysfont", RemoteSysFont)
    display.add_area_type ("lineargauge", RemoteLinearGauge)
    #setup_display (display, demo_id + "_display")
    setup_display (display, DEMO_7_DISPLAY + "_display")
    display.screen_clear ()
    display.show_area ()
    DEMO_LIST [demo_id]["display"] = display
    return display

## end demo_7_init

def demo_7_loop () :
    demo_id = "demo_7"
    if demo_id not in DEMO_LIST :
        return

    display = DEMO_LIST [demo_id]["display"]

    #display.screen_reload ()

## end demo_7_loop

DEMO_8_DISPLAY = "demo_5"

#-------------------------------------------------------------------------------
def demo_8_init () :
    demo_id = "demo_8"
    demo_canvas = tkinter.Canvas(tk_display ,
                                **{**CANVAS_DEFAULT ,
                                    **{
                                    "bg" : CANVAS_BG
                                    }})
    demo_canvas.grid (column = 1 ,
                        row = 2 ,
                        **GRID_DEFAULT)

    if demo_id not in DEMO_LIST :
        return

    from PIL import Image

    DEMO_LIST [demo_id]["canvas"] = demo_canvas

    display = RemoteDisplay (width = DISPLAY_WIDTH ,
                            height = DISPLAY_HEIGHT ,
                            display = demo_canvas)
    display.add_area_type ("sysfont", RemoteSysFont)

    display.add_area_type ("image", RemoteImage)
    python_image = Image.open('images/curt.jpg')
    display.add_image_object ("me", python_image)
    python_image = Image.open('images/mecold.jpg')
    display.add_image_object ("mecold", python_image)
    python_image = Image.open('images/heart.jpg')
    display.add_image_object ("heart", python_image)

    #setup_display (display, demo_id + "_display")
    setup_display (display, DEMO_8_DISPLAY + "_display")
    display.screen_clear ()
    display.show_area ()
    DEMO_LIST [demo_id]["display"] = display
    return display

## end demo_8_init

def demo_8_loop () :
    demo_id = "demo_8"
    if demo_id not in DEMO_LIST :
        return

    display = DEMO_LIST [demo_id]["display"]

    #display.screen_reload ()

## end demo_8_loop

#-------------------------------------------------------------------------------

DEMO_9_DISPLAY = "demo_6"

def demo_9_init () :
    demo_id = "demo_9"
    demo_canvas = tkinter.Canvas(tk_display ,
                                **{**CANVAS_DEFAULT ,
                                    **{
                                    "bg" : CANVAS_BG
                                    }})
    demo_canvas.grid (column = 2 ,
                        row = 2 ,
                        **GRID_DEFAULT)

    if demo_id not in DEMO_LIST :
        return

    DEMO_LIST [demo_id]["canvas"] = demo_canvas

    display = RemoteDisplay (width = DISPLAY_WIDTH ,
                            height = DISPLAY_HEIGHT ,
                            display = demo_canvas)
    #display.add_area_type ("sysfont", RemoteSysFont)
    display.add_area_type ("sysfont", RemoteSysFont)
    display.add_area_type ("7segment", Remote7Segment)
    display.add_area_type ("lamp", RemoteLamp)
    display.add_area_type ("datetime", RemoteDateTime)
    #display.setup_config_dict (DEMO_9_DISPLAY)
    #display.setup_config_dict (rem_demo_displays.demo_9_display)
    setup_display (display, DEMO_9_DISPLAY + "_display")
    DEMO_LIST [demo_id]["display"] = display
    display.screen_clear ()
    display.show_area ()
    return display

## end demo_9_init

def demo_9_loop () :
    demo_id = "demo_9"
    if demo_id not in DEMO_LIST :
        return

    display = DEMO_LIST [demo_id]["display"]
    canvas = DEMO_LIST [demo_id]["canvas"]
    #display.screen_reload ()

## end demo_9_loop

def update_loop ():
    #print("Update loop")
    demo_1_loop ()
    demo_2_loop ()
    demo_3_loop ()
    demo_4_loop ()
    demo_5_loop ()
    demo_6_loop ()
    demo_7_loop ()
    demo_8_loop ()
    demo_9_loop ()
    tk_display.after(1000, update_loop)

################################################################################
# MAIN
################################################################################

DISPLAY_1 = demo_1_init ()
DISPLAY_2 = demo_2_init ()
DISPLAY_3 = demo_3_init ()
DISPLAY_4 = demo_4_init ()
DISPLAY_5 = demo_5_init ()
DISPLAY_6 = demo_6_init ()
DISPLAY_7 = demo_7_init ()
DISPLAY_8 = demo_8_init ()
DISPLAY_9 = demo_9_init ()
json_displays = None         # No longer needed

# call update_loop after zero seconds
tk_display.after(0, update_loop)

print ("Starting Display")
tk_display.mainloop()

