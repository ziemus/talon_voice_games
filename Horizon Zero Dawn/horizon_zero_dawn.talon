mode: user.game
and not mode: sleep
and app: horizon_zero_dawn
-
settings():
	user.mouse_enable_pop_click = 0
	user.mouse_hide_mouse_gui = 1
    key_hold = 64.0
	key_wait = 16.0
    user.mouse_hold = 64000
	user.mouse_wait = 0
	user.game_turn_around_mouse_delta = 999
	user.game_turn_sideways_mouse_delta = 800
    user.game_noise_pop_binding_default = "move"
    user.game_noise_hiss_binding_default = "click"

tag(): user.wsad_game_controls
tag(): user.first_person_game_controls

# all standard keybindings
# except for sprint toggle bound to backslash instead of caps lock

touch | click | yoink:
	user.game_click(0)

# game
slide | (crouch | duck) [toggle | switch]:
	key(c)
[dodge] roll | dodge | [slow] mount:
	key(ctrl)
interact | use | play | pick [up] | gather | quicksave:
	key(e)
loot | harvest:
	user.game_hold_key_native("e", 1500000)
focus [mode] [toggle | switch]:
	key(v)
(medicine [pouch] | pouch) [use]:
	key(q)
[selected] (trap | tool) [use]:
	key(f)
(trap | tool | rock) aim:
	key(f:down)
(trap | tool | rock) (quit | cancel | no aim | aim done):
	user.game_click(1)
	key(f:up)
(trap | tool | rock) (throw | release):
	key(f:up)
tools [cycle] left:
	key(z)
tools [cycle] right:
	key(x)
(hud | objectives) show:
	key(h)
manual save:
	key(g)

# combat
[weapon] [switch | equip] <digits>:
	user.horizon_zero_dawn_weapon_switch(digits)
#it is probably easier to just use a foot pedal than light attack and heavy attack though
light attack [mode] [switch | toggle]:
	key(shift:up)
heavy attack [mode] [switch | toggle]:
	key(shift:down)
aim:
	user.game_press_mouse(1, 1)
aim done | no aim:
	user.game_press_mouse(1, 0)
reload | red:
	key(r)
concentrate | concentration:
	key(shift)
[weapon] wheel [show]:
	key(tab:down)
no [weapon] wheel | [weapon] wheel (hide | done):
	key(tab:up)
craft:
	user.game_click(0, 1, 650000)
[target] tag:
	user.game_click(0)

# menu
menu open:
	key(backspace)
menu pause | escape:
	key(escape)
page left:
	key(q)
page right:
	key(e)
take all:
	key(e)
drop | unequip | (modification | mod) clear | ditch:
	key(r)
highlight [track] | disassemble all:
	key(g)
take | select | equip | modify | disassemble:
	key(f)
(skills | skill tree) [show]:
	key(k)
crafting [show]:
	key(o)
(journal | log | quests | quest) [show]:
	key(j)
map [show]:
	key(m)
(notebook | notes) [show]:
	key(n)