mode: user.game
and not mode: sleep
and title: /Antichamber/
and app.name: /UDK.exe/
and app.exe: /UDK.exe/
-
settings():
    user.mouse_enable_pop_click = 0
    user.game_turn_around_mouse_delta = 555
    user.game_sprint_state_default = 0
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "jump"

tag(): user.first_person_game_controls

tic | click:
    mouse_click(0)

#no sprint toggle in game, so the run and run hold comments do the same thing
#inverted sprint mechanism
run [hold]:
    user.release_game_key('shift')
walk [hold]:
    user.game_hold_key_native('shift')

^Antichamber return$:
    user.press_game_key('escape')
^Antichamber quit$:
	user.game_hold_key_native('escape', 2000000)