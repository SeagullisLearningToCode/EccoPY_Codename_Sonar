"""
████████████████████████████████████████████████████████████████████▓░░░░░░░░░░░░░░░░░░░░░
█████████████████████▒░▒▒▒▒▒▒▓▓█████████████████████████████████████▓░░░░░░░░░░░░░░░░░░░░░
███████████████▓▓▒▒░░░░░░░░░░░░░░░░░░░▒▓▓███████████████████████████▒░░░░░░░░░░░░░░░░░░░░░
████████████▓▒░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░▒▒█████████████████████▓▓░░░░░░░░░░░░░░░░░░░░░
██████████▓░░░░░░░░░░░░░░░░░░▒▒░░▒▒░░▒▒▒░▒░░░░░░░▒██████████████████▓▒░░░░░░░░░░░░░░░░░░░░
█████████▒░░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░▒████████████████▓▒░░░░░░░░░░░░░░░░░░░░
███████▒░░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒██████████████▓▒░░░░░░░░░░░░░░░░░░░░
████▓░░░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒░▒███████████▓▓▓░░░░░░░░░░░░░░░░░░░░
████▓▒░░░░░░▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████▓▓▓▒▒▒▒▒▒▒░░▓███████████▓░░░░░░░░░░░░░░░░░░░░
████▒░░░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████▓▒▒▒▒▒▒▒▒▒░░████████▓█▓░░░░░░░░░░░░░░░░░░░░
█▓▒▒▒░░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓██████▓▓▒▒▒▒▒▒▒▒▒▒▒░▒▓██████▓▒░░░░░░░░░░░░░░░░░░░░
█▓▓▓▒░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░▒▒████▒░░░░░░░░░░░░░░░░░░░░
███▓░░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░▓▓▓░░░░░░░░░░░░░░░░░░░░
███▒░░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░░░░░░░
██▒░░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒░░░░░░░░░
██▒░▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓████████▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒░░░░░░
██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓▓▓▓▓▓█▓█▓▓▓▓▓▒▒▒▒▒▒░░░░
█▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█▓██████████▓▓▒▒▒▒▒░░░
▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓▓▓▓█████████▓▓▓▓████████████▓▒▒▒░░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████████████████▓░▒▒▓███████████▓▒▒░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓▓██████████████████████░░░░░░░▒▒▒▓▓▒▒▓▒▒▒░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▓███████████████████████▓░░░░░░░░░░░░░░░░░▒░
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒█████████████████████▓▓▓▒░░░░░░░░░░░░░░░░░░░
 __                     ___  __              ___       __   __
/ _` |  | |    |       |__  |__)  /\   |\/| |__  |  | /  \ |__) |__/
\__> \__/ |___ |___    |    |  \ /~~\  |  | |___ |/\| \__/ |  \ |  \
                                                    Version: 1.014 Shut Up Gull


This file stores very simple functions with the sole purpose of de-bloating the Main.py file
This file is also makes stating certain things faster and possibly easier.

This version of the Gull Framework uses Pygame 2.0.1 and Pyglet (latest version) as of 8/16/21
"""
# IMPORTS---------------------------------------------------------------------------------------------------------------------
import os
import sys
from pygame import *
from pyglet import *
import getpass as gp
from datetime import *
from random import *
from configparser import *

# VARIABLES-------------------------------------------------------------------------------------------------------------------

load = mixer.music

# Today's Date
td = date.today()

td_c_s = str(td)  # Converts the current date into a String
td_c_s_yo = td_c_s[0:4]  # Get year only
# Today's Time
tt = datetime.now()


# FUNCTIONS-------------------------------------------------------------------------------------------------------------------

# p function
# reason: same as the p function but made it faster to make a print statement by using a few characters
def p(t="passed"):
    """
    Print
    Make print statements faster than python's print("Hello World")

    Example: p("Hello World")
    Output: Hello World
    """
    print(t)


# sps function
# Reason: easier and shorter
def sps(t: str):
    """
    Same thing as p() but adds in "passed"

    Example: sps("it")
    Output: passed it
    """
    p(f"passed {t}")


