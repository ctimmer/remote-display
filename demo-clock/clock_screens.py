#

JSON_FILE_NAME = "clock_screens.json"
JSON_FILE_INDENT = 2 # 1-8 for pretty print / None for minimize

#----------------------------------
# CLOCK_SCREEN
#----------------------------------
C_TIME_BG_RGB = (255, 255, 255)
C_TIME_TEXT_RGB = (128, 0, 0)

C_WEATHER_BG_RGB = (204, 153, 255)
C_WEATHER_HEADING_BG_RGB = (77, 0, 153)
C_WEATHER_HEADING_TEXT_RGB = (230, 204, 255)
C_WEATHER_LABEL_BG_RGB = (255, 0, 0)
C_WEATHER_LABEL_TEXT_RGB = (255, 230, 230)
C_WEATHER_DATA_BG_RGB = (128, 0, 0)
C_WEATHER_DATA_TEXT_RGB = (255, 153, 153)
STATUS_BG_RGB = (255, 204, 0)
STATUS_TEXT_RGB = (0, 0, 0)

CLOCK_SCREEN = {
    "page_id" : "clock" ,
    "area_id": "clockscreen" ,
    "vpos": 0 ,
    "vlen": 240 ,
    "hpos": 0 ,
    "hlen": 320 ,
    "borderwidth" : 2 ,
    "bordercolorname" : "WHITE" ,
    #"paddingwidth" : 2 ,
    "backgroundcolorname" : "BLACK" ,
    "areas" : [
            {
            "type" : "datetime" ,
            "area_id" : "c_time" ,
            "vpos" : 8 ,
            "vlen" : 74 ,
            "hpos" : 12 ,
            "hlen" : 294 ,
            "paddingwidth" : 2 ,
            #"digit_size" : "l" ,
            #"bold" : True ,
            "scale" : 10 ,
            "formattype" : "t" ,
            "text" : "88:88" ,
            "backgroundcolorrgb" : C_TIME_BG_RGB ,
            "textcolorrgb" : C_TIME_TEXT_RGB
            } ,
            {
            "type" : "container" ,
            "area_id" : "c_weather" ,
            "vpos" : 92 ,
            "vlen" : 111 ,
            "hpos" : 2 ,
            "hlen" : 311 ,
            "paddingwidth" : 2 ,
            "backgroundcolorrgb" : C_WEATHER_BG_RGB ,
            "areas" : [
                {
                "type" : "sysfont" ,
                "area_id" : "c_heading" ,
                "vpos" : 0 ,
                "vlen" : 26 ,
                "hpos" : 8 ,
                "hlen" : 128 ,
                "paddingwidth" : 1 ,
                "scale" : 3 ,
                "text" : "Weather" ,
                "backgroundcolorrgb" : C_WEATHER_HEADING_BG_RGB ,
                "textcolorrgb" : C_WEATHER_HEADING_TEXT_RGB
                } ,
                {
                "type" : "sysfont" ,
                "area_id" : "c_temp_heading" ,
                "vpos" : 27 ,
                "vlen" : 26 ,
                "hpos" : 56 ,
                "hlen" : 90 ,
                "paddingwidth" : 1 ,
                "scale" : 3 ,
                "text" : "Temp:" ,
                "backgroundcolorrgb" : C_WEATHER_LABEL_BG_RGB ,
                "textcolorrgb" : C_WEATHER_LABEL_TEXT_RGB
                } ,
                {
                "type" : "sysfont" ,
                "area_id" : "c_temperature" ,
                "vpos" : 3 ,
                "vlen" : 50 ,
                "hpos" : 150 ,
                "hlen" : 150 ,
                "paddingwidth" : 4 ,
                "scale" : 6 ,
                "text" : "----" ,
                "backgroundcolorrgb" : C_WEATHER_DATA_BG_RGB ,
                "textcolorrgb" : C_WEATHER_DATA_TEXT_RGB
                } ,
                {
                "type" : "sysfont" ,
                "area_id" : "c_wind_heading" ,
                "vpos" : 54 ,
                "vlen" : 26 ,
                "hpos" : 56 ,
                "hlen" : 90 ,
                "paddingwidth" : 1 ,
                "scale" : 3 ,
                "text" : "Wind:" ,
                "backgroundcolorrgb" : C_WEATHER_LABEL_BG_RGB ,
                "textcolorrgb" : C_WEATHER_LABEL_TEXT_RGB
                } ,
                {
                "type" : "sysfont" ,
                "area_id" : "c_wind" ,
                "vpos" : 54 ,
                "vlen" : 26 ,
                "hpos" : 150 ,
                "hlen" : 132 ,
                "paddingwidth" : 1 ,
                "scale" : 3 ,
                "text" : "-------" ,
                "backgroundcolorrgb" : C_WEATHER_DATA_BG_RGB ,
                "textcolorrgb" : C_WEATHER_DATA_TEXT_RGB
                } ,
                {
                "type" : "sysfont" ,
                "area_id" : "c_pressure_heading" ,
                "vpos" : 81 ,
                "vlen" : 26 ,
                "hpos" : 56 ,
                "hlen" : 90 ,
                "paddingwidth" : 1 ,
                "scale" : 3 ,
                "text" : "Pres:" ,
                "backgroundcolorrgb" : C_WEATHER_LABEL_BG_RGB ,
                "textcolorrgb" : C_WEATHER_LABEL_TEXT_RGB
                } ,
                {
                "type" : "sysfont" ,
                "area_id" : "c_pressure" ,
                "vpos" : 81 ,
                "vlen" : 26 ,
                "hpos" : 150 ,
                "hlen" : 132 ,
                "paddingwidth" : 1 ,
                "scale" : 3 ,
                "text" : "-----" ,
                "backgroundcolorrgb" : C_WEATHER_DATA_BG_RGB ,
                "textcolorrgb" : C_WEATHER_DATA_TEXT_RGB
                }
                ]
            } ,
            {
            "type" : "sysfont" ,
            "area_id" : "status" ,
            "vpos" : 211 ,
            "vlen" : 20 ,
            "hpos" : 2 ,
            "hlen" : 311 ,
            "paddingwidth" : 2 ,
            "scale" : 2 ,
            "text" : "Have a nice day" ,
            "backgroundcolorrgb" : STATUS_BG_RGB ,
            "textcolorrgb" : STATUS_TEXT_RGB
            }
        ]
    }

