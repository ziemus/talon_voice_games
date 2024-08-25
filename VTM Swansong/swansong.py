from talon import Module, Context
mod = Module()
mod.apps.vtm_swansong = """
title: /^Vampire  $/
and app.name: /^Vampire The Masquerade: Swansong$/
and app.exe: /Swansong.*\.exe$/
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: vtm_swansong
"""
ctx.lists["user.game_number_shortcuts"] = {
    "one": "1",
    "two": "2",
}
