#

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
