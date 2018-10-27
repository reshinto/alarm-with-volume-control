"""
Run alarm application
Tested on windows 10 and
mac high sierra and Mojave
"""
import datetime
import time
import os


def menu(os_app=None):
    """Run menu for user selection input"""
    choice = input("""\
Alarm Clock APP
Please choose an option:
1) Run alarm without date specification
2) Choose a single day of the week
3) Turn alarm on during Weekdays
4) Turn alarm on during Weekends
5) Select multiple days of the week
9) Load settings
0) Settings
> """)
    choice_dict = {
        "1": _menu1,
        "2": _menu2,
        "3": _menu3,
        "4": _menu4,
        "5": _menu5,
        "9": _menu9,
        "0": _menu0
    }
    if choice_dict.get(choice) is None:
        print("\n\t{} is an Invalid input\n".format(choice))
        menu(os_app)
    else:
        choice_dict[choice](os_app)


def _menu1(os_app):
    run_sch(os_app)


def _menu2(os_app):
    date_choice = get_dates()
    run_sch(os_app, date_choice)


def _menu3(os_app):
    date_choice = [1, 2, 3, 4, 5]
    run_sch(os_app, date_choice)


def _menu4(os_app):
    date_choice = [6, 7]
    run_sch(os_app, date_choice)


def _menu5(os_app):
    date_choice = get_dates()
    run_sch(os_app, date_choice)


def _menu9(os_app):
    if file_is_empty() is True:
        print("\n\tNo settings available\n")
        menu(os_app)
    else:
        with open("settings/settings.txt", "r") as f:
            data = f.read().split("\n")
            if data[0] != "None":
                date_choice = [int(i) for i in data[0]]
            else:
                date_choice = None
            if data[1] != "None":
                time_choice = data[1]
            else:
                time_choice = None
            if data[2] != "None":
                ringtone_choice = data[2]
            else:
                ringtone_choice = None
            if data[3] != "None":
                volume_choice = data[3]
            else:
                volume_choice = None
            run_sch(os_app, choice=date_choice, al_time=time_choice,
                    ringtone=ringtone_choice, vol=volume_choice)


def _menu0(os_app):
    settings(os_app)


def get_dates(choice=None):
    """Set a day or days to turn alarm on"""
    if choice is None:
        choice = input("""\
 Which day or days do you want the alarm to be turned on?
 Monday    : 1
 Tuesday   : 2
 Wednesday : 3
 Thursday  : 4
 Friday    : 5
 Saturday  : 6
 Sunday    : 7
 > """)
    return _get_dates(choice)


def _get_dates(choice):
    """get dates main function"""
    date_dict = {
        "1": 1,
        "2": 2,
        "3": 3,
        "4": 4,
        "5": 5,
        "6": 6,
        "7": 7
    }
    date_choice = []
    for i in choice:
        if date_dict.get(i) is None:
            print("\n\tInvalid input\n")
            return get_dates(choice=None)
        date_choice.append(int(i))
    return date_choice


def run_sch(os_app, choice=None, al_time=None, ringtone=None, vol=None):
    """
    Runs alarm app according to input schedule
    App will sleep until alarm time to prevent uneccessary CPU usage
    to run in the background silently
    """
    schedule = choice
    alarm_time = get_alarm_time(al_time)
    print("\n\tAlarm is ON\n")
    try:
        while True:
            while alarm_time != current_time():
                time.sleep(1)
            if schedule is None:
                _run_sch(os_app, ringtone, vol)
            else:
                for i in schedule:
                    if i == current_date().isoweekday() and \
                       alarm_time == current_time():
                        _run_sch(os_app, ringtone, vol)
    except KeyboardInterrupt:
        print("\n\tAlarm has been turned OFF")


def _run_sch(os_app, ringtone, vol):
    """
    run schedule
    Sleep is implemented if user attempted KeyboardInterrupt during alarm time
    to prevent continuous alarm from ringing
    """
    os_app(ringtone, vol)
    print("\n\tAlarm is still ON\n\tPress ctrl + c again to turn off!")
    time.sleep(60)


def get_alarm_time(al_time=None):
    """Set alarm time"""
    if al_time is None:
        hour, minute = None, None
    else:
        hour = al_time[:-3]
        minute = al_time[3:]
    return _get_hour(hour) + ":" + _get_minute(minute)


