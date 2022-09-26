app: darkest_dungeon
and not mode: sleep
and mode: user.game
-
settings():
    user.mouse_hide_mouse_gui = 1
    
tag(): user.game_basic_movement
tag(): user.game_character_sheet
stay:
    user.mouse_stay_in_place(1)
come:
    user.mouse_stay_in_place(0)
(scroll | page) up | seal | ceil:
    user.mouse_scroll_up_continuous()
[scroll | page] down | day:
    user.mouse_scroll_down_continuous()
zoom in | closer | close:
    user.mouse_scroll_up_continuous()
zoom out | farther | far:
    user.mouse_scroll_down_continuous()
drag:
	user.mouse_drag(0)
buy <digits>:
    user.game_click(0, digits)
sell <digits>:
    #selling requires a longer holding time than buying
    user.game_click(0, digits, 50000)
take all:
    user.press_game_key("space")
torch:
    user.press_game_key("t")
[curio] use | [room] enter | interact:
    user.press_game_key("w")
[skill] [switch] <digits>:
    user.darkest_dungeon_skill_switch(digits)
menu | go back | cancel | escape:
    user.press_game_key("escape")
help [show]:
    user.press_game_key("h")