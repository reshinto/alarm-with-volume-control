"""
Alarm app on OSX
Tested on High Seirra and Mojave
"""

import subprocess


def run_command(command):
    """
    Runs shell commands
    Need to decode if using python3 (byte code to string)
    """
    return subprocess.check_output(command,
                                   shell=True).decode("utf-8").strip()


def get_volume():
    """Get current Volume level"""
    command = "osascript -e 'set ovol to output volume of"\
              "(get volume settings)'"
    return run_command(command)


def set_volume(vol):
    """Set volume level from 0 to 100"""
    command = "osascript -e 'set volume output volume {}'".format(vol)
    return run_command(command)


def check_mute():
    """Check current mute status"""
    command = "osascript -e 'output muted of (get volume settings)'"
    return run_command(command)


def on_mute():
    """Turn mute on if false"""
    command = "osascript -e 'set volume output muted true'"
    run_command(command)
    if check_mute() == "true":
        print("\nmute is now ON")


def off_mute():
    """Turn mute off if true"""
    command = "osascript -e 'set volume output muted false'"
    run_command(command)
    if check_mute() == "false":
        print("\nmute is now OFF")


def toggle_mute():
    """Toggles mute status (currently not implemented)"""
    if check_mute() == "false":
        on_mute()
    elif check_mute() == "true":
        off_mute()
    else:
        print("Unable to discover mute status")


def play_alarm(ringtone, current_vol):
    """
    ffplay: Portable Media Play using FFmpeg library & SDL library
    -nodisp: Disable graphical display
    -loglevel quiet: Set logging level & flags to quiet mode (display nothing)
    -autoexit: Exit when file is done playing
    """
    try:
        while True:
            subprocess.call(["ffplay", "-nodisp", "-loglevel", "quiet",
                             "-autoexit", ringtone])
    except KeyboardInterrupt:
        set_volume(current_vol)


def mac_app(ringtone=None, vol=None):
    """
    Runs alarm app
    """
    if ringtone is None:
        ringtone = "/Volumes/Speed/Dev/Python_projects/My_Projects/"\
                   "alarm-volume-control/audio/sample.mp3"
    if vol is None:
        vol = "60"
    mute_status = check_mute()
    if mute_status == "true":
        off_mute()
    current_vol = get_volume()
    set_volume(vol)
    play_alarm(ringtone, current_vol)
    if mute_status == "true":
        on_mute()
