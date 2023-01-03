from talon import Module, Context, actions, ctrl

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

is_tool_aim: bool = False
is_weapon_aim: bool = False
is_weapon_wheel: bool = False

@ctx.action_class("user")
class GameActions:

    def game_before_on_pop():
        actions.user.horizon_override(False)

    def game_before_on_hiss():
        actions.user.horizon_override(False)

    def game_switch_sprint(do_turn_on: bool):
        actions.key("shift")  # there is no point in tracking sprint state in this game


@mod.action_class
class HorizonZeroDawnActions:

    def horizon_weapon_aim_toggle():
        """"""
        actions.user.horizon_weapon_aim(not is_weapon_aim)

    def horizon_tool_aim_toggle():
        """"""
        actions.user.horizon_tool_aim(not is_tool_aim)

    def horizon_override(is_override: bool):
        """"""
        if is_override:
            actions.key("e:down")
        else:
            actions.key("e:up")

    def horizon_retreat():
        """fast retreat action to compensate for voice command execution time
        compared to clicking the keys on the keyboard"""
        actions.user.horizon_weapon_wheel(False)
        actions.user.horizon_weapon_aim(False)
        actions.user.switch_game_movement_direction("s")
        actions.user.switch_game_movement(True)
        # actions.user.game_turn_camera_around()
        actions.user.game_switch_sprint(True)

    def horizon_duck():
        """"""
        actions.key("c")

    def horizon_weapon_wheel_toggle():
        """"""
        actions.user.horizon_weapon_wheel(not is_weapon_wheel)

    def horizon_weapon_wheel(is_show: bool):
        """"""
        global is_weapon_wheel
        if is_show:
            actions.key("tab:down")
        else:
            actions.key("tab:up")
        is_weapon_wheel = is_show

    def horizon_climb_down():
        """"""
        actions.user.horizon_duck()
        actions.user.switch_game_movement_direction("s")

    def horizon_weapon_aim(is_on: bool):
        """"""
        global is_weapon_aim
        actions.user.game_press_mouse(1, is_on)
        is_weapon_aim = is_on

    def horizon_bow_draw(is_on: bool):
        """aim ranged weapon and/or draw arrow
        or cancel aiming drawn weapon"""
        if is_on:
            actions.user.horizon_weapon_aim(True)
            actions.user.game_press_mouse(0, True)
        else:
            actions.user.horizon_weapon_aim(False)
            actions.user.game_press_mouse(0, False)

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
