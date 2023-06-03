# remote-display
Display server that display data received from 1 or more clients

## **Classes**

### **RemoteDisplay**

**Purpose:**

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

RemoteDisplay.update_text_area

RemoteDisplay.update_lamp_area

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
    "page_id" : "testconfig" ,
    "id": "screen",
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
