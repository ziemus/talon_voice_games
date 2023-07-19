mode: user.game
and not mode: sleep
and app: dishonored
-
settings():
    user.game_turn_around_mouse_delta = 1050
	user.game_turn_horizontally_mouse_delta = 550
	user.game_turn_vertically_mouse_delta = 100
    user.game_item_ability_switch_scroll_amount = 10
    user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "long click"
    key_hold = 64.0
	key_wait = 16.0
    user.mouse_hold = 64000
	user.mouse_wait = 0
    
tag(): user.game_arrow_keys_toggle_wsad_movement
tag(): user.first_person_game_controls
tag(): user.game_skills
tag(): user.game_weapon_switch
tag(): user.game_weapon_block
tag(): user.game_weapon_aim
tag(): user.game_quick_access_menu
tag(): user.game_lean_sideways

keyhole [look] [through] | [body] (carry | drop):
    user.game_long_use()
zoom | spy | pie:
	key(alt)
noise binding exploration mode | noise explore | exploring:
	user.game_noise_control_switch("pop","move")
	user.game_noise_control_switch("hiss","jump")
noise binding fight mode | noise fight | fighting:
	user.game_noise_control_switch("pop","right click")
	user.game_noise_control_switch("hiss","long click")