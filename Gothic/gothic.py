from talon import Module, Context, actions, ctrl
from enum import Enum

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


class GothicAttackMode(Enum):
    FORWARD = 0
    SIDEWAYS = 1

    def get_next(self):
        if self == GothicAttackMode.FORWARD:
            return GothicAttackMode.SIDEWAYS
        else:
            return GothicAttackMode.FORWARD


class GothicAttackDirection(Enum):
    FORWARD = "up"
    LEFT = "left"
    RIGHT = "right"

    def get_next(self):
        if self == GothicAttackDirection.FORWARD:
            return self
        elif self == GothicAttackDirection.LEFT:
            return GothicAttackDirection.RIGHT
        else:
            return GothicAttackDirection.LEFT

    def __str__(self):
        return str(self.value)


current_attack_mode: GothicAttackMode = GothicAttackMode.FORWARD
current_attack_direction: GothicAttackDirection = GothicAttackDirection.FORWARD


@mod.action_class
class GothicActions:

    def gothic_attack_mode_change(mode: int = None):
        """Change to the specified mode or from the current mode to the alternate attack mode"""
        global current_attack_mode, current_attack_direction
        if mode is None:
            current_attack_mode = current_attack_mode.get_next()
        current_attack_mode = GothicAttackMode(mode)
        if current_attack_mode == GothicAttackMode.FORWARD:
            current_attack_direction = GothicAttackDirection.FORWARD
        else:
            current_attack_direction = GothicAttackDirection.LEFT

@ctx.action_class("user")
class GameActions:

    def game_before_on_hiss():
        global current_attack_direction
        # attack uses the same key binding as interaction, as attacking forward
        # so there is no need to declare a different attack noise binding
        if current_attack_mode == GothicAttackMode.FORWARD:
            return (True, True)
        # if the player wants to tack sideways the attack key needs to change automatically
        # to allow the player for performing combos
        attack_key = current_attack_direction
        actions.key(f"ctrl-{attack_key}")
        current_attack_direction = current_attack_direction.get_next()
        return (False, False)

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

    def game_quest_log_show():
        actions.key("l")

    def game_dodge():
        actions.key("down")

    def game_long_dodge():
        actions.user.game_dodge()

    def game_loot():
        actions.user.game_weapon_target_lock_toggle(True)
        actions.user.game_use()

    def game_inventory_show():
        actions.key("tab")

    def game_take_number(digits: int):
        actions.key(f"ctrl:down right:{digits} ctrl:up")

    def game_take_all():
        actions.key("ctrl-alt-right")

    def game_trade_buy_item():
        actions.user.game_take_number(1)

    def game_trade_buy_multiple_items():
        actions.user.game_take_all()

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
