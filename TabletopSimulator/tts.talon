app.name: Tabletop Simulator.exe
and app.exe: /^tabletop\ simulator\.exe$/i
and mode: all
-
settings():
    key_hold = 128.0
	key_wait = 16.0

^view that$:
    user.toggle_hold_key("alt")
^mag that$:
    user.toggle_hold_key("m")
^peek that$:
    user.toggle_hold_key("alt-shift")
