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
        vid/ ; Video Folder
"""
from data.frw.GF.EXT.GFTKE import *
from data.txt.men import *
from data.mu.Values import *

class MAIN_W_I(object):
    def __init__(self):
        # OSPATH
        self.main_dir = os.path.dirname(os.path.abspath(__file__))
        # GULL_FRAMEWORK_EXT
        self.tp = pygameTkIntegration()
        self.keys = self.tp.CombineDictToOne()
        self.dbg_controller = self.tp.debugController()
        # DICTIONARIES
        self.i_dict = imgDict(f"{self.main_dir}/data/img/")
        self.v_dict = getDirectory(f"{self.main_dir}/data/vid/", filter='.mp4', print_dict=True)
        self.options_changes = {
            "Video": {
                "boolvar": [BooleanVar(), BooleanVar()],
                "strvar": [StringVar(), StringVar(), StringVar(), StringVar()],
                "int": {
                    "vres": [[320, 240], [320, 244], [384, 240], [384, 244], [512, 256], [640, 480]],
                    "wres": self.tp.displayAutodetect()
                }
            }
        }
        # CONFIG_PARSER
        self.options_save = ConfigParser() # ;Launcher Configuration
        self.options_save_sm = ConfigParser() # ;Settings Menu Configuration
        # INT
        self.iterator_01 = 0
        self.iterator_02 = 0
        # INT_LIST
        self.iterator_03 = genIterList(len(winstrings['main']['options'])*6)
        # BOOLEANS
        self.lessguimode = False
        self.converttopygame = False
        self.is_running = True
        # GF
        self.wsf = GF.wsf()


class mainWindow(Tk):
    def __init__(self):
        super().__init__()
        # CLASS CALL
        self.sc_init = MAIN_W_I()
        # TKINTER
        self.wm_attributes()
        self["background"] = rgb(34, 87, 165)
        self.title(winstrings["main"]["title"][0])
        # THEME
        self.style = ttk.Style()
        self.style.theme_use('classic')
        # CODE

    def drawContents(self):
        # TKINTER
        options_frame = Frame(self, background=rgb(34, 87, 165)).grid(column=0, rowspan=len(winstrings['main']['choices']))

        def optionsFormat():
            # BACKGROUND COLORS
            rb = 92 + 20
            gb = 133 + 20
            bb = 171 + 20
            # FOREGROUND COLORS
            rf = rb - (round(rb / 3))
            gf = gb - (round(gb / 3))
            bf = bb - (round(bb / 3))
            # LIST
            of_options_list = [self.playGame, self.settingsMenu, self.saveGame, None]
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
                    pass
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
                           command=option_func).grid(column=0, row=self.sc_init.iterator_01, sticky='nw', pady=10)
                self.sc_init.iterator_01 += 1
                self.sc_init.iterator_03[1] += 1

        def bkgrdImage():
            # IMAGES
            bkgrd = loadimage(self.sc_init.i_dict[6])
            bkgrd_tl = loadimage(self.sc_init.i_dict[4])
            # CODE
            Label(self, image=bkgrd, background=rgb(34, 87, 165)).grid(column=1, row=0, rowspan=len(winstrings['main']['choices']), sticky="nw")
            Label(self, foreground='DarkBlue', image=bkgrd_tl).grid(column=1, row=len(winstrings['main']['choices']) - 1)
            gc.collect()

        bkgrdImage()
        optionsFormat()

    def settingsMenu(self):
        # TKINTER
        set_menu = Toplevel()
        set_menu.title(winstrings["main"]["choices"][1])
        # NOTEBOOKS
        set_menu_nb = ttk.Notebook(set_menu)
        set_menu_nb['width'] = 567
        # STR
        color = 'systemActiveAreaFill'
        # FRAMES
        frame_01 = Frame(set_menu_nb, bg=color)  # ;Video
        frame_02 = Frame(set_menu_nb, bg=color)  # ;Audio
        frame_03 = Frame(set_menu_nb, bg=color)  # ;Controller
        frame_04 = Frame(set_menu_nb, bg=color)  # ;Game
        frame_05 = Frame(set_menu_nb, bg=color)  # ;User Interface/Start-up
        frame_06 = Frame(set_menu, bg='systemMenuActive')
        # COMBO_BOXES
        SET_MENU_PRESET_CMBBX = ttk.Combobox(frame_06)
        SET_MENU_PRESET_CMBBX['values'] = settings_user_made_presets
        # LISTS
        cb_bttns_str_list = []
        option_button_list = cb_bttns_str_list  # ;confirm_bttns_string_list
        frme_list = [frame_01, frame_02, frame_03, frame_04, frame_05]
        f_l = frme_list # ;Abstracted
        # DICTIONARIES
        funct_iter_tracker = {
            "v": [],
            'a': [],
            'c': [],
            'g': [],
            'ui': [],
        }
        # CODE
        for reset in range(len(self.sc_init.iterator_03)):
            if reset == 1:
                pass
            else:
                self.sc_init.iterator_03[reset] = 0

        frame_06.grid_propagate(0)
        frame_06['height'] = 24

        if len(settings_user_made_presets) >= 1:
            Label(set_menu, text=winstrings['main']['preset_strings'], bg='systemMenu', relief='groove', bd=3).grid(column=0, row=1, sticky='nw', padx=1)
            SET_MENU_PRESET_CMBBX.grid(column=0, row=1, sticky='nw', padx=60)

        # ;OPTIONS FUNCTIONS------------------------------------------------------------------------------------------------------------------------------------------------
        def video():
            # PYGAME
            vr_resolutions = self.sc_init.options_changes['video'.title()]['int']['vres']
            wr_resolutions = self.sc_init.options_changes['video'.title()]['int']['wres']
            # FRAMES
            frame_01_01 = Frame(frame_01, relief='raised', bd=10)
            # BOOLEANVARS
            custom_res_bv = self.sc_init.options_changes['video'.title()]['boolvar'][0]
            r_disable_ripple_bv = self.sc_init.options_changes['video'.title()]['boolvar'][1]
            # STRINGVARS
            rx = self.sc_init.options_changes['Video']['strvar'][0]  # ;Window Resolution-Width
            ry = self.sc_init.options_changes['Video']['strvar'][1]  # ;Window Resolution-Height
            x = self.sc_init.options_changes['Video']['strvar'][2]  # ;2D Resolution-Width
            y = self.sc_init.options_changes['Video']['strvar'][3]  # ;2D Resolution-Height
            # ENTRIES
            x_txt = Entry(frame_01_01, textvariable=x, width=5)
            y_txt = Entry(frame_01_01, textvariable=y, width=5)
            rx_txt = Entry(frame_01_01, textvariable=rx, width=5)
            ry_txt = Entry(frame_01_01, textvariable=ry, width=5)
            # CHECKBUTTONS
            custom_res = Checkbutton(frame_01_01, variable=custom_res_bv, onvalue=True, offvalue=False)
            dir_chkbtn = Checkbutton(frame_01_01, variable=r_disable_ripple_bv, onvalue=True, offvalue=False)
            # SCALES
            wei_scale = Scale(frame_01_01, orient=HORIZONTAL, length=100, from_=weather_intensity_scale_limits[0], to=weather_intensity_scale_limits[1])
            # COMBO_BOXES
            vr_resolutions_cmbbox = ttk.Combobox(frame_01_01, width=7)
            wr_resolutions_cmbbox = ttk.Combobox(frame_01_01, width=9)
            # PACKER
            packer = [self.sc_init.iterator_03[3]]
            # DICTIONARIES
            int_val_globe_video = {
                "textboxes": {
                    "2d": {
                        "x": x_txt.get(),
                        "y": y_txt.get()
                    },
                    "wd": {
                        "rx": rx_txt.get(),
                        "ry": ry_txt.get()
                    }
                },
                "checkuttons": {
                    "custom_res_bv": custom_res_bv.get(),
                    "dir_chkbtn": r_disable_ripple_bv.get()
                },
                "scales": {
                    "wei": wei_scale.get()
                },
                "entries": {
                    "2d:": vr_resolutions_cmbbox.get(),
                    "wr": wr_resolutions_cmbbox.get()
                }
            }
            # CODE
            vr_resolutions_cmbbox['values'] = self.sc_init.tp.resToReadableForm(target=vr_resolutions)
            wr_resolutions_cmbbox['values'] = self.sc_init.tp.resToReadableForm(target=wr_resolutions)

            for video_settings_strings in winstrings["main"]["options"]["Video"]["set"]:
                Label(frame_01_01, text=video_settings_strings).grid(column=0, row=self.sc_init.iterator_03[3], sticky="w")
                self.sc_init.iterator_03[3] += 1

            for it in packer:
                funct_iter_tracker['v'].append(it)

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

            return int_val_globe_video

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
            # DICTIONARIES
            int_val_globe_audio = {
                "comboboxes": {
                    "music": combox_01.get(),
                    "sfx": combox_02.get()
                },
                "scales": {
                    "music": volume_music.get(),
                    "sfx": volume_sfx.get()
                }
            }
            # INT-ITER VARS ;Assembly like-vars
            i = 0
            q = 0
            a = 1
            z = 1
            # PACKER
            packer = [i, q, a, z, self.sc_init.iterator_03[4]]
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

            for it in packer:
                funct_iter_tracker['a'].append(it)

            combox_01['values'] = (winstrings["main"]["options"]["Audio"]["special"]["games"]["retail"][0])
            combox_01['state'] = "readonly"
            combox_01.grid(column=1, row=0)

            volume_music.grid(column=1, row=3)

            combox_02['values'] = (winstrings["main"]["options"]["Audio"]["special"]["games"]["retail"][0])
            combox_02['state'] = "readonly"
            combox_02.grid(column=1, row=0)

            volume_sfx.grid(column=1, row=3)

            sframe_02_01.grid(column=0, row=1, padx=53)

            return int_val_globe_audio

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
            # DICTIONARIES
            int_val_globe_user_input = {
                "comboboxes": {
                    "keyboard": [i.get() for i in usi_keyboard_type_bindings_list],
                    "joystick": [i.get() for i in usi_joystick_type_bindings_list]
                }
            }
            # INT_ITERS ;Generic assembly-like vars
            i = 0
            q = 0
            a = 0
            z = 0
            # INT_ITERS_ARR ;Generic assembly-like extended vars
            e = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            # PACKER
            packer = [i, q, a, z, e]
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

            for it in packer:
                funct_iter_tracker['c'].append(it)

            # ;Grid
            usi_keyboard_type_bindings.grid(column=0, row=0)
            frame02.grid(column=1, row=0)
            sframe_03_01.grid(column=0, row=0, padx=108)

            return int_val_globe_user_input

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
            # PACKER
            packer = [self.sc_init.iterator_03[5], self.sc_init.iterator_03[6]]
            # DICTIONARIES
            int_val_globe_game = {
                "comboboxes": {
                    "difficulty_list": difficulty_list_combobox.get(),
                    "mod_list": difficulty_list_combobox.get()
                }
            }
            # CODE
            self.sc_init.iterator_03[5] = 0
            for game_label_string in option_str_list:
                Label(label_sect, text=game_label_string).grid(column=0, row=self.sc_init.iterator_03[5], pady=10, sticky='w')
                self.sc_init.iterator_03[5] += 1

            combobox_list = [difficulty_list_combobox, mod_list_combobox]
            options_val_list = [difficulties, games]

            self.sc_init.iterator_03[6] = 0
            for game_cb_list in range(len(combobox_list)):
                list_ = combobox_list[game_cb_list]
                n_val_list = options_val_list[game_cb_list]
                list_['values'] = n_val_list
                list_['state'] = "readonly"
                if game_cb_list == 0:
                    list_['width'] = 18
                list_.grid(column=0, row=self.sc_init.iterator_03[6], padx=10, pady=10, sticky='w')
                self.sc_init.iterator_03[6] += 1

            for it in packer:
                funct_iter_tracker['g'].append(it)

            # ;Grid
            frame_04_01.grid(column=0, row=0, padx=184)
            label_sect.grid(column=0, row=0, rowspan=len(options_val_list), sticky='n')
            value_sect.grid(column=1, row=0, rowspan=len(options_val_list), sticky='n')

            return int_val_globe_game

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
            # PACKER
            packer = [self.sc_init.iterator_03[7]]
            # DICTIONARIES
            int_val_globe_video = {
                "checkbuttons": {
                    "ui_minimal_mode": mm.get(),
                    "ui_play_movies": pm.get()
                },
                "comboboxes": {
                    "ui_themes": ui_cmb_thms.get()
                }
            }
            # CODE
            ui_cmb_thms['values'] = ui_thms_list

            for ui_txt in dict_abs['options_start_up']:  # ;Loop through and render labels
                Label(frame_05_01, text=ui_txt).grid(column=0, row=self.sc_init.iterator_03[7], padx=10, pady=5, sticky='w')
                self.sc_init.iterator_03[7] += 1

            for it in packer:
                funct_iter_tracker['ui'].append(it)

            checkBv(mm, miminal_mode)
            checkBv(pm, play_movies)

            # ;Grid
            frame_05_01.grid(column=0, row=0, padx=240)
            ui_ckb_mm.grid(column=1, row=0)
            ui_ckb_p_m.grid(column=1, row=1)
            ui_cmb_thms.grid(column=1, row=2, padx=10)

            return int_val_globe_video

        # ;SAVE BUTTONS------------------------------------------------------------------------------------------------------------------------------------------------
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

        # ;SAVE BUTTONS LIST------------------------------------------------------------------------------------------------------------------------------------------------
        ls_bttns_list = [apply, cancel, ok] # ;Contains functions

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
            Button(frame_06, text=string_list, command=function_list, bg='systemMenu').grid(column=0, row=1, padx=m * 16 + set_menu_nb['width']/1.8, sticky='e')
            self.sc_init.iterator_03[2] += 1

        # ;Option String Loop------------------------------------------------------------------------------------------------------------------------------------------------
        for string in winstrings["main"]["options"]: # ;Gets the strings within this directory
            if self.sc_init.iterator_03[0] >= 5: # ;If class-wide iterator hits 5 then roll back to 0
                self.sc_init.iterator_03[0] = 0
            sel_list = f_l[self.sc_init.iterator_03[0]] # ;target list with class-widde iterator
            set_menu_nb.add(sel_list, text=string) # ;Add to Notebook with looped 'string'
            self.sc_init.iterator_02 += 1 # ;add 1
            self.sc_init.iterator_03[0] += 1 # ;add 1

        # ;Grid and Grabbers------------------------------------------------------------------------------------------------------------------------------------------------
        frame_06.grid(column=0, row=1, sticky='s')
        set_menu_nb.grid(column=0, row=0)
        set_menu.grab_set() # ;When settings menu is pressed all input goes to said or refrenced menu

        video = video()
        audio = audio()
        ui = user_input()
        game = game()
        usr_int = user_interface()
        frame_06['width'] = set_menu_nb['width'] # ; This will increase the user's screenspace
        flp(frame_01.getvar('custom_res_bv'))
        return video, audio, ui, game, usr_int

    def playGame(self):
        # CODE
        self.sc_init.is_running = False

    def saveGame(self):
        # INT
        time = randint(10, randint(10*2, randint(10*4, 5999999)))
        # CODE
        for t in range(time):
            t -= 1
            p(f"Saving Game {int(t/time*100)}%")
        p("Saved")

    def firstRun(self, **kwargs):
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
        self.sc_init.options_save_sm['SETTINGS'] = {
            "Video-2D-Resolution": "None"
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
         Kwarg                       Def Value       Description
         ___________________________ _________ _______________________________________________________________________________________________
        | get_iters                 | False   | gets the self.sc_init.iterator_03 list                                                        |
        | debug_mode                | False   | Enables all printable keyword arguments.                                                      |
        | get_sc_init_oc            | False   | gets the self.sc_init.options_changes dictionary and prints it.                               |
        | get_sc_init_iters_intel   | False   | same as get_iters but when the value changes or the list's memory                             |
         -------------------------------------------------------------------------------------------------------------------------------------

        :param kwargs:
        :return:
        """
        # KWARGS
        run_get_sc_init_iters = kwargs.get("get_iters", False)
        run_get_sc_init_oc = kwargs.get('get_option_changes', False)
        run_debug_mode = kwargs.get("debugmode", False)
        # CODE
        if run_debug_mode is True:
            run_get_sc_init_iters = True
            run_get_sc_init_oc = True
        if run_get_sc_init_iters is True:
            run_get_sc_init_iters_intel = kwargs.get("get_iters_intel", False)
            if run_get_sc_init_iters_intel is True or run_debug_mode is True:
                iter_vals = []
        while self.sc_init.is_running is True:
            if run_get_sc_init_iters and run_get_sc_init_iters_intel is True or run_debug_mode is True:
                for length in self.sc_init.iterator_03:
                    if length not in iter_vals:
                        p(f"Class Wide Iterators {self.sc_init.iterator_03}")
                    iter_vals.append(length)
                if len(iter_vals) == len(self.sc_init.iterator_03)*5000:
                    iter_vals.clear()
            else:
                if run_get_sc_init_iters is True and run_get_sc_init_iters_intel is False:
                    p_statement = f"Class Wide Iterators {self.sc_init.iterator_03}"
                    p(p_statement)
                if run_get_sc_init_oc is True:
                    flp(self.sc_init.options_changes)
            self.update_idletasks()
            self.update()


mw = mainWindow()
mw.drawContents()
mw.firstRun()
mw.run(debugmode=True)
