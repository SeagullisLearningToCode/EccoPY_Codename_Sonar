from data.frw.GF.GF import td_c_s_yo

# ;ENGLISH_STRINGS
ui_version_number = ["Gull Framework TK Extension", "1.0"]
winstrings = {
    "main": {
        "title": [f"Bottlenose GUI Version {ui_version_number[1]} {ui_version_number[0]}", f"Ecco The Dolphin Rewritten Version {ui_version_number[1]} {ui_version_number[0]}"],
        "choices": ["Play          ", "Options", "Save        ", "Load       ", "Exit          "],
        "bottomtext": f"SeagullinSeagulls {td_c_s_yo}\nCode: https://github.com/SeagullisLearningToCode/EccoPY_Codename_Sonar",
        "options": {
            "Video": {
                "tooltips": [
                    "EccoPY uses an external and internal resolution system\n Now with ""Window Resolution"", this will change the actual size of the window without affecting the internal resolution.",  # ;Window Resolution
                    "EccoPY uses an external and internal resolution system\n Now with ""2D Resolution"" this will change the game's resolution without resizing the window.",  # ;2D Resolution
                    "In the original Ecco, there a ripple effect that makes the water surface feels alive, disabling this will make the game run slightly faster but will remove the feel of the original game.",  # ;Disable Ripple
                    "This is a new addition to Ecco the Dolphin, this adds weather effects based on the level that Ecco's in, this includes rain, snow, fog and possibly enviromental effects"  # ;Weather Effects Intensity
                ],
                "set": ["Window Resolution (size)", "2D Resolution", "Ripple Effect", "Weather Effects intensity"]
            },
            "Audio": {
                "tooltips": {
                    "Music": ["What Ecco OST do you want to use?", "Use custom music", "Specifify a directory that contains audio files", "How loud do you want the music to be?"],
                    "SFX": ["What Sound effects from a Ecco game do you want to use", "Use custom sfx", "How loud do you want the sfx to be?"]
                },
                "set": {
                    "Music": ["Soundtrack", "Use custom music?", "Custom music directory", "Volume"],
                    "SFX": ["Sound Effects", "Use custom sounds", "Custom Sound directory", "Volume"]
                },
                "special": {
                    "games": {
                        "retail": [
                            ["Ecco The Dolphin (PC/CD)", "Ecco The Dolphin (Genesis/MD)",
                             "Ecco: Tides Of Time (CD)", "Ecco: Tides of Time (Genesis/MD)",
                             "ecco the dolphin: defender of the future".title() + "PS2/DC"]
                        ],
                        "proto": [
                            ["0249", "X11"]
                        ]
                    }
                }
            },
            "Controlls": {
                "tooltips": ["Bind Controls"],
                "set": [
                    ["Enable Debug Bindings"],  # ;Setting Strings
                    ["Keyboard", "Controller", "Joystick"]  # ;User Input type (note that joystick is the controller alt name)
                ],
                "bindings": [
                    ["Up", "Down", "Left", "Right"],  # ;Movement
                    ["Swim", "Sonar", "Dash", "Pause", "Exit game"],  # ;Action Buttons
                    ["TurnOffMusic", "TurnOffSfx"],  # ;Pause Buttons
                    ["ShowFPS", "ShowPOS", "ShowAll"],  # ;Debug
                ],
                "bindings_names": ["movement".title(), "action buttons".title(), "pause buttons".title(), "debug buttons".title()]
            },
            "Game": {
                "tooltips": [],
                "set": {
                    "Difficulty": [
                        ["Truely Alone Mode", "Exploration Mode"],  # ;Passive modes
                        ["Easy", "Normal", "Hard", "Extreme"],  # ;Normal difficulty settings
                        ["Agressive", "No mercy", "Survival", "One Life mode"],  # ;Extreme Modes
                        ["Randomized (Each enemy)", "Randomized (Truely)"] # ;Misc
                    ],
                    "Game": [
                        ["Ecco the Dolphin", "Ecco: The Tides of Time"],  # ;Retail Releases
                        [],  # ;Mod Names go here
                        ["Playable Review", "0429", "X11"]  # ;Prototypes any pre-release build goes here
                    ]
                }
            },
            "User Interface": { # ;User will be able to change the start-up look (very minimal)
                "Tooltips": ["Makes the start menu based on the original (might be different on some systems and may be disabled on console releases)", "Play Movies on start-up"],
                "set": {
                    "Start-Up": ["Play Movies", "Miminal Mode"], # ; Requires restart
                }
            }
        },
        "save_options": ["Cancel", "Apply", "Ok"],
        "help_buttons": ["?", "Need Help?"]
    }
}
winstrings_settings_tooltips_dict = {

}