'''
            {
            "type" : "container" ,
            "area_id" : "scroll" ,
            "vpos": 54 ,
            "vlen": 106  ,
            "hpos": 2 ,
            "hlen": 304 ,
            "paddingwidth" : 1 ,
            "backgroundcolorname" : "BLACK" ,
            "areas" : [
                ]
            } ,
            {
            "type" : "7seg" ,
            "area_id" : "7seg_output" ,
            "digit_size" : "l" ,
            "bold" : True ,
            "vpos" : 164 ,
            "vlen" : 62 ,
            "hpos" : 54 ,
            "hlen" : 200 ,
            "paddingwidth" : 2 ,
            "text" : "12:34" ,
            "backgroundcolorname" : "CYAN" ,
            "textcolorname" : "BLACK"
            }
'''
W_BG_RGB = (0, 0, 0)
W_BORDER_RGB = (0, 0, 0)
W_BORDER_WIDTH = 1
W_BORDER_RGB = (255, 255, 255)

WEATHER_SCREEN = {
    "page_id" : "weather" ,
    "area_id": "weatherscreen" ,
    "vpos": 0 ,
    "vlen": 240 ,
    "hpos": 0 ,
    "hlen": 320 ,
    "borderwidth" : W_BORDER_WIDTH ,
    "bordercolorrgb" : W_BORDER_RGB ,
    #"paddingwidth" : 2 ,
    "backgroundcolorrgb" : W_BG_RGB ,
    "areas" : [
        ]
    }

