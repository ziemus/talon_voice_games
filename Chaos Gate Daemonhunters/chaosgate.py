from talon import Module, Context, actions

mod = Module()
mod.apps.chaos_gate_daemonhunters = """
app.name: ChaosGate.exe
and app.exe: /^chaosgate\.exe$/i
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: chaos_gate_daemonhunters
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