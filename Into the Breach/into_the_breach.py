from talon import Module, Context, actions

mod = Module()
mod.apps.into_the_breach = """
os: windows
app.name: Breach.exe
and app.exe: /^breach\.exe$/i
"""

ctx = Context()
ctx.matches = """
app: into_the_breach
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
    def foot_switch_olympus_top_down():
        actions.key("alt:down")

    def foot_switch_olympus_top_up(held: bool):
        actions.key("alt:up")

    def foot_switch_olympus_center_down():
        actions.key("ctrl:down")

    def foot_switch_olympus_center_up(held: bool):
        actions.key("ctrl:up")