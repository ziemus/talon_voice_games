from talon import Module, Context, actions

mod = Module()
mod.apps.expedition33 = """
os: windows
and app.name: Expedition 33
and app.exe: /^sandfall\-win64\-shipping\.exe$/i
"""

ctx = Context()
ctx.matches = """
mode: user.game
and app: expedition33
"""

ctx.lists["user.game_number_shortcuts"] = {
}

@ctx.action_class("user")
class GameActions:
    def game_camera_center():
        actions.key("c")

    def on_pop_start():
        #actions.key("e")
        actions.user.game_click(0)

    def on_hiss_start():
        actions.key("f:down")

    def on_hiss_stop():
        actions.key("f:up") 
    #     actions.key("q")

    def custom_game_setup():
        actions.tracking.control_toggle(False)

    def custom_game_cleanup():
        actions.tracking.control_toggle(True)
        

@ctx.action_class("user")
class FootSwitchActions:
    def foot_switch_olympus_top_down():
        actions.key("space:down")

    def foot_switch_olympus_top_up(held: bool):
        actions.key("space:up")

    def foot_switch_olympus_left_down():
        actions.key("q:down")

    def foot_switch_olympus_left_up(held: bool):
        actions.key("q:up")

    def foot_switch_olympus_center_down():
        actions.key("w:down")

    def foot_switch_olympus_center_up(held: bool):
        actions.key("w:up")

    def foot_switch_olympus_right_down():
        actions.key("e:down")

    def foot_switch_olympus_right_up(held: bool):
        actions.key("e:up")

    def foot_switch_pcsensor_left_down():
        actions.key("f:down")

    def foot_switch_pcsensor_left_up(held: bool):
        actions.key("f:up")

    def foot_switch_pcsensor_center_down():
        actions.user.mouse_drag(0)
        
    def foot_switch_pcsensor_center_up(held: bool):
        actions.user.mouse_drag_end()

    def foot_switch_pcsensor_right_down():
        actions.user.mouse_drag(1)

    def foot_switch_pcsensor_right_up(held: bool):
        actions.user.mouse_drag_end()