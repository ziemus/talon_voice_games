from talon import Module, Context, actions

mod = Module()
mod.apps.dos2 = """
app.name: Divinity Original Sin 2
and app.exe: /^eocapp\\.exe$/i
"""

ctx = Context()
ctx.matches = """
app: dos2
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
    "eleven": "-",
    "twelve": "=",
}

@ctx.action_class("user")
class FootSwitchActions:
    def foot_switch_olympus_center_down():
        actions.user.toggle_hold_key("w")

    def foot_switch_olympus_center_up(held: bool):
        actions.user.toggle_hold_key("w")

    def foot_switch_olympus_top_down():
        actions.skip()
    
    def foot_switch_olympus_top_up(held: bool):
        actions.user.toggle_hold_key("/")

    def foot_switch_pcsensor_center_down():
        actions.user.mouse_scroll_down_continuous()

    def foot_switch_pcsensor_center_up(held: bool):
        actions.user.mouse_scroll_stop()

    def foot_switch_pcsensor_left_down():
        actions.user.mouse_scroll_up_continuous()
        
    def foot_switch_pcsensor_left_up(held: bool):
        actions.user.mouse_scroll_stop()
               
    def foot_switch_pcsensor_right_down():
        actions.user.mouse_drag(2)

    def foot_switch_pcsensor_right_up(held: bool):
        actions.user.mouse_drag_end()