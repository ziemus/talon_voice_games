mode: user.game
and not mode: sleep
and app: hellblade_senuas_sacrifice
-
tag(): user.first_person_game_controls
tag(): user.game_weapon_target_lock
tag(): user.game_weapon_block
tag(): user.wsad_game_controls

focus | cuss:
    key("e:down")
(focus | cuss) (done | down | one):
    key("e:up")

kick | key:
    key("f")
get up:
    user.press_game_key("space", 20)

tar | tech | zip:
    user.game_weapon_target_lock_previous()
rat | rut | cap:
    user.game_weapon_target_lock_next()

light [attack] [mode] [switch | toggle]:
    user.game_noise_control_switch("hiss","long click")
heavy [attack] [mode] [switch | toggle]:
    user.game_noise_control_switch("hiss","right long click")

noise binding exploration mode | noise explore | exploring:
    user.game_noise_control_switch("pop","move")
    user.game_noise_control_switch("hiss","use")
noise binding fight mode | noise fight | fighting:
    user.game_noise_control_switch("pop","block toggle")
    user.game_noise_control_switch("hiss","long click")

touch that:
	user.game_click(0)