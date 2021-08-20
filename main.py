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
        # INIT/
        #   VAR/
        #       OSP/
        self.main_dir = os.path.dirname(os.path.abspath(__file__))
        #           DICT/
        self.i_dict = image_dict(f"{self.main_dir}/data/img/")
        #           ARR/
        self.size = [1024, 450]
        #           CFGS/
        self.options_save = ConfigParser()
        #           INT/
        self.iterator_01 = 0
        self.iterator_02 = 0
        #           BOOLEANS/
        self.lessguimode = False
        self.converttopygame = False
        self.is_running = True
        #   GFE/
        self.tp = pygame_Tk_Integration()
        #       INIT/
        #           KEYS/
        self.keys = self.tp.CombineDictToOne()
        #           CBTTNS/
        #               DBG/
        self.dbg_controller = self.tp.debug_controller()


class MAIN_WINDOW(Tk):
    def __init__(self, **kwargs):
        # INIT/
        #   SUP/
        super().__init__()
        #       VAR/
        #           I/
        self.sc_init = MAIN_W_I()
        #       TK/
        self["background"] = rgbtohex(34, 87, 165)
        #           T/
        self.title(winstrings["main"]["title"][0])

    def DRAW_CONTENTS(self):
        # INIT/
        #   VARS/
        #       TK/
        options_frame = Frame(self, background=rgbtohex(34, 87, 165)).grid(column=0, rowspan=5)

        def options_format():
            # INIT/
            #   VAR/
            #       INT/
            #           BKGRD/
            rb = 92 + 20
            gb = 133 + 20
            bb = 171 + 20
            #           FGRD/
            rf = rb - (round(rb / 3))
            gf = gb - (round(gb / 3))
            bf = bb - (round(bb / 3))
            # CODE/
            for subdict in winstrings["main"]["choices"]:
                label_background = rgbtohex(rb - (self.sc_init.iterator_01 * 4),
                                            gb - (self.sc_init.iterator_01 * 4),
                                            bb - (self.sc_init.iterator_01 * 4))
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
                                                        row=self.sc_init.iterator_01
                                                        )
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
                                                            row=self.sc_init.iterator_01
                                                            )
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
            # INIT/
            #   VAR/
            #       STR/
            #           IMG/
            bkgrd = loadimage(self.sc_init.i_dict[2])
            # CODE/
            Label(self, image=bkgrd, background=rgbtohex(34, 87, 165)).grid(column=1, row=0, rowspan=5, sticky="ne")

        bkgrd_image()
        options_format()
        Label(self, foreground='DarkBlue', text=winstrings["main"]["bottomtext"], font='"Arial Bold" 14').grid(column=1, row=4)

    def SETTINGS_MENU(self):
        # INIT/
        #   VAR/
        #       TK/
        set_menu = Toplevel()
        set_menu.title(winstrings["main"]["choices"][1])
        #           NB/
        set_menu_nb = ttk.Notebook(set_menu)
        #               FRME/
        frame_01 = Frame(set_menu_nb)  # ;Video
        frame_02 = Frame(set_menu_nb)  # ;Audio
        frame_03 = Frame(set_menu_nb)  # ;Controller
        frame_04 = Frame(set_menu_nb)  # ;Game
        #       INT/
        i = 0

        # CODE/
        def cancel():
            # CODE/
            self.forget(set_menu)

        for choiceOptions in winstrings["main"]["save_options"]:
            if choiceOptions == "Ok":
                pass
            elif choiceOptions == "Apply":
                pass
            elif choiceOptions == "Cancel":
                Button(set_menu, text=choiceOptions, command=cancel).grid(column=i + 1, row=5)
            i += 1

        def video():
            # INIT/
            #   VAR/
            #       INT/
            i = 1
            #       STRV/
            #           RES/
            x = StringVar()
            y = StringVar()
            #               ENT/
            x_txt = Entry(frame_01, textvariable=x, width=5)
            y_txt = Entry(frame_01, textvariable=y, width=5)
            #           GME/
            rx = StringVar()
            ry = StringVar()
            #               ENT/
            rx_txt = Entry(frame_01, textvariable=rx, width=5)
            ry_txt = Entry(frame_01, textvariable=ry, width=5)
            #       CKBN/
            #           DIR/
            dir_chkbtn = Checkbutton(frame_01, variable=r_disable_ripple, onvalue=True, offvalue=False)
            #       SCAE/
            #           WEI/
            wei_scale = Scale(frame_01, orient=HORIZONTAL, length=100, from_=weather_intensity_scale_limits[0], to=weather_intensity_scale_limits[1])

            # CODE/

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
            # INIT/
            #   VAR/
            #       TK/
            #           NB/
            sframe_02_01 = ttk.Notebook(frame_02)
            #               FRME/
            frame_02_01_01 = Frame(sframe_02_01)  # ;Music
            frame_02_01_02 = Frame(sframe_02_01)  # ;SFX
            #           CMBOX/
            combox_01 = ttk.Combobox(frame_02_01_01)  # ;Music
            combox_02 = ttk.Combobox(frame_02_01_02)  # ;SFX
            #           SCAE/
            volume_music = Scale(frame_02_01_01, orient=HORIZONTAL, length=200, from_=snd_vol_lmts[0], to=snd_vol_lmts[1])
            volume_sfx = Scale(frame_02_01_02, orient=HORIZONTAL, length=200, from_=snd_vol_lmts[0], to=snd_vol_lmts[1])
            #       INT/
            #           ITERS/ ; Generic assembly-like vars
            i = 0
            q = 0
            a = 1
            z = 1
            # CODE/

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
            # INIT/
            #   VAR/
            #       TK/
            #           NB/
            sframe_03_01 = ttk.Notebook(frame_03)  # ;Main
            usi_keyboard_type_bindings = ttk.Notebook(sframe_03_01)
            usi_keyboard_type_bindings_movement = ttk.Notebook(usi_keyboard_type_bindings)
            #           FRME/
            frame_keyboard = Frame(usi_keyboard_type_bindings)
            frame_joystick = Frame(sframe_03_01)
            frame02 = Frame(frame_03, relief="groove", bd=10)
            frame_usi_type_movement = Frame(usi_keyboard_type_bindings_movement)
            #           CMBOX/
            #               KYB/ ;Keyboard
            #                   MVM/
            kyb_mvm_up = ttk.Combobox(frame_keyboard) # ;Up
            kyb_mvm_down = ttk.Combobox(frame_keyboard) # ;Down
            kyb_mvm_left = ttk.Combobox(frame_keyboard) # ;Left
            kyb_mvm_right = ttk.Combobox(frame_keyboard) # ;Right
            #                   AB/
            kyb_ab_swim = ttk.Combobox(frame_keyboard) # ;Swim
            kyb_ab_sonar = ttk.Combobox(frame_keyboard) # ;Sonar
            kyb_ab_dash = ttk.Combobox(frame_keyboard) # ;Dash
            #                   PB/
            kyb_pb_tom = ttk.Combobox(frame_keyboard) # ;TurnOffMusic
            kyb_pb_tose = ttk.Combobox(frame_keyboard) # ;TurnOffSFX
            #                   DBB/
            kyb_dbb_sfps = ttk.Combobox(frame_keyboard) # ;ShowFPS
            kyb_dbb_spos = ttk.Combobox(frame_keyboard) # ;ShowPOS
            kyb_dbb_sall = ttk.Combobox(frame_keyboard) # ;ShowAll
            #               JYS/ ;Joystick
            #                   MVM/
            jys_mvm_up = ttk.Combobox(frame_joystick) # ;Up
            jys_mvm_down = ttk.Combobox(frame_joystick) # ;Down
            jys_mvm_left = ttk.Combobox(frame_joystick) # ;Left
            jys_mvm_right = ttk.Combobox(frame_joystick) # ;Right
            #                   AB/
            jys_ab_swim = ttk.Combobox(frame_joystick) # ;Swim
            jys_ab_sonar = ttk.Combobox(frame_joystick) # ;Sonar
            jys_ab_dash = ttk.Combobox(frame_joystick) # ;Dash
            #                   PB/
            jys_pb_tom = ttk.Combobox(frame_joystick) # ;TurnOffMusic
            jys_pb_tose = ttk.Combobox(frame_joystick) # ;TurnOffSFX
            #                   DBB/
            jys_dbb_sfps = ttk.Combobox(frame_joystick) # ;ShowFPS
            jys_dbb_spos = ttk.Combobox(frame_joystick) # ;ShowPOS
            jys_dbb_sall = ttk.Combobox(frame_joystick) # ;ShowAll
            #       DICT/
            usi_keyboard_type_bindings_list = [kyb_mvm_up, kyb_mvm_left, kyb_mvm_right, kyb_mvm_down, kyb_ab_dash, kyb_ab_swim, kyb_ab_sonar, kyb_pb_tom, kyb_pb_tose, kyb_dbb_sall, kyb_dbb_sfps, kyb_dbb_spos] # ;For loop
            usi_joystick_type_bindings_list = [jys_mvm_up, jys_mvm_left, jys_mvm_right, jys_mvm_down, jys_ab_dash, jys_ab_swim, jys_ab_sonar, jys_pb_tom, jys_pb_tose, jys_dbb_sall, jys_dbb_sfps, jys_dbb_spos] # ;For loop
            #       INT/
            #           ITERS/ ;Generic assembly-like vars
            i = 0
            q = 0
            a = 0
            z = 0
            #           ITERS_ARR/ ;Generic assembly-like extended vars
            e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            # CODE/

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
                Label(frame_keyboard, text=usi_keyboard_type_bindings_movement_strings).grid(column=0, row=i + 1, sticky="w")
                i += 1

            # ;Keyboard/ActionButtons/
            Label(
                frame_keyboard,
                text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][1],
                font='"Helvectica Light" 16',
                relief="groove",
                bd=5
            ).grid(column=0, row=i + 1, sticky="w")

            for usi_keyboard_type_bindings_ab_strings in winstrings["main"]["options"]["Controlls"]["bindings"][1]:
                Label(frame_keyboard, text=usi_keyboard_type_bindings_ab_strings).grid(column=0, row=(i + q + 2), sticky="w")
                q += 1

            # ;Keyboard/PauseButtons/
            Label(
                frame_keyboard,
                text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][2],
                font='"Helvectica Light" 16',
                relief="groove",
                bd=5
            ).grid(column=0, row=i + q + 1, sticky="w")

            for usi_keyboard_type_bindings_pb_strings in winstrings["main"]["options"]["Controlls"]["bindings"][2]:
                Label(frame_keyboard, text=usi_keyboard_type_bindings_pb_strings).grid(column=0, row=(i + q + a + 2), sticky="w")
                a += 1

            # ;Keyboard/DebugButtons/
            if usi_enable_debugmode is True:
                Label(
                    frame_keyboard,
                    text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][3],
                    font='"Helvectica Light" 16',
                    relief="groove",
                    bd=5,
                    anchor="center"
                ).grid(column=0, row=i + q + a + 1, sticky="w")

                for usi_keyboard_type_bindings_db_b_strings in winstrings["main"]["options"]["Controlls"]["bindings"][3]:
                    Label(frame_keyboard, text=usi_keyboard_type_bindings_db_b_strings).grid(column=0, row=(i + q + a + z + 1), sticky="w")
                    z += 1

            # ;Joystick
            usi_keyboard_type_bindings.add(frame_joystick, text=winstrings["main"]["options"]["controlls".title()]["set"][1][1])

            # ;Joystick/Movement/
            Label(
                frame_joystick,
                text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][0],
                font='"Helvectica Light" 16',
                relief="groove",
                bd=5
            ).grid(column=0, row=0, sticky="w")

            for usi_joystick_type_bindings_movement_strings in winstrings["main"]["options"]["Controlls"]["bindings"][0]:
                Label(frame_joystick, text=usi_joystick_type_bindings_movement_strings).grid(column=0, row=e[0] + 1, sticky="w")
                e[0] += 1

            # ;Joystick/ActionButtons/
            Label(
                frame_joystick,
                text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][1],
                font='"Helvectica Light" 16',
                relief="groove",
                bd=5
            ).grid(column=0, row=e[0] + 1, sticky="w")

            for usi_joystick_type_bindings_ab_strings in winstrings["main"]["options"]["Controlls"]["bindings"][1]:
                Label(frame_joystick, text=usi_joystick_type_bindings_ab_strings).grid(column=0, row=(e[0] + e[1] + 2), sticky="w")
                e[1] += 1

            # ;Joystick/PauseButtons/
            Label(
                frame_joystick,
                text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][2],
                font='"Helvectica Light" 16',
                relief="groove",
                bd=5
            ).grid(column=0, row=e[0] + e[1] + 1, sticky="w")

            for usi_joystick_type_bindings_pb_strings in winstrings["main"]["options"]["Controlls"]["bindings"][2]:
                Label(frame_joystick, text=usi_joystick_type_bindings_pb_strings).grid(column=0, row=(e[0] + e[1] + e[2] + 2), sticky="w")
                e[2] += 1

            # ;Joystick/DebugButtons/
            if usi_enable_debugmode is True:
                Label(
                    frame_joystick,
                    text=winstrings["main"]["options"]['controlls'.title()]['bindings_names'][3],
                    font='"Helvectica Light" 16',
                    relief="groove",
                    bd=5,
                    anchor="center"
                ).grid(column=0, row=e[0] + e[1] + e[2] + 1, sticky="w")

                for usi_joystick_type_bindings_db_b_strings in winstrings["main"]["options"]["Controlls"]["bindings"][3]:
                    Label(frame_keyboard, text=usi_joystick_type_bindings_db_b_strings).grid(column=0, row=(e[0] + e[1] + e[2] + e[3] + 2), sticky="w")
                    e[3] += 1

            for keyboard_combobox in usi_keyboard_type_bindings_list:
                keyboard_combobox['width'] = 15
                keyboard_combobox['values'] = self.sc_init.keys
                if not e[4] == 4 and not e[4] == 9:
                    keyboard_combobox.grid(column=1, row=e[4]+1)
                e[4] += 1

            for joystick_combobox in usi_joystick_type_bindings_list:
                joystick_combobox['width'] = 6
                joystick_combobox['values'] = self.sc_init.tp.pg_joys_list
                if len(self.sc_init.tp.pg_controllers) <= 0:
                    joystick_combobox['state'] = 'disabled'
                if not e[5] == 4 and not e[5] == 9:
                    joystick_combobox.grid(column=1, row=e[5]+1)
                e[5] += 1

            # ;Grid
            usi_keyboard_type_bindings.grid(column=0, row=0)
            frame02.grid(column=1, row=0)
            sframe_03_01.grid(column=0, row=0)

        def game():
            # INIT/
            #   VAR/
            #       ABS/
            #           ARR/
            difficulty_list = winstrings['main']['options']['Game']['set']['Difficulty']
            mod_list = winstrings['main']['options']['Game']['set']['Game']
            option_str_list = winstrings['main']['options']['Game']['set']
            #       PG/
            #           FRME/
            label_sect = Frame(frame_04) # ;Left
            value_sect = Frame(frame_04) # ;Right
            #           CMBOX/
            difficulty_list_combobox = ttk.Combobox(value_sect)
            mod_list_combobox = ttk.Combobox(value_sect)
            #       ARR/
            difficulties = merge(difficulty_list)
            games = merge(mod_list)
            #       INT/
            #           ITERS/ ;Generic assembly-like vars
            i = 0
            q = 0
            # CODE/
            for game_label_string in option_str_list:
                Label(
                    label_sect,
                    text=game_label_string
                ).grid(column=0, row=i, pady=10, sticky='w')
                i += 1

            # INIT/VAR/ABS/ARR
            combobox_list = [difficulty_list_combobox, mod_list_combobox]
            options_val_list = [difficulties, games]
            # CODE/
            for game_cb_list in range(len(combobox_list)):
                list = combobox_list[game_cb_list]
                n_val_list = options_val_list[game_cb_list]
                list['values'] = n_val_list
                if game_cb_list == 0:
                    list['width'] = 18
                list.grid(column=0, row=q, padx=10, pady=10, sticky='w')
                q += 1

            # ;Grid
            label_sect.grid(column=0, row=0, rowspan=len(options_val_list), sticky='n')
            value_sect.grid(column=1, row=0, rowspan=len(options_val_list), sticky='n')

        for string in winstrings["main"]["options"]:
            if not self.sc_init.iterator_02 == 5:
                if string == "Video":
                    set_menu_nb.add(frame_01, text=string)
                elif string == "Audio":
                    set_menu_nb.add(frame_02, text=string)
                elif string == "Controlls":
                    set_menu_nb.add(frame_03, text=string)
                elif string == "Game":
                    set_menu_nb.add(frame_04, text=string)
            self.sc_init.iterator_02 += 1

        set_menu_nb.grid(column=0, row=0)

        video()
        audio()
        user_input()
        game()

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

    def run(self): # Now I'm going somewhere
        while self.sc_init.is_running is True:
            self.update_idletasks()
            self.update()


mw = MAIN_WINDOW()
mw.DRAW_CONTENTS()
mw.run()