def flp(l: dict):
    """
    For in Loop Print From Dictionary
    """
    for key in l:
        p(f"{key}: {l.get(key)}")


# Get Presence
# reason: shorten it up a bit with the os.path.exists
def GetPresSpec(file: str):
    """
    Does the file exist

    Returns: None
    """
    getpres = os.path.exists
    p(f"{getpres(file)}")


# Raise Custom Error Function (RCEF)

def RCE(rfe: str, et: int):
    """
    This function can raise a custom error which it's easier to use

    Refrences
    ----------
    rfe: String
    et: which error do you want to raise
        Values:
                0 = File Not Found Error (ERROR)
                1 = File Exists Error (ERROR
                2 = Not an Error but a Warning (WARNING)
                3 = EccoPY_RenderTypeInvaild_Error (ERROR)
    """
    error_type = et
    if error_type == 0:  # FNFE
        p(f"ERROR: {rfe}")
        raise FileNotFoundError
    elif error_type == 1:  # FEE
        p(f"ERROR: {rfe}")
        raise FileExistsError
    elif error_type == 2:  # NEBW
        p(f"WARNING: {rfe}")
    elif error_type == 3:  # EP_RTI_E
        p(f"ERROR: {rfe}")
        raise ValueError
    else:
        p("Can't go higher than 1 at the moment...\n Sorry About that :(")
        raise ValueError


def HVFFTAOHV(dirname: str,
              filename: str,
              destination: str,
              printresults: bool,
              outputresulttofile: bool):  # True = 1, False = 0
    """
    Hex Values From File To Array Of Hex Values
    This Function converts the hex values inside a text document and prints the values as an array
    """
    """
    Unfortunately what sucks about this function as of now is that I can possibly figure out a way to convert it into an actual hex value.
    """
    # FUNC/
    #   ARGS/
    #       VARS/
    #           STR/
    dfn = dirname  # ;Shortens dirname arg
    fn = filename  # ;Shortens and filename arg
    dtn = destination  # ;Shortens destination arg
    #           BOOL/
    orf = outputresulttofile  # ;Shortens outputresulttofile arg (this makes it to where if you don't want the results made into a file, the function prints the result instead)
    pr = printresults  # ;Shortens the printresults arg
    #           MSC/
    gun = gp.getuser()  # ;Shortens and gets the current username

    #   CODE/
    #       VARS/
    #           STR/
    gdn = (dfn + fn)  # ;Combine and Shortens dfn and fn which creates the full path
    gun_gdn = (gun + gdn)  # ;Combines and shortens gun and gdn which will do something
    fp_uni = ("/Users/" + gun + "/" + dtn + fn)  # ;Combines and shortens gun and dtn and fn
    #           CSN/
    pat = open(gdn, "r")  # ;Opens the file and gives python read and write access
    #               PAT/
    dat = pat.read()
    #           LIST/
    void_names = ["none", "null", "0"]
    preres = []
    res = []
    #   CODE
    pat.close()  # ;Prevents memory leakage
    r = dat.split(' ')
    if orf is True:
        if dtn == void_names[0] or void_names[0].upper() or void_names[1] or void_names[1].upper() or void_names[2]:
            pass
        else:
            if os.path.exists(dtn) is False:  # ;if directory doesn't exist then create it
                os.makedirs(dtn)
    if os.path.exists(gdn) is False:
        RCE(f"The file specified cannot be found \n {gdn}", 0)
    else:

        for i in r:
            preres.append(i)
        if len(preres[-1]) >= 4:
            if preres[-1].__contains__(preres[-2]):
                preres.pop(-1)
                preres.append(preres[-1])
            else:
                preres[-1][-1].rindex("\n")

    for fi in preres:
        pointer_hex_string = f"0x{fi}"
        translator = int(pointer_hex_string, 16)
        real_hex_value = translator
        res.append(real_hex_value)
    if orf is True:
        if dtn == void_names[0] or void_names[0].upper() or void_names[1] or void_names[1].upper() or void_names[2]:
            pass
            if os.path.exists(f"{dtn}{fn}") is False:
                destfile = open(f"{dtn}{fn}", "w+")
            destfile = open(f"{dtn}{fn}", "w+")
            destfile.write(str(f"Pre-result_001: {preres} {len(preres)}\n\nResult: {res} {len(res)}"))
        destfile.close()  # ;Prevent memory leakage
    if pr is True:
        p(f"pre-result_001: {preres}")
        p(f"Result: {res}")
    return res


