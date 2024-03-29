from talon import Module, Context, actions, ctrl

mod = Module()
mod.apps.darkest_dungeon_2 = """
title: Darkest Dungeon II
and app.exe: Darkest Dungeon II.exe
"""

ctx = Context()
ctx.matches = """
app: darkest_dungeon_2
and mode: user.game
"""


@ctx.action_class("user")
class GameActions:
    
    def game_before_on_pop():
        actions.key("w:up")
        return (True, True)
    
    def on_hiss_start():
        actions.key("w:down")
        actions.next()