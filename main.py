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
from data.frw.GF.EXT.GFTKE import *
from data.txt.men import *
from data.mu.Values import *


class MAIN_W_I(object):
    def __init__(self):
        # OSPATH
        self.main_dir = os.path.dirname(os.path.abspath(__file__))
        # DICTIONARIES
        self.i_dict = image_dict(f"{self.main_dir}/data/img/")
        # LISTS
        self.size = [1024, 450]
        # CONFIG_PARSER
        self.options_save = ConfigParser()
        # INT
        self.iterator_01 = 0
        self.iterator_02 = 0
        # INT_LIST
        self.iterator_03 = [0, 0, 0, 0, 0, 0, 0, 0]
        # BOOLEANS
        self.lessguimode = False
        self.converttopygame = False
        self.is_running = True
        # GULL_FRAMEWORK_EXT
        self.tp = pygame_Tk_Integration()
        self.keys = self.tp.CombineDictToOne()
        self.dbg_controller = self.tp.debug_controller()


class MAIN_WINDOW(Tk):
    def __init__(self, **kwargs):
        super().__init__()
        # CLASS CALL
        self.sc_init = MAIN_W_I()
        # TKINTER
        self["background"] = rgbtohex(34, 87, 165)
        self.title(winstrings["main"]["title"][0])

    def DRAW_CONTENTS(self):
        # TKINTER
        options_frame = Frame(self, background=rgbtohex(34, 87, 165)).grid(column=0, rowspan=5)

        def options_format():
            # BACKGROUND COLORS
            rb = 92 + 20
            gb = 133 + 20
            bb = 171 + 20
            # FOREGROUND COLORS
            rf = rb - (round(rb / 3))
            gf = gb - (round(gb / 3))
            bf = bb - (round(bb / 3))
            # LIST
            of_options_list = [self.PLAY_GAME, self.SETTINGS_MENU, self.SAVE_GAME, None, None]
            # CODE
            for subdict in winstrings["main"]["choices"]:
                label_background = rgbtohex(rb - (self.sc_init.iterator_01 * 4),
                                            gb - (self.sc_init.iterator_01 * 4),
                                            bb - (self.sc_init.iterator_01 * 4))
                label_foreground = rgbtohex(rf - (self.sc_init.iterator_01 * 4),
                                            gf - (self.sc_init.iterator_01 * 4),
                                            bf - (self.sc_init.iterator_01 * 4))
                option_func = of_options_list[self.sc_init.iterator_03[1]]
                p(type(option_func))
                if option_func is None:
                    Label(options_frame,
                          bg=label_background,
                          relief='groove',
                          fg=label_foreground,
                          bd=10,
                          text=subdict,
                          font='"Myanmar MN" 36').grid(column=0,
                                                       row=self.sc_init.iterator_01,
                                                       sticky="w")
                else:
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
                           command=option_func).grid(column=0,
                                                     row=self.sc_init.iterator_01
                                                     )
                self.sc_init.iterator_01 += 1
                self.sc_init.iterator_03[1] += 1

        def bkgrd_image():
            # IMAGES
            bkgrd = loadimage(self.sc_init.i_dict[1])
            # CODE
            Label(self, image=bkgrd, background=rgbtohex(34, 87, 165)).grid(column=1, row=0, rowspan=5, sticky="ne")
            gc.collect()

        bkgrd_image()
        options_format()
        Label(self, foreground='DarkBlue', text=winstrings["main"]["bottomtext"], font='"Arial Bold" 14').grid(column=1, row=4)

    def SETTINGS_MENU(self):
        # TKINTER
        set_menu = Toplevel()
        set_menu.title(winstrings["main"]["choices"][1])
        # NOTEBOOKS
        set_menu_nb = ttk.Notebook(set_menu)
        # FRAMES
        frame_01 = Frame(set_menu_nb)  # ;Video
        frame_02 = Frame(set_menu_nb)  # ;Audio
        frame_03 = Frame(set_menu_nb)  # ;Controller
        frame_04 = Frame(set_menu_nb)  # ;Game
        frame_05 = Frame(set_menu_nb)  # ;User Interface/Start-up
        # LISTS
        cb_bttns_str_list = [];
        option_button_list = cb_bttns_str_list  # ;confirm_bttns_string_list
        frme_list = [frame_01, frame_02, frame_03, frame_04, frame_05];
        f_l = frme_list
        # INT
        i = 0
        # INT_LISTS
        l = [0, 0, 0, 0, 0]

        # CODE
        def cancel():
            """
            Cancels changes
            :return:
            """
            # CODE
            self.forget(set_menu)

        def ok():
            """
            Writes changes to a config file and closes window
            :return:
            """
            # CODE
            p("Settings Saved")
            cancel()

        def apply():
            """
            Writes changes to a config file but doesn't close window
            :return:
            """
            # CODE
            p("Settings Saved")

        ls_bttns_list = [cancel, apply, ok]

        for save_buttons in winstrings['main']['save_options']:
            option_button_list.append(save_buttons)

        for choiceOptions in range(len(option_button_list)):
            i += 4.5
            m = 10 * i  # ;Math
            function_list = ls_bttns_list[choiceOptions]
            string_list = option_button_list[choiceOptions]
            Button(set_menu, text=string_list, command=function_list).grid(column=0, row=1, padx=m, sticky='e')
            p(m)

        def video():
            # INT
            i = 1
            # FRAMES
            frame_01_01 = Frame(frame_01, relief='solid', bd=5)
            # STRINGVARS
            rx = StringVar()  # ;Window Resolution-Width
            ry = StringVar()  # ;Window Resolution-Height
            x = StringVar()  # ;2D Resolution-Width
            y = StringVar()  # ;2D Resolution-Height
            # ENTRIES
            x_txt = Entry(frame_01_01, textvariable=x, width=5)
            y_txt = Entry(frame_01_01, textvariable=y, width=5)
            rx_txt = Entry(frame_01_01, textvariable=rx, width=5)
            ry_txt = Entry(frame_01_01, textvariable=ry, width=5)
            # CHECKBUTTONS
            dir_chkbtn = Checkbutton(frame_01_01, variable=r_disable_ripple, onvalue=True, offvalue=False)
            # SCALES
            wei_scale = Scale(frame_01_01, orient=HORIZONTAL, length=100, from_=weather_intensity_scale_limits[0], to=weather_intensity_scale_limits[1])
            # CODE

            for video_settings_strings in winstrings["main"]["options"]["Video"]["set"]:
                Label(frame_01_01, text=video_settings_strings).grid(column=0, row=i, sticky="w")
                i += 1

            # ;Window Res
            rx_txt.grid(column=1, row=1, sticky='w', padx=10)
            Label(frame_01_01, text=in_between_entries).grid(column=1, row=1, sticky='w', padx=70)
            ry_txt.grid(column=1, row=1, sticky='w', padx=90)

            # ;2D Res
            x_txt.grid(column=1, row=2, sticky='w', padx=10)
            Label(frame_01_01, text=in_between_entries).grid(column=1, row=2, sticky='w', padx=70)
            y_txt.grid(column=1, row=2, sticky='w', padx=90)

            frame_01_01.grid(column=0, row=0, padx=100)
            dir_chkbtn.grid(column=1, row=3, sticky='w', padx=10)
            wei_scale.grid(column=1, row=4, sticky='w', padx=10)

        def audio():
            # NOTEBOOKS
            sframe_02_01 = ttk.Notebook(frame_02)
            # FRAMES
            frame_02_01_01 = Frame(sframe_02_01)  # ;Music
            frame_02_01_02 = Frame(sframe_02_01)  # ;SFX
            # COMBO_BOXES
            combox_01 = ttk.Combobox(frame_02_01_01, width=34)  # ;Music
            combox_02 = ttk.Combobox(frame_02_01_02, width=34)  # ;SFX
            # SCALES
            volume_music = Scale(frame_02_01_01, orient=HORIZONTAL, length=200, from_=snd_vol_lmts[0], to=snd_vol_lmts[1])
            volume_sfx = Scale(frame_02_01_02, orient=HORIZONTAL, length=200, from_=snd_vol_lmts[0], to=snd_vol_lmts[1])
            # INT-ITER VARS ;Assembly like-vars
            i = 0
            q = 0
            a = 1
            z = 1
            # CODE

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
            # NOTEBOOK
            sframe_03_01 = ttk.Notebook(frame_03)  # ;Main
            usi_keyboard_type_bindings = ttk.Notebook(sframe_03_01)
            # FRAMES
            frame_keyboard = Frame(usi_keyboard_type_bindings)
            frame_joystick = Frame(sframe_03_01)
            frame02 = Frame(frame_03, relief="groove", bd=10)
            # COMBO_BOXES
            # ;Kyb-Movements
            kyb_mvm_up = ttk.Combobox(frame_keyboard)  # ;Up
            kyb_mvm_down = ttk.Combobox(frame_keyboard)  # ;Down
            kyb_mvm_left = ttk.Combobox(frame_keyboard)  # ;Left
            kyb_mvm_right = ttk.Combobox(frame_keyboard)  # ;Right
            # ;Kyb-ActionButtons
            kyb_ab_swim = ttk.Combobox(frame_keyboard)  # ;Swim
            kyb_ab_sonar = ttk.Combobox(frame_keyboard)  # ;Sonar
            kyb_ab_dash = ttk.Combobox(frame_keyboard)  # ;Dash
            # ;Kyb-PauseButtons
            kyb_pb_tom = ttk.Combobox(frame_keyboard)  # ;TurnOffMusic
            kyb_pb_tose = ttk.Combobox(frame_keyboard)  # ;TurnOffSFX
            # ;Kyb-DebugButtons
            kyb_dbb_sfps = ttk.Combobox(frame_keyboard)  # ;ShowFPS
            kyb_dbb_spos = ttk.Combobox(frame_keyboard)  # ;ShowPOS
            kyb_dbb_sall = ttk.Combobox(frame_keyboard)  # ;ShowAll
            # ;Jys-Movements
            jys_mvm_up = ttk.Combobox(frame_joystick)  # ;Up
            jys_mvm_down = ttk.Combobox(frame_joystick)  # ;Down
            jys_mvm_left = ttk.Combobox(frame_joystick)  # ;Left
            jys_mvm_right = ttk.Combobox(frame_joystick)  # ;Right
            # ;Jys-ActionButtons
            jys_ab_swim = ttk.Combobox(frame_joystick)  # ;Swim
            jys_ab_sonar = ttk.Combobox(frame_joystick)  # ;Sonar
            jys_ab_dash = ttk.Combobox(frame_joystick)  # ;Dash
            # ;Jys-PauseButtons
            jys_pb_tom = ttk.Combobox(frame_joystick)  # ;TurnOffMusic
            jys_pb_tose = ttk.Combobox(frame_joystick)  # ;TurnOffSFX
            # ;Jys-DebugButtons
            jys_dbb_sfps = ttk.Combobox(frame_joystick)  # ;ShowFPS
            jys_dbb_spos = ttk.Combobox(frame_joystick)  # ;ShowPOS
            jys_dbb_sall = ttk.Combobox(frame_joystick)  # ;ShowAll
            # LISTS
            usi_keyboard_type_bindings_list = [kyb_mvm_up, kyb_mvm_left, kyb_mvm_right, kyb_mvm_down, kyb_ab_dash, kyb_ab_swim, kyb_ab_sonar, kyb_pb_tom, kyb_pb_tose, kyb_dbb_sall, kyb_dbb_sfps, kyb_dbb_spos]  # ;For loop
            usi_joystick_type_bindings_list = [jys_mvm_up, jys_mvm_left, jys_mvm_right, jys_mvm_down, jys_ab_dash, jys_ab_swim, jys_ab_sonar, jys_pb_tom, jys_pb_tose, jys_dbb_sall, jys_dbb_sfps, jys_dbb_spos]  # ;For loop
            # INT_ITERS ;Generic assembly-like vars
            i = 0
            q = 0
            a = 0
            z = 0
            # INT_ITERS_ARR ;Generic assembly-like extended vars
            e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            # CODE

            # ;Keyboard
            usi_keyboard_type_bindings.add(frame_keyboard, text=winstrings["main"]["options"]["controlls".title()]["set"][1][0])

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
                ).grid(column=0, row=e[0] + e[1] + e[2] + 1, sticky="w", pady=5)

                for usi_joystick_type_bindings_db_b_strings in winstrings["main"]["options"]["Controlls"]["bindings"][3]:
                    Label(frame_keyboard, text=usi_joystick_type_bindings_db_b_strings).grid(column=0, row=(e[0] + e[1] + e[2] + e[3] + 2), sticky="w")
                    e[3] += 1

            for keyboard_combobox in usi_keyboard_type_bindings_list:
                keyboard_combobox['width'] = 15
                keyboard_combobox['values'] = self.sc_init.keys
                if not e[4] == 4 and not e[4] == 9:
                    keyboard_combobox.grid(column=1, row=e[4] + 1, padx=10)
                e[4] += 1

            for joystick_combobox in usi_joystick_type_bindings_list:
                joystick_combobox['width'] = 6
                joystick_combobox['values'] = self.sc_init.tp.pg_joys_list
                if len(self.sc_init.tp.pg_controllers) <= 0:
                    joystick_combobox['state'] = 'disabled'
                if not e[5] == 4 and not e[5] == 9:
                    joystick_combobox.grid(column=1, row=e[5] + 1, padx=10)
                e[5] += 1

            # ;Grid
            usi_keyboard_type_bindings.grid(column=0, row=0)
            frame02.grid(column=1, row=0)
            sframe_03_01.grid(column=0, row=0, padx=86)

        def game():
            # DICTIONARIES_ABSTRACTED
            difficulty_list = winstrings['main']['options']['Game']['set']['Difficulty']
            mod_list = winstrings['main']['options']['Game']['set']['Game']
            option_str_list = winstrings['main']['options']['Game']['set']
            # FRAMES
            frame_04_01 = Frame(frame_04, relief='solid', bd=5)  # ;Main Frame
            label_sect = Frame(frame_04_01)  # ;Left
            value_sect = Frame(frame_04_01)  # ;Right
            # COMBO_BOXES
            difficulty_list_combobox = ttk.Combobox(value_sect)
            mod_list_combobox = ttk.Combobox(value_sect)
            # MERGERS_LISTS
            difficulties = merge(difficulty_list)
            games = merge(mod_list)
            # INT_ITERS ;Generic assembly-like vars
            i = 0
            q = 0
            # CODE
            for game_label_string in option_str_list:
                Label(
                    label_sect,
                    text=game_label_string
                ).grid(column=0, row=i, pady=10, sticky='w')
                i += 1

        def user_interface():
            pass

            combobox_list = [difficulty_list_combobox, mod_list_combobox]
            options_val_list = [difficulties, games]

            for game_cb_list in range(len(combobox_list)):
                list = combobox_list[game_cb_list]
                n_val_list = options_val_list[game_cb_list]
                list['values'] = n_val_list
                list['state'] = "readonly"
                if game_cb_list == 0:
                    list['width'] = 18
                list.grid(column=0, row=q, padx=10, pady=10, sticky='w')
                q += 1

            # ;Grid
            frame_04_01.grid(column=0, row=0)
            label_sect.grid(column=0, row=0, rowspan=len(options_val_list), sticky='n')
            value_sect.grid(column=1, row=0, rowspan=len(options_val_list), sticky='n')

        for string in winstrings["main"]["options"]:
            if self.sc_init.iterator_03[0] >= 5:
                self.sc_init.iterator_03[0] = 0
            sel_list = f_l[self.sc_init.iterator_03[0]]
            set_menu_nb.add(sel_list, text=string)
            self.sc_init.iterator_02 += 1
            self.sc_init.iterator_03[0] += 1

        set_menu_nb.grid(column=0, row=0)

        video()
        audio()
        user_input()
        game()

    def PLAY_GAME(self):
        self.sc_init.is_running = False

    def SAVE_GAME(self):
        # INT
        time = randint(10, 5000)
        # CODE
        p("Saving Game...")
        for t in range(time):
            t -= 1
            if t == 0:
                p("Saved")

    def run(self):  # ;Now I'm going somewhere
        while self.sc_init.is_running is True:
            self.update_idletasks()
            self.update()

mw = MAIN_WINDOW()
mw.DRAW_CONTENTS()
mw.run()