def image_dict(targetpath: str, **kwargs):
    #   init/
    #       pych/ ; For Pycharm
    """
    Takes the files within a folder and translate the paths to a dictionary (targetname --> returnname)

    :param targetpath:
    :param kwargs:
    :return: Dict
    """
    #       vars/
    #           int/
    counter = 0
    #           str/
    t_path = targetpath
    #           dict/
    d = {}
    #           op/
    g_fit = os.listdir(t_path) # hey you get fit
    #           kwargs/
    #               extras/
    v_names = kwargs.get("EVerboseResults", False) # prints the process
    #   code/
    for file in g_fit:
        if file.__contains__(".jpg") or file.__contains__(".bmp") or file.__contains__(".png") or file.__contains__(".gif"):
            counter += 1
            d.update({counter: t_path+file})
    if v_names is True:
        flp(d)
    return d


# CLASSES------------------------------------------------------------------------------------------------------------------------------------------------------------------

class GF_MATH_CONVERT_FROM_LIST(object):
    def __init__(self):
        dummyvar = 0
        # init/
        #   VARS/
        #       LISTS/
        #           EXAMPLE/

    def hextoint(self, tl: list, dl: list):
        # FUNC/
        #   VARS/
        #       BOOL/
        islisthexed = False
        #       VARS/
        nothexval = 0
        #   CODE/
        for hexchecker in tl:
            for i in range(len(tl)):
                if type(hexchecker) != hex:
                    nothexval += 1
                    p()
        for value in tl:
            dl.append(int(value))


class GF_MUSICPLAYER_DICT_FORM(object):
    def __init__(self):
        dummyvar = 0
        # Func/
        #   Args/
        #       Vars/
        #           Dict/

    def play(self,
             target: dict,
             name: str,
             loop: int):
        filename = target.get(name)
        load.load(filename)
        if loop != 1 or 0:
            if randint(0, 100) == 1:
                p(f"Gull: Sorry I can't do that option {loop}, maybe tell me a yes or a no, or in what I can read a 1 or a 0 (representing on or off).")
            raise ValueError
        load.play(loop)

    def que(self,
            target: dict,
            name: str):
        filename = target.get(name)
        load.queue(filename)

    def queFromDict(self, target: dict):  # takes the values from the target and qeues them
        names = target
        for i in names:
            p(f"Gull: Putting {i} from your written list into my list")
            self.que(names, i)


class GF_DEVLOG(object):
    """
    This deals with Logging stuff into a file

    Functions Avaible
    ---------------------------
    RECORD_CONSOLE(self, what: sys.stderr, sys.stdout, sys.stdin)
    """

    def __init__(self,
                 filepath: str = "/Documents/SIS/EccoPY/LOGS/",
                 textfile: str = "DEVELOPERLOG",
                 filetype: str = ".log",
                 limit_fs: float = 0x164210,
                 isThisEnabled: bool = True):
        # Init/
        #   Args/
        #       Vars/
        #           STR/
        self.fp = (filepath)
        self.tf = (textfile)
        self.ft = (filetype)
        #           Float/
        self.lfs = (limit_fs)
        #           Booleans/
        self.ise = isThisEnabled
        #   STATEMENTS/
        #       Vars/
        #           STR/
        self.gun = gp.getuser()
        # ;Seagull

    def RECORD_CONSOLE(self, what):
        if what is not sys.stderr or sys.stdout or sys.stdin:
            p(f"Gull: ARGUMENT OF RECORD WHICH IS {what} ISN'T 'sys.stderr', 'sys.stdout OR 'sys.stdin'\n SOLUTION: Try changing 'what' to one of those options")
            raise ValueError
        if os.path.exists(f"/Users/{self.gun}{self.fp}") is False:
            os.makedirs(
                f"/Users/{self.gun}{self.fp}"
            )
        if os.path.exists(f"/Users/{self.gun}{self.fp}{self.tf + str(what)}{self.ft}") is False:
            what = open(f"/Users/{self.gun}{self.fp}{self.tf + str(what)}", "w+")
        if self.ise == True:
            if not os.path.getsize(f"/Users/{self.gun}{self.fp}{self.tf}") >= self.lfs:
                what = open(f"/Users/{self.gun}{self.fp}{self.tf}", "w+")
                if os.path.getsize(f"/Users/{self.gun}{self.fp}/{self.tf}") >= self.lfs:
                    what.close()
        else:
            if randint(0, 25) == 1:
                p("Ok")


