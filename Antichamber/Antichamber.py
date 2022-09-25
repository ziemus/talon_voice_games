from talon import noise, actions, Context, Module
from user.knausj_talon.modes.game_mode.GameModeHelper import GameModeHelper
from user.knausj_talon.modes.game_mode.BaseGame import BaseGame

antichamber_module = Module()
antichamber_module.apps.Antichamber = """
title: /Antichamber/
and app.name: /UDK.exe/
and app.exe: /UDK.exe/
"""

antichamber_context = Context()
antichamber_context.matches = """
mode: user.game
and not mode: sleep
and app: Antichamber
"""


@antichamber_context.action_class('user')
class AntichamberActions:

    def game_get_default_sprint_state():
        return True

    def is_default_eye_mouse_noise_behavior():
        return False
    
    def game_get_mouse_delta_x_for_turning_camera_around():
        return 555


antichamber_game = GameModeHelper.get_game_from_library("UDK.exe")


def on_pop(_):
    if not GameModeHelper.is_game_active_and_game_mode(antichamber_game):
        return
    else:
        actions.user.switch_game_movement()


def on_hiss(is_active):
    if not GameModeHelper.is_game_active_and_game_mode(antichamber_game):
        return
    elif is_active:
        actions.user.game_jump()


noise.register('pop', on_pop)
noise.register('hiss', on_hiss)