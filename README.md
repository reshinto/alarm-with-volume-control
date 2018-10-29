# Alarm Clock

An alarm clock that overrides the computer's volume and mute settings when the alarm goes off.
All initial settings will be saved and reverted back when alarm is snoozed.
Users will be able to select which days of the week to activate the alarm.
Once the alarm time has been set, app will loop daily or weekly.
You can use can music file as alarm. (tested with .mp3)

# Prerequisites

What things you need to install the software and how to install them (Windows 10 only)
Ubuntu and Mac OSX requires no installation.

```
Python 3.5

Use pip install for the following:
pip install pycaw
pip install pydub
pip install comtypes
```

## Installing

```
If you are using conda, on terminal, cd to the directory you saved the file.
Then type:
  conda env create -f alarm_env.yml
```

Or

```
Pip install everything if you do not want to use Anaconda
```

### Tested on Windows 10, Ubuntu 18.04, Mac OSX (High Sierra, Mojave)

On windows terminal, cd to saved directory then do the following:
1) Type: python run_app.py
2) Select an option from the menu, then follow the instructions
6) Once all of the required settings has been set, Alarm will turn on and you are good to go
7) Press 'ctrl + c' to snooze
8) Press 'ctrl + c' again to quit

## Author

This is my first written python program as a beginner.
