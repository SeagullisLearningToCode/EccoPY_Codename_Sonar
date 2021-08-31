"""
 __                     ___  __              ___       __   __
/ _` |  | |    |       |__  |__)  /\   |\/| |__  |  | /  \ |__) |__/
\__> \__/ |___ |___    |    |  \ /~~\  |  | |___ |/\| \__/ |  \ |  \  Xtension

This file stores very simple functions with the sole purpose of de-bloating the Main.py file (used to be)
This file is also makes stating certain things faster and possibly easier.
"""
# IMPORTS---------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image

from data.frw.GF.GF import *

# VARIABLES-------------------------------------------------------------------------------------------------------------------

# FAMILY EXTENTSION INFO
INFO = {
    "Type": "Extentsion",
    "Name": ["Gull", "Tkinter"],
    "Author/s": "SeagullIsLearningToCode",
    "Age": [8, 2, 2021],
    "Desc": "Official Extentsion of the Gull Framework for added support for Tkinter GUI python module."
}
flp(INFO)

# FUNCTIONS-------------------------------------------------------------------------------------------------------------------

def loadimage(image):
    """
    May help with PIL's garbage collection so it's less bloated
    :param image:
    :return: image:
    """
    # IMAGES
    i = ImageTk.PhotoImage(Image.open(image))
    # CODE/
    ip = i
    ip_pmm = i
    ip_pmm.protect = ip_pmm
    return ip


def rgb(r: int, g: int, b: int, **kwargs):
    """
        Converts RGB values to Hexadecimal values

        :param r: Red
        :param g: Green
        :param b: Blue
        :param kwargs: printresults = False
        :return: Formated String
        """
    # KWARGS_BOOLEANS
    pr = kwargs.get("printresults", False)
    convert_to_bgr = kwargs.get("convert_bgr", False)
    # CODE
    if r > 255:
        p(f"Red: {r}")
        raise ValueError
    elif g > 255:
        p(f"Green {g}")
        raise ValueError
    elif b > 255:
        p(f"Blue {b}")
        raise ValueError

    if pr is True:
        p("#%02x%02x%02x" % (r, g, b))
        if convert_to_bgr is True:
            p("#%02x%02x%02x" % (b, g, r))

    if convert_to_bgr is True:
        return "#%02x%02x%02x" % (b, g, r)
    else:
        return "#%02x%02x%02x" % (r, g, b)

def check_bv(boolvar: BooleanVar, target):
    """
    Check boolvar and send it's value

    :param boolvar:
    :param target:
    :return:
    """
    # ABS
    bv = boolvar
    t = target
    # CODE
    if boolvar.get() is True:
        target = True
    else:
        target = False

# CLASSES------------------------------------------------------------------------------------------------------------------------------------------------------------------

