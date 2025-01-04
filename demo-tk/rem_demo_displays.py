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

JSON_FILE_NAME = "rem_demo_displays.json"
JSON_FILE_INDENT = 2 # 1-8 for pretty print / None for minimize

DISPLAY_VPOS = 0
DISPLAY_VLEN = 240
DISPLAY_HPOS = 0
DISPLAY_HLEN = 320
DISPLAY_BORDERWIDTH = 4
DISPLAY_BORDERCOLORNAME = "RED"
DISPLAY_PADDINGWIDTH = 2
DISPLAY_BACKGROUNDCOLORNAME = "BLACK"

HEADING_TYPE = "sysfont"
HEADING_TEXTCOLORNAME = "WHITE"
HEADING_SCALE = 2
HEADING_VPOS = 0
HEADING_VLEN = 22
HEADING_HPOS = 0
HEADING_HLEN = 308
HEADING_BORDERWIDTH = 0
HEADING_BORDERCOLORNAME = "WHITE"
HEADING_PADDINGWIDTH = 4
HEADING_BACKGROUNDCOLORNAME = "BLUE"

DATALABEL_BACKGROUNDCOLORNAME = "BLACK"
DATALABEL_TEXTCOLORNAME = "WHITE"
DATA_BACKGROUNDCOLORNAME = "WHITE"
DATA_TEXTCOLORNAME = "BLACK"

demo_1_display = {
    "vpos" : DISPLAY_VPOS ,
    "vlen" : DISPLAY_VLEN ,
    "hpos" : DISPLAY_HPOS ,
    "hlen" : DISPLAY_HLEN ,
    "borderwidth" : DISPLAY_BORDERWIDTH ,
    "bordercolorname" : DISPLAY_BORDERCOLORNAME ,
    "paddingwidth" : DISPLAY_PADDINGWIDTH ,
    "backgroundcolorname" : DISPLAY_BACKGROUNDCOLORNAME ,
    "areas" : [
        {
        "type" : HEADING_TYPE ,
        "scale" : HEADING_SCALE ,
        "textcolorname" : HEADING_TEXTCOLORNAME ,
        "vpos" : HEADING_VPOS ,
        "vlen" : HEADING_VLEN ,
        "hpos" : HEADING_HPOS ,
        "hlen" : HEADING_HLEN ,
        "borderwidth" : HEADING_BORDERWIDTH ,
        "bordercolorname" : HEADING_BORDERCOLORNAME ,
        "paddingwidth" : HEADING_PADDINGWIDTH ,
        "backgroundcolorname" : HEADING_BACKGROUNDCOLORNAME ,
        "text" : " DEMO 1 - Fonts"
        } ,
        {
        "type" : "sysfont" ,
        "scale" : 1 ,
        "vpos": 24 ,
        "vlen": 10 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "paddingwidth" : 1 ,
        "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
        "textcolorname" : DATA_TEXTCOLORNAME ,
        "text" : "Sysfont Scale: 1"
        } ,
        {
        "type" : "sysfont" ,
        "scale" : 2 ,
        "vpos": 35 ,
        "vlen": 18 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "paddingwidth" : 1 ,
        "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
        "textcolorname" : DATA_TEXTCOLORNAME ,
        "text" : "Sysfont Scale: 2"
        } ,
        {
        "type" : "sysfont" ,
        "scale" : 3 ,
        "vpos": 54 ,
        "vlen": 26 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "paddingwidth" : 1 ,
        "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
        "textcolorname" : DATA_TEXTCOLORNAME ,
        "text" : "Sysfont Scale: 3"
        } ,
        {
        "type" : "sysfont" ,
        "scale" : 4 ,
        "vpos": 81 ,
        "vlen": 30 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "paddingwidth" : 1 ,
        "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
        "textcolorname" : DATA_TEXTCOLORNAME ,
        "text" : "Scale: 4"
        } ,
        {
        "type" : "text" ,
        "font" : "courier" ,
        "vpos": 112 ,
        "vlen": 30 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "paddingwidth" : 1 ,
        "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
        "textcolorname" : DATA_TEXTCOLORNAME ,
        "text" : "Courier"
        } ,
        {
        "type" : "text" ,
        "font" : "helvetica" ,
        "vpos": 143 ,
        "vlen": 20 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "paddingwidth" : 2 ,
        "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
        "textcolorname" : DATA_TEXTCOLORNAME ,
        "text" : "Helvetica"
        } ,
        {
        "type" : "text" ,
        "font" : "times" ,
        "vpos": 164 ,
        "vlen": 19 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "paddingwidth" : 2 ,
        "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
        "textcolorname" : DATA_TEXTCOLORNAME ,
        "text" : "Times"
        } ,
        {
        "type" : "text" ,
        "font" : "sans" ,
        "vpos": 184 ,
        "vlen": 29 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "paddingwidth" : 2 ,
        "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
        "textcolorname" : DATA_TEXTCOLORNAME ,
        "text" : "Sans"
        }
        ]
    }

#-------------------------------------------------------------------------------
# demo_2 - Seven segement display
#-------------------------------------------------------------------------------

DEMO_2_CONTAINER_HPOS = 0
DEMO_2_CONTAINER_HLEN = 306
DEMO_2_LABEL_HPOS = 0
DEMO_2_LABEL_HLEN = 100
DEMO_2_DATA_HPOS = 101
DEMO_2_DATA_HLEN = 205

