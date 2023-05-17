from talon import Context, actions

gothic2_context = Context()
gothic2_context.matches = """
app: gothic2
and mode: user.game
"""


@gothic2_context.action_class("user")
class Gothic2Actions:

    def game_use():
        actions.key("ctrl")

    def game_weapon_block_start():
        actions.key("down")

    def game_weapon_block_stop():
        # block is a quick action in gothic 2
        # that needs to be timed with the opponent's attack
        # and is not triggered for a period of time like in gothic 1
        # because of that blocks won't really work with voice commands
        # but they can still be used with noise controls
        # for ease of use it is triggered on both start and stop
        actions.user.game_weapon_block_start()

    def gothic_climb_up():
        actions.user.game_jump()

    def game_take_all():
        actions.key("alt")

    def game_trade_buy_item():
        actions.user.game_use()

    def game_trade_buy_multiple_items():
        actions.user.game_take_all()
