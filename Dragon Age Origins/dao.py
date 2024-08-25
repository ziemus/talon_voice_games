from talon import Module, Context, actions

mod = Module()
mod.apps.dragon_age_origins = """
title: Dragon Age: Origins
and app.name: Dragon Age: Origins
and app.exe: daorigins.exe
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: dragon_age_origins
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
}

mod.list("dao_hero_selection")
ctx.lists["user.dao_hero_selection"] = {
    "one": "f1",
    "two": "f2",
    "three": "f3",
    "four": "f4",
}

@ctx.action("user.game_after_on_pop")
def game_after_on_pop():
    actions.user.game_click(0)

# @ctx.action("user.on_hiss_start")
# def on_hiss_start():
#     actions.key("space")
#     actions.next()