W_DAY_BG_RGB = (255, 242, 204)
W_DAY_BORDER_WIDTH = 1
W_DAY_BORDER_RGB = (0, 102, 255)
W_DAY_VLEN = 45

def get_wfc_day_area () :
#WFC_DAY_AREA = {
    return {
        "vpos": None ,
        "vlen": W_DAY_VLEN ,
        "hpos": 2 ,
        "hlen": 312 ,
        "borderwidth" : W_DAY_BORDER_WIDTH ,
        "bordercolorrgb" : W_DAY_BORDER_RGB ,
        #"paddingwidth" : 2 ,
        "backgroundcolorrgb" : W_DAY_BG_RGB ,
        "areas" : []
        }

## Daily weather forcasts
WFC_DOW_BG_RGB = (153, 31, 0)
WFC_DOW_RGB = (255, 214, 204)
WFC_LABEL_BG_RGB = (255, 242, 204)
WFC_LABEL_RGB = (102, 77, 0)
WFC_TEXT_BG_RGB = (102, 77, 0)
WFC_TEXT_RGB = (255, 242, 204)
WFC_FIRST_LINE_VPOS = 1
WFC_SECOND_LINE_VPOS = (WFC_FIRST_LINE_VPOS + 21)

def get_wfc_dow () :
    return {
        "type" : "sysfont" ,
        "area_id" : None ,
        "vpos": (WFC_FIRST_LINE_VPOS + 2) ,
        "vlen": 34 ,
        "hpos": 0 ,
        "hlen": 50 ,
        "scale" : 4 ,
        #"borderwidth" : W_DAY_BORDER_WIDTH ,
        #"bordercolorrgb" : W_DAY_BORDER_RGB ,
        "paddingwidth" : 2 ,
        "backgroundcolorrgb" : WFC_DOW_BG_RGB ,
        "textcolorrgb" : WFC_DOW_RGB ,
        "text" : "Xx"
        }
def get_wfc_temp_label () :
    return {
        "type" : "sysfont" ,
        "vpos": WFC_FIRST_LINE_VPOS ,
        "vlen": 20 ,
        "hpos": 52 ,
        "hlen": 50 ,
        "scale" : 2 ,
        "paddingwidth" : 2 ,
        "backgroundcolorrgb" : WFC_LABEL_BG_RGB ,
        "textcolorrgb" : WFC_LABEL_RGB ,
        "text" : "Temp"
        }
def get_wfc_temp_low_label () :
#WFC_DOW = {
    return {
        "type" : "sysfont" ,
        #"area_id" : None ,
        "vpos": WFC_FIRST_LINE_VPOS ,
        "vlen": 20 ,
        "hpos": 110 ,
        "hlen": 26 ,
        "scale" : 2 ,
        #"borderwidth" : W_DAY_BORDER_WIDTH ,
        #"bordercolorrgb" : W_DAY_BORDER_RGB ,
        "paddingwidth" : 2 ,
        "backgroundcolorrgb" : WFC_LABEL_BG_RGB ,
        "textcolorrgb" : WFC_LABEL_RGB ,
        "text" : "Lo"
        }
def get_wfc_temp_low () :
#WFC_DOW = {
    return {
        "type" : "sysfont" ,
        "area_id" : None ,
        "vpos": WFC_FIRST_LINE_VPOS ,
        "vlen": 20 ,
        "hpos": 140 ,
        "hlen": 50 ,
        "scale" : 2 ,
        #"borderwidth" : W_DAY_BORDER_WIDTH ,
        #"bordercolorrgb" : W_DAY_BORDER_RGB ,
        "paddingwidth" : 2 ,
        "backgroundcolorrgb" : WFC_TEXT_BG_RGB ,
        "textcolorrgb" : WFC_TEXT_RGB ,
        "text" : "----"
        }
def get_wfc_temp_high_label () :
    return {
        "type" : "sysfont" ,
        "vpos": WFC_FIRST_LINE_VPOS ,
        "vlen": 20 ,
        "hpos": 200 ,
        "hlen": 26 ,
        "scale" : 2 ,
        "paddingwidth" : 2 ,
        "backgroundcolorrgb" : WFC_LABEL_BG_RGB ,
        "textcolorrgb" : WFC_LABEL_RGB ,
        "text" : "Hi"
        }
