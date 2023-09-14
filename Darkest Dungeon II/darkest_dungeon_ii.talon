app: darkest_dungeon_2
and mode: user.game
and not mode: sleep
-
tag(): user.game_mouse_enabled

let:
    user.press_game_key("a", 1, 500000)
rye | ray | right:
    user.press_game_key("d", 1, 500000)

choose that:
	user.game_click(0, 1, 1250000)

stagecoach | ([stage] coach | carriage) (show | hide):
    key(z)
(character | car | hero) [sheet] (show | hide) | team (show | hide):
    key(c)

bag [show | hide]:
    key(i)
item drop | drop that:
    key("shift:down")
    mouse_click(0)
    key("shift:up")

map (show | hide):
    key(m)
goal (show | hide):
    key(g)

token show:
    key("tab:down")
token hide:
    key("tab:up")

detail show:
    key("alt:down")
detail hide:
    key("alt:up")