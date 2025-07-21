from talon import Module, Context, actions

mod = Module()
mod.apps.baba_is_you = """
app.name: Baba Is You
and app.exe: /^baba\ is\ you\.exe$/i
"""

ctx = Context()
ctx.matches = """
app: baba_is_you
"""

# @ctx.action_class("user")
# class FootSwitchActions:
#     def foot_switch_olympus_top_down():
#         actions.key("w:down")

#     def foot_switch_olympus_top_up(held: bool):
#         actions.key("w:up")

#     def foot_switch_olympus_center_down():
#         actions.key("s:down")

#     def foot_switch_olympus_center_up(held: bool):
#         actions.key("s:up")

#     def foot_switch_olympus_left_down():
#         actions.key("a:down")

#     def foot_switch_olympus_left_up(held: bool):
#         actions.key("a:up")

#     def foot_switch_olympus_right_down():
#         actions.key("d:down")

#     def foot_switch_olympus_right_up(held: bool):
#         actions.key("d:up")

#     def foot_switch_pcsensor_center_down():
#         actions.key("z:down")

#     def foot_switch_pcsensor_center_up(held: bool):
#         actions.key("z:up")

#     def foot_switch_pcsensor_left_down():
#         actions.key("space:down")

#     def foot_switch_pcsensor_left_up(held: bool):
#         actions.key("space:up")

#     def foot_switch_pcsensor_right_down():
#         actions.key("r:down")

#     def foot_switch_pcsensor_right_up(held: bool):
#         actions.key("r:up")