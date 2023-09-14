from talon import Module, Context, actions, ctrl

is_tool_aim: bool = False
is_heavy_attack_mode: bool = False

mod = Module()
mod.apps.hellblade_senuas_sacrifice = """
title: /^Hellblade: Senua's Sacrifice.*/
and app.name: /^Hellblade: Senua's Sacrifice$/
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: hellblade_senuas_sacrifice
"""
ctx.lists["user.game_number_shortcuts"] = {
}
