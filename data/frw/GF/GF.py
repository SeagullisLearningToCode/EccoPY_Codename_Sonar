"""
 __                     ___  __              ___       __   __
/ _` |  | |    |       |__  |__)  /\   |\/| |__  |  | /  \ |__) |__/
\__> \__/ |___ |___    |    |  \ /~~\  |  | |___ |/\| \__/ |  \ |  \
                                                    Version: 1.014 Shut Up Gull

This file stores very simple functions with the sole purpose of de-bloating the Main.py file (used to be)
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
import gc
from importlib import util

# ;VARIABLES-------------------------------------------------------------------------------------------------------------------

load = mixer.music

# ;Today's Date
td = date.today()

td_c_s = str(td)  # Converts the current date into a String
td_c_s_yo = td_c_s[0:4]  # Get year only
# ;Today's Time
tt = datetime.now()
GF_FILE_PATH = os.path.dirname(os.path.abspath(__file__))
GF_XTN_FOLDER_PATH = f"{GF_FILE_PATH}/EXT/"

# ;FUNCTIONS-------------------------------------------------------------------------------------------------------------------

# ;p function
# ;reason: same as the p function but made it faster to make a print statement by using a few characters
def p(t="passed", **kwargs):
    """
    Print
    Make print statements faster than python's print("Hello World")

    Example: p("Hello World")
    Output: Hello World
    """
    # CODE
    print(t)

# ;sps function
# ;Reason: easier and shorter
def sps(t: str):
    """
    Same thing as p() but adds in "passed"

    Example: sps("it")
    Output: passed it
    """
    # CODE
    p(f"passed {t}")


def flp(l: dict):
    """
    For in Loop Print From Dictionary
    """
    for key in l:
        p(f"{key}: {l.get(key)}")


# ;Get Presence
# ;reason: shorten it up a bit with the os.path.exists
def GetPresSpec(file: str, **kwargs):
    """
    Does the file exist

    Returns: None by default
    """
    # KWARGS
    GPS_RETURN_EXIST = kwargs.get('return_result', False)
    # OSPATH
    getpres = os.path.exists
    # CODE
    if GPS_RETURN_EXIST is False:
        p(getpres(file))

    return getpres(file)

# ;Raise Custom Error Function (RCEF)

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
    # INT
    error_type = et
    # CODE
    if error_type == 0:  # ;FNFE
        p(f"ERROR: {rfe}")
        raise FileNotFoundError
    elif error_type == 1:  # ;FEE
        p(f"ERROR: {rfe}")
        raise FileExistsError
    elif error_type == 2:  # ;NEBW
        p(f"WARNING: {rfe}")
    elif error_type == 3:  # ;EP_RTI_E
        p(f"ERROR: {rfe}")
        raise ValueError
    else:
        p("Can't go higher than 1 at the moment...\n Sorry About that :(")
        raise ValueError


def HVFFTAOHV(dirname: str,
              filename: str,
              destination: str,
              printresults: bool,
              outputresulttofile: bool):  # ;True = 1, False = 0
    """
    Hex Values From File To Array Of Hex Values
    This Function converts the hex values inside a text document and prints the values as an array
    """
    """
    Unfortunately what sucks about this function as of now is that I can possibly figure out a way to convert it into an actual hex value.
    """
    # STRINGS
    dfn = dirname  # ;Shortens dirname arg
    fn = filename  # ;Shortens and filename arg
    dtn = destination  # ;Shortens destination arg
    # BOOLEANS
    orf = outputresulttofile  # ;Shortens outputresulttofile arg (this makes it to where if you don't want the results made into a file, the function prints the result instead)
    pr = printresults  # ;Shortens the printresults arg
    # MISC
    gun = gp.getuser()  # ;Shortens and gets the current username

    # CODE
    gdn = (dfn + fn)  # ;Combine and Shortens dfn and fn which creates the full path
    gun_gdn = (gun + gdn)  # ;Combines and shortens gun and gdn which will do something
    fp_uni = ("/Users/" + gun + "/" + dtn + fn)  # ;Combines and shortens gun and dtn and fn
    pat = open(gdn, "r")  # ;Opens the file and gives python read and write access
    dat = pat.read()

    void_names = ["none", "null", "0"]
    preres = []
    res = []

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
    """
    Takes the files within a folder and translate the paths to a dictionary (targetname --> returnname)

    :param targetpath:
    :param kwargs:
    :return: Dict
    """
    # INT
    counter = 0
    # STRINGS
    t_path = targetpath
    # DICTIONARIES
    d = {}
    # OSPATH
    g_fit = os.listdir(t_path)  # ;hey you get fit
    # KWARGS_BOOLEANS
    v_names = kwargs.get("EVerboseResults", False)  # ;prints the process
    # CODE
    for file in g_fit:
        if file.__contains__(".jpg") or file.__contains__(".bmp") or file.__contains__(".png") or file.__contains__(".gif"):
            counter += 1
            d.update({counter: t_path + file})
    if v_names is True:
        flp(d)
    return d


def get_directory(targetpath: str, **kwargs):
    """
    Takes the files within a folder and translate the paths to a dictionary (targetname --> returnname)
    :param targetpath:
    :param kwargs:
    :return: Dict
    """
    # KWARGS
    GD_FILTER = kwargs.get("filter", None)
    GD_PRINT_DICT = kwargs.get("print_dict", True)
    # INT
    counter = 0
    # STRINGS
    t_path = targetpath
    # DICTIONARIES
    d = {}
    # OSPATH
    g_fit = os.listdir(t_path)
    # CODE
    for file in g_fit: # ;Loop through directory
        if GD_FILTER is not None: # ;if argument is not a NONE type
            if file.__contains__(GD_FILTER): # ;if filename contains a word, number or file type
                counter += 1
                d.update({counter: t_path + file})
        else:
            counter += 1
            d.update({counter: t_path + file})
    if GD_PRINT_DICT is True:
        flp(d)
    return d


def merge(target_list, **kwargs):
    """
    Takes a nested list into a single list

    :param target_list:
    :param kwargs:
    :return:
    """
    # LISTS
    tl = target_list
    i = []  # ;result var
    # KWARGS_BOOLEANS
    show_result = kwargs.get("show_result", False)
    # CODE

    for cat in tl:
        for value in cat:
            i.append(value)

    if show_result is True:
        p(i)

    return i


def rem_dupes_lst(target, **kwargs):
    # LIST
    new_list = []
    # KWARGS
    print_result = kwargs.get("print_result", False)
    sender = kwargs.get("send", None)
    # CODE
    if sender is not None:
        for i in target:
            if i not in target:
                sender.append(i)
    else:
        for i in target:
            if i not in target:
                new_list.append(i)

    if print_result is True:
        p(new_list)

    return new_list

def gen_iter_list(amount, **kwargs):
    # KWARGS
    GIL_PRINTRESULT = kwargs.get('print_result', False)
    GIL_LISTNAME = kwargs.get('listname', None)
    # ABS
    a = amount
    ln = GIL_LISTNAME
    pr = GIL_PRINTRESULT
    # LIST
    l = []
    # CODE
    if GIL_LISTNAME is not None:
        for i in range(a):
            ln.append(0)
        if pr is True:
            p(ln)
        return ln
    else:
        for i in range(a):
            l.append(0)
        if pr is True:
            p(f"gen_iter_list <print_result>: {l}")
        return l


# CLASSES------------------------------------------------------------------------------------------------------------------------------------------------------------------

class GF_MATH_CONVERT_FROM_LIST(object):
    def __init__(self):
        pass

    def hextoint(self, tl: list, dl: list):
        # INT
        nothexval = 0
        # CODE
        for hexchecker in tl:
            for i in range(len(tl)):
                if type(hexchecker) != hex:
                    nothexval += 1
        for value in tl:
            dl.append(int(value))


class GF_MUSICPLAYER_DICT_FORM(object):
    def __init__(self):
        pass

    def play(self, target: dict, name: str, loop: int):
        # DICTIONARIES
        filename = target.get(name)
        # CODE
        load.load(filename)
        if loop != 1 or 0:
            if randint(0, 100) == 1:
                p(f"Gull: Sorry I can't do that option {loop}, maybe tell me a yes or a no, or in what I can read a 1 or a 0 (representing on or off).")
            raise ValueError
        load.play(loop)

    def que(self,
            target: dict,
            name: str):
        # DICTIONARIES
        filename = target.get(name)
        # CODE
        load.queue(filename)

    def queFromDict(self, target: dict):  # takes the values from the target and qeues them
        # DICTIONARIES
        names = target
        # CODE
        for i in names:
            self.que(names, i)


class GF_DEVLOG(object):
    """
    This deals with Logging stuff into a file

    Functions Avaible
    ---------------------------
    RECORD_CONSOLE(self, what: sys.stderr, sys.stdout, sys.stdin)
    """

    def __init__(self, filepath: str = "/Documents/SIS/EccoPY/LOGS/", textfile: str = "DEVELOPERLOG", filetype: str = ".log", limit_fs: float = 0x164210, isThisEnabled: bool = True):
        # STRINGS
        self.fp = (filepath)
        self.tf = (textfile)
        self.ft = (filetype)
        # FLOATS
        self.lfs = (limit_fs)
        # BOOLEANS
        self.ise = isThisEnabled
        # STATEMENTS
        self.gun = gp.getuser()

    def RECORD_CONSOLE(self, what):
        # CODE
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
    writeSettingsFile(self, dir: str *optional*, name: str *optional*, **kwargs)
    """

    def __init__(self):
        super().__init__()
        # USERNAME
        self.gun = gp.getuser() # ;Get Current Username
        # DIRECTORIES
        self.subdir = f"{self.gun}/EP_S/"
        self.user_settings_folder = f"/Documents/Seagulls/EccoPY/"

    def writeSettingsFile(self, dir: str = "/Documents/Seagulls/EccoPY/", name: str = "Settings", **kwargs):
        # KWARGS
        WSF_RETURN_FILEPATH = kwargs.get('return_path', True)
        # STRINGS
        d = dir
        n = name
        getdir = f"/Users/{self.gun}{d}{self.subdir}"
        # CODE
        if os.path.exists(getdir) is False:
            os.makedirs(getdir)
        if os.path.exists(f"{getdir}{n}.ini") is False:
            newfile = open(f"{getdir}{n}.ini", "w+")  # Creates new file
            newfile.close()

        if WSF_RETURN_FILEPATH is True:
            path_name = f"{getdir}{n}.ini"
            p(path_name)
            return path_name


