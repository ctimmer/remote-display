#

from area_modules.remote_linear_guage import RemoteLinearGuage

class RemoteLinearGuageTicks (RemoteLinearGuage) :
    def __init__ (self ,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        self.tick_args = []
        self.tick_count = 10
        self.tick_width = 3
        self.tick_color = 0
        if "tickcount" in area_config :
            self.tick_count = area_config ["tickcount"]
        if "tickwidth" in area_config :
            self.tick_width = area_config ["tickwidth"]
        if "tickcolorname" in area_config :
            self.tick_color = remote_display.get_color_name (area_config["tickcolorname"])
        elif "tickcolorrgb" in area_config :
            self.tick_color = remote_display.convert_rgb (*area_config["tickcolorrgb"])
        if self.vertical_guage :
            self.init_vertical ()
        else :
            self.init_horizontal ()
    def init_vertical (self) :
        tick_len = self.ylen / self.tick_count
        for y_idx in range (1, self.tick_count) :
            named_args = {"y" : None ,
                          "h" : self.tick_width ,
                          "x" : self.xmin ,
                          "w" : self.xlen ,
                          "color" : self.tick_color}
            named_args["y"] = (self.ymin + round (tick_len * y_idx)) - self.tick_width
            self.tick_args.append (named_args)
    def init_horizontal (self) :
        tick_len = self.xlen / self.tick_count
        for x_idx in range (1, self.tick_count) :
            named_args = {"y" : self.ymin ,
                          "h" : self.ylen ,
                          "x" : None ,
                          "w" : self.tick_width ,
                          "color" : self.tick_color}
            named_args["x"] = self.xmin + round (tick_len * x_idx)
            self.tick_args.append (named_args)
    def update (self, **kwargs) :
        super().update (**kwargs)
        RemoteLinearGuageTicks.reload (self, reload_all = False)
    def reset (self) :
        #
        #---- Set area parameters to initial state
        #
        self.reload (reload_all = True)
        #
    def reload (self, reload_all = True) :
        if not self.page_is_active (self.page_id) :
            return
        if reload_all :
            super().reload ()
        for named_args in self.tick_args :
            self.remote_display.rectangle_fill (**named_args)

## end RemoteLinearGuageTicks ##