class pygame_Tk_Integration(object):
    """
    Have Tkinter and pygame work together (unfinished)
    """

    def __init__(self):
        # INITS
        init()
        joystick.init()
        p("\nTP Initiallized")
        # INT
        self.amount_pressed = 0
        # PYGAME_KEYB ;Keyboard
        self.keyi = KEYDOWN
        # LISTS
        self.pg_controllers = [joystick.Joystick(x) for x in range(joystick.get_count())]
        self.pg_joys_list = []
        # DICTIONARIES
        self.pg_keyb_list = {
            "alphabet": {
                "no-mod": ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                           "a", "s", "d", "f", "g", "h", "j", "k", "l",
                           "z", "x", "c", "v", "b", "n", "m"],
                "mod": []  # ;Gull, copy the values from self.pg_keyb_list["alphabet"]["no-mod"] and paste into self.pg_keyb_list["alphabet"]["mod"] as uppercase values
            },
            "numerical": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            "symbolics": {
                "no-mod": ["`", "-", "=", "[", "]", "\\", ";", "'", ",", ".", "/"],
                "mod": ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", '"', "<", ">", "?"],
            },
            "tc": ["backspace", "tab", "pause", "delete", "end", "page up", "page down", "home", "insert"],  # ;Text Commands
            "arrow_keys": {
                "3bttn": ["up arrow", "down arrow", "left arrow", "right arrow"],
                "4bttn": [],
                "9bttn": []
            },
            "key_pad": {
                "numpad": [],
                "misc": ["period", "divide", "multiply", "minus", "plus", "enter", "equals", "numlock", "print screen"]
            },
            "function_buttons": {
                "num": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15"],
                "str": ["escape", "sysrq", "scrollock", "break", "capslock", "right shift", "left shift",
                        "right control", "left control", "right alt", "left alt", "right meta", "left meta",
                        "right Windows key", "left Windows key", "mode shift", "menu", "break", "power", "help"]
            }
        }

    def FinishDict(self, **kwargs):
        """
        Fills in the blanks in self.pg_keyb_list

        :param kwargs:
        :return:
        """
        # KWARGS_BOOLEANS
        SHOWRESULT = kwargs.get('showresult', False)
        # CODE
        for key in self.pg_keyb_list["alphabet"]["no-mod"]:
            self.pg_keyb_list["alphabet"]["mod"].append(key.upper())

        for number in self.pg_keyb_list["numerical"]:
            self.pg_keyb_list["key_pad"]["numpad"].append(f"keypad {number}")

        if SHOWRESULT is True:
            p(f"{self.pg_keyb_list['alphabet']['mod']}\n{self.pg_keyb_list['key_pad']['numpad']}")

    def CombineDictToOne(self, **kwargs):
        """
        :param kwargs:
        :return: allvars
        """
        # LISTS
        refrenced_dicts_list = [self.pg_keyb_list['alphabet']['no-mod'], self.pg_keyb_list['numerical'], self.pg_keyb_list['symbolics']['no-mod'], self.pg_keyb_list['symbolics']['mod'], self.pg_keyb_list['tc'],
                                self.pg_keyb_list['arrow_keys']['3bttn'], self.pg_keyb_list['key_pad']['misc'], self.pg_keyb_list['key_pad']['numpad'], self.pg_keyb_list['function_buttons']['num'], self.pg_keyb_list['function_buttons']['str']]
        allvars = []
        # KWARGS_BOOLEANS
        IncludeAlphaCaps = kwargs.get("include_alpha_caps", False)
        ShowResult = kwargs.get("show_result", False)
        IncludeFD = kwargs.get("include_fd", False)
        # CODE
        # ;Alpha
        if IncludeFD is True:
            self.FinishDict(showresult=False)
        else:
            self.FinishDict()

        if IncludeAlphaCaps is True:
            refrenced_dicts_list.append(self.pg_keyb_list['alphabet']['mod'])

        for keyb_key_val in refrenced_dicts_list:
            for key_val in keyb_key_val:
                allvars.append(key_val)

        if ShowResult is True:
            p(f"{allvars}\n{len(allvars)}")

        return allvars

    def SHOW_PYGAME_BINDINGS_CURRENT_DEVICE(self, **kwargs):
        # KWARGS_BOOLEANS
        show_len_bindings = kwargs.get("show_len_bindings", False)
        # CODE
        if show_len_bindings is True:
            p(f"{key.get_pressed()}\n{len(key.get_pressed())}")
        else:
            p(key.get_pressed())

    def debug_controller(self, **kwargs):
        """
        Copied from https://www.pygame.org/docs/ref/joystick.html#pygame.joystick.Joystick.get_guid

        :param kwargs:
        :return:
        """
        # KWARGS_BOOLEAN
        show_number_of_controllers = kwargs.get("show_num_of_controllers", False)
        show_controller_info = kwargs.get("show_controller_info", False)
        # CODE
        if show_number_of_controllers is True:
            p(joystick.get_count())

        if show_controller_info is True:
            for controller in range(joystick.get_count()):
                jys = joystick.Joystick(controller)
                try:
                    cid = jys.get_instance_id()
                except AttributeError:
                    cid = jys.get_id()
                    p(f"Joystick {cid}")

                controller_name = jys.get_name()
                p(f"\nJoystick Name: {controller_name}")

                try:
                    controller_guid = jys.get_guid()
                except AttributeError:
                    pass
                else:
                    p(f"GUID: {controller_guid}")

                controller_axes = jys.get_numaxes()
                p(f"Num of Axes: {controller_axes}")

                for axes in range(controller_axes):
                    controller_axis = jys.get_axis(axes)
                    p(f"Axis {axes}, Value: {controller_axis}")

                controller_buttons = jys.get_numbuttons()
                p(f"Number of Buttons: {controller_buttons}")

                for buttons in range(controller_buttons):
                    button = jys.get_button(buttons)
                    p(f"Button: {buttons}, Value: {button}")

                controller_hats = jys.get_numhats()  # ;Wait, controllers has hats? What a werid world we live in
                p(f"Number of Hats: {controller_hats}")

                for hats in range(controller_hats):
                    hat = jys.get_hat(hats)
                    p(f"Hat: {hats}, Value: {str(hat)}")

        for controller in range(joystick.get_count()):
            jys = joystick.Joystick(controller)
            try:
                cid = jys.get_instance_id()
            except AttributeError:
                cid = jys.get_id()

            controller_buttons = jys.get_numbuttons()

            for buttons in range(controller_buttons):
                self.pg_joys_list.append(f"Button {buttons}")

    def DISPLAY_AUTODETECT(self, **kwargs): # ; inheirited from EccoPY
        """
        Inherited from EccoPY in settings.py
        :param kwargs:
        :return:
        """
        # PYGAME
        indexes = len(display.list_modes())
        # KWARGS
        DA_PRINT_RESULT = kwargs.get("print_result", False)
        # LIST
        sizes_autodetect = []
        sizes_autodetect_filtered = []
        # CODE
        for resolution in display.list_modes():
            sizes_autodetect.append(resolution)
            if len(sizes_autodetect) == indexes:
                sizes_autodetect.sort()

            for unique_resolutions in sizes_autodetect:
                if unique_resolutions not in sizes_autodetect_filtered:
                    sizes_autodetect_filtered.append(unique_resolutions)

        if DA_PRINT_RESULT is True:
            p(f"AUTODETECT RESULTS (UNFILTERED): {sizes_autodetect}")
            p(f"\nAUTODETECT RESULTS: {sizes_autodetect_filtered}\n\nDETECTED {len(sizes_autodetect_filtered)} Windowsize options\n")
        sizes_autodetect_filtered.sort()

        return sizes_autodetect_filtered

    def resolution_to_readable_form(self, **kwargs):
        # KWARGS
        RTRF_PRINT_RESULT = kwargs.get("print_result", False)
        RTRF_STRING_REPLACEMENT = kwargs.get("between_string", "x")
        # CODE



# EOF----------------------------------------------------------------------------------------------------------------------------------------------------------------------