demo_2_display = {
    "vpos" : DISPLAY_VPOS ,
    "vlen" : DISPLAY_VLEN ,
    "hpos" : DISPLAY_HPOS ,
    "hlen" : DISPLAY_HLEN ,
    "borderwidth" : DISPLAY_BORDERWIDTH ,
    "bordercolorname" : DISPLAY_BORDERCOLORNAME ,
    "paddingwidth" : DISPLAY_PADDINGWIDTH ,
    "backgroundcolorname" : DISPLAY_BACKGROUNDCOLORNAME ,
    "areas" : [
        {
        "type" : HEADING_TYPE ,
        "scale" : HEADING_SCALE ,
        "textcolorname" : HEADING_TEXTCOLORNAME ,
        "vpos" : HEADING_VPOS ,
        "vlen" : HEADING_VLEN ,
        "hpos" : HEADING_HPOS ,
        "hlen" : HEADING_HLEN ,
        "borderwidth" : HEADING_BORDERWIDTH ,
        "bordercolorname" : HEADING_BORDERCOLORNAME ,
        "paddingwidth" : HEADING_PADDINGWIDTH ,
        "backgroundcolorname" : HEADING_BACKGROUNDCOLORNAME ,
        "type" : "sysfont" ,
        "text" : " DEMO 2 - Seven Segment"
        } ,
        {
        "vpos": 24 ,
        "vlen": 193 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "container" ,
            "vpos": 0 ,
            "vlen": 19 ,
            "hpos": DEMO_2_CONTAINER_HPOS ,
            "hlen": DEMO_2_CONTAINER_HLEN ,
            "areas" : [
                {
                "type" : "sysfont" ,
                "scale" : 2 ,
                "vpos": 0 ,
                "vlen": 19 ,
                "hpos": DEMO_2_LABEL_HPOS ,
                "hlen": DEMO_2_LABEL_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATALABEL_TEXTCOLORNAME ,
                "text" : "dig sz"
                } ,
                {
                "type" : "sysfont" ,
                "scale" : 2 ,
                "vpos": 0 ,
                "vlen": 19 ,
                "hpos": DEMO_2_DATA_HPOS ,
                "hlen": DEMO_2_DATA_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATA_TEXTCOLORNAME ,
                "text" : "      digits"
                }
                ]
            } ,
            {
            "type" : "container" ,
            "vpos": 20 ,
            "vlen": 19 ,
            "hpos": DEMO_2_CONTAINER_HPOS ,
            "hlen": DEMO_2_CONTAINER_HLEN ,
            "areas" : [
                {
                "type" : "sysfont" ,
                "scale" : 2 ,
                "vpos": 0 ,
                "vlen": 19 ,
                "hpos": DEMO_2_LABEL_HPOS ,
                "hlen": DEMO_2_LABEL_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATALABEL_TEXTCOLORNAME ,
                "text" : "default"
                } ,
                {
                "area_id" : "sevensegment_1" ,
                "type" : "7segment" ,
                "formattype" : "d" ,
                "vpos": 0 ,
                "vlen": 19 ,
                "hpos": DEMO_2_DATA_HPOS ,
                "hlen": DEMO_2_DATA_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATA_TEXTCOLORNAME ,
                "text" : "1234567890abcdef"
                }
                ]
            } ,
            {
            "type" : "container" ,
            "vpos": 40 ,
            "vlen": 19 ,
            "hpos": DEMO_2_CONTAINER_HPOS ,
            "hlen": DEMO_2_CONTAINER_HLEN ,
            "areas" : [
                {
                "type" : "sysfont" ,
                "scale" : 2 ,
                "vpos": 0 ,
                "vlen": 19 ,
                "hpos": DEMO_2_LABEL_HPOS ,
                "hlen": DEMO_2_LABEL_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATALABEL_TEXTCOLORNAME ,
                "text" : "'s' bld"
                } ,
                {
                "area_id" : "sevensegment_2" ,
                "type" : "7segment" ,
                "digit_size" : "s" ,
                "bold" : True ,
                "vpos": 0 ,
                "vlen": 19 ,
                "hpos": DEMO_2_DATA_HPOS ,
                "hlen": DEMO_2_DATA_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATA_TEXTCOLORNAME ,
                "text" : "+-1234.567890: X"
                }
                ]
            } ,
            {
            "type" : "container" ,
            "vpos": 60 ,
            "vlen": 36 ,
            "hpos": DEMO_2_CONTAINER_HPOS ,
            "hlen": DEMO_2_CONTAINER_HLEN ,
            "areas" : [
                {
                "type" : "sysfont" ,
                "scale" : 2 ,
                "vpos": 0 ,
                "vlen": 36 ,
                "hpos": DEMO_2_LABEL_HPOS ,
                "hlen": DEMO_2_LABEL_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATALABEL_TEXTCOLORNAME ,
                "text" : "'m' bld"
                } ,
                {
                "area_id" : "sevensegment_3" ,
                "type" : "7segment" ,
                "digit_size" : "m" ,
                "bold" : True ,
                "vpos": 0 ,
                "vlen": 36 ,
                "hpos": DEMO_2_DATA_HPOS ,
                "hlen": DEMO_2_DATA_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATA_TEXTCOLORNAME ,
                "text" : "1234567890"
                }
                ]
            } ,
            {
            "type" : "container" ,
            "vpos": 97 ,
            "vlen": 61 ,
            "hpos": DEMO_2_CONTAINER_HPOS ,
            "hlen": DEMO_2_CONTAINER_HLEN ,
            "areas" : [
                {
                "type" : "sysfont" ,
                "scale" : 2 ,
                "vpos": 0 ,
                "vlen": 61 ,
                "hpos": DEMO_2_LABEL_HPOS ,
                "hlen": DEMO_2_LABEL_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATALABEL_TEXTCOLORNAME ,
                "text" : "'l' bld"
                } ,
                {
                "area_id" : "sevensegment_4" ,
                "type" : "7segment" ,
                "digit_size" : "l" ,
                "bold" : True ,
                "vpos": 0 ,
                "vlen": 61 ,
                "hpos": DEMO_2_DATA_HPOS ,
                "hlen": DEMO_2_DATA_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATA_TEXTCOLORNAME ,
                "text" : "1234"
                }
                ]
            } ,
            {
            "type" : "container" ,
            "vpos": 159 ,
            "vlen": 32 ,
            "hpos": DEMO_2_CONTAINER_HPOS ,
            "hlen": DEMO_2_CONTAINER_HLEN ,
            "areas" : [
                {
                "type" : "sysfont" ,
                "scale" : 2 ,
                "vpos": 0 ,
                "vlen": 32 ,
                "hpos": DEMO_2_LABEL_HPOS ,
                "hlen": DEMO_2_LABEL_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATALABEL_TEXTCOLORNAME ,
                "text" : "'mn' bld"
                } ,
                {
                "area_id" : "sevensegment_5" ,
                "type" : "7segment" ,
                "digit_size" : "mn" ,
                "bold" : True ,
                "vpos": 0 ,
                "vlen": 32 ,
                "hpos": DEMO_2_DATA_HPOS ,
                "hlen": DEMO_2_DATA_HLEN ,
                "paddingwidth" : 2 ,
                "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
                "textcolorname" : DATA_TEXTCOLORNAME ,
                "text" : "+1234567890abc"
                }
                ]
            }
            ]
        }
        ]
    }

