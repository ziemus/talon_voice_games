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

    def game_lean_left_start():
        actions.key("q:down")

    def game_lean_left_stop():
        actions.key("q:up")

    def game_lean_right_start():
        actions.key("e:down")

    def game_lean_right_stop():
        actions.key("e:up")

    def game_heal():
        actions.key("r")

    def game_crouch():
        actions.key("c")

    def game_skill_use():
        actions.user.game_click(1)

    def game_stealth_kill():
        #actually not a kill but choking, but since a stealth kill in this game is achieved with just attacking one can just hiss instead of that
        actions.user.game_hold_key_native("ctrl", 2550000)

    def game_weapon_block_start():
        actions.key("ctrl:down")

    def game_weapon_block_stop():
        actions.key("ctrl:up")

    def game_use():
        actions.key("f")

    def game_hold_use():
        actions.user.game_hold_key_native("f", 650000)

    def game_weapon_draw():
        actions.user.game_use()

    def game_quick_access_menu_show():
        actions.user.game_press_mouse(2, True)

    def game_quick_access_menu_hide():
        actions.user.game_press_mouse(2, False)
