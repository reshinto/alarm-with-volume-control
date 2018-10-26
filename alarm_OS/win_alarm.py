#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

# Required to set Master volume (Tested on Windows 10)
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Required to set volume of alarm file
from pydub import AudioSegment
from pydub.playback import play


def mastervol():
    """
    Required to activate PC Master volume control.
    """
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))
    return volume


def set_mastervol(db):
    """
    Set & override current PC Master volume and mute status.
    (tested on windows 10)
    """
    # Turn off mute
    mastervol().SetMute(0, None)
    # Set PC volume from min vol -75 to max vol 0
    mastervol().SetMasterVolumeLevel(db, None)


def initialmute():
    """
    Get initial mute status.
    Purpose is to convert mute (if muted) to unmute,
    and revert back to initial settings after alarm has gone off.
    """
    initial_mute = mastervol().GetMute()
    return initial_mute


def initialvol():
    """
    Get initial PC Master volume.
    Purpose is to revert back to initial settings after alarm has gone off.
    """
    inital_volume = mastervol().GetMasterVolumeLevel()
    return inital_volume


def playalarm(filename=None):
    """
    Open and play alarm file
    *Take note: increasing db too high will reduce music quality 
    Input filename with extension, or path including filename with extension
    Input file path: e.g. "c:\alarm\xxx.mp3" or filename if in the same directory e.g. "xxx.mp3"
    """
    if filename is None:
        filename = "audio/sample.mp3"
    alarm = AudioSegment.from_mp3(filename)
    # Set alarm file volume: increase db >= 0, decrease db <= -1 
    volume = 10
    play_alarm = alarm + volume
    # Play alarm file
    play(play_alarm)


def volume_input():
    """
    Allow user to set PC Master volume when alarm is activated.
    This will temporary override PC settings until alarm has gone off.
    """
    # Request for PC volume when alarm rings
    x = float(input(" PC Volume 0 (min) ~ 100 (max): "))
    if x>100:
        print("\n Cannot be more than 100! Please try again. \n")
        volume_input()
    elif x<0:
        print("\n Cannot be less than 0! Please try again. \n")
        volume_input()
    else:
        dba = x / 100 * 75 - 75
    return dba


def view_initial_vol():
    dbb = initialvol()
    # View initial volume similar to input value
    view_dbb = int((dbb + 75) / 75 * 100)
    print(" Your current PC volume is at {}".format(view_dbb))
    return dbb 


def win_app(_ringtone=None, _vol=None):
    """
    This is where the Volume is controlled, mute is deactivated, and alarm is played.
    Allows for snoozing via keyboard interrupt.
    """
    dbc = initialmute()
    dbb = view_initial_vol()
    if _vol is None:
        _vol = volume_input()
    while True:
        try:
            # Set values from -75 to 0: increase volume = higher value
            # This will override your current PC master volume when alarm is activated
            set_mastervol(_vol)
            # Display current date & time program activated on terminal
            print("\n This alarm started on " + time.ctime())
            print("\n Press 'ctrl c' to snooze!\n")
            playalarm(_ringtone)
            # Needs work! Looking for better methods of snoozing
        except KeyboardInterrupt:
            # Set values from 0 to -80: decrease volume = lower value
            # Revert back PC master volume to initial value
            set_mastervol(dbb)
            # Revert back mute status to initial value
            mastervol().SetMute(dbc, None)
            print("\n Snoozed\n")
            break