DEMO_3_POINT_VLEN = 15
DEMO_3_POINT_VOFFSET = (DEMO_3_POINT_VLEN + 2)
DEMO_3_POINT_HLEN = 26
DEMO_3_POINT_HOFFSET = ((DEMO_3_POINT_HLEN // 2) + 10) # ???
DEMO_3_POINT_ON = (124, 252, 0)
DEMO_3_POINT_OFF = (105, 105, 105)

demo_3_display = {
    "vpos" : DISPLAY_VPOS ,
    "vlen" : DISPLAY_VLEN ,
    "hpos" : DISPLAY_HPOS ,
    "hlen" : DISPLAY_HLEN ,
    "borderwidth" : DISPLAY_BORDERWIDTH ,
    "bordercolorname" : DISPLAY_BORDERCOLORNAME ,
    "paddingwidth" : DISPLAY_PADDINGWIDTH ,
    "backgroundcolorname" : DISPLAY_BACKGROUNDCOLORNAME ,
    "areas" : [
        {
        "type" : HEADING_TYPE ,
        "scale" : HEADING_SCALE ,
        "textcolorname" : HEADING_TEXTCOLORNAME ,
        "vpos" : HEADING_VPOS ,
        "vlen" : HEADING_VLEN ,
        "hpos" : HEADING_HPOS ,
        "hlen" : HEADING_HLEN ,
        "borderwidth" : HEADING_BORDERWIDTH ,
        "bordercolorname" : HEADING_BORDERCOLORNAME ,
        "paddingwidth" : HEADING_PADDINGWIDTH ,
        "backgroundcolorname" : HEADING_BACKGROUNDCOLORNAME ,
        "text" : " DEMO 3 - Lamps"
        } ,
        {
        "type" : "lamp" ,
        "area_id" : "onoff" ,
        "vpos" : 30 ,
        "vlen" : 15 ,
        "hpos" : 120 ,
        "hlen" : 40 ,
        "padding" : 5 ,
        "lampcolors" :
            [
            {
            "name" : "on" ,
            "lampcolorrgb" : (124, 252, 0) ,
            "textcolorname" : "BLACK" ,
            "text" : "  ON"
            } ,
            {
            "name" : "off" ,
            "lampcolorrgb" : (105, 105, 105) ,
            "textcolorname" : "WHITE" ,
            "text" : "  OFF"
            }
            ]
        } ,
        {
        "type" : "lamp" ,
        "area_id" : "status" ,
        "vpos" : 50 ,
        "vlen" : 15 ,
        "hpos" : 110 ,
        "hlen" : 74 ,
        "padding" : 5 ,
        "lampcolors" :
            [
            {
            "name" : "safe" ,
            "lampcolorrgb" : (124, 252, 0) ,
            "textcolorname" : "BLACK" ,
            "text" : "   SAFE"
            } ,
            {
            "name" : "warning" ,
            "lampcolorname" : "YELLOW" ,
            "textcolorname" : "BLACK" ,
            "text" : " WARNING"
            } ,
            {
            "name" : "danger" ,
            "lampcolorname" : "RED" ,
            "textcolorname" : "WHITE" ,
            "text" : " DANGER!"
            }
            ]
        } ,
        {
        "type" : "lamp" ,
        "area_id" : "direction" ,
        "vpos" : 80 ,
        "vlen" : 15 ,
        "hpos" : 110 ,
        "hlen" : 74 ,
        "padding" : 5 ,
        "lampcolors" :
            [
            {
            "name" : "north" ,
            "lampcolorrgb" : (124, 252, 0) ,
            "textcolorname" : "BLACK" ,
            "text" : " North"
            } ,
            {
            "name" : "east" ,
            "lampcolorrgb" : (124, 252, 0) ,
            "textcolorname" : "BLACK" ,
            "text" : "  East"
            } ,
            {
            "name" : "south" ,
            "lampcolorrgb" : (124, 252, 0) ,
            "textcolorname" : "BLACK" ,
            "text" : " South"
            } ,
            {
            "name" : "west" ,
            "lampcolorrgb" : (124, 252, 0) ,
            "textcolorname" : "BLACK" ,
            "text" : "  West"
            }
            ]
        } ,
        {
        "type" : "container" ,
        "area_id" : "compass" ,
        "vpos" : 109 ,
        "vlen" : 120 ,
        "hpos" : 0 ,
        "hlen" : 140 ,
        "backgroundcolorname" : "WHITE" ,
        "areas" : [
            {
            "type" : "lamp" ,
            "area_id" : "compass_n" ,
            "vpos" : 0 ,
            "vlen" : DEMO_3_POINT_VLEN ,
            "hpos" : (DEMO_3_POINT_HOFFSET * 2) ,
            "hlen" : DEMO_3_POINT_HLEN ,
            "padding" : 5 ,
            "lampcolors" :
                [
                {
                "name" : "on" ,
                "lampcolorrgb" : (0, 0, 255) ,
                "textcolorname" : "BLACK" ,
                "text" : "N"
                } ,
                {
                "name" : "off" ,
                "lampcolorrgb" : DEMO_3_POINT_OFF ,
                "textcolorname" : "WHITE" ,
                "text" : "N"
                }
                ]
            } ,
            {
            "type" : "lamp" ,
            "area_id" : "compass_nw" ,
            "vpos" : DEMO_3_POINT_VOFFSET ,
            "vlen" : DEMO_3_POINT_VLEN ,
            "hpos" : (DEMO_3_POINT_HOFFSET * 1) ,
            "hlen" : DEMO_3_POINT_HLEN ,
            "padding" : 5 ,
            "lampcolors" :
                [
                {
                "name" : "on" ,
                "lampcolorrgb" : (51, 0, 204) ,
                "textcolorname" : "BLACK" ,
                "text" : "NW"
                } ,
                {
                "name" : "off" ,
                "lampcolorrgb" : DEMO_3_POINT_OFF ,
                "textcolorname" : "WHITE" ,
                "text" : "NW"
                }
                ]
            } ,
            {
            "type" : "lamp" ,
            "area_id" : "compass_ne" ,
            "vpos" : (DEMO_3_POINT_VOFFSET * 1) ,
            "vlen" : DEMO_3_POINT_VLEN ,
            "hpos" : (DEMO_3_POINT_HOFFSET * 3) ,
            "hlen" : DEMO_3_POINT_HLEN ,
            "padding" : 5 ,
            "lampcolors" :
                [
                {
                "name" : "on" ,
                "lampcolorrgb" : (51, 0, 204) ,
                "textcolorname" : "BLACK" ,
                "text" : "NE"
                } ,
                {
                "name" : "off" ,
                "lampcolorrgb" : DEMO_3_POINT_OFF ,
                "textcolorname" : "WHITE" ,
                "text" : "NE"
                }
                ]
            } ,
            {
            "type" : "lamp" ,
            "area_id" : "compass_w" ,
            "vpos" : (DEMO_3_POINT_VOFFSET * 2) ,
            "vlen" : DEMO_3_POINT_VLEN ,
            "hpos" : 0 ,
            "hlen" : DEMO_3_POINT_HLEN ,
            "padding" : 5 ,
            "lampcolors" :
                [
                {
                "name" : "on" ,
                "lampcolorrgb" : (128, 0, 128) ,
                "textcolorname" : "BLACK" ,
                "text" : "W"
                } ,
                {
                "name" : "off" ,
                "lampcolorrgb" : DEMO_3_POINT_OFF ,
                "textcolorname" : "WHITE" ,
                "text" : "W"
                }
                ]
            } ,

            {
            "type" : "lamp" ,
            "area_id" : "compass_e" ,
            "vpos" : (DEMO_3_POINT_VOFFSET * 2) ,
            "vlen" : DEMO_3_POINT_VLEN ,
            "hpos" : (DEMO_3_POINT_HOFFSET * 4) ,
            "hlen" : DEMO_3_POINT_HLEN ,
            "padding" : 5 ,
            "lampcolors" :
                [
                {
                "name" : "on" ,
                "lampcolorrgb" : (128, 0, 128) ,
                "textcolorname" : "BLACK" ,
                "text" : "E"
                } ,
                {
                "name" : "off" ,
                "lampcolorrgb" : DEMO_3_POINT_OFF ,
                "textcolorname" : "WHITE" ,
                "text" : "E"
                }
                ]
            } ,
            {
            "type" : "lamp" ,
            "area_id" : "compass_sw" ,
            "vpos" : (DEMO_3_POINT_VOFFSET * 3) ,
            "vlen" : DEMO_3_POINT_VLEN ,
            "hpos" : (DEMO_3_POINT_HOFFSET * 1) ,
            "hlen" : DEMO_3_POINT_HLEN ,
            "padding" : 5 ,
            "lampcolors" :
                [
                {
                "name" : "on" ,
                "lampcolorrgb" : (204, 0, 51) ,
                "textcolorname" : "BLACK" ,
                "text" : "SW"
                } ,
                {
                "name" : "off" ,
                "lampcolorrgb" : DEMO_3_POINT_OFF ,
                "textcolorname" : "WHITE" ,
                "text" : "SW"
                }
                ]
            } ,
            {
            "type" : "lamp" ,
            "area_id" : "compass_se" ,
            "vpos" : (DEMO_3_POINT_VOFFSET * 3) ,
            "vlen" : DEMO_3_POINT_VLEN ,
            "hpos" : (DEMO_3_POINT_HOFFSET * 3) ,
            "hlen" : DEMO_3_POINT_HLEN ,
            "padding" : 5 ,
            "lampcolors" :
                [
                {
                "name" : "on" ,
                "lampcolorrgb" : (204, 0, 51) ,
                "textcolorname" : "BLACK" ,
                "text" : "SE"
                } ,
                {
                "name" : "off" ,
                "lampcolorrgb" : DEMO_3_POINT_OFF ,
                "textcolorname" : "WHITE" ,
                "text" : "SE"
                }
                ]
            } ,
            {
            "type" : "lamp" ,
            "area_id" : "compass_s" ,
            "vpos" : (DEMO_3_POINT_VOFFSET * 4) ,
            "vlen" : DEMO_3_POINT_VLEN ,
            "hpos" : (DEMO_3_POINT_HOFFSET * 2) ,
            "hlen" : DEMO_3_POINT_HLEN ,
            "padding" : 5 ,
            "lampcolors" :
                [
                {
                "name" : "on" ,
                "lampcolorrgb" : (255, 0, 0) ,
                "textcolorname" : "BLACK" ,
                "text" : "S"
                } ,
                {
                "name" : "off" ,
                "lampcolorrgb" : DEMO_3_POINT_OFF ,
                "textcolorname" : "WHITE" ,
                "text" : "S"
                }
                ]
            }

            ]
        }
        ]
    }

DEMO_4_TRIG_BACKGROUNDCOLORNAME = "BLACK"
DEMO_4_TRIG_VALUECOLORNAME = "WHITE"
DEMO_4_TRIG_RANGEMIN = -1.0
DEMO_4_TRIG_RANGEMAX = 1.0
demo_4_display = {
    "vpos" : DISPLAY_VPOS ,
    "vlen" : DISPLAY_VLEN ,
    "hpos" : DISPLAY_HPOS ,
    "hlen" : DISPLAY_HLEN ,
    "borderwidth" : DISPLAY_BORDERWIDTH ,
    "bordercolorname" : DISPLAY_BORDERCOLORNAME ,
    "paddingwidth" : DISPLAY_PADDINGWIDTH ,
    "backgroundcolorname" : DISPLAY_BACKGROUNDCOLORNAME ,
    "areas" : [
        {
        "type" : HEADING_TYPE ,
        "scale" : HEADING_SCALE ,
        "textcolorname" : HEADING_TEXTCOLORNAME ,
        "vpos" : HEADING_VPOS ,
        "vlen" : HEADING_VLEN ,
        "hpos" : HEADING_HPOS ,
        "hlen" : HEADING_HLEN ,
        "borderwidth" : HEADING_BORDERWIDTH ,
        "bordercolorname" : HEADING_BORDERCOLORNAME ,
        "paddingwidth" : HEADING_PADDINGWIDTH ,
        "backgroundcolorname" : HEADING_BACKGROUNDCOLORNAME ,
        "text" : " DEMO 4 - Linear Gauge"
        } ,
        {
        "type" : "container" ,
        "vpos" : 23 ,
        "vlen" : 206 ,
        "hpos" : 0 ,
        "hlen" : 80 ,
        "paddingwidth" : 2 ,
        "backgroundcolorname" : "YELLOW" ,
        "areas" : [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos" : 0 ,
            "vlen" : 18 ,
            "hpos" : 0 ,
            "hlen" : 76 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : "RED" ,
            "text" : "  250F"
            } ,
            {
            "type" : "sysfont" ,
            "area_id" : "Ftext" ,
            "scale" : 3 ,
            "vertical" : True ,
            "vpos" : 18 ,
            "vlen" : 166 ,
            "hpos" : 6 ,
            "hlen" : 24 ,
            "paddingwidth" : 4 ,
            "backgroundcolorname" : "GREEN" ,
            "text" : " 000F"
            } ,
            {
            "type" : "lineargauge" ,
            "area_id" : "Fdisplay" ,
            "verticalgauge" : True ,
            "rangemin" : -50 ,
            "rangemax" : 250 ,
            "valuecolorname" : "BLUE" ,
            "vpos" : 18 ,
            "vlen" : 166 ,
            "hpos" : 37 ,
            "hlen" : 34 ,
            "paddingwidth" : 0 ,
            "backgroundcolorname" : "RED" ,
            "value" : 98.6
            } ,
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos" : 184 ,
            "vlen" : 18 ,
            "hpos" : 0 ,
            "hlen" : 76 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : "BLUE" ,
            "text" : "  -50F"
            }
            ]
        } ,
        {
        "type" : "container" ,
        "vpos" : 23 ,
        "vlen" : 206 ,
        "hpos" : 82 ,
        "hlen" : 80 ,
        "paddingwidth" : 2 ,
        "backgroundcolorname" : "YELLOW" ,
        "areas" : [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos" : 0 ,
            "vlen" : 18 ,
            "hpos" : 0 ,
            "hlen" : 76 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : "RED" ,
            "text" : "  180C"
            } ,
            {
            "type" : "sysfont" ,
            "area_id" : "Ctext" ,
            "scale" : 3 ,
            "vertical" : True ,
            "vpos" : 18 ,
            "vlen" : 166 ,
            "hpos" : 6 ,
            "hlen" : 24 ,
            "paddingwidth" : 4 ,
            "backgroundcolorname" : "GREEN" ,
            "text" : " 000C"
            } ,
            {
            "type" : "lineargauge" ,
            "area_id" : "Cdisplay" ,
            "verticalgauge" : True ,
            "rangemin" : -50 ,
            "rangemax" : 180 ,
            "valuecolorname" : "BLUE" ,
            "vpos" : 18 ,
            "vlen" : 166 ,
            "hpos" : 37 ,
            "hlen" : 34 ,
            "paddingwidth" : 0 ,
            "backgroundcolorname" : "RED" ,
            "value" : 98.6
            } ,
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos" : 184 ,
            "vlen" : 18 ,
            "hpos" : 0 ,
            "hlen" : 76 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : "BLUE" ,
            "text" : "  -50C"
            }
            ]
        } ,
        {
        "type" : "container" ,
        "vpos" : 23 ,
        "vlen" : 206 ,
        "hpos" : 164 ,
        "hlen" : 80 ,
        "paddingwidth" : 2 ,
        "backgroundcolorname" : "YELLOW" ,
        "areas" : [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos" : 0 ,
            "vlen" : 18 ,
            "hpos" : 0 ,
            "hlen" : 76 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : "RED" ,
            "text" : "  500K"
            } ,
            {
            "type" : "sysfont" ,
            "area_id" : "Ktext" ,
            "scale" : 3 ,
            "vertical" : True ,
            "vpos" : 18 ,
            "vlen" : 166 ,
            "hpos" : 6 ,
            "hlen" : 24 ,
            "paddingwidth" : 4 ,
            "backgroundcolorname" : "GREEN" ,
            "text" : " 000K"
            } ,
            {
            "type" : "lineargauge" ,
            "area_id" : "Kdisplay" ,
            "verticalgauge" : True ,
            "rangemin" : 200 ,
            "rangemax" : 500 ,
            "valuecolorname" : "BLUE" ,
            "vpos" : 18 ,
            "vlen" : 166 ,
            "hpos" : 37 ,
            "hlen" : 34 ,
            "paddingwidth" : 0 ,
            "backgroundcolorname" : "RED" ,
            "value" : 98.6
            } ,
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos" : 184 ,
            "vlen" : 18 ,
            "hpos" : 0 ,
            "hlen" : 76 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : "BLUE" ,
            "text" : "  200K"
            }
            ]
        } ,
        {
        "type" : "container" ,
        "vpos" : 23 ,
        "vlen" : 206 ,
        "hpos" : 245 ,
        "hlen" : 63 ,
        "paddingwidth" : 1 ,
        "backgroundcolorname" : "YELLOW" ,
        "areas" : [
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_0" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 3 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_1" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 13 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_2" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 23 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_3" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 33 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_4" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 43 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_5" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 53 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_6" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 63 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_7" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 73 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_8" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 83 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_9" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 93 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_10" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 103 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_11" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 113 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_12" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 123 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_13" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 133 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_14" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 143 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_15" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 153 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_16" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 163 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_17" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 173 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_18" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 183 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  } ,
                  {
                  "type" : "lineargauge" ,
                  "area_id" : "trig_19" ,
                  "verticalgauge" : False ,
                  "rangemin" : DEMO_4_TRIG_RANGEMIN ,
                  "rangemax" : DEMO_4_TRIG_RANGEMAX ,
                  "valuecolorname" : DEMO_4_TRIG_VALUECOLORNAME ,
                  "vpos" : 193 ,
                  "vlen" : 10 ,
                  "hpos" : 0 ,
                  "hlen" : 61 ,
                  "paddingwidth" : 0 ,
                  "backgroundcolorname" : DEMO_4_TRIG_BACKGROUNDCOLORNAME ,
                  "value" : 0.0
                  }
                  ]
        }
        ]
    }

