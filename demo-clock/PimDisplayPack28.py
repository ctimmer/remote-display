#
from machine import Pin, SPI, PWM
import time

## Button constants
BUTTON_A_PIN = const (15)
BUTTON_B_PIN = const (13)
BUTTON_X_PIN = const (14)
BUTTON_Y_PIN = const (12)
## RGB LED constants
RGB_RED_PIN = const (26)
RGB_GREEN_PIN = const (27)
RGB_BLUE_PIN = const (28)
RGB_FREQ = const (1000)

class PimoroniGPIO () :
    def __init__ (self ,
                  pin_read_delay = 300) :
        ticks_ms = time.ticks_ms ()
        ## Button set up
        self.pin_read_delay = pin_read_delay
        self.buttons = {
            "A" : {
                "pin" : Pin (BUTTON_A_PIN, Pin.IN, Pin.PULL_UP) ,
                "next_read_ms" : ticks_ms ,
                "pushed" : False
                } ,
            "B" : {
                "pin" : Pin (BUTTON_B_PIN, Pin.IN, Pin.PULL_UP) ,
                "next_read_ms" : ticks_ms ,
                "pushed" : False
                } ,
            "X" : {
                "pin" : Pin (BUTTON_X_PIN, Pin.IN, Pin.PULL_UP) ,
                "next_read_ms" : ticks_ms ,
                "pushed" : False
                } ,
            "Y" : {
                "pin" : Pin (BUTTON_Y_PIN, Pin.IN, Pin.PULL_UP) ,
                "next_read_ms" : ticks_ms ,
                "pushed" : False
                }
            }
        ## RGB LED set up
        self.rgb_red_pin = PWM (Pin (RGB_RED_PIN), freq = RGB_FREQ)
        self.rgb_green_pin = PWM (Pin (RGB_GREEN_PIN), freq = RGB_FREQ)
        self.rgb_blue_pin = PWM (Pin (RGB_BLUE_PIN), freq = RGB_FREQ)
        self.set_rgb_led (0, 0, 0)   # Turn off

    ## Button methods
    def read_button_pin (self, button_entry) :
        current_ticks_ms = time.ticks_ms ()
        if current_ticks_ms >= button_entry ["next_read_ms"] :
            if button_entry ["pin"].value () == 0 :
                button_entry ["pushed"] = True
            else :
                button_entry ["pushed"] = False
            button_entry ["next_read_ms"] = current_ticks_ms
        return button_entry ["pushed"]
    def read_button (self, button_id) :
        return self.read_button_pin (self.buttons [button_id])
    def read_buttons (self, button_list = ["A", "B", "X", "Y"]) :
        ret_reads = {}
        for button_id in button_list :
            ret_reads [button_id] = self.read_button (button_id)
        return ret_reads
    def set_alias (self, alias_id, button_id) :
        self.buttons [alias_id] = self.buttons [button_id]
        #print (self.buttons)

    ## RGB LED methods
    def set_rgb_led (self, red, green, blue) :
        #red = red >> 2
        red = red % 64
        greed = green % 64
        blue = blue % 64
        self.rgb_red_pin.duty_u16 (((63 - red) * 65535) // 63)     # RED
        self.rgb_green_pin.duty_u16 (((63 - green) * 65535) // 63) # GREEN:
        self.rgb_blue_pin.duty_u16 (((255 - blue) * 65535) // 255)  # BLUE:
        #return
        #self.rgb_red_pin.duty_u16 ((red * 65535) // 255)     # RED
        #self.rgb_green_pin.duty_u16 ((green * 65535) // 255) # GREEN:
        #self.rgb_blue_pin.duty_u16 ((blue * 65535) // 255)  # BLUE:
        return
        print ("rgb:",int(red * 65535 / 255),int(blue * 65535 / 255),int(green * 65535 / 255))
        self.rgb_red_pin.duty_u16 (int(red * 65535 / 255))    # RED
        self.rgb_green_pin.duty_u16 (int(green * 65535 / 255)) # GREEN:
        self.rgb_blue_pin.duty_u16 (int(blue * 65535 / 255))  # BLUE:


#-------------------------------------------------
if __name__ == "__main__" :
    led_on_ms = 5000
    Pim = PimoroniGPIO ()
    Pim.set_alias ("HOME", "A")
    Pim.set_alias ("NEXT_PAGE", "X")
    Pim.set_alias ("PREVIOUS_PAGE", "Y")
    led_turn_off_ms = None
    test_col = 0
    for count in range (0, 256) :
        button = Pim.read_buttons (("HOME", "NEXT_PAGE", "PREVIOUS_PAGE", "B"))
        #print (button)
        print (count)
        #Pim.set_rgb_led (count, 0, count)
        #time.sleep (0.1)
        #continue

        ticks_ms = time.ticks_ms ()
        if button ["HOME"] :
            Pim.set_rgb_led (165, 42, 42)
            led_turn_off_ms = time.ticks_add (ticks_ms, led_on_ms)
        elif button ["NEXT_PAGE"] :
            Pim.set_rgb_led (0, 128, 0)    # Green
            led_turn_off_ms = time.ticks_add (ticks_ms, led_on_ms)
        elif button ["PREVIOUS_PAGE"] :
            Pim.set_rgb_led (255, 0, 0)    # Red
            led_turn_off_ms = time.ticks_add (ticks_ms, led_on_ms)
        elif button ["B"] :
            Pim.set_rgb_led (0, 0, 255)    # Blue
            led_turn_off_ms = time.ticks_add (ticks_ms, led_on_ms)
        if led_turn_off_ms is not None :
            if time.ticks_diff (ticks_ms, led_turn_off_ms) >= 0 :
                Pim.set_rgb_led (0, 0, 0)  # Black
                led_turn_off_ms = None
        time.sleep (0.5)

