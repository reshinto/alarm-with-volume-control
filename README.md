# Alarm Clock

An alarm clock that overrides the computer's volume and mute settings when the alarm goes off.
All initial settings will be saved and reverted back when alarm is snoozed.
User will be able to select which day or days of the week to activate the alarm.
Once the alarm time has been set, app will loop daily or weekly.
You can use any music file as an alarm. (tested with .mp3)

# Prerequisites

What you need to install and how to install them (Windows 10 only).
Ubuntu and Mac OSX requires no installation (should support any python 3 versions).

```
Python 3.5

Use pip install for the following:
pip install pycaw
pip install pydub
pip install comtypes
```

## Installing

```
If you are using conda, cd to the directory where you saved this app.
Then type:
  conda env create -f alarm_env.yml
```

Or

```
Pip install everything.
```

### Tested on Windows 10, Ubuntu 18.04, Mac OSX (High Sierra, Mojave)

In terminal, cd to the directory where you saved this app, then do the following:
1) Type: python run_app.py
2) Select an option from the menu, then follow the instructions
6) Once all of the required settings has been set, Alarm will turn on and you are good to go
7) Press 'ctrl + c' to snooze
8) Press 'ctrl + c' again to quit
