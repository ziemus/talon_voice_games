mode: user.game
and not mode: sleep
and app: Antichamber
-
tag(): user.wsad_game_controls
tag(): user.first_person_game_controls

tic | click:
    mouse_click(0)

#no sprint toggle in game, so the run and run hold comments do the same thing
#inverted sprint mechanism
run [hold]:
    user.release_game_key('shift')
walk [hold]:
    user.hold_game_key('shift')

^Antichamber return$:
    user.press_game_key('escape')
^Antichamber quit$:
	user.hold_game_key('escape', '2s')