def get_wfc_temp_high () :
    return {
        "type" : "sysfont" ,
        "area_id" : None ,
        "vpos": WFC_FIRST_LINE_VPOS ,
        "vlen": 20 ,
        "hpos": 230 ,
        "hlen": 50 ,
        "scale" : 2 ,
        #"borderwidth" : W_DAY_BORDER_WIDTH ,
        #"bordercolorrgb" : W_DAY_BORDER_RGB ,
        "paddingwidth" : 2 ,
        "backgroundcolorrgb" : WFC_TEXT_BG_RGB ,
        "textcolorrgb" : WFC_TEXT_RGB ,
        "text" : "----"
        }


## Wind / Pressure
def get_wfc_wind_label () :
    return {
        "type" : "sysfont" ,
        #"area_id" : None ,
        "vpos": WFC_SECOND_LINE_VPOS ,
        "vlen": 20 ,
        "hpos": 52 ,
        "hlen": 50 ,
        "scale" : 2 ,
        #"borderwidth" : W_DAY_BORDER_WIDTH ,
        #"bordercolorrgb" : W_DAY_BORDER_RGB ,
        "paddingwidth" : 2 ,
        "backgroundcolorrgb" : WFC_LABEL_BG_RGB ,
        "textcolorrgb" : WFC_LABEL_RGB ,
        "text" : "Wind"
        }
def get_wfc_wind () :
    return {
        "type" : "sysfont" ,
        "area_id" : None ,
        "vpos" : WFC_SECOND_LINE_VPOS ,
        "vlen" : 20 ,
        "hpos" : 104 ,
        "hlen" : 85 ,
        "paddingwidth" : 1 ,
        "scale" : 2 ,
        "text" : "-------" ,
        "backgroundcolorrgb" : WFC_TEXT_BG_RGB ,
        "textcolorrgb" : WFC_TEXT_RGB
        }
def get_wfc_pressure_label () :
    return {
        "type" : "sysfont" ,
        #"area_id" : None ,
        "vpos": WFC_SECOND_LINE_VPOS ,
        "vlen": 20 ,
        "hpos": 194 ,
        "hlen": 50 ,
        "scale" : 2 ,
        #"borderwidth" : W_DAY_BORDER_WIDTH ,
        #"bordercolorrgb" : W_DAY_BORDER_RGB ,
        "paddingwidth" : 2 ,
        "backgroundcolorrgb" : WFC_LABEL_BG_RGB ,
        "textcolorrgb" : WFC_LABEL_RGB ,
        "text" : "Pres"
        }
def get_wfc_pressure () :
    return {
        "type" : "sysfont" ,
        #"area_id" : None ,
        "vpos": WFC_SECOND_LINE_VPOS ,
        "vlen": 20 ,
        "hpos": 246 ,
        "hlen": 62 ,
        "scale" : 2 ,
        #"borderwidth" : W_DAY_BORDER_WIDTH ,
        #"bordercolorrgb" : W_DAY_BORDER_RGB ,
        "paddingwidth" : 2 ,
        "backgroundcolorrgb" : WFC_TEXT_BG_RGB ,
        "textcolorrgb" : WFC_TEXT_RGB ,
        "text" : "-----"
        }

