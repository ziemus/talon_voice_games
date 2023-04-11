mode: user.game
and not mode: sleep
and app: gothic
-
settings():
    user.game_turn_around_mouse_delta = 50
	user.game_turn_horizontally_mouse_delta = 10
	user.game_turn_vertically_mouse_delta = 10
    user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "use"
    user.game_sprint_state_default = 1
    key_hold = 64.0
	key_wait = 16.0
    
tag(): user.first_person_game_controls
tag(): user.game_basic_movement_arrows
tag(): user.game_weapons
tag(): user.game_weapon_block
tag(): user.game_weapon_target_lock
tag(): user.game_trade

climb up:
    key("alt:down up")
climb stop:
    key("alt:up")

go <user.arrow_keys>:
    key(arrow_keys)

attack forward | war:
    user.gothic_attack_mode_change(0)
attack sideways | side | I'd:
    user.gothic_attack_mode_change(1)
attack change | chat:
    user.gothic_attack_mode_change()