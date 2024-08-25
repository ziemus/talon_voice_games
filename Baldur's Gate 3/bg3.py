from talon import Module, Context, actions

mod = Module()
mod.apps.baldurs_gate_3 = """
app.name: bg3.exe
and app.exe: /bg3(_dx11)?\.exe/
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: baldurs_gate_3
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
    "twelve": "="
}

#@ctx.action("user.game_before_on_hiss")
#def game_before_on_hiss(is_start: bool):
#    if is_start:
#        actions.key("t")
#    return (True, True)