demo_5_display = {
    "vpos" : DISPLAY_VPOS ,
    "vlen" : DISPLAY_VLEN ,
    "hpos" : DISPLAY_HPOS ,
    "hlen" : DISPLAY_HLEN ,
    "borderwidth" : DISPLAY_BORDERWIDTH ,
    "bordercolorname" : DISPLAY_BORDERCOLORNAME ,
    "paddingwidth" : DISPLAY_PADDINGWIDTH ,
    "backgroundcolorname" : DISPLAY_BACKGROUNDCOLORNAME ,
    "areas" : [
        {
        "type" : HEADING_TYPE ,
        "scale" : HEADING_SCALE ,
        "textcolorname" : HEADING_TEXTCOLORNAME ,
        "vpos" : HEADING_VPOS ,
        "vlen" : HEADING_VLEN ,
        "hpos" : HEADING_HPOS ,
        "hlen" : HEADING_HLEN ,
        "borderwidth" : HEADING_BORDERWIDTH ,
        "bordercolorname" : HEADING_BORDERCOLORNAME ,
        "paddingwidth" : HEADING_PADDINGWIDTH ,
        "backgroundcolorname" : HEADING_BACKGROUNDCOLORNAME ,
        "text" : " DEMO 5 - Images"
        } ,
        {
        "type" : "container" ,
        "vpos" : 24 ,
        "vlen" : 100 ,
        "hpos" : 25 ,
        "hlen" : 260 ,
        "backgroundcolorname" : "yellow" ,
        "areas" : [
            {
            "type" : "image" ,
            "image_id" : "me" ,
            "vpos" : 6 ,
            "vlen" : 0 ,
            "hpos" : 30 ,
            "hlen" : 0
            } ,
            {
            "type" : "image" ,
            "image_id" : "mecold" ,
            "vpos" : 12 ,
            "vlen" : 0 ,
            "hpos" : 150 ,
            "hlen" : 0
            }
            ]
        } ,
        {
        "type" : "container" ,
        "vpos" : 126 ,
        "vlen" : 100 ,
        "hpos" : 120 ,
        "hlen" : 80  ,
        "backgroundcolorname" : "green" ,
        "areas" : [
            {
            "type" : "image" ,
            "image_id" : "heart" ,
            "vpos" : 10 ,
            "vlen" : 0 ,
            "hpos" : 12 ,
            "hlen" : 0
            }
            ]
        }
        ]
    }

