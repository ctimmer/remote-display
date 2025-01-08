#

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
            "vpos" : 0 ,
            "vlen" : 20 ,
            "hpos" : 0 ,
            "hlen" : 160 ,
            "paddingwidth" : 2 ,
            "text" : "Hello World!" ,
            "backgroundcolorname" : "YELLOW" ,
            "textcolorname" : "RED"
            } ,
            {
            "type" : "sysfont" ,
            "area_id" : "text_output" ,
            "vpos" : 40 ,
            "vlen" : 20 ,
            "hpos" : 10 ,
            "hlen" : 288 ,
            "paddingwidth" : 2 ,
            "text" : "No Output" ,
            "backgroundcolorname" : "YELLOW" ,
            "textcolorname" : "RED"
            } ,
            {
            "type" : "7seg" ,
            "area_id" : "7seg_output" ,
            "digit_size" : "l" ,
            "bold" : True ,
            "vpos" : 80 ,
            "vlen" : 62 ,
            "hpos" : 60 ,
            "hlen" : 200 ,
            "paddingwidth" : 2 ,
            "text" : "11:30" ,
            "backgroundcolorname" : "CYAN" ,
            "textcolorname" : "BLACK"
            } ,
            {
            "type" : "sysfont" ,
            "area_id" : "text_end" ,
            "vpos" : 200 ,
            "vlen" : 20 ,
            "hpos" : 30 ,
            "hlen" : 250 ,
            "paddingwidth" : 2 ,
            "text" : "" ,
            "backgroundcolorname" : "YELLOW" ,
            "textcolorname" : "RED"
            } ,
        ]
    }