mode: user.game
and not mode: sleep
and app: dragon_age_origins
-
tag(): user.game_genre_crpg
tag(): user.game_map
tag(): user.game_camera_keyboard_controls
tag(): user.game_camera_zoom
#tag(): user.game_basic_movement
tag(): user.game_sprint_controls

[tactical] pause | pass:
    key(space)

party select | party take:
    key("=")
car {user.dao_hero_selection}:
    key(dao_hero_selection)
group car {user.dao_hero_selection}:
    key("shift-{dao_hero_selection}")

skills show:
    key(k)
(spellbook | talents) show:
    key(p)
world map show:
    key(n)
tactic show:
    key(\)
weapon switch:
    key(/)

hold position | hold up | move freely | relax:
    key(h)
hud (show | hide):
    key(v)

#pop misheard as "go" too often
#and pot as go
#go | pot: skip()