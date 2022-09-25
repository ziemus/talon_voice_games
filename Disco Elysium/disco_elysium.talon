app: disco_elysium
and not mode: sleep
and mode: user.game
-
settings():
    user.mouse_hide_mouse_gui = 1

continue | co | next | ness:
    key(enter)
[dialogue] <digits>:
    key('{digits}')
help:
    key(f1)
quicksave:
    key(f5)
pause | menu | go back:
    key(escape)
(character | car) [sheet] | sheet:
    key(c)
inventory | bag:
    key(i)
thought [cabinet] | cabinet | cab:
    key(t)
[quest] (journal | log):
    key(j)
map:
    key(m)
highlight | hi:
    key(tab:down)
(highlight | hi) (end | stop | no):
    key(tab:up)
run:
    user.game_switch_sprint(1)
    user.game_noise_control_switch('pop','double click')
walk:
    user.game_switch_sprint(0)
    user.game_noise_control_switch('pop','click')
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
[inventory | bag] (take | wear | grab | use):
    mouse_click(1)
(language | lang | lan) [switch]:
    key(l)