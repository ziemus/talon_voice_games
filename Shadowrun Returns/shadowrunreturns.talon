app: shadowrunreturns
and mode: user.game
and not mode: sleep
-
tag(): user.game_genre_crpg
tag(): user.game_weapon_switch

[weapon] reload | red:
    key(r)
gear [screen] [show]:
    key(g)
(character | car) last:
    key(shift-tab)
(character | car) next:
    key(tab)
spellbook [show]:
    key(q)
turn end:
    user.game_interactable_objects_highlight_stop()
    key(enter)
game pause:
    key(pagedown)
^fullscreen$:
    key(alt-enter)
