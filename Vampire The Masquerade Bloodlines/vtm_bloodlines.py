from talon import Module, Context

mod = Module()
mod.apps.vtm_bloodlines = """
title: Vampire: Bloodlines
and app.name: Bloodlines Executable
and app.exe: Vampire.exe
"""

vtm_context = Context()
vtm_context.matches = """
mode: user.game
and not mode: sleep
and app: vtm_bloodlines
"""


@vtm_context.action_class("user")
class Actions:

    def game_get_mouse_delta_x_for_turning_camera_around():
        return 100
