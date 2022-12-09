from talon import Module, Context, actions, ctrl

mod = Module()
mod.apps.horizon_zero_dawn = """
title: Horizon Zero Dawn: Complete Edition
and app.name: Horizon Zero Dawn
"""


@mod.action_class
class HorizonZeroDawnActions:

    def horizon_zero_dawn_weapon_switch(digits: int):
        """Shortcut for switching weapons. Accepts only 'keys' 1-4."""
        if digits in range(1, 5):
            actions.key(f"{digits}")