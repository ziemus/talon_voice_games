from talon import Module, Context, actions, ctrl

is_tool_aim: bool = False
is_heavy_attack_mode: bool = False

mod = Module()
mod.apps.gothic = """
title: GOTHIC 1
and app.name: GOTHIC
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: gothic
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
class GameActions:

    def game_weapon_draw():
        actions.key("space")

    def game_weapon_melee_show():
        actions.key("1")

    def game_weapon_ranged_show():
        actions.key("2")

    def game_weapon_block_start():
        actions.user.game_weapon_target_lock_toggle(True)
        actions.key("down:down")

    def game_weapon_block_stop():
        actions.key("down:up")
        # don't release ctrl so that you don't lose your target lock

    def game_weapon_target_lock_start():
        actions.key("ctrl:down")

    def game_weapon_target_lock_stop():
        actions.key("ctrl:up")

    def game_dodge():
        actions.key("down")

    def game_long_dodge():
        actions.user.game_dodge()

    def game_inventory_show():
        actions.key("tab")

    def game_trade_buy_item():
        actions.key("ctrl-right")

    def game_trade_buy_multiple_items():
        actions.key("ctrl-alt-right")

    def game_trade_sell_item():
        actions.key("ctrl-left")

    def game_trade_sell_multiple_items():
        actions.key("ctrl-alt-left")

    def game_use():
        actions.key("ctrl-up")

    def game_jump(is_hold: bool = None):
        actions.key("alt")

    def game_crouch():
        actions.key("x")
        # TODO check if this needs to be pressed or just toggles

    def game_dive_start():
        actions.key("alt:down")

    def game_dive_stop():
        actions.key("alt:up")

    def game_camera_first_person():
        actions.key("f:down")

    def game_camera_third_person():
        actions.key("f:up")

    def game_quick_load():
        actions.key("f9")
