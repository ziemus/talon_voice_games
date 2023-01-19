from talon import Module, Context, actions

mod = Module()
mod.apps.vtm_bloodlines = """
title: Vampire: Bloodlines
and app.name: Bloodlines Executable
and app.exe: Vampire.exe
"""

ctx = Context()
ctx.matches = """
app: vtm_bloodlines
and mode: user.game
"""
ctx.lists["user.game_number_shortcuts"] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "F one": "f1",
    "F two": "f2",
    "F three": "f3",
    "F four": "f4",
    "F five": "f5",
}


@ctx.action_class("user")
class Actions:

    def game_quick_save():
        actions.key("f9")

    def game_quick_load():
        actions.key("f12")

    def game_crouch():
        actions.key("ctrl")

    def game_sprint_start():
        actions.key("insert")

    def game_sprint_stop():
        actions.key("insert")

    def game_quest_log_show():
        actions.key("l")

    def game_camera_first_person():
        actions.key("z")
