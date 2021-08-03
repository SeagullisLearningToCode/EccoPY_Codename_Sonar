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
from PIL import ImageTk, Image
from data.frw.GF.GF import *


# VARIABLES-------------------------------------------------------------------------------------------------------------------

# FAMILY EXTENTSION INFO
INFO = {
    "Type": "Extentsion",
    "Name": ["Gull", "Tkinter"],
    "Author/s": [
        ["SeagullinSeagulls", "SeagullisLearningToCode"]
    ],
    "Age": [8, 2, 2021],
    "Desc": "Official Extentsion of the Gull Framework for added support for Tkinter GUI python module"
}

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
