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
WEATHER_SCREEN = {
    "page_id" : "weather" ,
    "area_id": "weatherscreen" ,
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
M_LINE_VPOS = 0
M_LINE_VPOS_INC = 21
M_LINE_VLEN = 20
M_LINE_HPOS = 2
M_LINE_HLEN = 311
M_LINE_BG_RGB = (0, 0, 0)
M_LINE_TEXT_RGB = (255, 255, 255)
M_LINE = {
    "type" : "sysfont" ,
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
m_vpos = M_LINE_VPOS
M_LINE_IDS = ["m_line1", "m_line2", "m_line3", "m_line4", "m_line5"]
m_lines = []
for area_id in M_LINE_IDS :
    m_line = M_LINE.copy ()
    m_line["area_id"] = area_id
    m_line["vpos"] = m_vpos
    MESSAGE_SCREEN["areas"].append (m_line)
    m_lines.append ("")
    m_vpos += M_LINE_VLEN   # + 1

INFORMATION_SCREEN = {
    "page_id" : "information" ,
    "area_id": "informationscreen" ,
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

'''
SCROLL_VPOS = 0
SCROLL_VPOS_INC = 21
SCROLL_VLEN = 20
SCROLL_HPOS = 0
SCROLL_HLEN = 288
SCROLL_LINE = {
    "type" : "sysfont" ,
    "area_id" : None ,
    "vpos" : None ,
    "vlen" : 20 ,
    "hpos" : 0 ,
    "hlen" : 302 ,
    "paddingwidth" : 2 ,
    "text" : "" ,
    "backgroundcolorrgb" : (204, 255, 102) ,
    "textcolorname" : "BLACK"
    }

vpos = SCROLL_VPOS
SCROLL_AREA_IDS = ["line1", "line2", "line3", "line4", "line5"]
scroll_text = []
for area_id in SCROLL_AREA_IDS :
    scroll_line = SCROLL_LINE.copy ()
    scroll_line["area_id"] = area_id
    scroll_line["vpos"] = vpos
    DEMO_SCREEN["areas"][2]["areas"].append (scroll_line)
    scroll_text.append (scroll_line["text"])
    vpos += SCROLL_VPOS_INC
'''

if __name__ == "__main__" :
    import json
    print ("Building JSON clock display configuration:" ,
           JSON_FILE_NAME)
    json_dict = {
        "CLOCK_SCREEN" : CLOCK_SCREEN ,
        "WEATHER_SCREEN" : WEATHER_SCREEN ,
        "MESSAGE_SCREEN" : MESSAGE_SCREEN ,
        "INFORMATION_SCREEN" : INFORMATION_SCREEN
    }
    with open (JSON_FILE_NAME, "w") as json_fp :
        json.dump (json_dict ,
                    json_fp)
                    #ensure_ascii = True ,
                    #check_circular = True ,
                    #indent = JSON_FILE_INDENT)

## end __MAIN__ #

