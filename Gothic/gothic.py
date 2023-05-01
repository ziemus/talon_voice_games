from talon import Module, Context, actions, settings, ctrl
from enum import Enum

mod = Module()
mod.apps.gothic = """
title: GOTHIC 1
and app.name: GOTHIC
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: gothic
"""


class GothicAttackMode(Enum):
    FORWARD = 0
    SIDEWAYS = 1

    def get_next(self):
        if self == GothicAttackMode.FORWARD:
            return GothicAttackMode.SIDEWAYS
        else:
            return GothicAttackMode.FORWARD


class GothicAttackDirection(Enum):
    FORWARD = "up"
    LEFT = "left"
    RIGHT = "right"

    def get_next(self):
        if self == GothicAttackDirection.FORWARD:
            return self
        elif self == GothicAttackDirection.LEFT:
            return GothicAttackDirection.RIGHT
        else:
            return GothicAttackDirection.LEFT

    def __str__(self):
        return str(self.value)


ctx.lists["user.game_inventory_tabs"] = {
    "weapon": "weapons",
    "armor": "armor",
    "spell": "magic",
    "spells": "magic",
    "magic": "magic",
    "art": "artifacts",
    "arts": "artifacts",
    "artifacts": "artifacts",
    "food": "food",
    "drink": "potions",
    "potion": "potions",
    "potions": "potions",
    "note": "notes",
    "notes": "notes",
    "trinket": "miscellaneous",
    "trinkets": "miscellaneous",
    "miss": "miscellaneous",
    "miscellaneous": "miscellaneous",
}

ctx.lists["user.game_directions"] = {
    "north": "up",
    "nor": "up",
    "no": "up",
    "south": "down",
    "so": "down",
    "west": "delete",
    "wet": "delete",
    "we": "delete",
    "east": "pagedown",
    "ease": "pagedown",
    "aye": "pagedown",
}

current_attack_mode: GothicAttackMode = GothicAttackMode.SIDEWAYS
current_attack_direction: GothicAttackDirection = GothicAttackDirection.FORWARD

inventory_tabs = {
    "weapons": 0,
    "armor": 1,
    "magic": 2,
    "artifacts": 3,
    "food": 4,
    "potions": 5,
    "notes": 6,
    "miscellaneous": 7,
}

is_in_dialogue: bool = False
is_equipped_spell: bool = False
is_casting_spell: bool = False


@mod.action_class
class GothicActions:

    def gothic_attack_mode_change(mode: int = None):
        """Change to the specified mode or from the current mode to the alternate attack mode"""
        global current_attack_mode, current_attack_direction
        if mode is None:
            current_attack_mode = current_attack_mode.get_next()
        current_attack_mode = GothicAttackMode(mode)
        if current_attack_mode == GothicAttackMode.FORWARD:
            current_attack_direction = GothicAttackDirection.FORWARD
        else:
            current_attack_direction = GothicAttackDirection.LEFT

    def gothic_dialogue_end():
        """End dialog"""
        global is_in_dialogue
        actions.user.switch_game_movement(False)
        actions.key("0 up enter")
        is_in_dialogue = False

    def gothic_climb_up():
        """"""
        actions.key("alt:down")
        actions.user.game_hold_key_native("up", 1000000)
        actions.key("alt:up")

    def gothic_spell_cast_toggle():
        """"""
        global is_casting_spell
        if is_casting_spell:
            actions.key("up:down")
        else:
            actions.key("up:up")
        is_casting_spell = not is_casting_spell


def inventory_take_give_number(is_taking: bool, number: int):
    arrow_key = "right" if is_taking else "left"

    hundreds = int(number / 100)
    tens = int((number % 100) / 10)
    ones = int(number % 10)

    actions.key("ctrl:down")
    actions.key(f"shift:down {arrow_key}:{hundreds} shift:up")
    actions.key(f"alt:down {arrow_key}:{tens} alt:up")
    actions.key(f"{arrow_key}:{ones}")
    actions.key("ctrl:up")


