#


PARAMETERS = {
    "TRACE_ON" : False
    #TRACE_ON = True
    }

from display_modules.ili9341_display import ILI9341Display as DISPLAY_MODULE
DEVICE_DISPLAY = DISPLAY_MODULE
TRACE_DISPLAY = None

if PARAMETERS["TRACE_ON"] :
    TRACE_DISPLAY = DEVICE_DISPLAY
    from display_modules.trace_display import TraceDisplay
    DEVICE_DISPLAY = TraceDisplay
