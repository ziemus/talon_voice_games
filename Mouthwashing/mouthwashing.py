from talon import Module, Context, actions

mod = Module()
mod.apps.mouthwashing = """
os: windows
and app.name: Mouthwashing.exe
and app.exe: /^mouthwashing\.exe$/i
and title: Mouthwashing
"""

ctx = Context()
ctx.matches = """
app: mouthwashing
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