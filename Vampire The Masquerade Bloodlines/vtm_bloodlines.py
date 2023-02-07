from talon import Module, Context, actions, ctrl

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
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "zero": "0",
    "F one": "f1",
    "F two": "f2",
    "F three": "f3",
    "F four": "f4",
    "F five": "f5",
}

is_feeding: bool = False


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

    def game_weapon_drop():
        actions.key("backspace")

    def game_weapon_melee_show():
        actions.key("f1")

    def game_weapon_ranged_show():
        actions.key("f2")

    def game_weapon_thrown_show():
        actions.key("f5")

    def game_skill_use():
        actions.mouse_click(1)

    def game_skill_duration_end():
        actions.key("f8")

    def game_skill_show_all():
        actions.key("f6")

    def game_before_on_pop():
        if is_feeding:
            actions.user.vtmb_feed(False)
            return (False, False)  # just end feeding and skip the regular binding
        return (True, True)  # continue

    def game_weapon_block_start():
        actions.key("tab:down")

    def game_weapon_block_stop():
        actions.key("tab:up")


@mod.action_class
class VtmbActions:

    def vtmb_hotkey_discipline_use(hotkey_number: str):
        """"""
        actions.key(hotkey_number)
        actions.sleep("150ms")
        actions.user.game_skill_use()

    def vtmb_feed(is_start: bool):
        """"""
        actions.key("f")
        actions.user.vtmb_feed_state_set(is_start)

    def vtmb_feed_state_set(is_start: bool):
        """"""
        global is_feeding
        is_feeding = is_start
