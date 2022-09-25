from talon import actions, Context, Module

talos_game_module = Module()
talos_game_module.apps.TheTalosPrinciple = """
title: Talos - 64bit
and app.name: Talos
and app.exe: Talos.exe
"""

talos_game_context = Context()
talos_game_context.matches = """
mode: user.game
and not mode: sleep
and app: TheTalosPrinciple
"""


@talos_game_context.action_class("user")
class Actions:

    def is_default_eye_mouse_noise_behavior():
        return False

    def game_get_mouse_delta_x_for_turning_camera_around():
        return 787

    def game_before_on_pop():
        actions.user.talos_cancel_test_reset()

    def game_before_on_hiss():
        actions.user.talos_cancel_test_reset()


@talos_game_module.action_class
class TalosActions:

    def talos_reset_test():
        """"""
        actions.user.game_switch_sprint(False)
        actions.user.hold_game_key("x", "3s")

    def talos_cancel_test_reset():
        """"""
        actions.user.release_game_key("x")
