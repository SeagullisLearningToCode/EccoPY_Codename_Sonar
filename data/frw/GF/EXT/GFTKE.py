"""
 __                     ___  __              ___       __   __
/ _` |  | |    |       |__  |__)  /\   |\/| |__  |  | /  \ |__) |__/
\__> \__/ |___ |___    |    |  \ /~~\  |  | |___ |/\| \__/ |  \ |  \
                                                    Version: 1 Shut Up Gull (Tkinter Extentsion)


This file stores very simple functions with the sole purpose of de-bloating the Main.py file
This file is also makes stating certain things faster and possibly easier.
"""
# IMPORTS---------------------------------------------------------------------------------------------------------------------
from tkinter import *
from tkinter import ttk
from curses import *

import pygame.event
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


# Tkinter Images
def loadimage(image):
    """
    May help with PIL's garbage collection so it's less bloated
    :param image:
    :return: image:
    """
    # init/
    #   vars/
    #       str/
    #           img/
    i = ImageTk.PhotoImage(Image.open(image))
    #               protection/ ; Apply protection please
    ip = i
    ip_pmm = i
    ip_pmm.protect = ip_pmm
    return ip


def rgbtohex(r: int, g: int, b: int, **kwargs):
    """
        Converts RGB values to Hexadecimal values

        :param r: Red
        :param g: Green
        :param b: Blue
        :param kwargs: printresults = False
        :return: Formated String
        """
    # init/
    #   kwargs/
    #       Booleans/
    pr = kwargs.get("printresults", False)
    convert_to_bgr = kwargs.get("convert_bgr", False)
    # code/
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


# CLASSES------------------------------------------------------------------------------------------------------------------------------------------------------------------

class pygame_Tk_Integration(object):
    """
    Have Tkinter and pygame work together (unfinished)
    """

    def __init__(self):
        # init/
        #   pg/
        #       it/
        init()
        p("\nTP Initiallized")
        #   var/
        #       int/
        self.amount_pressed = 0
        #       pg/
        #           keyb/
        self.keyi = KEYDOWN
        #       dict/
        self.pg_keyb_list = {
            "alphabet": {
                "no-mod": ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
                           "a", "s", "d", "f", "g", "h", "j", "k", "l",
                           "z", "x", "c", "v", "b", "n", "m"],
                "mod": [] # ;Gull, copy the values from self.pg_keyb_list["alphabet"]["no-mod"] and paste into self.pg_keyb_list["alphabet"]["mod"] as uppercase values
            },
            "numerical": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"],
            "symbolics": {
                "no-mod": ["`", "-", "=", "[", "]", "\\", ";", "'", ",", ".", "/"],
                "mod": ["~", "`", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "_", "+", "{", "}", "|", ":", '"', "<", ">", "?"],
            },
            "tc": ["backspace", "tab", "pause", "delete", "end", "page up", "page down", "home", "insert"], # ;Text Commands
            "arrow_keys": {
                "3bttn": ["up", "down", "left", "right"],
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
        This function shouldn't be runned

        :return:
        """
        # INIT/
        #   VAR/
        #       KWARGS/
        #           BOOLEANS/
        SHOWRESULT = kwargs.get('showresult', False)
        # CODE/
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
        # INIT/
        #   VAR/
        #       ARR/
        allvars = []
        #       KWARGS/
        #           BOOLEANS/
        IncludeAlphaCaps = kwargs.get("include_alpha_caps", False)
        ShowResult = kwargs.get("show_result", False)
        IncludeFD = kwargs.get("include_fd", False)
        # CODE/
        # ;Alpha
        if IncludeFD is True:
            self.FinishDict(showresult=False)
        else:
            self.FinishDict()

        for key_alpha_nm_val in self.pg_keyb_list["alphabet"]["no-mod"]:
            allvars.append(key_alpha_nm_val)

        if IncludeAlphaCaps is True:
            for key_alpha_m_val in self.pg_keyb_list["alphabet"]["mod"]:
                    allvars.append(key_alpha_m_val)

        # ;Numbers
        for key_num_val in self.pg_keyb_list["numerical"]:
                allvars.append(key_num_val)

        # ;Symbolic
        for key_sym_nm_val in self.pg_keyb_list["symbolics"]["no-mod"]:
                allvars.append(key_sym_nm_val)

        for key_sym_m_val in self.pg_keyb_list["symbolics"]["mod"]:
            allvars.append(key_sym_m_val)

        # ;tc
        for key_tc_val in self.pg_keyb_list["tc"]:
            allvars.append(key_tc_val)

        # ;ArrowKeys
        for key_aw_val in self.pg_keyb_list["arrow_keys"]["3bttn"]:
            allvars.append(f"{key_aw_val} arrow")

        # ;KeyPad
        for key_kp_m_val in self.pg_keyb_list["key_pad"]["misc"]:
            allvars.append(f"keypad {key_kp_m_val}")

        for key_kp_np_val in self.pg_keyb_list["key_pad"]["numpad"]:
            allvars.append(key_kp_np_val)

        # ;FunctionButtons
        for key_fb_num_val in self.pg_keyb_list["function_buttons"]["num"]:
            allvars.append(f"f{key_fb_num_val}")

        for key_fb_str_val in self.pg_keyb_list["function_buttons"]["str"]:
            allvars.append(key_fb_str_val)

        if ShowResult is True:
            p(f"{allvars}\n{len(allvars)}")

        return allvars

    def SHOW_PYGAME_BINDINGS_CURRENT_DEVICE(self, **kwargs):
        # INIT/
        #   VAR/
        #       KWARGS/
        #           BOOLEANS/
        show_len_bindings = kwargs.get("show_len_bindings", False)
        # CODE/
        if show_len_bindings is True:
            p(f"{key.get_pressed()}\n{len(key.get_pressed())}")
        else:
            p(key.get_pressed())

# EOF----------------------------------------------------------------------------------------------------------------------------------------------------------------------
