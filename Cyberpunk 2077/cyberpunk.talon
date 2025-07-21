mode: user.game
and not mode: sleep
and app: cyberpunk2077
-
settings():
	user.game_item_ability_switch_scroll_amount = 10

tag(): user.game_action_rpg

# GAME CONTROLS
[target] tag:
	user.game_click(2)
# ATTACK MODE SECTION
#it is probably easier to just use a foot pedal than light attack and heavy attack though
light [attack] [mode] [switch | toggle]:
	user.cyberpunk_heavy_attack_mode_toggle(0)
heavy [attack] [mode] [switch | toggle]:
	user.cyberpunk_heavy_attack_mode_toggle(1)
quick [attack]:
	key(q)
body take:
	user.game_stealth_body_carry()

cyberware [systems] [show] | implants:
	key(e)
consumable use | consume:
	key(x)
scan [toggle]:
	key(capslock)
[quick] hack details [show] | det:
	key(z)

(dialog | die) {user.game_next_keyword}:
	key(e)
(dialog | die) {user.game_previous_keyword}:
	key(q)
(dialog | die) {user.game_next_keyword} <number>:
	key("e:{number}")
(dialog | die) {user.game_previous_keyword} <number>:
	key("q:{number}")
(dialog | die) skip | kip:
	key(c)

notifications [show | hide]:
	key(n)
[cell | mobile] phone [show | hide] | mobile:
	key(t)

continue that:
	key(c)

# VEHICLE
# it will be probably best to use foot pedals for steering the vehicle
# it'll probably be enough for a standard three pedal switch
# to function as left (a), right (d) and break (s)
# and for the pop move noise control to function as accelerate (w)
# alternatively hiss may function as accelerate and pop as break,
# depending on the timing end precision required
camera cycle | cam change:
	key(q)
straight:
	key(q:3)
vehicle exit | get off:
	#first the handbrake
	key(space)
	user.game_long_use()
[vehicle] jump out:
	user.game_long_use()
camera reverse | cam rev:
	user.game_click(2)
lights cycle | light change:
	key(alt)
handbrake:
	key(space)
horn:
	key(ctrl)
#will probably just use "red" anyway
radio toggle:
	key(r)
#ghouled probably you noise controls for panzer
Panzer Primary Cannon | pan:
	user.game_click(0)
Panzer Missile Launcher | piss:
	user.game_click(1)
smokescreen | [holy] smokes:
	key(Left Ctrl)
vehicle call:
	key(v)