from talon import Module, Context, actions, ctrl

mod = Module()
mod.apps.the_thaumaturge = """
title: /^The Thaumaturge  $/
and app.name: /^The Thaumaturge$/
and app.exe: TheThaumaturge-Win64-Shipping.exe
"""