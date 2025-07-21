app: it_takes_two
and mode: user.game
and not mode: sleep
-
tag(): user.game_camera_controls
tag(): user.game_basic_movement
tag(): user.game_sprint_controls

crouch | duck:
	user.game_crouch()
cancel:
    key("q")