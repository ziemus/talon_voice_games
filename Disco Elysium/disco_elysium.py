from talon import Module, Context, actions

mod = Module()
mod.apps.disco_elysium = """
title: Disco Elysium
and app.exe: Disco Elysium.exe
and app.name: Disco Elysium.exe
"""

ctx = Context()
ctx.matches = """
app: disco_elysium
and not mode: sleep
and mode: user.game
"""


@ctx.action_class('user')
class GameActions:

    def is_default_eye_mouse_noise_behavior():
        return False

    def game_before_on_pop():
        actions.user.mouse_scroll_stop()