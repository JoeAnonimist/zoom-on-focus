import os
from cudatext import *
import cudatext_cmd as cmds
from cudax_lib import get_translation

_   = get_translation(__file__)  # I18N

fn_config = os.path.join(app_path(APP_DIR_SETTINGS), 'cuda_myzoom.ini')

zoom_level = 3
zoom_on_focus = False


def bool_to_str(v): return '1' if v else '0'
def str_to_bool(s): return s=='1'


class Command:
    
    def __init__(self):
        
        global zoom_level
        global zoom_on_focus
        
        zoom_level = int(ini_read(fn_config, 'settings', 'zoom_level', str(zoom_level)))
        zoom_on_focus = str_to_bool(ini_read(fn_config, 'settings', 'zoom_on_focus', str(zoom_level)))

    def config(self):

        ini_write(fn_config, 'op', 'zoom_level', str(zoom_level))
        file_open(fn_config)
        
    def run(self):
        pass


                
    def on_focus(self, ed_self):

        for h in ed_handles():
            Editor(h).cmd(cmds.cCommand_ZoomReset)
            if Editor(h).get_prop(PROP_FOCUSED) == True and zoom_on_focus == True:
                for i in range(zoom_level):
                    Editor(h).cmd(cmds.cCommand_ZoomIn)
                
