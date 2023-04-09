from talon import Module, Context, actions, ctrl

mod = Module()
mod.apps.dishonored = """
title: Dishonored
and app.name: Dishonored.exe
and app.exe: Dishonored.exe
"""

ctx = Context()
ctx.matches = """
app: dishonored
and mode: user.game
"""
ctx.lists["user.game_number_shortcuts"] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
}


@ctx.action_class("user")
class Actions:

    def game_heal():
        actions.key("r")

    def game_potion_drink():
        actions.key("t")

    def game_crouch():
        actions.key("c")

    def game_skill_use():
        actions.user.game_click(1)
        actions.user.game_weapon_aim_toggle(False)

    def game_stealth_choke():
        actions.user.game_hold_key_native("ctrl", 2550000)

    def game_weapon_block_start():
        actions.key("ctrl:down")

    def game_weapon_block_stop():
        actions.key("ctrl:up")

    def game_weapon_aim_stop():
        actions.user.game_use()
        actions.user.game_press_mouse(1, False)

    def game_weapon_hide():
        actions.user.game_long_use()

    def game_use():
        actions.key("f")

    def game_long_use():
        actions.user.game_hold_key_native("f", 650000)

    def game_hold_use():
        actions.key("f:down")

    def game_release_use():
        actions.key("f:up")

    def game_weapon_draw():
        actions.user.game_use()

    def game_quick_access_menu_show():
        actions.user.game_press_mouse(2, True)

    def game_quick_access_menu_hide():
        actions.user.game_press_mouse(2, False)

    def game_before_on_pop():
        if actions.user.game_is_weapon_aim():
            actions.user.game_skill_use()
            return (False, False)
        return (True, True)
