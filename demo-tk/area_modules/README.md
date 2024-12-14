# Demo-tk Area Modules

Areas determine the type of information and location of data to be displayed

## Modules
- remote_area.py
  - This is the base module for the rest of the area modules
- remote_7segment.py
  - DEMO 2
  - Display numbers and some characters in 7 segment format
  - effecient way to pack numbers onto the display
- remote_container.py
  - DEMO (all)
  - Allows grouping of areas
  - The container can be moved on the display without recalculating the embedded areas coordenates
- remote_datetime.py
  - DEMO 6
  - When updated show the current date/time in various formats
- remote_image.py
  - DEMO 5
  - Draws images on the display
- remote_lamp.py
  - DEMO 3
  - Shows state (eg. on/off) via text and background color.
- remote_linear_guage.py
  - DEMO 4
  - Show numeric value level in vertical or horizontal orientation
- remote_linear_guage_ticks.py
  - DEMO none
  - subclass of remote_linear_guage.py
  - Add ticks to guage
- remote_sysfont.py
  - DEMO 1
  - Internal font that can be scaled as needed
- remote_template.py
  - DEMO none
  - This is a do-nothing module that can be used as a starting point for building your own modules
- remote_text.py
  - DEMO 1
  - Font oriented text display

## Simple example

Set up:
```python
# Standard import
from area_modules.remote_sysfont import RemoteSysFont

# The display implementation will vary with display type and size
display = RemoteDisplay (width = DISPLAY_WIDTH ,
                        height = DISPLAY_HEIGHT ,
                        display = demo_canvas)

# Associate "sysfont" with RemoteSysFont module
display.add_area_type ("sysfont", RemoteSysFont)
```

Display configuration snipet

"type":"sysfont" must match "add_area_type" above.
```json
"areas" :
  [
  {
  "type": "sysfont",
  "area_id": "my_id",
  "scale": 2,
  "vpos": 35,
  "vlen": 18,
  "hpos": 0,
  "hlen": 308,
  "paddingwidth": 1,
  "backgroundcolorname": "WHITE",
  "textcolorname": "BLACK",
  "text": "Sysfont Scale: 2"
  }
  ...
  ]
```

To change the area text dislay

```
    display.area_update (area_id="my_id" ,
                        value="New Text")
```

## DEMO 7, 8, 9

These displays show the outline of each area in the display above it. The code for this:

```
    display.screen_clear ()
    display.show_area ()

```