demo_6_display = {
    "vpos" : DISPLAY_VPOS ,
    "vlen" : DISPLAY_VLEN ,
    "hpos" : DISPLAY_HPOS ,
    "hlen" : DISPLAY_HLEN ,
    "borderwidth" : DISPLAY_BORDERWIDTH ,
    "bordercolorname" : DISPLAY_BORDERCOLORNAME ,
    "paddingwidth" : DISPLAY_PADDINGWIDTH ,
    "backgroundcolorname" : DISPLAY_BACKGROUNDCOLORNAME ,
    "areas" : [
        {
        "type" : HEADING_TYPE ,
        "scale" : HEADING_SCALE ,
        "textcolorname" : HEADING_TEXTCOLORNAME ,
        "vpos" : HEADING_VPOS ,
        "vlen" : HEADING_VLEN ,
        "hpos" : HEADING_HPOS ,
        "hlen" : HEADING_HLEN ,
        "borderwidth" : HEADING_BORDERWIDTH ,
        "bordercolorname" : HEADING_BORDERCOLORNAME ,
        "paddingwidth" : HEADING_PADDINGWIDTH ,
        "backgroundcolorname" : HEADING_BACKGROUNDCOLORNAME ,
        "text" : " DEMO 6 - Date / Time"
        } ,
        {
        "vpos": 24 ,
        "vlen": 22 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 0 ,
            "hlen": 150 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATALABEL_TEXTCOLORNAME ,
            "text" : "Typ 'd'"
            } ,
            {
            "area_id" : "date_1" ,
            "type" : "datetime" ,
            "formattype" : "d" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 151 ,
            "hlen": 155 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATA_TEXTCOLORNAME ,
            "text" : "YYYY-MM-DD"
            }
            ]
        } ,
        {
        "vpos": 46 ,
        "vlen": 22 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 0 ,
            "hlen": 150 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATALABEL_TEXTCOLORNAME ,
            "text" : "Typ 't'"
            } ,
            {
            "area_id" : "date_2" ,
            "type" : "datetime" ,
            "formattype" : "t" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 151 ,
            "hlen": 155 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATA_TEXTCOLORNAME ,
            "text" : "YYYY-MM-DD"
            }
            ]
        } ,
        {
        "vpos": 68 ,
        "vlen": 22 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 0 ,
            "hlen": 110 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATALABEL_TEXTCOLORNAME ,
            "text" : "Typ 'dt'"
            } ,
            {
            "area_id" : "date_3" ,
            "type" : "datetime" ,
            "formattype" : "dt" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 111 ,
            "hlen": 195 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATA_TEXTCOLORNAME
            }
            ]
        } ,
        {
        "vpos": 90 ,
        "vlen": 22 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 0 ,
            "hlen": 110 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATALABEL_TEXTCOLORNAME ,
            "text" : "Typ 'ts'"
            } ,
            {
            "area_id" : "date_4" ,
            "type" : "datetime" ,
            "formattype" : "ts" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 111 ,
            "hlen": 195 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATA_TEXTCOLORNAME
            }
            ]
        } ,
        {
        "vpos": 112 ,
        "vlen": 22 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 0 ,
            "hlen": 150 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATALABEL_TEXTCOLORNAME ,
            "text" : "%m/%d/%Y"
            } ,
            {
            "area_id" : "date_5" ,
            "type" : "datetime" ,
            "formatstr" : "%m/%d/%Y" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 151 ,
            "hlen": 155 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATA_TEXTCOLORNAME
            }
            ]
        } ,
        {
        "vpos": 134 ,
        "vlen": 22 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 0 ,
            "hlen": 150 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATALABEL_TEXTCOLORNAME ,
            "text" : "%H:%M:%S"
            } ,
            {
            "area_id" : "date_6" ,
            "type" : "datetime" ,
            "formatstr" : "%H:%M:%S" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 151 ,
            "hlen": 155 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATA_TEXTCOLORNAME
            }
            ]
        } ,
        {
        "vpos": 156 ,
        "vlen": 22 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 0 ,
            "hlen": 150 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATALABEL_TEXTCOLORNAME ,
            "text" : "Seconds %S"
            } ,
            {
            "area_id" : "date_7" ,
            "type" : "datetime" ,
            "formatstr" : "Seconds %S" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 151 ,
            "hlen": 155 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATA_TEXTCOLORNAME
            }
            ]
        } ,
        {
        "vpos": 178 ,
        "vlen": 22 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 0 ,
            "hlen": 150 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATALABEL_TEXTCOLORNAME ,
            "text" : "Da:%d Hr:%H"
            } ,
            {
            "area_id" : "date_8" ,
            "type" : "datetime" ,
            "formatstr" : "Da:%d Hr:%H" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 151 ,
            "hlen": 155 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATA_TEXTCOLORNAME ,
            "text" : "Not Active"
            }
            ]
        } ,
        {
        "vpos": 200 ,
        "vlen": 22 ,
        "hpos": 0 ,
        "hlen": 308 ,
        "backgroundcolorname" : "YELLOW" ,
        "paddingwidth" : 1 ,
        "areas" :
            [
            {
            "type" : "sysfont" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 0 ,
            "hlen": 150 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATALABEL_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATALABEL_TEXTCOLORNAME ,
            "text" : "Da:%d Hr:%H"
            } ,
            {
            "area_id" : "date_9" ,
            "type" : "datetime" ,
            "formattype" : "d" ,
            "scale" : 2 ,
            "vpos": 0 ,
            "vlen": 20 ,
            "hpos": 151 ,
            "hlen": 155 ,
            "paddingwidth" : 2 ,
            "backgroundcolorname" : DATA_BACKGROUNDCOLORNAME ,
            "textcolorname" : DATA_TEXTCOLORNAME ,
            "text" : "Not Active"
            }
            ]
        }
        ]
    }

