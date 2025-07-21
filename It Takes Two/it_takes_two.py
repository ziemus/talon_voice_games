from talon import Module, Context, actions

mod = Module()
mod.apps.it_takes_two = """
os: windows
and app.name: It Takes Two
"""

ctx = Context()
ctx.matches = """
app: it_takes_two
"""

@ctx.action_class("user")
class Actions:
    def game_start_running():
        actions.key("capslock")

    def game_start_walking():
        actions.key("capslock")

    def game_switch_sprint(do_turn_on: bool = None):
        actions.key("capslock")

    def game_crouch():
        actions.user.toggle_hold_key("c")


@ctx.action_class("user")
class FootSwitchActions:
    def foot_switch_olympus_top_down():
        actions.key("f:down")

    def foot_switch_olympus_top_up(held: bool):
        actions.key("f:up")

    def foot_switch_olympus_center_down():
        actions.key("w:down")

    def foot_switch_olympus_center_up(held: bool):
        actions.key("w:up")

    def foot_switch_olympus_left_down():
        actions.key("e:down")

    def foot_switch_olympus_left_up(held: bool):
        actions.key("e:up")

    def foot_switch_olympus_right_down():
        actions.key("shift:down")

    def foot_switch_olympus_right_up(held: bool):
        actions.key("shift:up")

    def foot_switch_pcsensor_center_down():
        actions.key("f:down")

    def foot_switch_pcsensor_center_up(held: bool):
        actions.key("f:up")

    def foot_switch_pcsensor_left_down():
        actions.skip()

    def foot_switch_pcsensor_left_up(held: bool):
        actions.user.game_crouch()

    def foot_switch_pcsensor_right_down():
        actions.user.mouse_drag_toggle(0)

    def foot_switch_pcsensor_right_up(held: bool):
        actions.user.mouse_drag_toggle(0)