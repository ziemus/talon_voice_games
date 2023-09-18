from talon import Module, Context, actions, settings
from enum import Enum

mod = Module()
mod.apps.gothic = """
title: GOTHIC 1
and app.name: GOTHIC
"""

mod.apps.gothic2 = """
title: /Gothic II/
and app.name: Gothic II
"""

common_context = Context()
common_context.matches = """
app: gothic
and mode: user.game

app: gothic2
and mode: user.game
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


current_attack_mode: GothicAttackMode = GothicAttackMode.SIDEWAYS
current_attack_direction: GothicAttackDirection = GothicAttackDirection.FORWARD

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
            actions.key("up:up")
        else:
            actions.key("up:down")
        is_casting_spell = not is_casting_spell


@common_context.action_class("user")
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
            actions.user.gothic_spell_cast_toggle()
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

    def game_weapon_target_lock_start():
        actions.key("ctrl:down")

    def game_weapon_target_lock_stop():
        actions.key("ctrl:up")

    def game_quick_access_menu_show():
        actions.key("space:down")

    def game_quick_access_menu_hide():
        actions.key("space:up")

    def game_quest_log_show():
        actions.key("l")

    def game_character_sheet_show():
        actions.key("b")

    def game_dodge():
        actions.key("down")

    def game_long_dodge():
        actions.user.game_dodge()

    def game_inventory_show():
        actions.key("tab")

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