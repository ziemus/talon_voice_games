mode: user.game
and not mode: sleep
and app: horizon_zero_dawn
-
tag(): user.game_action_rpg

# GAME CONTROLS
# MOVEMENT SECTION
slide | lie:
	user.game_crouch()
climb down:
	user.horizon_climb_down()
# EXPLORATION AND INTERACTIONS SECTION
examine | play (it | that):
	user.game_use()
# FOCUS MODE SECTION
focus [mode] [toggle | switch] | scan | cuss:
	key(v)
[target] tag:
	user.game_click(0)
highlight [track] | track:
	key(g)
# TOOLS SECTION
rock [aim]:
	user.horizon_tool_aim_toggle()
[rock] throw | threw:
	user.horizon_tool_throw()

(hud | objectives) show:
	key(h)
(datapoint | note) (view | read):
	user.mouse_stay_in_place(1)
	key(enter)
	sleep(1s)
	key(enter)
	user.mouse_stay_in_place(0)
override:
	user.game_hold_use()
#you can also end override with both hiss and pop or even use/talk to/trade with...
override done:
	user.game_release_use()
# COMBAT CONTROLS
oof | oops | retreat:
	user.horizon_retreat()
# ATTACK MODE SECTION
#it is probably easier to just use a foot pedal than light attack and heavy attack though
light [attack] [mode] [switch | toggle]:
	user.horizon_heavy_attack_mode_toggle(0)
heavy [attack] [mode] [switch | toggle]:
	user.horizon_heavy_attack_mode_toggle(1)
# BOW SECTION
[bow] get | draw concentrate:
	user.horizon_bow_draw()
	key(shift)
[bow] draw:
	user.horizon_bow_draw()
[bow] draw two:
	user.horizon_bow_draw(2)
[bow] draw three:
	user.horizon_bow_draw(3)
fire:
	user.game_press_mouse(0, 0)
reload | red | ret:
	key(r)
concentrate | con | come:
	user.game_weapon_aim_toggle(1)
	key(shift)

# MENU CONTROLS
menu open:
	key(backspace)
page left | quench | quick:
	key(q)
page right | each | eat :
	key(e)
(drop | unequip) (it | that) | (modification | mod) [slot] clear | function [group] 1:
	user.horizon_function_group_1()
disassemble [many | multiple] | job create | show on map | map point | function [group] 2:
	key(g)
# craft voice command takes care of both crafting controls: in weapon wheel and in crafting menu, so I excluded it from function group 3
(take | disassemble | select | equip | modify) (it | that) | quest activate | datapoint play | function [group] 3:
	user.horizon_function_group_3()