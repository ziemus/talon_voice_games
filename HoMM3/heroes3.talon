mode: user.game
and not mode: sleep
and app.exe: Heroes3.exe
and app.name: Heroes of Might and Magic® III
and title: /Heroes of Might and Magic III/
-
settings():
    user.mouse_hide_mouse_gui = 1
    key_hold = 32.0
    user.mouse_hold = 10000

combat spell [book] [show]:
    key(c)
spell cast:
    key(c)
adventure spell [book] [show]:
    key(a)
spell [book] [turn] [page] <user.arrow_key>:
    key(arrow_key)

(creature | troops) dismiss:
    key(d)
(creature | troops) upgrade:
    key(u)

^dig here$:
    key(d)
puzzle map [show]:
    key(p)

town next:
    key(down)
town prev:
    key(up)

^hero sleep$:
    key(z)
^hero wake$:
    key(w)

quest log [show]:
    key(q)
scenario info [show]:
    key(i) 

[curse] stay:
    user.mouse_stay_in_place(1)
[curse] come:
    user.mouse_stay_in_place(0)
(scroll | page) up:
    user.mouse_scroll_up_continuous()
[scroll | page] down | day:
    user.mouse_scroll_down_continuous()
drag:
	user.mouse_drag(0)
end drag | drag end:
    user.mouse_drag_end()
duke:
	user.game_click(0, 2)
{user.prose_formatter} <user.prose>$:
    user.insert_formatted(prose, prose_formatter)
menu | go back | cancel | escape:
    key(escape)
