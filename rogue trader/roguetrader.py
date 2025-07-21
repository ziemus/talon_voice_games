from talon import Module, Context, actions, cron

mod = Module()
mod.apps.wh40k_rogue_trader = r"""
app.name: WH40KRT.exe
and app.exe: /^wh40krt\.exe$/i
"""

mod.list("wh40k_rogue_trader_character_shortcuts")
mod.list("wh40k_rogue_trader_consumable_shortcuts")
mod.list("wh40k_rogue_trader_weapon_shortcuts")
mod.list("wh40k_rogue_trader_ability_shortcuts")

ctx = Context()
ctx.matches = """
mode: user.game
and app: wh40k_rogue_trader
"""


@ctx.action_class("user")
class Actions:
    def on_pop_start():
        actions.user.switch_game_movement(False)
        actions.next()

    # def game_jump(is_hold: bool = None):
    #     actions.key("space")
    #     cron.after("1s", actions.user.game_interactable_objects_highlight_start)


ctx.lists["user.wh40k_rogue_trader_character_shortcuts"] = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
}

ctx.lists["user.wh40k_rogue_trader_consumable_shortcuts"] = {
    "one": "f1",
    "two": "f2",
    "three": "f3",
    "four": "f4",
}

ctx.lists["user.wh40k_rogue_trader_weapon_shortcuts"] = {
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
    "eleven": "-",
    "twelve": "=",
}

ctx.lists["user.wh40k_rogue_trader_ability_shortcuts"] = {
    "one": "shift-1",
    "two": "shift-2",
    "three": "shift-3",
    "four": "shift-4",
    "five": "shift-5",
    "six": "shift-6",
    "seven": "shift-7",
    "eight": "shift-8",
    "nine": "shift-9",
    "zero": "shift-0",
    "eleven": "ctrl-1",
    "twelve": "ctrl-2",
    "thirteen": "ctrl-3",
    "fourteen": "ctrl-4",
    "fifteen": "ctrl-5",
    "sixteen": "ctrl-6",
    "seventeen": "ctrl-7",
    "eighteen": "ctrl-8",
    "nineteen": "ctrl-9",
    "twenty": "ctrl-0",
}