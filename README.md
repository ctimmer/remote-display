# remote-display
Display server that display data received from 1 or more clients

## **Classes**

### **RemoteDisplay**

**Purpose:**

```mermaid
graph TD;
    A-->B;
    A-->C;
    B-->D;
    C-->D;
```

Configure the fields (areas) for the display

API to update areas (fields) on a display

Example usage:
```python
from machine import Pin, SPI

from ili9341_display import ILI9341Display
from remote_display import RemoteDisplay

spi = SPI (
          SPI_ID,
          baudrate = BAUDRATE ,
          polarity = POLARITY ,
          phase = PHASE ,
          bits = BITS ,
          sck = Pin (SCK) ,
          mosi = Pin (MOSI) ,
          miso = Pin (MISO)
          )
display = Display (spi,
                  width = DISPLAY_WIDTH ,
                  height = DISPLAY_HEIGHT ,
                  rotation = ROTATION ,
                  dc = Pin (DC),
                  cs = Pin (CS) ,
                  rst = Pin (RST)
                  )
#
 Interface to the display
disp = RemoteDisplay (display_object = display)

# Display configuration
disp.setup_config_file ("testconfig.json")

# Update display fields
disp.update_text_area (area = "UpperRight", value = "Test")
disp.update_text_area (area = "UpperLeft", value = "Upper Left")

disp.page_by_name ("testconfig")
```
**Methods**

RemoteDisplay.init (display_object=OBJ)

- display_object - Initialized heardware display interface

RemoteDisplay.setup_config_file (file_name)

  - file_name - JSON configuration file, calls setup_config_dict

RemoteDisplay.setup_config_dict (config_dict)

  - config_dict - configuration distionary

RemoteDisplay.area_reload (area)

  - area - area to be redisplayed. Also reloads areas contained within this area

RemoteDisplay.screen_reload ()

  - Redisplays the active screen (page)

RemoteDisplay.show_areas ()

RemoteDisplay.show_area (area_id)

RemoteDisplay.page_by_name (page_name)

RemoteDisplay.page_by_index (page_index)


### **ILI9341Display**

**Purpose:**

Provides a generic API to the actual hardware library

### **TraceDisplay**

**Purpose:**

## **Configuration File**

Example:
```json
{
    "page_id" : "configexample" ,
    "area_id": "displayscreen",
    "vpos": 0,
    "vlen": 240,
    "hpos": 0,
    "hlen": 320,
    "areas": [
        {
            "id": "FirstRow",
            "vpos": 0,
            "vlen": 82,
            "hpos": 0,
            "hlen": 320,
            "areas": [
                {
                    "id": "UpperLeft",
                    "type": "text",
                    "value": "UL: No Value",
                    "hpos": 1,
                    "hlen": 159,
                    "vpos": 1,
                    "vlen": 80,
                    "padding": 1
                },
                {
                    "id": "UpperRight",
                    "type": "text",
                    "value": "UR: No Value",
                    "hpos": 160,
                    "hlen": 159,
                    "vpos": 1,
                    "vlen": 80,
                    "padding": 1
                }
            ]
        }
    ]
}
```
## **REMOTE DISPLAY**

```python
# Display configuration file (display_config.py)
# Determines the type of display
# and if the trace interface is to be included
TRACE_ON = False
#TRACE_ON = True

from display_modules.st7789s3_display import ST7789Display
DEVICE_DISPLAY = ST7789Display
TRACE_DISPLAY = None

if TRACE_ON :
    TRACE_DISPLAY = DEVICE_DISPLAY
    from display_modules.trace_display import TraceDisplay
    DEVICE_DISPLAY = TraceDisplay


# Configurationtion (config.json):
{
    "page_id" : "configexample" , # if omitted, auto assigned
    "area_id": "displayscreen",   # Optional
    "vpos": 0,        # default
    "vlen": 240,      # display height normally
    "hpos": 0,        # default
    "hlen": 320,      # display width normally
    "areas": [        # areas (display fields)
        {
        }
    ]
}

# implementation:
DISPLAY_WIDTH = 320
DISPLAY_HEIGHT = 170
ROTATION = 0
disp = RemoteDisplay (width = DISPLAY_WIDTH ,
                        height = DISPLAY_HEIGHT ,
                        rotation = ROTATION)

# Add area type
disp.add_area_type ("7segment", Remote7Segment)

# Add font
disp.add_font ('vga1_16x32', 'vga1_16x32')

# Add image
disp.add_image ('nixie0', 'images/nixie0.raw', iwidth, iheight)

disp.setup_config_file ("config.json")

```

## **AREA MODULES**

### **remote_area**

Base parent class inherited by all other area classes

```python
    {
    "area_id" : str ,     # optional, set by area child
    "type" : "container" ,  # default if omitted
    "vpos": int ,
    "vlen": int ,
    "hpos": int ,
    "hlen": int ,
    "borderwidth" : int ,
    "bordercolorname" : str ,
    "bordercolorrgb : [int, int, int] ,
    "paddingwidth" : int ,
    "backgroundcolorname" : str ,
    "font" : str ,
    "textcolorname" : str ,
    "textcolorrgb : [int, int, int]
    }

# Import:
from area_modules.remote_area import RemoteArea
```
**Configuration id's handled by remote_area**
- area_id
- type
- vpos
- vlen
- hpos
- hlen
- borderwidth
- bordercolorbyname, bordercolorrgb
- paddingwidth
- font
  - id of predefined font
- textcolorbyname, textcolorrgb
  - Becomes self.textcolor

**Calculated values that can be used by the child classes:**
- self.xmin
- self.xlen
- self.ymin
- self.ylen
- self.xymid

### **remote_7segment**


```py
# Configuration File:
    {
    "area_id" : "7seg" ,
    "type" : "7segment" ,
    "vpos": 80,
    "vlen": 42,
    "hpos": 30,
    "hlen": 200 ,
    "borderwidth" : 4 ,
        "bordercolorname" : "BLUE" ,
        "paddingwidth" : 2 ,
        "text" : "1.2345:abcdef?" ,
        "digit_size" : "mn" ,
        "bold" : true ,
        "backgroundcolorname" : "CYAN" ,
        "textcolorname" : "RED"
    }


```