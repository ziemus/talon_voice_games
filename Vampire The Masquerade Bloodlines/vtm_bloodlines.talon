mode: user.game
and not mode: sleep
and app: vtm_bloodlines
-
settings():
    user.game_turn_around_mouse_delta = 780
	user.game_turn_horizontally_mouse_delta = 380
	user.game_turn_vertically_mouse_delta = 100
    user.game_item_ability_switch_scroll_amount = 10
    user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "long click"
    user.game_sprint_state_default = 1
    
tag(): user.game_arrow_keys_toggle_wsad_movement
tag(): user.first_person_game_controls
tag(): user.game_weapons
tag(): user.game_skills

noise binding exploration mode | noise explore | exploring:
	user.game_noise_control_switch("pop","move")
	user.game_noise_control_switch("hiss","long click")
noise binding fight mode | noise fight | fighting:
	user.game_noise_control_switch("pop","right click")
	user.game_noise_control_switch("hiss","long click")

[attack] secondary | sec:
    key(tab)
block:
    user.vtmb_block()
block done:
    user.vtmb_block(0)
^block state reset$:
    user.vtmb_block_state_set(0)

armor [clothing]:
    key(f3)

(discipline | weapon) [switch | toggle]:
    key(t)

eat | feed:
    user.vtmb_feed(1)
(eat | feed) done:
    user.vtmb_feed(0)
^feeding state reset$:
    user.vtmb_feed_state_set(0)

^computer hack$:
    key(ctrl-c)
^terminal <user.format_text>+$:
    user.insert_many(format_text_list)
^terminal {user.prose_formatter} <user.prose>$:
    user.insert_formatted(prose, prose_formatter)
^terminal scratch that$:
    user.clear_last_phrase()

dialog history [show]:
    key(home)
dialog [history] up | ceil:
    key(pageup)
dialog [history] down | day:
    key(pagedown)

^hot keys show$:
    key(k)

[blood] buff:
    user.vtmb_hotkey_discipline_use("2")
[blood] heal:
    user.vtmb_hotkey_discipline_use("3")
[blood] strike | try:
    user.vtmb_hotkey_discipline_use("4")
[blood] purge | purr:
    user.vtmb_hotkey_discipline_use("5")
[blood] shield | she:
    user.vtmb_hotkey_discipline_use("6")
command | come:
    user.vtmb_hotkey_discipline_use("7")
[blood] theft | thieve | steal:
    user.vtmb_hotkey_discipline_use("8")