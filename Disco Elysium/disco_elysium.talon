title: Disco Elysium
and app.exe: Disco Elysium.exe
and app.name: Disco Elysium.exe
and not mode: sleep
and mode: user.game
-
settings():
    user.mouse_hide_mouse_gui = 1
    #Most of the time the player will use the default behavior of click on pop anyway,
    #but just in case they don't have a means of toggling sprint by pushing Caps Look
    #(which is not supported by talon)
    #I want to make it possible for the player
    #to switch to sprinting instead of walking by voice only
    #and that requires double clicking on pop
    #wich is implemented by game noise controls
    user.mouse_enable_pop_click = 0
    user.mouse_wait = 50000

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