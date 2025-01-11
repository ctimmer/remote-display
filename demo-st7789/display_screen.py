#

JSON_FILE_NAME = "display_screen.json"
JSON_FILE_INDENT = 2 # 1-8 for pretty print / None for minimize

DEMO_SCREEN = {
    "area_id": "demoscreen" ,
    "vpos": 0 ,
    "vlen": 240 ,
    "hpos": 0 ,
    "hlen": 320 ,
    "borderwidth" : 4 ,
    "bordercolorname" : "RED" ,
    "paddingwidth" : 2 ,
    "backgroundcolorname" : "BLUE" ,
    "areas" : [
            {
            "type" : "sysfont" ,
            "vpos" : 2 ,
            "vlen" : 20 ,
            "hpos" : 76 ,
            "hlen" : 156 ,
            "paddingwidth" : 2 ,
            "text" : " st7789 Demo" ,
            "backgroundcolorname" : "WHITE" ,
            "textcolorrgb" : (128, 0, 0)
            } ,
            {
            "type" : "sysfont" ,
            "area_id" : "text_output" ,
            "vpos" : 28 ,
            "vlen" : 20 ,
            "hpos" : 10 ,
            "hlen" : 288 ,
            "paddingwidth" : 2 ,
            "text" : "No Output" ,
            "backgroundcolorname" : "YELLOW" ,
            "textcolorname" : "RED"
            } ,
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
        ]
    }
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

if __name__ == "__main__" :
    import json
    print ("Building JSON display configuration:" ,
           JSON_FILE_NAME)
    json_dict = {
        "DEMO_SCREEN" : DEMO_SCREEN
    }
    with open (JSON_FILE_NAME, "w") as json_fp :
        json.dump (DEMO_SCREEN ,
                    json_fp ,
                    ensure_ascii = True ,
                    check_circular = True ,
                    indent = JSON_FILE_INDENT)

## end __MAIN__ #