@ctx.action_class("user")
class GameActions:

    def game_before_on_pop():
        is_target = actions.user.game_is_weapon_target_lock()
        if is_in_dialogue:
            actions.key("escape")  # skip dialog
            return (False, False)
        elif is_target and not is_equipped_spell:
            actions.user.game_attack()
            return (False, False)
        elif is_target and is_equipped_spell:
            actions.gothic_spell_cast_toggle()
            return (False, False)
        return (True, True)

    def game_attack(is_held: bool = None):
        global current_attack_direction
        attack_key = current_attack_direction
        actions.key(f"{attack_key}")
        current_attack_direction = current_attack_direction.get_next()

    def game_weapon_draw():
        actions.key("space")

    def game_weapon_melee_show():
        actions.user.game_number_shortcut("1")

    def game_weapon_ranged_show():
        actions.user.game_number_shortcut("2")

    def game_number_shortcut(game_number_shortcuts: str):
        global is_equipped_spell, is_casting_spell
        if game_number_shortcuts == "1":  # meele weapon
            actions.user.gothic_attack_mode_change(GothicAttackMode.FORWARD)
            is_equipped_spell = False
        elif game_number_shortcuts == "2":  # ranged weapon
            actions.user.gothic_attack_mode_change(GothicAttackMode.FORWARD)
            is_equipped_spell = False
        else:  # magic
            is_equipped_spell = True
        is_casting_spell = False

        #if bow's equipped, target needs to be unlocked first
        # and then the animation of releasing the bow string needs to finish
        # otherwise weapons won't change
        actions.user.game_weapon_target_lock_toggle(False)
        actions.sleep("500ms")

        actions.key(game_number_shortcuts)

    def game_weapon_block_start():
        actions.key("down:down")

    def game_weapon_block_stop():
        actions.key("down:up")
        # don't release ctrl so that you don't lose your target lock

    def game_weapon_target_lock_start():
        actions.key("ctrl:down")

    def game_weapon_target_lock_stop():
        actions.key("ctrl:up")

    def game_quest_log_show():
        actions.key("l")

    def game_character_sheet_show():
        actions.key("b")

    def game_dodge():
        actions.key("down")

    def game_long_dodge():
        actions.user.game_dodge()

    def game_loot():
        actions.user.game_long_use()

    def game_inventory_show():
        actions.key("tab")

    def game_inventory_tab_go(game_inventory_tabs: str):
        new_tab_number = inventory_tabs[game_inventory_tabs]
        actions.key(f"left:7 right:{new_tab_number}")

    def game_inventory_tab_next():
        actions.key("right")

    def game_inventory_tab_previous():
        actions.key("left")

    def game_take_all():
        # looting has a time limit so it needs to be quick
        # but most NPCs have under fifty items stacks in their inventory
        inventory_take_give_number(True, 5000)

    def game_take_number(digits: int):
        inventory_take_give_number(True, digits)

    def game_trade_buy_item():
        inventory_take_give_number(True, 1)

    def game_trade_buy_multiple_items():
        #you usually want to buy the whole stack, and that's usually under 100
        inventory_take_give_number(True, 100)

    def game_trade_buy_number_of_items(number: int):
        inventory_take_give_number(True, number)

    def game_trade_sell_item():
        inventory_take_give_number(False, 1)

    def game_trade_sell_multiple_items():
        #you usually want to sell the whole stack, and that's usually under 100
        inventory_take_give_number(False, 100)

    def game_trade_sell_number_of_items(number: int):
        inventory_take_give_number(False, number)

    def game_use():
        actions.key("ctrl-up")

    def game_long_use():
        actions.user.game_weapon_target_lock_toggle(True)
        #the game needs to be given time for the animation of kneeling by the chest
        actions.sleep("850ms")
        actions.key("up")
        actions.user.game_weapon_target_lock_toggle(False)

    def game_hold_use():
        actions.user.game_weapon_target_lock_toggle(True)
        actions.sleep("850ms")
        actions.user.switch_game_movement_direction("up")
        actions.user.switch_game_movement(True)

    def game_release_use():
        actions.user.switch_game_movement(False)
        actions.user.game_weapon_target_lock_toggle(False)

    def game_talk():
        global is_in_dialogue
        actions.user.game_use()
        actions.user.switch_game_movement(False)
        is_in_dialogue = True

    def game_jump(is_hold: bool = None):
        actions.key("alt")

    def game_crouch():
        actions.key("a")

    def game_dive_start():
        actions.user.switch_game_movement(False)
        actions.key("alt:down")

    def game_dive_stop():
        actions.user.switch_game_movement_direction("up")
        actions.user.switch_game_movement(False)
        actions.key("alt:up")

    def game_quick_load():
        actions.key("f9")

    def game_camera_first_person():
        actions.key("f:down")

    def game_camera_third_person():
        actions.key("f:up")

    def game_turn_camera(direction: str, cursor_movement_multiplier: float = None):
        duration = 0
        duration_setting = ""

        if direction in ["right", "left"]:
            duration_setting = "user.game_turn_horizontally_mouse_delta"
        elif direction in ["down", "up"]:
            duration_setting = "user.game_turn_vertically_mouse_delta"
        else:
            return
        duration = settings.get(duration_setting)

        if cursor_movement_multiplier:
            duration *= cursor_movement_multiplier
            duration = int(duration)
        actions.user.game_hold_key_native(direction, duration)

    def game_turn_camera_around():
        duration = settings.get("user.game_turn_around_mouse_delta")
        actions.user.game_hold_key_native("left", duration)

    def get_game_movement_keys():
        return ["up", "down", "right", "left", "delete", "pagedown"]

    def get_held_game_keys():
        return [
            "up",
            "down",
            "left",
            "right",
            "delete",
            "pagedown",
            "f",
            "alt",
            "ctrl",
            "shift",
        ]
