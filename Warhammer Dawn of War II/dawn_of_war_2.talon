app: dawn_of_war_2
and mode: user.game
-
settings():
	user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
    key_hold = 64.0
	key_wait = 16.0
    user.mouse_hold = 64000
	user.game_noise_pop_binding_default = "right click"
	user.game_noise_hiss_binding_default = "long click"
	user.game_minimum_hiss_duration = "80ms"

key(f14): user.game_menu()

eff {user.game_number_shortcuts}:
	key("f{game_number_shortcuts}")

[get] {user.game_number_shortcuts}:
	key(game_number_shortcuts)
take many:
	key(ctrl-a)
take hero:
	key(f1)
take next:
	key(tab)
take last:
	key(ctrl-tab)
take clear:
	key(escape)
take none:
	key(ctrl:down)
	user.game_click()
	key(ctrl:up)

^unit set {user.game_number_shortcuts}:
	key(ctrl-game_number_shortcuts)

{user.letter}:
	key(user.letter)