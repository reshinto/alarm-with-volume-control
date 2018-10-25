"""
Run alarm application
Tested on windows 10 and
mac high sierra and Mojave
"""
import platform
from itertools import combinations
import time
import schedule


def run_schedule():
    """
    Run schedule forever
    Disable through keyboard interrupt
    """
    print("\n\talarm is on")
    while True:
        schedule.run_pending()
        time.sleep(1)


def combi_sch(combi, os_app):
    """
    Initialize alarm time.
    Set user input combinations settings for alarm schedule.
    """
    al_hr = input(" Please set the alarm hour (xx) time: ")
    al_min = input(" Please set the alarm minute (xx) time: ")
    al_time = al_hr + ":" + al_min
    # Looking for ways to simplify and make the following code more efficient
    a = schedule.every().monday.at(al_time).do(os_app)
    b = schedule.every().tuesday.at(al_time).do(os_app)
    c = schedule.every().wednesday.at(al_time).do(os_app)
    d = schedule.every().thursday.at(al_time).do(os_app)
    e = schedule.every().friday.at(al_time).do(os_app)
    f = schedule.every().saturday.at(al_time).do(os_app)
    g = schedule.every().sunday.at(al_time).do(os_app)
    combinations(combi, 7)
    run_schedule()


def get_choice(os_app):
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
    # removes spaces and ensures all input values are lowercase
    choice_list = list(combi.replace(" ", "").lower())
    acceptable_list = list("abcdefg")
    result = ""
    for i in choice_list:
        if i not in acceptable_list:
            print("\n\tInvalid input\n")
            return os_check()
        result += i
    if result == "":
        os_check()
    combi_sch(result, os_app)


def os_check():
    """Check OS and run the support app accordingly"""
    os = platform.system()
    if os == "Darwin":
        from alarm_OS.mac_alarm import mac_app
        get_choice(mac_app)
    elif os == "Windows":
        from alarm_OS.win_alarm import win_app
        get_choice(win_app)
    else:
        print("OS not supported")


if __name__ == "__main__":
    os_check()
