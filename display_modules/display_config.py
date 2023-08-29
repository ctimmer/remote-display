#

TRACE_ON = False
#TRACE_ON = True

from display_modules.st7789s3_display import ST7789Display
DEVICE_DISPLAY = ST7789Display
TRACE_DISPLAY = None

if TRACE_ON :
    TRACE_DISPLAY = DEVICE_DISPLAY
    from display_modules.trace_display import TraceDisplay
    DEVICE_DISPLAY = TraceDisplay
