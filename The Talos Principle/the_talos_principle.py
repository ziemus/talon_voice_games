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

    def game_before_on_pop():
        actions.user.talos_cancel_test_reset()
        return (True, True)

    def game_before_on_hiss():
        actions.user.talos_cancel_test_reset()
        return (True, True)


@talos_game_module.action_class
class TalosActions:

    def talos_reset_test():
        """"""
        actions.user.game_switch_sprint(False)
        actions.user.game_hold_key_native("x", 3000000)

    def talos_cancel_test_reset():
        """"""
        actions.user.release_game_key("x")
