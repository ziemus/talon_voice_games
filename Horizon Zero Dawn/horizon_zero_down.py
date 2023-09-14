from talon import Module, Context, actions, ctrl

is_tool_aim: bool = False
is_heavy_attack_mode: bool = False

mod = Module()
mod.apps.horizon_zero_dawn = """
title: Horizon Zero Dawn: Complete Edition
and app.name: Horizon Zero Dawn
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: horizon_zero_dawn
"""
ctx.lists["user.game_number_shortcuts"] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4"
}


@ctx.action_class("user")
class GameActions:

    def game_before_on_pop():
        actions.user.game_release_use()
        return (True, True)

    def game_before_on_hiss(is_start: bool):
        actions.user.game_release_use()
        if is_start and is_heavy_attack_mode:
            actions.key("shift:down")
        return (True, True)

    def game_after_on_hiss(is_start: bool):
        if not is_start and is_heavy_attack_mode:
            actions.key("shift:up")

    def game_mount_stop():
        for i in range(4):
            actions.user.game_mount_ride_slower()
        actions.user.switch_game_movement(False)


@mod.action_class
class HorizonZeroDawnActions:

    def horizon_tool_aim_toggle():
        """"""
        actions.user.horizon_tool_aim(not is_tool_aim)

    def horizon_retreat():
        """fast retreat action to compensate for voice command execution time
        compared to clicking the keys on the keyboard"""
        actions.user.game_quick_access_menu_toggle(False)
        actions.user.game_weapon_aim_toggle(False)
        actions.user.switch_game_movement_direction("s")
        actions.user.switch_game_movement(True)
        actions.user.game_switch_sprint(True)

    def horizon_climb_down():
        """"""
        actions.user.game_crouch()
        actions.user.switch_game_movement_direction("s")

    def horizon_bow_draw(number_of_arrows: int = 1):
        """aim bow if not aiming already and then draw the specified number of arrows"""
        actions.user.game_weapon_aim_toggle(True)
        actions.user.press_game_key("r", number_of_arrows - 1, 500000)
        actions.user.game_press_mouse(0, True)

    def horizon_tool_aim(is_on: bool):
        """"""
        global is_tool_aim
        if is_on:
            actions.key("f:down")
        else:
            actions.user.game_click(1)
            actions.key("f:up")
        is_tool_aim = is_on

    def horizon_tool_throw():
        """"""
        global is_tool_aim
        actions.key("f:up")
        is_tool_aim = False

    def horizon_heavy_attack_mode_toggle(turn_on: bool = None):
        """"""
        global is_heavy_attack_mode
        turn_on = not is_heavy_attack_mode if turn_on is None else turn_on
        is_heavy_attack_mode = turn_on

    def horizon_function_group_3():
        """"""
        actions.user.game_hold_key_native("f", 650000)

    def horizon_function_group_1():
        """"""
        actions.user.game_hold_key_native("r", 650000)