def _get_hour(hour):
    """
    hour must be in 24 hour format
    hour must have 2 digits (e.g.: 1 -> 01)
    """
    # list of values from 00 to 23, append 0 if single digit
    hour_format = ["0"+str(i) if i < 10 else str(i) for i in range(0, 24)]
    if hour is None:
        hour = input(" Please set the alarm hour (xx) time: ")
    if hour not in hour_format:
        print("\n\tInvalid hour input (only 00 to 23 are acceptable)\n")
        return _get_hour(None)
    return hour


def _get_minute(minute):
    """minutes must have 2 digits (e.g.: 1 -> 01)"""
    # list of values from 00 to 59, append if single digit
    minute_format = ["0"+str(i) if i < 10 else str(i) for i in range(0, 60)]
    if minute is None:
        minute = input(" Please set the alarm minute (xx) time: ")
    if minute not in minute_format:
        print("\n\tInvalid minute input (only 00 to 59 are acceptable)\n")
        return _get_minute(None)
    return minute


def current_date():
    """Get the current date"""
    return datetime.date.today()


def current_time():
    """Get the current time in hours and minutes 24 hour format"""
    return str(datetime.datetime.today())[-15:-10]


def settings(os_app=None):
    """Settings menu"""
    choice = input("""\
Select setting options
1) set schedule settings
2) set alarm time settings
3) set ringtone settings
4) set alarm volume settings
5) view saved settings
0) return to main menu
> """)
    choice_dict = {
        "1": _set_schedule,
        "2": _set_time,
        "3": _set_ringtone,
        "4": _set_volume,
        "5": _view_settings,
        "0": menu,
    }
    if choice_dict.get(choice) is None:
        print("\n\tInvalid input")
        settings()
    else:
        if choice == "0":
            choice_dict[choice](os_app)
        else:
            choice_dict[choice]()


def _initial_write(_dates="None", _time="None",
                   _ringtone="None", _volume="None"):
    with open("settings/settings.txt", "w") as ftxt:
        ftxt.write(_dates + "\n")
        ftxt.write(_time + "\n")
        ftxt.write(_ringtone + "\n")
        ftxt.write(_volume + "\n")


def _overwrite(line_num, _data):
    with open("settings/settings.txt", "r+") as f:
        new_data = f.read().split("\n")
        new_data[line_num] = _data
        f.seek(0)
        f.write(new_data[0] + "\n")
        f.write(new_data[1] + "\n")
        f.write(new_data[2] + "\n")
        f.write(new_data[3] + "\n")


def _set_schedule():
    """Set, write, and save schedule settings to settings.txt file"""
    _dates = "".join([str(i) for i in get_dates()])
    if file_is_empty() is True:
        _initial_write(_dates=_dates)
    elif file_is_empty() is False:
        _overwrite(0, _dates)
    settings()


def _set_time():
    """Set, write, and save alarm time setting to settings.txt file"""
    _time = get_alarm_time()
    if file_is_empty() is True:
        _initial_write(_time=_time)
    elif file_is_empty() is False:
        _overwrite(1, _time)
    settings()


def _set_ringtone():
    """Set, write, and save ringtone setting to settings.txt file"""
    _path = input("""\
Key in file path
e.g.: 'alarm-volume-control/audio/sample.mp3'
> """)
    if file_is_empty() is True:
        _initial_write(_ringtone=_path)
    elif file_is_empty() is False:
        _overwrite(2, _path)
    settings()


def _set_volume():
    """Set, write, and save alarm volume setting to settings.txt file"""
    _vol = input("Alarm volume level: 0 to 100\n> ")
    if file_is_empty() is True:
        _initial_write(_volume=_vol)
    elif file_is_empty() is False:
        _overwrite(3, _vol)
    settings()


def _view_settings():
    """View currently saved settings"""
    if file_is_empty() is True:
        print("\n\tNo settings saved\n")
        settings()
    else:
        _read_schedule()
        _read_time()
        _read_ringtone()
        _read_volume()
    print()
    settings()


def _read(line_num):
    with open("settings/settings.txt", "r") as f:
        lines = f.readlines()
        f.seek(0)
        for i, line in enumerate(lines):
            if i == line_num:
                print(line, end="")


def _read_schedule():
    """Read schedule settings"""
    _read(0)


def _read_time():
    """Read alarm time settings"""
    _read(1)


def _read_ringtone():
    """Read ringtone settings"""
    _read(2)


def _read_volume():
    """Read volume settings"""
    _read(3)


def file_is_empty():
    """Check text file if it is empty"""
    if os.stat("settings/settings.txt").st_size == 0:
        return True
    return False