## Build weather configuration
line_vpos = 2
for line_idx in range (0, 5) :
    day_area = get_wfc_day_area ()
    day_area ["area_id"] = "w_" + str (line_idx)
    day_area ["vpos"] = line_vpos
    ## day of week
    dow = get_wfc_dow ()
    dow ["area_id"] = "w_dow_{}".format (line_idx)
    day_area ["areas"].append (dow)
    ## high/low temperatures
    line_area = get_wfc_temp_label ()
    day_area ["areas"].append (line_area)
    line_area = get_wfc_temp_low_label ()        # Low temperature
    day_area ["areas"].append (line_area)
    line_area = get_wfc_temp_low ()
    line_area ["area_id"] = "w_temp_low_" + str (line_idx)
    day_area ["areas"].append (line_area)
    line_area = get_wfc_temp_high_label ()       # High temperature
    day_area ["areas"].append (line_area)
    line_area = get_wfc_temp_high ()
    line_area ["area_id"] = "w_temp_high_" + str (line_idx)
    day_area ["areas"].append (line_area)

    ## Wind / Pressure
    line_area = get_wfc_wind_label ()
    day_area ["areas"].append (line_area)
    line_area = get_wfc_wind ()
    line_area ["area_id"] = "w_wind_direction_" + str (line_idx)
    day_area ["areas"].append (line_area)
    line_area = get_wfc_pressure_label ()
    day_area ["areas"].append (line_area)
    line_area = get_wfc_pressure ()
    line_area ["area_id"] = "w_pressure_" + str (line_idx)
    day_area ["areas"].append (line_area)
    ##
    WEATHER_SCREEN ["areas"].append (day_area)
    line_vpos += (W_DAY_VLEN + 2)

#----------------------------------------------------------------------
M_BG_RGB = (0, 0, 0)
M_BORDER_WIDTH = 1
M_BORDER_RGB = (255, 255, 255)

MESSAGE_SCREEN = {
    "page_id" : "messages" ,
    "area_id": "messagescreen" ,
    "vpos": 0 ,
    "vlen": 240 ,
    "hpos": 0 ,
    "hlen": 320 ,
    "borderwidth" : M_BORDER_WIDTH ,
    "bordercolorrgb" : M_BORDER_RGB ,
    #"paddingwidth" : 2 ,
    "backgroundcolorrgb" : M_BG_RGB ,
    "areas" : [
        ]
    }
M_HEADING_VPOS = 6
M_FIRST_LINE_VPOS = 34
M_UPDATE_AREA_ID = "m_update"
M_HEADING = {
    "type" : "sysfont" ,
    "vpos" : M_HEADING_VPOS ,
    "vlen" : 24 ,
    "hpos" : 8 ,
    "hlen" : 144 ,
    #"paddingwidth" : 2 ,
    "scale" : 3 ,
    "text" : "MESSAGES" ,
    "backgroundcolorrgb" : (0, 0, 255) ,
    "textcolorrgb" : (255, 0, 0)
    }
M_HEADING_UPDATE = {
    "type" : "datetime" ,
    "area_id" : M_UPDATE_AREA_ID ,
    "vpos" : (M_HEADING_VPOS + 5),
    "vlen" : 16 ,
    "hpos" : 160 ,
    "hlen" : 150 ,
    #"paddingwidth" : 2 ,
    "scale" : 2 ,
    "formatstr" : "%m/%d %H:%M" ,
    "text" : "No Messages" ,
    "backgroundcolorrgb" : (0, 0, 255) ,
    "textcolorrgb" : (255, 0, 0)
    }
MESSAGE_SCREEN["areas"].append (M_HEADING)
MESSAGE_SCREEN["areas"].append (M_HEADING_UPDATE)

M_LINE_VPOS_INC = 21
M_LINE_VLEN = 20
M_LINE_HPOS = 2
M_LINE_HLEN = 311
M_LINE_BG_RGB = (0, 0, 0)
M_SCALE = 2
M_LINE_TEXT_RGB = (255, 255, 255)
M_LINE = {
    "type" : "sysfont" ,
    "scale" : M_SCALE ,
    "area_id" : None ,
    "vpos" : None ,
    "vlen" : M_LINE_VLEN ,
    "hpos" : M_LINE_HPOS ,
    "hlen" : M_LINE_HLEN ,
    "paddingwidth" : 2 ,
    "text" : "" ,
    "backgroundcolorrgb" : M_LINE_BG_RGB ,
    "textcolorrgb" : M_LINE_TEXT_RGB
    }


