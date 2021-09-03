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
        self.options_changes = {
            "Video": [],
            "Audio-Music": [],
            "Audio-SFX": [],
            "Controlls-Keyboard": [],
            "Controlls-Joystick": [],
            "Game": [],
            "UI": [],
        }
        # CONFIG_PARSER
        self.options_save = ConfigParser()
        # INT
        self.iterator_01 = 0
        self.iterator_02 = 0
        # INT_LIST
        self.iterator_03 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        # BOOLEANS
        self.lessguimode = False
        self.converttopygame = False
        self.is_running = True
        # GF
        self.wsf = GF.wsf()
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
        self["background"] = rgb(34, 87, 165)
        self.title(winstrings["main"]["title"][0])
        # THEME
        self.style = ttk.Style()
        self.style.theme_use('classic')
        # CODE

    def DRAW_CONTENTS(self):
        # TKINTER
        options_frame = Frame(self, background=rgb(34, 87, 165)).grid(column=0, rowspan=5)

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
                label_background = rgb(rb - (self.sc_init.iterator_01 * 4),
                                       gb - (self.sc_init.iterator_01 * 4),
                                       bb - (self.sc_init.iterator_01 * 4))
                label_foreground = rgb(rf - (self.sc_init.iterator_01 * 4),
                                       gf - (self.sc_init.iterator_01 * 4),
                                       bf - (self.sc_init.iterator_01 * 4))
                option_func = of_options_list[self.sc_init.iterator_03[1]]
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
            Label(self, image=bkgrd, background=rgb(34, 87, 165)).grid(column=1, row=0, rowspan=5, sticky="ne")
            gc.collect()

        bkgrd_image()
        options_format()
        Label(self, foreground='DarkBlue', text=winstrings["main"]["bottomtext"], font='"Arial Bold" 14').grid(column=1, row=4)

    def SETTINGS_MENU(self):
        # COLORS_LIST_OFFSETS
        sm_bkgrd_clr = [1.6, 1.6, 1.5]
        sm_colors_presets = {
            "grey": rgb(round(236 / sm_bkgrd_clr[0]), round(236 / sm_bkgrd_clr[1]), round(236 / sm_bkgrd_clr[2]))  # ; Based on MacOSX element
        }
        # TKINTER
        set_menu = Toplevel()
        set_menu.title(winstrings["main"]["choices"][1])
        # NOTEBOOKS
        set_menu_nb = ttk.Notebook(set_menu)
        # FRAMES
        frame_01 = Frame(set_menu_nb, bg=rgb(227, 227, 227))  # ;Video
        frame_02 = Frame(set_menu_nb, bg=rgb(227, 227, 227))  # ;Audio
        frame_03 = Frame(set_menu_nb, bg=rgb(227, 227, 227))  # ;Controller
        frame_04 = Frame(set_menu_nb, bg=rgb(227, 227, 227))  # ;Game
        frame_05 = Frame(set_menu_nb, bg=rgb(227, 227, 227))  # ;User Interface/Start-up
        frame_06 = Frame(set_menu, bg=sm_colors_presets["grey"])
        # COMBO_BOXES
        SET_MENU_PRESET_CMBBX = ttk.Combobox(frame_06)
        SET_MENU_PRESET_CMBBX['values'] = settings_user_made_presets
        # LISTS
        cb_bttns_str_list = []
        option_button_list = cb_bttns_str_list  # ;confirm_bttns_string_list
        frme_list = [frame_01, frame_02, frame_03, frame_04, frame_05]
        f_l = frme_list
        # INT
        i = 0
        # INT_LISTS
        l = [0, 0, 0, 0, 0]
        # CODE
        frame_06.grid_propagate(0)
        frame_06['height'] = 24

        if len(settings_user_made_presets) >= 1:
            Label(set_menu, text=winstrings['main']['preset_strings'], bg=sm_colors_presets['grey'], relief='groove', bd=3).grid(column=0, row=1, sticky='nw', padx=1)
            SET_MENU_PRESET_CMBBX.grid(column=0, row=1, sticky='nw', padx=60)

        def cancel():
            """
            Cancels changes
            :return:
            """
            # CODE
            set_menu.grab_release()
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

        ls_bttns_list = [apply, cancel, ok]

        for save_buttons in winstrings['main']['save_options']:
            option_button_list.append(save_buttons)

        for choiceOptions in range(len(option_button_list)):
            if self.sc_init.iterator_03[2] >= len(option_button_list):
                self.sc_init.iterator_03[2] = 0
            save_buttons_p = option_button_list[self.sc_init.iterator_03[2]]
            save_buttons_get_len = len(save_buttons_p)
            m = save_buttons_get_len ** self.sc_init.iterator_03[2]  # ;Math
            function_list = ls_bttns_list[choiceOptions]
            string_list = option_button_list[choiceOptions]
            Button(frame_06, text=string_list, command=function_list, bg=sm_colors_presets["grey"]).grid(column=0, row=1, padx=m * 16 + 500, sticky='e')
            self.sc_init.iterator_03[2] += 1

        def video():
            # PYGAME
            vr_resolutions = [
                [320, 240], [320, 244], [384, 240], [384, 244], [512, 256], [640, 480]
            ]
            wr_resolutions = self.sc_init.tp.DISPLAY_AUTODETECT()
            # INT
            i = 0
            # FRAMES
            frame_01_01 = Frame(frame_01, relief='raised', bd=10)
            # BOOLEANVARS
            custom_res_bv = BooleanVar()
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
            custom_res = Checkbutton(frame_01_01, variable=custom_res_bv, onvalue=True, offvalue=False)
            dir_chkbtn = Checkbutton(frame_01_01, variable=r_disable_ripple, onvalue=True, offvalue=False)
            # SCALES
            wei_scale = Scale(frame_01_01, orient=HORIZONTAL, length=100, from_=weather_intensity_scale_limits[0], to=weather_intensity_scale_limits[1])
            # COMBO_BOXES
            vr_resolutions_cmbbox = ttk.Combobox(frame_01_01, width=7)
            wr_resolutions_cmbbox = ttk.Combobox(frame_01_01, width=9)
            # CODE

            vr_resolutions_cmbbox['values'] = self.sc_init.tp.res_to_readable_form(target=vr_resolutions)
            wr_resolutions_cmbbox['values'] = self.sc_init.tp.res_to_readable_form(target=wr_resolutions)

            for video_settings_strings in winstrings["main"]["options"]["Video"]["set"]:
                Label(frame_01_01, text=video_settings_strings).grid(column=0, row=i, sticky="w")
                i += 1

            # ;Window Res
            if custom_res_bv.get() is True:
                rx_txt.grid(column=1, row=1, sticky='w', padx=10)
                Label(frame_01_01, text=in_between_entries).grid(column=1, row=1, sticky='w', padx=70)
                ry_txt.grid(column=1, row=1, sticky='w', padx=90)

                # ;2D Res
                x_txt.grid(column=1, row=2, sticky='w', padx=10)
                Label(frame_01_01, text=in_between_entries).grid(column=1, row=2, sticky='w', padx=70)
                y_txt.grid(column=1, row=2, sticky='w', padx=90)
            else:
                custom_res.grid(column=1, row=0, padx=10, sticky='w')

            frame_01_01.grid(column=0, row=0)
            dir_chkbtn.grid(column=1, row=3, sticky='w', padx=10)
            wei_scale.grid(column=1, row=4, sticky='w', padx=10)
            wr_resolutions_cmbbox.grid(column=1, row=1, padx=10, sticky='w')
            vr_resolutions_cmbbox.grid(column=1, row=2, padx=10, sticky='w')

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
            # LISTS
            audio_settings_frames_list = [frame_02_01_01, frame_02_01_02]
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
                frames_list = audio_settings_frames_list[self.sc_init.iterator_03[4]]
                sframe_02_01.add(frames_list, text=audio_settings_strings)
                self.sc_init.iterator_03[4] += 1

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

            sframe_02_01.grid(column=0, row=1, padx=53)

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
                keyboard_combobox['width'] = 13
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
            sframe_03_01.grid(column=0, row=0, padx=108)

        def game():
            # DICTIONARIES_ABSTRACTED
            difficulty_list = winstrings['main']['options']['Game']['set']['Difficulty']
            mod_list = winstrings['main']['options']['Game']['set']['Game']
            option_str_list = winstrings['main']['options']['Game']['set']
            # FRAMES
            frame_04_01 = Frame(frame_04, relief='raised', bd=10)  # ;Main Frame
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
                Label(label_sect, text=game_label_string).grid(column=0, row=i, pady=10, sticky='w')
                i += 1

            combobox_list = [difficulty_list_combobox, mod_list_combobox]
            options_val_list = [difficulties, games]

            for game_cb_list in range(len(combobox_list)):
                list_ = combobox_list[game_cb_list]
                n_val_list = options_val_list[game_cb_list]
                list_['values'] = n_val_list
                list_['state'] = "readonly"
                if game_cb_list == 0:
                    list_['width'] = 18
                list_.grid(column=0, row=q, padx=10, pady=10, sticky='w')
                q += 1

            # ;Grid
            frame_04_01.grid(column=0, row=0, padx=184)
            label_sect.grid(column=0, row=0, rowspan=len(options_val_list), sticky='n')
            value_sect.grid(column=1, row=0, rowspan=len(options_val_list), sticky='n')

        def user_interface():
            # BOOLEANVARS
            mm = BooleanVar()
            pm = BooleanVar()
            # DICTIONARIES_ABSTRACTED
            dict_abs = {  # ;Abstracted
                "options_start_up": winstrings['main']['options']['User Interface']['set']['Start-Up']
            }
            # FRAMES
            frame_05_01 = Frame(frame_05, relief='raised', bd=10)
            frame_05_01.configure(width=200)
            # CHECKBUTTONS
            ui_ckb_mm = Checkbutton(frame_05_01, variable=mm, onvalue=True, offvalue=False)  # ;Minimal Mode
            ui_ckb_p_m = Checkbutton(frame_05_01, variable=pm, onvalue=True, offvalue=False)  # ;Play Movies
            # COMBO_BOXES
            ui_cmb_thms = ttk.Combobox(frame_05_01, width=5)
            # LISTS
            ui_thms_list = [theme for theme in self.style.theme_names()]
            # CODE
            ui_cmb_thms['values'] = ui_thms_list

            for ui_txt in dict_abs['options_start_up']:  # ;Loop through and render labels
                Label(frame_05_01, text=ui_txt).grid(column=0, row=self.sc_init.iterator_03[3], padx=10, pady=5, sticky='w')
                self.sc_init.iterator_03[3] += 1

            check_bv(mm, miminal_mode)
            check_bv(pm, play_movies)

            # ;Grid
            frame_05_01.grid(column=0, row=0, padx=240)
            ui_ckb_mm.grid(column=1, row=0)
            ui_ckb_p_m.grid(column=1, row=1)
            ui_cmb_thms.grid(column=1, row=2, padx=10)

        for string in winstrings["main"]["options"]:
            if self.sc_init.iterator_03[0] >= 5:
                self.sc_init.iterator_03[0] = 0
            sel_list = f_l[self.sc_init.iterator_03[0]]
            set_menu_nb.add(sel_list, text=string)
            self.sc_init.iterator_02 += 1
            self.sc_init.iterator_03[0] += 1


        frame_06.grid(column=0, row=1, sticky='e')
        set_menu_nb.grid(column=0, row=0)
        set_menu.grab_set()

        video()
        audio()
        user_input()
        game()
        user_interface()
        frame_06['width'] = set_menu_nb.winfo_screenmmwidth()+65

    def PLAY_GAME(self):
        # CODE
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

    def FIRST_RUN(self, **kwargs):
        # KWARGS
        FR_PRINT_INI_FILE = kwargs.get('print_ini_file', False)
        # GF
        # STRINGS
        point_usr_dir = f"/Users/{self.sc_init.wsf.gun}"
        point_doc_dir_ls = f"{point_usr_dir}{self.sc_init.wsf.user_settings_folder}{self.sc_init.wsf.subdir}/Launcher_Settings.ini" # ;This file can be placed anywhere
        # CODE
        def first_run_message():
            # CODE
            if GetPresSpec(point_doc_dir_ls) is False:
                message_window = msg.showinfo(title=winstrings['main']['title'][0], message=winstrings['main']['firstrunmessage'])

        self.sc_init.options_save['LAUNCHER'] = {
            "IsFirstRun": 'False'
        }
        if GetPresSpec(point_doc_dir_ls) is False:
            first_run_message()
            file = self.sc_init.wsf.writeSettingsFile(name="Launcher_Settings")
            self.sc_init.options_save['LAUNCHER']['IsFirstRun'] = 'True'
            launcher_settings_file = open(point_doc_dir_ls, "w+")
            if FR_PRINT_INI_FILE is True:
                p(launcher_settings_file.read())
            self.sc_init.options_save.write(launcher_settings_file)
            launcher_settings_file.close()
        else:
            self.sc_init.options_save['LAUNCHER']['IsFirstRun'] = 'False'
            launcher_settings_file = open(point_doc_dir_ls, "w")
            if FR_PRINT_INI_FILE is True:
                p(launcher_settings_file.read())
            self.sc_init.options_save.write(launcher_settings_file)
            launcher_settings_file.close()

    def run(self, **kwargs):
        """
         Kwarg                 Def Value Description
         _____________________ _________ _______________________________________________________________________________________________
        | get_iters           | False   | gets the self.sc_init_iterator_03 list                                                        |
        | get_iters_delay     | False   | Enables delay (get_iters=True is needed)                                                      |
        | get_iters_delay_val | 100     | Time needed to print (get_iters=True, get_iters_delay=True is needed) This slows down program |
         -------------------------------------------------------------------------------------------------------------------------------

        :param kwargs:
        :return:
        """
        # KWARGS
        run_get_sc_init_iters = kwargs.get("get_iters", False)
        if run_get_sc_init_iters is True:
            run_get_sc_init_iters_p_delay = kwargs.get('get_iters_delay', False)
            if run_get_sc_init_iters_p_delay is True:
                run_get_sc_init_iters_p_delay_val = kwargs.get('get_iters_delay_val', 100)
        # CODE
        while self.sc_init.is_running is True:
            if run_get_sc_init_iters and run_get_sc_init_iters_p_delay is True:
                p_statement = f"Class Wide Iterators {self.sc_init.iterator_03}"
                for i in range(run_get_sc_init_iters_p_delay_val):
                    if i >= run_get_sc_init_iters_p_delay_val - 1:
                        p(p_statement)
            else:
                if run_get_sc_init_iters is True and run_get_sc_init_iters_p_delay is False:
                    p_statement = f"Class Wide Iterators {self.sc_init.iterator_03}"
                    p(p_statement)
            self.update_idletasks()
            self.update()


mw = MAIN_WINDOW()
mw.DRAW_CONTENTS()
mw.FIRST_RUN()
mw.run()
