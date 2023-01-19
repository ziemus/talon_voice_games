mode: user.game
and not mode: sleep
and app: vtm_bloodlines
-
settings():
    user.game_turn_around_mouse_delta = 780
	user.game_turn_horizontally_mouse_delta = 380
	user.game_turn_vertically_mouse_delta = 100
    user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "long click"
    user.game_sprint_state_default = 1
    
tag(): user.game_arrow_keys_toggle_wsad_movement
tag(): user.first_person_game_controls

noise binding exploration mode | noise explore | exploring:
	user.game_noise_control_switch("pop","move")
	user.game_noise_control_switch("hiss","long click")
noise binding fight mode | noise fight | fighting:
	user.game_noise_control_switch("pop","right click")
	user.game_noise_control_switch("hiss","long click")

[attack] secondary | sec:
    key(tab)
block:
    key(tab:down)
block done:
    key(tab:up)

[weapon] (holster | hide):
    key(h)
weapon last:
    key(\)
weapon drop:
    key(backspace)
[weapon] (melee | white):
    key(f1)
[weapon] (ranged | range):
    key(f2)
[weapon] (thrown | throw | threw):
    key(f5)

armor [clothing]:
    key(f3)

[discipline] power show [all]:
    key(f6)
#it will probably be easier with just pop in "noise binding fight mode"
[discipline] power [use]:
    mouse_click(1)
[discipline] power end [all]:
    key(f8)

(discipline | weapon) [switch | toggle]:
    key(t)
(discipline | weapon) (previous | prev) | zip:
    key(])
(discipline | weapon) next | zap:
    key([)

eat | feed:
    key(f)

^computer hack$:
    key(ctrl-c)
^terminal [type] <user.format_text>+$:
    user.insert_many(format_text_list)
^terminal scratch that$:
    user.clear_last_phrase()

dialog history [show]:
    key(home)
dialog [history] up | ceil:
    key(pageup)
dialog [history] down | day:
    key(pagedown)

hot keys show:
    key(k)