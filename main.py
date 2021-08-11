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
# frw
# GF
# EXT
from data.frw.GF.EXT.GFTKE import *
# txt
from data.txt.men import *
# mu
from data.mu.Values import *


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
        self.i_dict = image_dict(f"{self.main_dir}/data/img/")
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
        self.is_running = True


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
                                                        row=self.sc_init.iterator_01)
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
        #           nb/
        set_menu_nb = ttk.Notebook(set_menu)
        #               frme/
        frame_01 = ttk.Frame(set_menu_nb)  # ;Video
        frame_02 = ttk.Frame(set_menu_nb)  # ;Audio
        frame_03 = ttk.Frame(set_menu_nb)  # ;Controller
        frame_04 = ttk.Frame(set_menu_nb)  # ;Game
        #       int/
        i = 0

        # code/

        for choiceOptions in winstrings["main"]["save_options"]:
            Button(set_menu, text=choiceOptions).grid(column=i + 1, row=5)
            i += 1

        def video():
            # init/
            #   var/
            #       int/
            i = 1
            #       strv/
            #           res/
            x = StringVar()
            y = StringVar()
            #               ent/
            x_txt = Entry(frame_01, textvariable=x, width=5)
            y_txt = Entry(frame_01, textvariable=y, width=5)
            #           gme/
            rx = StringVar()
            ry = StringVar()
            #               ent/
            rx_txt = Entry(frame_01, textvariable=rx, width=5)
            ry_txt = Entry(frame_01, textvariable=ry, width=5)
            #       ckbn/
            #           dir/
            dir_chkbtn = Checkbutton(frame_01, variable=r_disable_ripple, onvalue=True, offvalue=False)
            #       scae/
            #           wei/
            wei_scale = Scale(frame_01, orient=HORIZONTAL, length=100, from_=weather_intensity_scale_limits[0], to=weather_intensity_scale_limits[1])

            # code/

            for video_settings_strings in winstrings["main"]["options"]["Video"]["set"]:
                Label(frame_01, text=video_settings_strings).grid(column=0, row=i, sticky="e")
                i += 1

            x_txt.grid(column=2, row=1)
            Label(frame_01, text=in_between_entries).grid(column=3, row=1)
            y_txt.grid(column=4, row=1)

            rx_txt.grid(column=2, row=2)
            Label(frame_01, text=in_between_entries).grid(column=3, row=2)
            ry_txt.grid(column=4, row=2)

            dir_chkbtn.grid(column=2, row=3)

            wei_scale.grid(column=2, row=4)

        def audio():
            # init/
            #   var/
            #       tk/
            #           nb/
            sframe_02_01 = ttk.Notebook(frame_02)
            #               frme/
            frame_02_01_01 = Frame(sframe_02_01)  # ;Music
            frame_02_01_02 = Frame(sframe_02_01)  # ;SFX
            #           cmbox/
            combox_01 = ttk.Combobox(frame_02_01_01)  # ;Music
            combox_02 = ttk.Combobox(frame_02_01_02)  # ;SFX
            #           scae/
            volume_music = Scale(frame_02_01_01, orient=HORIZONTAL, length=200, from_=snd_vol_lmts[0], to=snd_vol_lmts[1])
            volume_sfx = Scale(frame_02_01_02, orient=HORIZONTAL, length=200, from_=snd_vol_lmts[0], to=snd_vol_lmts[1])
            #       int/
            #           iters/ ; Generic assembly-like vars
            i = 0
            q = 0
            a = 1
            z = 1
            # code/

            for music_strings in winstrings["main"]["options"]["Audio"]["set"]["Music"]:
                Label(frame_02_01_01, text=music_strings).grid(column=0, row=i, sticky="w")
                i += 1

            for sfx_strings in winstrings["main"]["options"]["Audio"]["set"]["SFX"]:
                Label(frame_02_01_02, text=sfx_strings).grid(column=0, row=q, sticky="w")
                q += 1

            for audio_settings_strings in winstrings["main"]["options"]["Audio"]["set"]:
                if audio_settings_strings == "Music":
                    sframe_02_01.add(frame_02_01_01, text=audio_settings_strings)
                elif audio_settings_strings == "SFX":
                    sframe_02_01.add(frame_02_01_02, text=audio_settings_strings)

            for unvailable_music_option in range(2):
                Label(frame_02_01_01, text="not available".upper()).grid(column=1, row=a)
                a += 1

            for unvailable_sfx_option in range(2):
                Label(frame_02_01_02, text="not available".upper()).grid(column=1, row=z)
                z += 1

            combox_01['values'] = (winstrings["main"]["options"]["Audio"]["special"]["games"]["retail"][0])
            combox_01['state'] = "readonly"
            combox_01.grid(column=1, row=0)

            volume_music.grid(column=1, row=3)

            combox_02['values'] = (winstrings["main"]["options"]["Audio"]["special"]["games"]["retail"][0])
            combox_02['state'] = "readonly"
            combox_02.grid(column=1, row=0)

            volume_sfx.grid(column=1, row=3)

            sframe_02_01.grid(column=0, row=1)

        def user_input():
            # init/
            #   var/
            #       tk/
            #           nb/
            sframe_03_01 = ttk.Notebook(frame_03)  # ;Main
            usi_keyboard_type_bindings = ttk.Notebook(sframe_03_01)
            #               nnb/
            usi_keyboard_type_bindings_movement = ttk.Notebook(usi_keyboard_type_bindings)
            #           frme/
            frame_keyboard = Frame(usi_keyboard_type_bindings)
            frame_joystick = Frame(sframe_03_01)
            frame02 = Frame(sframe_03_01)
            #               nfrme/
            frame_usi_type_movement = Frame(usi_keyboard_type_bindings_movement)
            #           ckbn/
            #               dm/
            ckbn_e_dm = Checkbutton(frame02, text="Debug Mode", variable=usi_enable_debugmode, onvalue=True, offvalue=False)
            #       int/
            #           iters/ ;Generic assembly-like vars
            i = 0
            q = 0
            a = 0
            z = 0
            #           iters_arr/ ;Generic assembly-like extended vars
            e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            # code/

            # ;Keyboard
            usi_keyboard_type_bindings.add(frame_keyboard, text=winstrings["main"]["options"]["controlls".title()]["set"][1][0])
            usi_keyboard_type_bindings_movement.add(frame_usi_type_movement, text=winstrings["main"]["options"]["controlls".title()]["bindings_names"][0])

            # ;Keyboard/Movement/
            Label(
                frame_keyboard,
                text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][0],
                font='"Helvectica Light" 16',
                relief="groove",
                bd=5
            ).grid(column=0, row=0, sticky="w")

            for usi_keyboard_type_bindings_movement_strings in winstrings["main"]["options"]["Controlls"]["bindings"][0]:
                Label(frame_keyboard, text=usi_keyboard_type_bindings_movement_strings).grid(column=0, row=i + 2, sticky="w")
                i += 1

            # ;Keyboard/ActionButtons/
            Label(
                frame_keyboard,
                text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][1],
                font='"Helvectica Light" 16',
                relief="groove",
                bd=5
            ).grid(column=0, row=i+2, sticky="w")

            for usi_keyboard_type_bindings_ab_strings in winstrings["main"]["options"]["Controlls"]["bindings"][1]:
                Label(frame_keyboard, text=usi_keyboard_type_bindings_ab_strings).grid(column=0, row=(i + q + 3), sticky="w")
                q += 1

            # ;Keyboard/PauseButtons/
            Label(
                frame_keyboard,
                text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][2],
                font='"Helvectica Light" 16',
                relief="groove",
                bd=5
            ).grid(column=0, row=i+q+1, sticky="w")

            for usi_keyboard_type_bindings_pb_strings in winstrings["main"]["options"]["Controlls"]["bindings"][2]:
                Label(frame_keyboard, text=usi_keyboard_type_bindings_pb_strings).grid(column=0, row=(i + q + a + 2), sticky="w")
                a += 1

            # ;Keyboard/DebugButtons/
            if usi_enable_debugmode is True:
                dbm_l = Label(
                    frame_keyboard,
                    text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][2],
                    font='"Helvectica Light" 16',
                    relief="groove",
                    bd=5
                ).grid(column=0, row=i + q + 2, sticky="w")
                for usi_keyboard_type_bindings_db_b_strings in winstrings["main"]["options"]["Controlls"]["bindings"][1]:
                    Label(frame_keyboard, text=usi_keyboard_type_bindings_db_b_strings).grid(column=0, row=(i + q + a + 3), sticky="w")
                    a += 1
            # ;Keyboard/DebugButtons/CIDMIO/
            ckbn_e_dm.grid()

            # ;Joystick
            usi_keyboard_type_bindings.add(frame_joystick, text=winstrings["main"]["options"]["controlls".title()]["set"][1][1])



            # ;Grid
            usi_keyboard_type_bindings.grid(column=0, row=0)
            frame02.grid(column=1, row=0)
            sframe_03_01.grid(column=0, row=0)

        for string in winstrings["main"]["options"]:
            if not self.sc_init.iterator_02 == 4:
                if string == "Video":
                    set_menu_nb.add(frame_01, text=string)
                elif string == "Audio":
                    set_menu_nb.add(frame_02, text=string)
                elif string == "Controlls":
                    set_menu_nb.add(frame_03, text=string)
            self.sc_init.iterator_02 += 1

        set_menu_nb.grid(column=0, row=0)

        video()
        audio()
        user_input()

    def PLAY_GAME(self):
        self.sc_init.is_running = False

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
        while self.sc_init.is_running is True:
            self.DRAW_CONTENTS()
            self.mainloop()


mw = MAIN_WINDOW()
mw.run()
