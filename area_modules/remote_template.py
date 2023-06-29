
from area_modules.remote_area import RemoteArea

#-------------------------------------------------------------------------------
# RemoteTemplate
#-------------------------------------------------------------------------------
class RemoteTemplate (RemoteArea) :
    def __init__ (self,
                  remote_display,
                  area_config) :
        super().__init__ (remote_display, area_config)
        self.show_border_color = remote_display.get_color_name ("GREEN")
    def update (self, **kwargs) :
        #
        #---- Make changes to area parameters
        #
        self.reload (reload_all = False)
        #
    def reset (self) :
        #
        #---- Set area parameters to initial state
        #
        self.reload (reload_all = True)
        #
    def reload (self, reload_all = True) :
        if not self.page_is_active() :
            return
        if reload_all :
            self.reload_background ()
        #
        #---- Output to display here
        #
        if reload_all :
            self.reload_areas ()

## end RemoteTemplate ##
