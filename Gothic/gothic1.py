from talon import Context, actions

gothic1_context = Context()
gothic1_context.matches = """
app: gothic
and mode: user.game
"""

gothic1_context.lists["user.game_inventory_tabs"] = {
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


@gothic1_context.action_class("user")
class Gothic1Actions:

    def game_use():
        actions.key("ctrl-up")

    def game_loot():
        actions.user.game_long_use()

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

    def game_weapon_block_start():
        actions.key("down:down")

    def game_weapon_block_stop():
        actions.key("down:up")
        # don't release ctrl so that you don't lose your target lock