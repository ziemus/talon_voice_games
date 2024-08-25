mode: user.game
and app: MassEffectLegendaryEdition
-
settings():
	user.mouse_continuous_scroll_amount = 250
	user.mouse_wheel_down_amount = 250
	user.game_turn_around_mouse_delta = 10
	user.game_turn_horizontally_mouse_delta = 10000000
	user.game_turn_vertically_mouse_delta = 10
	user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
	key_hold = 128.0
	key_wait = 16.0
	user.mouse_hold = 64000
	user.mouse_wait = 0
	user.game_noise_pop_binding_default = "aim toggle"
	user.game_noise_hiss_binding_default = "long click"

key(left):
	user.game_turn_camera("left")
key(right):
	user.game_turn_camera("right")