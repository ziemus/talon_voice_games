app: darkest_dungeon
and not mode: sleep
and mode: user.game
-
settings():
    user.mouse_hide_mouse_gui = 1
    key_hold = 32.0
    user.mouse_wait = 50000
    user.mouse_hold = 50000
    user.mouse_continuous_scroll_amount = 1000
    
tag(): user.game_basic_movement
tag(): user.game_character_sheet
[hero] next:
    key(e)
[hero] (prev | previous):
    key(q)
stay:
    user.mouse_stay_in_place(1)
come:
    user.mouse_stay_in_place(0)
(scroll | page) up:
    user.mouse_scroll_up_continuous()
[scroll | page] down | day:
    user.mouse_scroll_down_continuous()
zoom in | closer | close:
    user.mouse_scroll_up_continuous()
zoom out | farther | far:
    user.mouse_scroll_down_continuous()
drag:
	user.mouse_drag(0)
(buy | take | sell) <digits>:
    user.mouse_stay_in_place(1)
    user.game_click(0, digits)
    user.mouse_stay_in_place(0)
shift down:
    key("shift:down")
shift up:
    key("shift:up")
map | bag | inventory:
    key(tab)
take all:
    key(space)
torch:
    key(t)
[item] use:
    user.game_click(1)
[room] enter | interact:
    user.press_game_key("w")
[skill] [switch] <digits>:
    user.darkest_dungeon_skill_switch(digits)
menu | go back | cancel | escape:
    key(escape)
help [show]:
    key(h)