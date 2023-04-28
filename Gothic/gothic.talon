mode: user.game
and not mode: sleep
and app: gothic
-
settings():
    user.game_turn_around_mouse_delta = 1800000
	user.game_turn_horizontally_mouse_delta = 900000
	user.game_turn_vertically_mouse_delta = 0
    user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
    user.game_default_movement_key = "up"
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "target lock toggle"
    user.game_sprint_state_default = 1
    user.game_sprint_hold_to_walk = 1
    key_hold = 64.0
	key_wait = 16.0
    
tag(): user.first_person_game_controls
tag(): user.game_weapons
tag(): user.game_weapon_block
tag(): user.game_weapon_target_lock
tag(): user.game_trade
tag(): user.game_inventory_tabs

noise binding exploration mode | noise explore | exploring:
	user.game_noise_control_switch("pop","default")
    user.game_noise_control_switch("hiss","default")
noise binding fight mode | noise fight | fighting:
	user.game_noise_control_switch("pop","default")
    user.game_noise_control_switch("hiss","block toggle")

climb up:
    user.gothic_climb_up()

dive out:
    user.game_dive_start()
    user.switch_game_movement_direction("down")
    user.switch_game_movement(1)

tell <number>:
    key("{number} enter")
dialogue skip | kip:
    key(escape)
dialogue end:
    user.gothic_dialogue_end()

go <user.arrow_keys>:
    key(arrow_keys)
go <user.arrow_key> <number>:
    key("{arrow_key}:{number}")

attack forward | war:
    user.gothic_attack_mode_change(0)
attack sideways | side | I'd:
    user.gothic_attack_mode_change(1)
attack change | chat:
    user.gothic_attack_mode_change()