demo_7_display = {
    "vpos" : DISPLAY_VPOS ,
    "vlen" : DISPLAY_VLEN ,
    "hpos" : DISPLAY_HPOS ,
    "hlen" : DISPLAY_HLEN ,
    "borderwidth" : DISPLAY_BORDERWIDTH ,
    "bordercolorname" : DISPLAY_BORDERCOLORNAME ,
    "paddingwidth" : DISPLAY_PADDINGWIDTH ,
    "backgroundcolorname" : DISPLAY_BACKGROUNDCOLORNAME ,
    "areas" : [
        {
        "type" : HEADING_TYPE ,
        "scale" : HEADING_SCALE ,
        "textcolorname" : HEADING_TEXTCOLORNAME ,
        "vpos" : HEADING_VPOS ,
        "vlen" : HEADING_VLEN ,
        "hpos" : HEADING_HPOS ,
        "hlen" : HEADING_HLEN ,
        "borderwidth" : HEADING_BORDERWIDTH ,
        "bordercolorname" : HEADING_BORDERCOLORNAME ,
        "paddingwidth" : HEADING_PADDINGWIDTH ,
        "backgroundcolorname" : HEADING_BACKGROUNDCOLORNAME ,
        "text" : " DEMO 7 - Open"
        }
        ]
    }

