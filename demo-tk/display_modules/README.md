# Demo-tk Display Modules

## Modules

- remote_display.py
  - Subclass of tkinter_display.py, dummy_display.py, or trace_display.py
- tkinter_display.py
  - Interface to tkinter canvas
- dummy_display.py
  - No display output if testing without a physical display
- trace_display.py
  - Subclass of tkinter_display.py, dummy_display.py
  - Displays function calls and parameters

## display_config.py

```
PARAMETERS = {
    "TRACE_ON" : False ,
    #"TRACE_ON" : True ,
    #"DISPLAY_OUT" : False
    "DISPLAY_OUT" : True
    }

if PARAMETERS ["DISPLAY_OUT"] :
    from display_modules.tkinter_display import TKINTERDisplay as DISPLAY_MODULE
else :
    from display_modules.dummy_display import DummyDisplay as DISPLAY_MODULE

DEVICE_DISPLAY = DISPLAY_MODULE
TRACE_DISPLAY = None

if PARAMETERS["TRACE_ON"] :
    print ("Trace: ON")
    TRACE_DISPLAY = DEVICE_DISPLAY
    from display_modules.trace_display import TraceDisplay
    DEVICE_DISPLAY = TraceDisplay

```

- PARAMETERS
  - TRACE_ON
    - True: Includes TraceDisplay to print all display function calls and parameter
    - False: Excludes TraceDislay
  - DISPLAY_OUT
    - True: Sends display output to physical display
    - False: Inhibits output to physical display
