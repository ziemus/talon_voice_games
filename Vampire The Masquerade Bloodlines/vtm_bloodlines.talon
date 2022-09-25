mode: user.game
and not mode: sleep
and app: vtm_bloodlines
-
tag(): user.wsad_game_controls
tag(): user.first_person_game_controls

duck | crouch | lean:
    key(ctrl)
[attack] secondary | sec:
    key(tab)
[weapon] (reload | rel | red):
    key(r)

[weapon] (holster | hide):
    key(h)
[weapon] last:
    key(\)
[weapon] drop:
    key(backspace)
[weapon] (melee | white | why):
    key(f1)
[weapon] (ranged | range | ray):
    key(f2)
[weapon] (thrown | throw | row):
    key(f5)

armor [clothing]:
    key(f3)

discipline [available | show]:
    key(f6)

[discipline] (pow | power) [use]:
    mouse_click(1)

discipline end [all] | ditch all:
    key(f8)

[discipline | weapon] (toggle | switch):
    key(t)
[discipline | weapon] (previous | prev | pre):
    key(])
[discipline | weapon] (next | nest | ness):
    key([)


eat | feed:
    key(f)

[quest] (log | journal):
    key(l)
(character | car) [sheet | editor]:
    key(c)

dialog history [show]:
    key(home)
dialog [history] up | ceil:
    key(pageup)
dialog [history] down | day:
    key(pagedown)

quick save:
    key(f9)
quick load:
    key(f12)

menu | go back | cancel | escape:
    key(escape)
hot keys [show]:
    key(k)
console show:
    key(`)

view [toggle]:
    key(z)

