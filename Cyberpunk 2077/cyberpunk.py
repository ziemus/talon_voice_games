from talon import Module, Context, actions

is_heavy_attack_mode: bool = False

mod = Module()
mod.apps.cyberpunk2077 = """
app.name: Cyberpunk 2077
and app.exe: /^cyberpunk2077\\.exe$/i
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: cyberpunk2077
"""
ctx.lists["user.game_number_shortcuts"] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4"
}


@ctx.action_class("user")
class GameActions:

    def game_use():
        actions.key("f")

    def game_long_use():
        actions.user.game_hold_key_native("f", 1000000)

    def game_heal():
        actions.key("x")
    
    def game_before_on_pop():
        return (True, True)

    def game_before_on_hiss(is_start: bool):
        if is_start and is_heavy_attack_mode:
            actions.key("shift:down")
        return (True, True)

    def game_after_on_hiss(is_start: bool):
        if not is_start and is_heavy_attack_mode:
            actions.key("shift:up")

    def game_tool_use():
        actions.user.game_click(2)

    def game_stealth_kill():
        actions.user.game_use()

    def game_stealth_choke():
        actions.key("r")

# TODO Integrate attack mode change into game mode controls
# TODO game_attack() behavior and probably game_click() should take into account the current attack mode
@mod.action_class
class Cyberpunk2077Actions:

    def game_stealth_body_carry():
        """"""
        actions.user.game_hold_key_native("r", 1000000)

    def cyberpunk_heavy_attack_mode_toggle(turn_on: bool = None):
        """"""
        global is_heavy_attack_mode
        turn_on = not is_heavy_attack_mode if turn_on is None else turn_on
        is_heavy_attack_mode = turn_on

