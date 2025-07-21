app.name: Citizen Sleeper.exe
and app.exe: /^citizen\ sleeper\.exe$/i
and mode: all
app.name: Citizen Sleeper 2.exe
and app.exe: /^citizen\ sleeper\ 2\.exe$/i
and mode: all
-
settings():
    key_hold = 28.0
	key_wait = 16.0
    user.mouse_continuous_scroll_amount = 2