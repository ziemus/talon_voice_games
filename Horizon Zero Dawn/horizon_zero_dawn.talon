mode: user.game
and not mode: sleep
and app: horizon_zero_dawn
-
settings():
	user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
	user.mouse_continuous_scroll_amount = 250
	user.mouse_wheel_down_amount = 250
    key_hold = 64.0
	key_wait = 16.0
    user.mouse_hold = 64000
	user.mouse_wait = 0
	user.game_turn_around_mouse_delta = 500
	user.game_turn_horizontally_mouse_delta = 300
	user.game_turn_vertically_mouse_delta = 100
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "click"

tag(): user.wsad_game_controls
tag(): user.first_person_game_controls
tag(): user.game_mouse_enabled

# GAME CONTROLS
# MOVEMENT SECTION
walk | run:
	key(capslock)
sprint | print:
	user.game_switch_sprint(1)
slide | lie:
	user.horizon_duck()
(crouch | duck) [toggle | switch]:
	user.horizon_duck()
climb down:
	user.horizon_climb_down()
dive:
	key(ctrl:down)
dive done:
	key(ctrl:up)
roll | dodge | dog:
	key(ctrl)
# EXPLORATION AND INTERACTIONS SECTION
(interact | talk | trade | examine) with | talk to | use | play (it | that) | pick [up] | gather:
	user.game_use()
(loot | harvest | search) (it | that):
	user.game_hold_key_native("e", 650000)
# FOCUS MODE SECTION
focus [mode] [toggle | switch] | scan:
	key(v)
[target] tag:
	user.game_click(0)
highlight [track] | track:
	key(g)
# TOOLS SECTION
(medicine [pouch] | pouch) [use] | heal:
	key(q)
[selected] tool [use]:
	key(f)
rock [aim]:
	user.horizon_tool_aim_toggle()
# no aim | aim done will get the same job done as rock aim done
rock (no aim | aim done):
	user.horizon_tool_aim(0)
[rock] throw:
	user.horizon_tool_throw()
# HUD SECTION
tool [cycle] left | zip:
	key(z)
tool [cycle] right | zap | lex:
	key(x)
[weapon] [fast] [equip | switch] {user.game_number_shortcuts}:
	key(game_number_shortcuts)
(hud | objectives) show:
	key(h)
[weapon] wheel [show]:
	user.horizon_weapon_wheel_toggle()
no [weapon] wheel | [weapon] wheel (hide | done):
	user.horizon_weapon_wheel(0)
craft:
	user.game_click(0, 1, 650000)
	user.game_hold_key_native("f", 650000)
(datapoint | note) (view | read):
	user.mouse_stay_in_place(1)
	key(enter)
	sleep(1s)
	key(enter)
	user.mouse_stay_in_place(0)
# SAVES SECTION
manual save:
	key(g)
quicksave:
	user.game_use()
# MOUNTS SECTION
override:
	user.horizon_override(1)
#you can also end override with both hiss and pop
no override | override done:
	user.horizon_override(0)
mount | dismount:
	user.game_use()
[mount] [ride] fast:
	user.game_switch_sprint(0)

[mount] [ride] slow:
	key(ctrl)
[mount] halt:
	key(ctrl)
	key(ctrl)
	key(ctrl)
	key(ctrl)
	user.switch_game_movement(0)
# COMBAT CONTROLS
# RETREAT SECTION
#get out from hiding after being detected (possibly while crouching)
oof | oops:
	user.horizon_duck()
	user.horizon_retreat()
nope:
	user.horizon_retreat()
#it is probably easier to just use a foot pedal than light attack and heavy attack though
# ATTACK MODE SECTION
light [attack] [mode] [switch | toggle]:
	key(shift:up)
heavy [attack] [mode] [switch | toggle]:
	key(shift:down)
# AIMING SECTION
[bow] get | draw concentrate:
	user.horizon_bow_draw(1)
	key(shift)
[bow] draw:
	user.horizon_bow_draw(1)
[bow] fire | fun:
	user.game_press_mouse(0, 0)
[bow] quit:
	user.horizon_bow_draw(0)
# toggle aim on and off
aim:
	user.horizon_weapon_aim_toggle()
# toggle weapon and rock (tool) aim off
aim done | no aim:
	user.horizon_tool_aim(0)
	user.horizon_weapon_aim(0)
reload | red:
	key(r)
concentrate | concentration | con | come:
	user.horizon_weapon_aim(1)
	key(shift)

# MENU CONTROLS
menu open:
	key(backspace)
menu [pause] | escape | back:
	key(escape)
page left | quench | quick:
	key(q)
page right | each | eat :
	key(e)
take all:
	key(e)
(drop | unequip) (it | that) | (modification | mod) [slot] clear | mark [to] sell | function [group] 1:
	#key(r)
	user.game_hold_key_native("r", 650000)
disassemble [many | multiple] | sell (many | multiple) | job create | show on map | map point | function [group] 2:
	key(g)
# craft voice command takes care of both crafting controls: in weapon wheel and in crafting menu, so I excluded it from function group 3
skill learn | (take | disassemble | buy | sell | select | equip | modify) (it | that) | quest activate | datapoint play | function [group] 3:
	user.game_hold_key_native("f", 650000)
skill tree [show]:
	key(k)
crafting [show]:
	key(o)
(journal | quest log) [show]:
	key(j)
map [show]:
	key(m)
[map] waypoint [place]:
	user.game_click(1)
map center:
	key(g)
map filter:
	key(tab)
[map] [filter] [icons] toggle:
	key(f)
[map] [filter] [icons] toggle all:
	key(g)
(notebook | notes) [show]:
	key(n)