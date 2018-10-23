import subprocess

import time
import schedule

from itertools import combinations

def run_command(command):
    output = subprocess.check_output(command, shell=True).decode("utf-8").strip()
    return output


def get_volume():
    command = "osascript -e 'set ovol to output volume of"\
              "(get volume settings)'"
    output = run_command(command)
    return output


def set_volume(vol):
    """volume control from 0 to 100"""
    command = "osascript -e 'set volume output volume {}'".format(vol)
    output = run_command(command)
    return output


def check_mute():
    command = "osascript -e 'output muted of (get volume settings)'"
    output = run_command(command)
    return output


def on_mute():
    command = "osascript -e 'set volume output muted true'"
    run_command(command)
    if check_mute() == "true":
        print("mute is now ON")


def off_mute():
    command = "osascript -e 'set volume output muted false'"
    run_command(command)
    if check_mute() == "false":
        print("mute is now OFF")


def toggle_mute():
    if check_mute() == "false":
        on_mute()
    elif check_mute() == "true":
        off_mute()
    else:
        print("Unable to discover mute status")
 

def play_alarm(ringtone, current_vol):
    try:
        while True:
            subprocess.call(["ffplay", "-nodisp", "-autoexit", ringtone])
    except KeyboardInterrupt:
        set_volume(current_vol)


def alarm_app():
    mute_status = check_mute()
    if mute_status == "true":
        off_mute()
    current_vol = get_volume()
    set_volume("60")
    ringtone = "/Volumes/Speed/Dev/Python_projects/My_Projects/Alarm_clock/"\
               "my_alarm/osx/sample.mp3"
    play_alarm(ringtone, current_vol)
    if mute_status == "true":
        on_mute()


def run_schedule(choices):
    choices
    print("alarm is on")
    while True:
        schedule.run_pending()
        time.sleep(1)


def combi_sch(combi):
    """
    Initialize alarm time.
    Set the basic settings to allow combinations of user input for alarm schedule.
    """
    al_hr = input(" Please set the alarm hour (xx) time: ")
    al_min = input(" Please set the alarm minute (xx) time: ")
    al_time = al_hr + ":" + al_min
    # Looking for ways to simplify and make the following code more efficient
    a = schedule.every().monday.at(al_time).do(alarm_app)
    b = schedule.every().tuesday.at(al_time).do(alarm_app)
    c = schedule.every().wednesday.at(al_time).do(alarm_app)
    d = schedule.every().thursday.at(al_time).do(alarm_app)
    e = schedule.every().friday.at(al_time).do(alarm_app)
    f = schedule.every().saturday.at(al_time).do(alarm_app)
    g = schedule.every().sunday.at(al_time).do(alarm_app)
    run_schedule(combinations(combi, 7))


def main():
    """
    The heart of the program, and displays alarm menu.
    Links settings to alarm schedules.
    """
    combi = input("""\
 Choose a combination of the following:
 Weekdays   : abcde
 Weekends   : fg 
 Mondays    : a
 Tuesdays   : b		
 Wednesdays : c
 Thursdays  : d
 Fridays    : e
 Saturdays  : f
 Sundays    : g
 > """)
    # Needs work! prevent user from selecting invalid values
    if combi != "h":
        combi_sch(combi)
    else:
        print("Wrong")
        main()


if __name__ == "__main__":
    main()