class GF_WRITE_SETTING_FILES(object):
    """
    This deals with writing non-existant settings file/s (mainly uses '.ini' files ATM)

    Functions Avaible
    ---------------------------
    writeSettingsFile(self, dir: str *optional*, name: str *optional*)
    """

    def __init__(self):
        dummyvar = 0
        # Init/
        #   Args/
        #       Vars/
        #           STR/

    def writeSettingsFile(self,
                          dir: str = "/Documents/Seagulls/EccoPY/",
                          name: str = "Settings"):
        d = dir
        n = name
        gun = gp.getuser()
        subdir = f"{gun}/EP_S/"
        getdir = f"/Users/{gun}{d}{subdir}"

        if os.path.exists(getdir) is False:
            os.makedirs(getdir)
        elif os.path.exists(f"{getdir}/{n}.ini") is False:
            newfile = open(f"{getdir}/{n}.ini", "w+")  # Creates new file
            newfile.close()


class GF_MAPPING(object):
    """
    This deals with mapping

    Functions Avaible
    ---------------------------
    LoadMap(self, filepath)
    """

    def __init__(self):
        dummyvar = 0
        # Init/
        #   Args/
        #       Vars/
        #           STR/

    def loadMap(self, filepath):
        """
        This function is now mainly used for either basic maps or static HUD
        """
        f = open(filepath, "r")
        data = f.read()
        f.close()
        data = data.split('\n')
        gmap = []
        for bit in data:
            gmap.append(list(bit))
        return gmap


class GF_INIT(object):
    """
    Gull Framework Root class

    THIS INITIALLIZES ALL THE CLASSES SHOWNABOVE
    PLEASE DON'T MODIFY IF YOU DON'T KNOW WHAT YOUR DOING!!!
    """

    def __init__(self, assembly_mode: bool = False):
        p("\nGull Framework Shut Up Gull \n      By SeagullinSeagulls\n            Code: https://github.com/SeagullisLearningToCode/Gull-Framework (Might be outdated)\n")
        # Init/
        #   Args/
        #       Vars/
        #           Booleans/
        self.enable_assembly_mode = (assembly_mode)
        #   I/
        if self.enable_assembly_mode == True:  # gives it somewhat of an assembly feel
            self.m = GF_MAPPING  # Deals with mapping
            self.dl = GF_DEVLOG  # Logs stuff
            self.wsf = GF_WRITE_SETTING_FILES  # Writes INI files
            self.mpdf = GF_MUSICPLAYER_DICT_FORM  # Deals with playing music from dicts
            self.cl = GF_MATH_CONVERT_FROM_LIST  # Deals with converting lists/dicts to differnt types of values inside them
        else:  # New age stuff
            self.map = GF_MAPPING
            self.log = GF_DEVLOG
            self.set = GF_WRITE_SETTING_FILES
            self.musicPlayer = GF_MUSICPLAYER_DICT_FORM
            self.convert = GF_MATH_CONVERT_FROM_LIST
        #   S/ ; Sandbox like psuedo directory

# INIT_GULL_FRAMEWORK----------------------------------------------------------------------------------------------------------------------------------------------------------------

GF = GF_INIT(True)
