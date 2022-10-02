mode: user.game
and not mode: sleep
and app: TheTalosPrinciple
-
settings():
	user.mouse_enable_pop_click = 0
	user.game_turn_around_mouse_delta = 787
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "click"

tag(): user.wsad_game_controls
tag(): user.first_person_game_controls

# no binding by default
(secondary | second | sec) [fire]:
    user.press_game_key('r')
use | take | drop | connect | select | touch | jam | click | yoink:
	mouse_click(0)
(alternative | alternate | alt) [use]:
	mouse_click(1)
([third] [person] view) | camera | cam:
	user.press_game_key('h')
^reset test$:
	user.talos_reset_test()
reset [stop]:
	user.release_game_key('x')
[show] (journal | log):
    user.release_game_key('shift')
    sleep(100ms)
	user.press_game_key('tab')
#no binding by default
fast forward:
	user.press_game_key('f')
(Toby | Tobii) reset:
	user.press_game_key('o')
[invoke] menu:
	user.press_game_key('f10')
exit test:
	user.press_game_key('escape')
[activate] console:
	user.press_game_key('f1')
[take] screenshot:
	user.press_game_key('f11')

# the default binding of the zoom in is to mouse scroll
# user.mouse_scroll() didn't do anything in the game
# this is not a default binding that you need to change in-game
# for the voice command to work
zoom in | close:
	user.hold_game_key('pageup')
zoom out | far:
	user.release_game_key('pageup')
(scroll | page) up:
	user.press_game_key('pageup')
(scroll | page) down:
	user.press_game_key('pagedown')

key(3):
    user.game_jump()
key(2):
	user.switch_game_movement()
key(1):
    user.game_turn_camera_around()