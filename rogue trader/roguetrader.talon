app: wh40k_rogue_trader
and not mode: sleep
-
tag(): user.game_genre_crpg
tag(): user.game_camera_keyboard_controls
tag(): user.game_camera_zoom
tag(): user.game_map
tag(): user.game_basic_movement

(encyclopedia | index) show: key(l)
colony [management] show: key(y)
cargo [management] show: key(b)
[void] ship go: key(v)
(formation | form) show: key(n)

take all:
    user.game_jump()
[game] pause:
    user.game_jump()

stop | top: key(g)
position hold | hold up | relax: key(h)
[cam] follow [car]: key(f)
UI (show | hide) <digits>:
    key("ctrl-f11:{digits}")

log show: key(p)
tab last: key(shift-q)
tab next: key(shift-e)
car last: key(shift-a)
car next: key(shift-d)

car {user.wh40k_rogue_trader_character_shortcuts}:
    key("alt-{wh40k_rogue_trader_character_shortcuts}")
party take: key(backspace)

dialog end: key(space)
weapon switch: key(x)
weapon {user.wh40k_rogue_trader_weapon_shortcuts}:
    key("{wh40k_rogue_trader_weapon_shortcuts}")
consume {user.wh40k_rogue_trader_consumable_shortcuts}:
    key("{wh40k_rogue_trader_consumable_shortcuts}")
(ability | skill | kill) {user.wh40k_rogue_trader_ability_shortcuts}:
    key("{wh40k_rogue_trader_ability_shortcuts}")

^mod manager show$: key(ctrl-f10)
^owlcat mod UI show$: key(shift-f10)