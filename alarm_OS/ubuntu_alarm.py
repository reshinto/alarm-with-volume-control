#!/usr/bin/env python3
"""
Alarm app on Linux
Tested on Ubuntu 18.04
"""
import subprocess
import re


def run_command(command):
    """
    Runs shell commands
    Need to decode if using python3 (byte code to string)
    """
    return subprocess.check_output(command,
                                   shell=True).decode("utf-8").strip()

def get_volume():
    """
    Get current volume from 0 to 100
    volume is actually in percentage (%)
    """
    command = "amixer sget Master"
    output = run_command(command)
    return re.search("(?:\[.*)(?:%)", output).group(0)[1:-1]


def set_volume(vol):
    """
    Set master volume
    vol must be a string from 0 to 100
    vol is actually in percentage (%)
    """
    command = "amixer --quiet set Master " + str(vol) + "%"
    return run_command(command)


def check_mute():
    """Check if mute is on or off"""
    command = "amixer sget Master"
    output = run_command(command)
    return re.findall("\[(.*?)\]", output)[2]


def on_mute():
    """if master is on, mute is off"""
    if check_mute() == "on":
        toggle_mute()
        print("\nMute is now ON")


def off_mute():
    """if master is off, mute is on"""
    if check_mute() == "off":
        toggle_mute()
        print("\nMute is now OFF")


def toggle_mute():
    command = "amixer --quiet -D pulse sset Master toggle"
    return run_command(command)


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


def ubuntu_app(ringtone=None, vol=None):
    """
    Runs alarm app
    """
    if ringtone is None:
        ringtone = "audio/sample.mp3"
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
