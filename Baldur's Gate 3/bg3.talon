mode: user.game
and not mode: sleep
and app: baldurs_gate_3
-
tag(): user.game_genre_crpg
tag(): user.game_map
tag(): user.game_camera_keyboard_controls
tag(): user.game_camera_zoom

take all:
    key(space)

group hide:
    key(shift-c)

hide:
    key(c)
shove:
    key(v)
jump:
    key(z)
throw:
    key(x)
(meele | ranged) [weapon] [set] [use]:
    key(f)

party view:
    key(tab)
hero last:
    key("[")
hero next:
    key("]")
car sheet [show]:
    key(n)

[tool] tip pin:
    key(t)
spellbook show:
    key(k)
(illithid | ill) power:
    key(b)

tactical (camera | cam) [toggle]:
    key(o)