m_vpos = M_FIRST_LINE_VPOS
M_LINE_IDS = [
    "m_line_1", "m_line_2", "m_line_3", "m_line_4", "m_line_5",
    "m_line_6", "m_line_7", "m_line_8", "m_line_9", "m_line_10"
    ]

for area_id in M_LINE_IDS :
    m_line = M_LINE.copy ()
    m_line["area_id"] = area_id
    m_line["vpos"] = m_vpos
    m_line["text"] = ""
    MESSAGE_SCREEN["areas"].append (m_line)
    m_vpos += M_LINE_VLEN   # + 1

MESSAGE_CONFIG = {
    "line_area_ids" : M_LINE_IDS ,          # scroll lines
    "update_area_id" : M_UPDATE_AREA_ID     # last update
    }

#----------------------------------------------------------------
ABOUT_SCREEN = {
    "page_id" : "about" ,
    "area_id": "aboutscreen" ,
    "vpos": 0 ,
    "vlen": 240 ,
    "hpos": 0 ,
    "hlen": 320 ,
    "borderwidth" : 2 ,
    "bordercolorname" : "WHITE" ,
    #"paddingwidth" : 2 ,
    "backgroundcolorname" : "BLACK" ,
    "areas" : [
        ]
    }

A_UPDATE_AREA_ID = "aboutscreen"
A_FIRST_LINE_VPOS = 4
A_LINE_VPOS_INC = 21
A_LINE_VLEN = 12
A_LINE_HPOS = 2
A_LINE_HLEN = 311
A_LINE_BG_RGB = (0, 0, 0)
A_SCALE = 1
A_LINE_TEXT_RGB = (255, 255, 255)
A_LINE = {
    "type" : "sysfont" ,
    "scale" : A_SCALE ,
    "area_id" : None ,
    "vpos" : None ,
    "vlen" : A_LINE_VLEN ,
    "hpos" : A_LINE_HPOS ,
    "hlen" : A_LINE_HLEN ,
    "paddingwidth" : 1 ,
    "text" : "" ,
    "backgroundcolorrgb" : A_LINE_BG_RGB ,
    "textcolorrgb" : A_LINE_TEXT_RGB
    }

a_vpos = A_FIRST_LINE_VPOS
A_LINE_IDS = [
    "a_line_1", "a_line_2", "a_line_3", "a_line_4", "a_line_5" ,
    "a_line_6", "a_line_7", "a_line_8", "a_line_9", "a_line_10" ,
    "a_line_11", "a_line_12", "a_line_13", "a_line_14", "a_line_15" ,
    "a_line_16", "a_line_17", "a_line_18", "a_line_19"
    ]
for area_id in A_LINE_IDS :
    a_line = A_LINE.copy ()
    a_line["area_id"] = area_id
    a_line["vpos"] = a_vpos
    a_line["text"] = area_id   # testing 
    ABOUT_SCREEN["areas"].append (a_line)
    a_vpos += A_LINE_VLEN   # + 1

ABOUT_CONFIG = {
    "line_area_ids" : A_LINE_IDS ,          # scroll lines
    "update_area_id" : A_UPDATE_AREA_ID     # last update
    }

#---------- MAIN ----------------
if __name__ == "__main__" :
    import json
    print ("Building JSON clock display configuration:" ,
           JSON_FILE_NAME)
    json_dict = {
        "CLOCK_SCREEN" : CLOCK_SCREEN ,
        "WEATHER_SCREEN" : WEATHER_SCREEN ,
        "MESSAGE_SCREEN" : MESSAGE_SCREEN ,
        "MESSAGE_CONFIG" : MESSAGE_CONFIG ,
        "ABOuT_SCREEN" : ABOUT_SCREEN ,
        "ABOUT_CONFIG" : ABOUT_CONFIG
        }
    with open (JSON_FILE_NAME, "w") as json_fp :
        json.dump (json_dict ,
                    json_fp)
                    #ensure_ascii = True ,
                    #check_circular = True ,
                    #indent = JSON_FILE_INDENT)

## end __MAIN__ #

