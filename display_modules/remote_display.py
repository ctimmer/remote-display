#
################################################################################
# The MIT License (MIT)
#
# Copyright (c) 2023 Curt Timmerman
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
################################################################################

import sys
import gc
import time
import random
import re
import json as json

try :
    from machine import Pin, SPI
except :
    print ("import machine Failed")


from display_config import DEVICE_DISPLAY

from area_modules.remote_area import RemoteArea

from area_modules.remote_container import RemoteContainer
from area_modules.remote_text import RemoteText
from area_modules.remote_image import RemoteImage
#from area_modules.remote_lamp import RemoteLamp
#from area_modules.remote_7segment import Remote7Segment
#from area_modules.remote_switchpage import RemoteSwitchPage
#from area_modules.remote_template import RemoteTemplate

#-------------------------------------------------------------------------------
# RemoteDisplay
#-------------------------------------------------------------------------------
class RemoteDisplay (DEVICE_DISPLAY) :
    def __init__ (self, **kwargs) :
        #print ("RemoteDisplay __init__:", kwargs)
        super ().__init__ (**kwargs)
        #---- Page variables
        self.page_count = 0
        self.page_by_name = {}
        self.page_by_index = []
        self.active_base_area = None
        self.active_page_id = ""
        #---- Areas
        self.areas = {}
        self.area_types = {   # Predefined types
                        "container" : RemoteContainer ,
                        "text" : RemoteText ,
                        "image" : RemoteImage
                        }
        #
        self.color_names = {
                        "BLACK" : self.convert_rgb (0, 0, 0) ,
                        "WHITE" : self.convert_rgb (255, 255, 255) ,
                        "RED" : self.convert_rgb (255, 0, 0) ,
                        "LIME" : self.convert_rgb (0, 255, 0) ,
                        "BLUE" : self.convert_rgb (0, 0, 255) ,
                        "YELLOW" : self.convert_rgb (255, 255, 0) ,
                        "CYAN" : self.convert_rgb (0, 255, 255) ,
                        "MAGENTA" : self.convert_rgb (255, 0, 255) ,
                        "SILVER" : self.convert_rgb (192, 192, 192) ,
                        "GRAY" : self.convert_rgb (128, 128, 128) ,
                        "MAROON" : self.convert_rgb (128, 0, 0) ,
                        "OLIVE" : self.convert_rgb (128, 128, 0) ,
                        "GREEN" : self.convert_rgb (0, 128, 0) ,
                        "PURPLE" : self.convert_rgb (80, 0, 80) ,
                        "TEAL" : self.convert_rgb (0, 128, 128) ,
                        "NAVY" : self.convert_rgb (0, 0, 128)
                        }
        self.fonts = {}
        self.images = {}
        self.font_default = None
        self.font_color_default = self.color_names ["WHITE"]
        self.background_color_default = self.color_names ["BLUE"]
        self.border_color_default = self.color_names ["BLUE"]
        self.border_width_default = 0
        self.padding_width_default = 0
        self.configuration_page = None

        # Check for configuration file
        if "config_file" in kwargs :
            self.setup_config_file (kwargs["config_file"])

    def setup_config_file (self, file_name) :
        config_dict = None
        try :
        #if True :
            with open(file_name, 'r') as config_file:
                config_dict = json.loads(config_file.read())
        except :
        #else :
            print ("Configuration file error:", file_name)
            return
        self.setup_config_dict (config_dict)
    def setup_config_dict (self, config_dict) :
        if config_dict is None :
            return
        if "page_id" not in config_dict :
            config_dict["page_id"] = "_PAGE_{:2d}".format (self.page_count)
        base_area = self.configure (config_dict, None)
        self.add_page (base_area)
        gc.collect ()
    def configure (self, area_config, page) :
        if "areas" not in area_config :
            area_config ["areas"] = []
        area_obj = None
        if "type" not in area_config :
            area_config ["type"] = "container"
        if area_config ["type"] not in self.area_types :
            print ("Unknown area type:", area_config["type"])
            area_config ["type"] = "container"
        area_config ["page"] = page
        area_obj = self.area_types [area_config ["type"]] (self, area_config)
        if area_obj is None :
            return None
        #area_obj["page"] = self.page
        if "area_id" in area_config :
            self.areas [area_config ["area_id"]] = area_obj
        for child in area_config ["areas"] :
            child ["page_id"] = area_config ["page_id"]
            child ["parent_hpos"] = area_obj.xmin
            child ["parent_vpos"] = area_obj.ymin
            area_obj.add_area (self.configure (child,page))
        return area_obj

    def get_color_name (self, color_name) :
        if color_name in self.color_names :
            return self.color_names [color_name]
        return 0         # black

    #---- Load command (eg. switch page)
    def add_update (self, update_id, update_class) :
        self.areas [update_id] = update_class (self)
    #---- User defined area type
    def add_area_type (self, area_type, area_class) :
        self.area_types [area_type] = area_class
    #---- Load font
    def add_font (self, font_id, file_name, width = None, height = None) :
        self.fonts [font_id] = super().font_initialize (file_name, width, height)
        if self.font_default == None :
            self.font_default = self.fonts [font_id]    # first font
    def add_font_specs (self, font_id, spec_list) :
        self.fonts [font_id] = spec_list
        if self.font_default == None :
            self.font_default = self.fonts [font_id]    # first font
    #---- Load raw image
    def add_image (self,
                    image_id ,
                    file_name ,
                    width = None ,
                    height = None ,
                    ramdisk_file_name = None) :
        image_dict = {
            "image_file" : file_name
            }
        if width is not None :
            image_dict ["width"] = width
            image_dict ["height"] = height
        if ramdisk_file_name is not None :
            try :
            #if True :
                with open (file_name, "rb") as disk_file :
                    with open (ramdisk_file_name, "wb") as ramdisk_file :
                        ramdisk_file.write (disk_file.read())
                image_file = ramdisk_file_name
            #else :
            except Exception :
                print ("copy to ramdisk failed:", file_name)
        #
        self.images [image_id] = image_dict
        '''
        self.images [image_id] = {"file_name" : image_file ,
                                  "width" : width ,
                                  "height" : height}
        '''
    def add_image_object (self, image_id, image_object) :
        self.images [image_id] = {"image_object" : image_object}
    def get_image_object (self, image_id) :
        return self.images [image_id]

    def area_reload (self, area) :
        area.reload ()

    def screen_reload (self) :
        self.screen_clear (color = self.background_color_default)
        self.area_reload (self.get_base_area ())

    def update_area (self, **kwargs) :
        area_id = None
        if "area" in kwargs :
            area_id = kwargs ["area"]
        elif "area_id" in kwargs :
            area_id = kwargs ["area_id"]
        else :
            print ("'area/area_id' parameter missing", kwargs)
            print ("udate_area kwargs:", kwargs)
            return
        ## area_id = kwargs ["area"]
        if area_id not in self.areas :
            print ("'area_id' invalid:", area_id)
            return
        self.areas[area_id].update (**kwargs)
    def process_update_queue (self, queue) :
        while not queue.empty_queue() :
            queue_entry = queue.pop_queue()
            #print (queue_entry)
            if "method" not in queue_entry :
                print ("process_update_queue: 'method' entry missing")
                continue
            method = queue_entry["method"]
            #print ("method:",method)
            if method == "update_area" :
                self.update_area (**queue_entry["params"])
            elif method == "update_area_list" :
                #print ("update_area_list")
                for queue_item in queue_entry["params"] :
                    #print (queue_item)
                    self.update_area (**queue_item)
            else :
                print ("process_update_queue: Unknown method:", method)

    def add_page (self, base_area) :
        page_id = base_area.page_id
        self.page_by_name [page_id] = base_area
        self.page_by_index.append (base_area)
        if len (self.page_by_index) <= 1 :
            self.change_active_page_id (page_id)    # Set 1st page active

    def change_active_page_id (self, page_id, reload = False) :
        if not reload \
        and page_id == self.active_page_id :
            return                               # No change
        self.active_page_id = page_id
        self.active_base_area = self.page_by_name [page_id]
        self.screen_reload ()
    def change_active_page_index (self, page_index, reload = False) :
        page_id = self.page_by_index [page_index].page_id
        self.change_active_page_id (page_id, reload = reload)
    def page_id_is_active (self, page_id) :
        return page_id == self.active_page_id
    def get_base_area (self) :
        return self.active_base_area
    def get_page_array (self) :
        return self.page_by_index
    def get_page_ids (self) :
        return self.page_by_name.keys ()

    def get_child_list (self, parent_id) :
        if parent_id not in self.areas :
            print ("Unknown area id:", parent_id)
            #print (self.areas)
            return
        parent_area = self.areas [parent_id]
        child_list = []
        for area in parent_area.areas :
            #print (area)
            if area.area_id is not None :
                child_list.append (area.area_id)
        return child_list

    def number_justify (self, num, textlen=10, pad=" ") :
        formatted = re.sub ("[^0-9.-]", "", num)
        if "-" in formatted :
            formatted = str ("-" + re.sub ("[^0-9.]", "", formatted))
        flen = len (formatted)
        if flen < textlen :
            formatted = (pad * (textlen - flen)) + formatted
        elif flen > textlen :
            formatted = formatted [(flen - textlen)]
        return formatted

    def get_font (self, font_id) :
        return self.fonts[font_id]
    def get_font_default (self) :
        return self.font_default
    def get_font_color_default (self) :
        return self.font_color_default
    def get_background_color_default (self) :
        return self.background_color_default
    def get_color_by_name (self, color_name) :
        return self.color_names[color_name.upper()]

    def show_area (self, area_id = None, show_all = True) :
        area = None
        if area_id is None :
            area = self.get_base_area()
        elif area_id in self.areas :
            area = self.areas [area_id]
        else :
            print ("Unknown area id:", area_id)
            return
        area.show_area (show_all = show_all)
        self.dump_area (area)

    def dump_area (self, area, level=0) :
        if area.area_id is not None :
            area_id = area.area_id
        else :
            area_id = "anon"
        if level <= 0 :
            indent = ""
        else :
            indent = "." * level + " "
        print (f"{indent}{area_id}" \
                    + f" x={area.xmin}" \
                    + f" w={area.xlen}" \
                    + f" y={area.ymin}" \
                    + f" h={area.ylen}" \
                    + f" mid=({area.xmid},{area.ymid})")
        #print (area_specs)
        for child in area.areas :
            self.dump_area (child, level + 1)
    def dump (self) :
        for area in self.get_page_array () :
            #print (area.area_id)
            self.dump_area (area)
            
    
## end RemoteDisplay ##
