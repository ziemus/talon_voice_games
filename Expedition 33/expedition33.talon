mode: user.game
and not mode: sleep
and app: expedition33
-
tag(): user.game_basic_movement
tag(): user.game_camera_controls

# expedition state [show | hide] | turn skip
^turn kip$:			                user.game_hold_key_native("tab", 1200000)
expedition state [show | hide]:     key(tab)
# switch item/ability panel
[it | at] witch:                    key(r)
# switch character
car [witch]:                        key(t)
# toggle walk
walk:                               key(ctrl)
# ingame accessibility options allow for toggling run state, advised
run:                                key(shift)
mount:                              key(z)
^combat flee$:                      user.game_hold_key_native("c", 1200000)
camp return:                        key(g)


# I'm guessing
pause | back | escape:              key(escape)
map show | hide:                    key(m)
# camp set:                         key(?)

# the following are also available via foot pedals or mouth sounds
# DODGE | gradient attack | (item | ability) 1 | heal team
dog | dodge:		key(q)
grad at:			key(q)
(it | at) one:		key(q)
heal em:			key(q)

# MOVE | GRADIENT COUNTER | (item | ability) 2 | show items
grad con:			key(w)
(it | at) two:		key(w)
item [show | hide]:	key(w)

# PARRY | interact | (item | ability) 3 | show skills
par:				key(e)
use:				key(e)
(it | at) three:	key(e)
kill [show | hide]:	key(e)

# strike | [melee] attack:  
hit:				key(f)
[melee] attack:		key(f)

# QUICK TIME EVENT | JUMP | mount fly
jump:				key(space)
mount fly:			key(space)