# Test Pseudo Menu
"""
File Structure
---------------

SonarMap/
    data/
        fnt/ ; Font Folder
        frw/ ; External Frameworks Folder
        img/ ; Image Folder
        mu/ ; Menu Scripts
        snd/ ; Sound Folder
        txt/ ; Text String Folder
"""
# Imports
from data.frw.GF.EXT.GFTKE import *
from data.txt.men import *


# Vars
# Code
#   Classes
class MAIN_W_I(object):
    def __init__(self):
        # init/
        #   var/
        #       osp/
        self.main_dir = os.path.dirname(os.path.abspath(__file__))
        #           dicts/
        self.i_dict = image_dict(f"{self.main_dir}/data/img/", EVerboseResults=True)
        #           arrs/
        self.size = [1024, 450]
        #           cfgs/
        self.options_save = ConfigParser()
        #           Int/
        self.iterator_01 = 0
        self.iterator_02 = 0
        #           Bools/
        self.lessguimode = False
        self.converttopygame = False


class MAIN_WINDOW(Tk):
    def __init__(self, **kwargs):
        # init/
        #   sup/
        super().__init__()
        #       var/
        #           i/
        self.sc_init = MAIN_W_I()
        #       TK/
        self["background"] = rgbtohex(34, 87, 165)
        #           T/
        self.title(winstrings["main"]["title"][0])

    def DRAW_CONTENTS(self):
        # init/
        #   vars/
        #       tk/
        options_frame = Frame(self, background=rgbtohex(34, 87, 165)).grid(column=0, rowspan=5)

        def options_format():
            # init/
            #   var/
            #       int/
            #           background/
            rb = 92 + 20
            gb = 133 + 20
            bb = 171 + 20
            #           foreground/
            rf = rb - (round(rb / 3))
            gf = gb - (round(gb / 3))
            bf = bb - (round(bb / 3))
            # code/
            for subdict in winstrings["main"]["choices"]:
                # Background
                label_background = rgbtohex(rb - (self.sc_init.iterator_01 * 4),
                                            gb - (self.sc_init.iterator_01 * 4),
                                            bb - (self.sc_init.iterator_01 * 4))
                # Foreground
                label_foreground = rgbtohex(rf - (self.sc_init.iterator_01 * 4),
                                            gf - (self.sc_init.iterator_01 * 4),
                                            bf - (self.sc_init.iterator_01 * 4))
                if self.sc_init.iterator_01 == 0:
                    Button(options_frame,
                           highlightcolor=label_background,
                           activebackground=label_background,
                           activeforeground=label_foreground,
                           bg=label_background,
                           relief='groove',
                           fg=label_foreground,
                           bd=10,
                           text=subdict,
                           font='"Myanmar MN" 36',
                           command=self.PLAY_GAME).grid(column=0,
                                                        row=self.sc_init.iterator_01,
                                                        sticky="w")
                elif self.sc_init.iterator_01 == 1:
                    Button(options_frame,
                           highlightcolor=label_background,
                           activebackground=label_background,
                           activeforeground=label_foreground,
                           bg=label_background,
                           relief='groove',
                           fg=label_foreground,
                           bd=10,
                           text=subdict,
                           font='"Myanmar MN" 36',
                           command=self.SETTINGS_MENU).grid(column=0,
                                                            row=self.sc_init.iterator_01,
                                                            sticky="w")
                else:
                    Label(options_frame,
                          bg=label_background,
                          relief='groove',
                          fg=label_foreground,
                          bd=10,
                          text=subdict,
                          font='"Myanmar MN" 36').grid(column=0,
                                                       row=self.sc_init.iterator_01,
                                                       sticky="w")
                self.sc_init.iterator_01 += 1

        def bkgrd_image():
            # init/
            #   var/
            #       str/
            #           img/
            bkgrd = loadimage(self.sc_init.i_dict[2])
            # code/
            Label(self, image=bkgrd, background=rgbtohex(34, 87, 165)).grid(column=1, row=0, rowspan=5, sticky="ne")

        bkgrd_image()
        options_format()
        Label(self, foreground='DarkBlue', text=winstrings["main"]["bottomtext"], font='"Arial Bold" 14').grid(column=1, row=4)

    def SETTINGS_MENU(self):
        # init/
        #   var/
        #       tk/
        set_menu = Toplevel()
        set_menu.title(winstrings["main"]["choices"][1])
        smf = Frame(set_menu, bg="black").grid(column=0,
                                               row=0)

        # code/
        def video():
            # init/
            #   var/
            #       int/
            i = 1
            # code/
            for video_settings_strings in winstrings["main"]["options"]["Video"]["set"]:
                Label(smf, text=video_settings_strings).grid(column=0, row=i)
                i += 1

        for string in winstrings["main"]["options"]:
            if not self.sc_init.iterator_02 == 4:
                if string == "Video":
                    Button(set_menu, text=string,
                           relief="ridge",
                           font="'Helvetica' 16",
                           command=video).grid(column=self.sc_init.iterator_02,
                                               row=0)
            self.sc_init.iterator_02 += 1

    def PLAY_GAME(self):
        sys.exit(0)

    def SAVE_GAME(self):
        # init/
        #   var/
        #       int/
        time = randint(10, 5000)
        # code/
        p("Saving Game...")
        for t in range(time):
            t -= 1
            if t == 0:
                p("Saved")

    def run(self):
        self.DRAW_CONTENTS()
        self.mainloop()


mw = MAIN_WINDOW()
mw.run()
