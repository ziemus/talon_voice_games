from talon import Module, Context, actions


mod = Module()
mod.apps.vtm_swansong = """
app.name: Dawn of War II
and app.exe: /^dow2\.exe$/i
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: dawn_of_war_2
"""

@ctx.action_class("user")
class Actions:
    def game_menu():
        actions.key("f10")