demo_8_display = {
    "vpos" : DISPLAY_VPOS ,
    "vlen" : DISPLAY_VLEN ,
    "hpos" : DISPLAY_HPOS ,
    "hlen" : DISPLAY_HLEN ,
    "borderwidth" : DISPLAY_BORDERWIDTH ,
    "bordercolorname" : DISPLAY_BORDERCOLORNAME ,
    "paddingwidth" : DISPLAY_PADDINGWIDTH ,
    "backgroundcolorname" : DISPLAY_BACKGROUNDCOLORNAME ,
    "areas" : [
        {
        "type" : HEADING_TYPE ,
        "scale" : HEADING_SCALE ,
        "textcolorname" : HEADING_TEXTCOLORNAME ,
        "vpos" : HEADING_VPOS ,
        "vlen" : HEADING_VLEN ,
        "hpos" : HEADING_HPOS ,
        "hlen" : HEADING_HLEN ,
        "borderwidth" : HEADING_BORDERWIDTH ,
        "bordercolorname" : HEADING_BORDERCOLORNAME ,
        "paddingwidth" : HEADING_PADDINGWIDTH ,
        "backgroundcolorname" : HEADING_BACKGROUNDCOLORNAME ,
        "text" : " DEMO 8 - Open"
        }
        ]
    }

