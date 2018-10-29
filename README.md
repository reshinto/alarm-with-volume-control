# Alarm Clock

An alarm clock that overrides the computer's volume and mute settings when the alarm goes off.
All initial settings will be saved and reverted back when alarm is snoozed.
Users will be able to select which days of the week to activate the alarm.
Once the alarm time has been set, program will loop weekly.
You can use can music file as alarm. (tested with .mp3)

# Prerequisites

What things you need to install the software and how to install them

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

### Tested on Windows 10

On windows terminal, cd to saved directory then do the following:
1) Type: python main.py
2) Input the desired PC master volume (activates only during alarms)
3) Choose the alarm date or dates
4) Input the hour time to wake you up (24 hour clock format)
5) Input the minute time to wake you up
6) Alarm will be set, and your good to go
7) Press 'ctrl + c' to snooze
8) Press 'ctrl + c' again to quit

## Authors

This is my first written python program as a beginner.

## License

Feel free to use as you please. (^.^)
