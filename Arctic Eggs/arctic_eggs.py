from talon import Module, Context, actions

mod = Module()
mod.apps.arctic_eggs = """
os: windows
and title: Arctic Eggs
and app.name: Godot Engine
and app.exe: /^game\.exe$/i
"""

ctx = Context()
ctx.matches = """
app: arctic_eggs
"""

@ctx.action_class("user")
class FootSwitchActions:
    def foot_switch_olympus_top_down():
        actions.skip()

    def foot_switch_olympus_top_up(held: bool):
        actions.user.game_turn_camera_around()

    def foot_switch_olympus_center_down():
        actions.key("w:down")

    def foot_switch_olympus_center_up(held: bool):
        actions.key("w:up")

    def foot_switch_olympus_left_down():
        actions.skip()

    def foot_switch_olympus_left_up(held: bool):
        actions.user.game_turn_camera('left')

    def foot_switch_olympus_right_down():
        actions.skip()

    def foot_switch_olympus_right_up(held: bool):
        actions.user.game_turn_camera('right')

    def foot_switch_pcsensor_center_down():
        actions.key("space:down")

    def foot_switch_pcsensor_center_up(held: bool):
        actions.key("space:up")

    def foot_switch_pcsensor_left_down():
        actions.user.mouse_scroll_up_continuous()

    def foot_switch_pcsensor_left_up(held: bool):
        actions.user.mouse_scroll_stop()

    def foot_switch_pcsensor_right_down():
        actions.user.mouse_scroll_down_continuous()

    def foot_switch_pcsensor_right_up(held: bool):
        actions.user.mouse_scroll_stop()