demo_9_display = {
    "vpos" : DISPLAY_VPOS ,
    "vlen" : DISPLAY_VLEN ,
    "hpos" : DISPLAY_HPOS ,
    "hlen" : DISPLAY_HLEN ,
    "borderwidth" : DISPLAY_BORDERWIDTH ,
    "bordercolorname" : DISPLAY_BORDERCOLORNAME ,
    "paddingwidth" : DISPLAY_PADDINGWIDTH ,
    "backgroundcolorname" : DISPLAY_BACKGROUNDCOLORNAME ,
    "areas" : [
        {
        "type" : HEADING_TYPE ,
        "scale" : HEADING_SCALE ,
        "textcolorname" : HEADING_TEXTCOLORNAME ,
        "vpos" : HEADING_VPOS ,
        "vlen" : HEADING_VLEN ,
        "hpos" : HEADING_HPOS ,
        "hlen" : HEADING_HLEN ,
        "borderwidth" : HEADING_BORDERWIDTH ,
        "bordercolorname" : HEADING_BORDERCOLORNAME ,
        "paddingwidth" : HEADING_PADDINGWIDTH ,
        "backgroundcolorname" : HEADING_BACKGROUNDCOLORNAME ,
        "text" : " DEMO 9 - Open"
        }
        ]
    }

if __name__ == "__main__" :
    import json
    print ("Building JSON display configuration:" ,
           JSON_FILE_NAME)
    json_dict = {
        "demo_1_display" : demo_1_display ,
        "demo_2_display" : demo_2_display ,
        "demo_3_display" : demo_3_display ,
        "demo_4_display" : demo_4_display ,
        "demo_5_display" : demo_5_display ,
        "demo_6_display" : demo_6_display ,
        "demo_7_display" : demo_7_display ,
        "demo_8_display" : demo_8_display ,
        "demo_9_display" : demo_9_display
    }
    with open (JSON_FILE_NAME, "w") as json_fp :
        json.dump (json_dict ,
                    json_fp ,
                    ensure_ascii = True ,
                    check_circular = True ,
                    indent = JSON_FILE_INDENT)

## end __MAIN__ #
