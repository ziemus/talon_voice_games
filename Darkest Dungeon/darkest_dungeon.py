from talon import Module, Context, actions, ctrl

mod = Module()
mod.apps.darkest_dungeon = """
title: Darkest Dungeon
and app.exe: darkest.exe
and app.name: Darkest.exe
"""


@mod.action_class
class DarkestDungeonActions:

    def darkest_dungeon_skill_switch(digits: int):
        """Shortcut for switching skills. Accepts only 1-5."""
        if digits in range(1, 6):
            actions.key(f"{digits}")


ctx = Context()
ctx.matches = """
app: darkest_dungeon
and not mode: sleep
and mode: user.game
"""

ctx.lists["user.game_directions"] = {
    "backward": "a",
    "back": "a",
    "west": "a",
    "left": "a",
    "forward": "d",
    "east": "d",
    "right": "d",
}


@ctx.action_class("user")
class GameActions:

    def game_character_sheet_show():
        """Show character card in character roaster.
        This game responds to mouse button down events only after they're pressed for some time"""
        ctrl.mouse_click(button=1, hold=16000)

    def get_game_movement_keys():
        return ["a", "d"]

    def game_before_on_pop():
        actions.user.switch_game_movement(0)