mode: user.game
and not mode: sleep
and app: expedition33
-
tag(): user.game_basic_movement
tag(): user.game_camera_controls

<user.letter>: key(letter)

# expedition state | turn skip
^turn kip$:			                user.game_hold_key_native("tab", 1200000)
team [show | hide]:                 key(tab)
# switch item/ability panel
[it | at] witch:                    key(r)
# switch character
car [witch]:                        key(t)
# toggle walk
slow:                               key(ctrl)
# ingame accessibility options allow for toggling run state, advised
run:                                key(shift)
mount | dismount:                   key(z)
^combat flee$:                      user.game_hold_key_native("c", 1200000)

# target right/left
tar:                                key(d)
tall:                               key(a)
# climb down
doo:                                key(s)

pause | back | escape:              key(escape)
map show:                           key(m)
camp set:                           key(g)

# the following are also available via foot switches or mouth sounds
# DODGE | gradient attack | (item | ability) 1 | heal team
dog | dodge:		key(q)
grad at:			key(q)
(it | at) one:		key(q)
^heal team$:		user.game_hold_key_native("q", 1200000)

# MOVE | GRADIENT COUNTER | (item | ability) 2 | show items
grad con:			key(w)
(it | at) two:		key(w)
item [show | hide]:	key(w)

# PARRY | interact | (item | ability) 3 | show skills
parry:				key(e)
use | talk | pick:  key(e)
(it | at) three:	key(e)
kill [show | hide]:	key(e)

# [melee] attack | learn skill | upgrade gear:  
hit:				key(f)
^kill learn$:       user.game_hold_key_native("f", 1200000)
^gear upgrade$:     user.game_hold_key_native("f", 1200000)

# QUICK TIME EVENT | JUMP | mount fly
jump:				key(space)
mount fly:			key(space)

gun:                user.game_click(1,1,120000)
touch:              user.game_click(0,1,120000)

^cutscene skip$:    user.game_hold_key_native("escape", 1200000)