class GF_MAPPING(object):
    """
    This deals with mapping

    Functions Avaible
    ---------------------------
    LoadMap(self, filepath)
    """

    def __init__(self):
        pass

    def loadMap(self, filepath):
        """
        This function is now mainly used for either basic maps or static HUD
        """
        # DIRECTORIES
        f = open(filepath, "r")
        # CODE
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
    """

    def __init__(self, **kwargs):
        p("\nGull Framework \n      By SeagullinSeagulls\n            Code: https://github.com/SeagullisLearningToCode/Gull-Framework (Might be outdated)\n")
        # KWARGS_BOOLEANS
        self.enable_assembly_mode = kwargs.get("assembly_mode", True)
        self.print_faq_possible = kwargs.get("print_faq_possible", False)  # ;Prints why I start functions like this
        self.init_all_classes = kwargs.get("init_all", False) # ;Runs all initilized classes
        self.load_all_palm_trees = kwargs.get("load_all_palm_trees", False) # ;Loads all "Palm Trees"
        #   CODE
        if self.init_all_classes is True:
            if self.enable_assembly_mode is True:
                self.m = GF_MAPPING()
                self.dl = GF_DEVLOG()
                self.wsf = GF_WRITE_SETTING_FILES()
                self.mpdf = GF_MUSICPLAYER_DICT_FORM()
                self.cl = GF_MATH_CONVERT_FROM_LIST()
            else:
                self.map = GF_MAPPING()
                self.log = GF_DEVLOG()
                self.set = GF_WRITE_SETTING_FILES()
                self.musicPlayer = GF_MUSICPLAYER_DICT_FORM()
                self.convert = GF_MATH_CONVERT_FROM_LIST()
        if self.enable_assembly_mode is True:  # ;gives it somewhat of an assembly feel
            self.m = GF_MAPPING # ;Deals with mapping
            self.dl = GF_DEVLOG # ;Logs stuff
            self.wsf = GF_WRITE_SETTING_FILES # ;Writes INI files
            self.mpdf = GF_MUSICPLAYER_DICT_FORM # ;Deals with playing music from dicts
            self.cl = GF_MATH_CONVERT_FROM_LIST # ;Deals with converting lists/dicts to differnt types of values inside them
        else:  # ;New age stuff
            self.map = GF_MAPPING
            self.log = GF_DEVLOG
            self.set = GF_WRITE_SETTING_FILES
            self.musicPlayer = GF_MUSICPLAYER_DICT_FORM
            self.convert = GF_MATH_CONVERT_FROM_LIST
        if self.print_faq_possible is True:
            p(f"Why do start functions with comments first?\n\nWell I do that because it makes it more organized for me (I hope this does the same to you), I guess it reminds me of something I can't think of it on the top of my head though.")
        # ;Palm Trees (TEST)
        if self.load_all_palm_trees is True:
            pt_dir_dict = get_directory(targetpath=GF_XTN_FOLDER_PATH, filter='.py', print_dict=False)
            for palm_tree in range(len(pt_dir_dict)):
                ext = util.spec_from_file_location("*", pt_dir_dict[palm_tree + 1])
                ext_mod = util.module_from_spec(ext)
                ext.loader.exec_module(ext_mod)


# INIT_GULL_FRAMEWORK----------------------------------------------------------------------------------------------------------------------------------------------------------------

GF = GF_INIT(assembly_mode=True)
