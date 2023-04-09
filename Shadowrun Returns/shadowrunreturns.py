from talon import Module, Context, actions, ctrl

mod = Module()
mod.apps.shadowrunreturns = """
title: Shadowrun
and app.name: Shadowrun.exe
and app.exe: Shadowrun.exe
"""

ctx = Context()
ctx.matches = """
app: shadowrunreturns
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

    def game_quick_load():
        actions.key("f9")

    def game_weapon_switch_previous():
        actions.key("shift-f")

    def game_weapon_switch_previous():
        actions.key("f")

    def game_interactable_objects_highlight_start():
        actions.key("alt:down")

    def game_interactable_objects_highlight_stop():
        actions.key("alt:up")

    def game_inventory_show():
        actions.key("e")
