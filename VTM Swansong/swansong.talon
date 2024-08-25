mode: user.game
and not mode: sleep
and app: vtm_swansong
-
tag(): user.first_person_game_controls


auspex | sense [unseen]:
    key(1)
obfuscate | celerity:
    key(2)
^dialog skip$:
    key(space)

focus | cuss:
    user.mouse_scroll_up(8)
(focus | cuss) less:
    user.mouse_scroll_down(8)

car sheet:
    key(tab)
^confirm that$:
    key(space)