from talon import Module, Context, actions

mod = Module()
mod.apps.planet_of_lana = """
os: windows
and app.name: Unity playback engine.
and app.exe: /^planet\ of\ lana\.exe$/i
and title: Planet of Lana
"""

ctx = Context()
ctx.matches = """
app: planet_of_lana
"""

@ctx.action_class("user")
class Actions:
    def game_jump(is_hold: bool):
        actions.key("space")

@ctx.action_class("user")
class FootSwitchActions:
    def foot_switch_olympus_top_down():
        actions.key("w:down")

    def foot_switch_olympus_top_up(held: bool):
        actions.key("w:up")

    def foot_switch_olympus_center_down():
        actions.key("s:down")

    def foot_switch_olympus_center_up(held: bool):
        actions.key("s:up")

    def foot_switch_olympus_left_down():
        actions.key("a:down")

    def foot_switch_olympus_left_up(held: bool):
        actions.key("a:up")

    def foot_switch_olympus_right_down():
        actions.key("d:down")

    def foot_switch_olympus_right_up(held: bool):
        actions.key("d:up")

    def foot_switch_pcsensor_center_down():
        actions.key("space:down")

    def foot_switch_pcsensor_center_up(held: bool):
        actions.key("space:up")

    def foot_switch_pcsensor_left_down():
        actions.key("q:down")

    def foot_switch_pcsensor_left_up(held: bool):
        actions.key("q:up")

    def foot_switch_pcsensor_right_down():
        actions.key("e:down")

    def foot_switch_pcsensor_right_up(held: bool):
        actions.key("e:up")

