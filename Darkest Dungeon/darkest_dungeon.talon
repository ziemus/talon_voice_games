app: darkest_dungeon
and not mode: sleep
and mode: user.game
-
tag(): user.game_basic_movement
tag(): user.game_character_sheet

[skill] [switch] <digits>:
    user.darkest_dungeon_skill_switch(digits)
menu | go back | cancel:
    user.press_game_key("escape")
help [show]:
    user.press_game_key("h")