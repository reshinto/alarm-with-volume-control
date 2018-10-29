"""
Alarm navigation menu
Tested on windows 10 (Not working at the moment)
Ubuntu 18.04
mac high sierra and Mojave
"""
import datetime
import time
import os


class AlarmMenu:
    """Alarm menu"""

    def __init__(self, alarm_app):
        self.app = alarm_app

    def menu(self):
        """Run menu for user selection input"""
        choice = input("""\
    Alarm Clock APP
    Please choose an option:
    1) Run alarm without date specification
    2) Choose a single day of the week
    3) Turn alarm on during Weekdays
    4) Turn alarm on during Weekends
    9) Load saved settings
    0) Settings
    > """)
        choice_dict = {
            "1": self.quick_start,
            "2": self.normal_mode,
            "3": self.weekday_mode,
            "4": self.weekend_mode,
            "9": self.load_settings,
            "0": self.settings
        }
        if choice_dict.get(choice) is None:
            print("\n\t{} is an Invalid input\n".format(choice))
            self.menu()
        else:
            choice_dict[choice]()

    def quick_start(self):
        """Run alarm app with only alarm time input"""
        self.run_sch()

    def normal_mode(self):
        """
        Select which day or days of the week to run alarm
        Alarm time input also required
        """
        date_choice = self.get_dates()
        self.run_sch(date_choice)

    def weekday_mode(self):
        """
        Run alarm app on weekdays only
        Alarm time input required
        """
        _weekday = [1, 2, 3, 4, 5]
        self.run_sch(_weekday)

    def weekend_mode(self):
        """
        Run alarm app on weekends only
        Alarm time input required
        """
        _weekend = [6, 7]
        self.run_sch(_weekend)

    def load_settings(self):
        """
        Load saved settings
        Schedule, time, ringtone, and volume settings can be saved
        at settings menu
        """
        if self.file_exist() is True and self.file_is_empty() is False:
            with open("settings.txt", "r") as ftxt:
                data = ftxt.read().split("\n")
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
                self.run_sch(choice=date_choice, al_time=time_choice,
                             ringtone=ringtone_choice, vol=volume_choice)
        else:
            print("\n\tNo settings saved!"
                  " Please first set settings at settings menu\n")
            self.menu()

    def settings(self):
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
            "1": self._set_schedule,
            "2": self._set_time,
            "3": self._set_ringtone,
            "4": self._set_volume,
            "5": self._view_settings,
            "0": self.menu,
        }
        if choice_dict.get(choice) is None:
            print("\n\tInvalid input")
            self.settings()
        else:
            choice_dict[choice]()

    def run_sch(self, choice=None, al_time=None, ringtone=None, vol=None):
        """
        Runs alarm app according to input schedule
        App will sleep until alarm time to prevent uneccessary CPU usage
        to run in the background silently
        """
        alarm_time = self.get_alarm_time(al_time)
        print("\n\tAlarm is ON\n")
        try:
            while True:
                while alarm_time != self.current_time():
                    time.sleep(1)
                if choice is None:
                    self._run_sch(ringtone, vol)
                else:
                    for i in choice:
                        if i == self.current_date().isoweekday() and \
                           alarm_time == self.current_time():
                            self._run_sch(ringtone, vol)
        except KeyboardInterrupt:
            print("\n\tAlarm has been turned OFF")

    def _run_sch(self, ringtone, vol):
        """
        run schedule
        Sleep is implemented if user attempted KeyboardInterrupt
        during alarm time to prevent alarmrm from continuously ringing
        """
        self.app(ringtone, vol)
        print("\n\tAlarm is still ON\n\tPress ctrl + c again to turn off!")
        time.sleep(60)

    @staticmethod
    def current_date():
        """Get current date"""
        return datetime.date.today()

    @staticmethod
    def current_time():
        """Get current time"""
        return str(datetime.datetime.today())[-15:-10]

    def get_alarm_time(self, al_time=None):
        """Set alarm time"""
        if al_time is None:
            hour, minute = None, None
        else:
            hour = al_time[:-3]
            minute = al_time[3:]
        return self._get_hour(hour) + ":" + self._get_minute(minute)

    def _get_hour(self, hour):
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
            return self._get_hour(None)
        return hour

    def _get_minute(self, minute):
        """minutes must have 2 digits (e.g.: 1 -> 01)"""
        # list of values from 00 to 59, append if single digit
        minute_format = ["0"+str(i) if i < 10 else str(i)
                         for i in range(0, 60)]
        if minute is None:
            minute = input(" Please set the alarm minute (xx) time: ")
        if minute not in minute_format:
            print("\n\tInvalid minute input (only 00 to 59 are acceptable)\n")
            return self._get_minute(None)
        return minute

    def get_dates(self, choice=None):
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
        return self._get_dates(choice)

    def _get_dates(self, choice):
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
                return self.get_dates(choice=None)
            date_choice.append(int(i))
        return date_choice

    @staticmethod
    def _initial_write(_dates="None", _time="None",
                       _ringtone="None", _volume="None"):
        """Create settings.txt and initialize inputs as None"""
        with open("settings.txt", "w") as ftxt:
            ftxt.write(_dates + "\n")
            ftxt.write(_time + "\n")
            ftxt.write(_ringtone + "\n")
            ftxt.write(_volume + "\n")

    @staticmethod
    def _overwrite(line_num, _data):
        """
        Overwrite saved settings in settings.txt
        for loop is used to rewrite each line in the settings.txt
        """
        with open("settings.txt", "r+") as ftxt:
            new_data = ftxt.read().split("\n")
            new_data[line_num] = _data
            ftxt.seek(0)
            for i in range(4):
                ftxt.write(new_data[i] + "\n")

    def _set_schedule(self):
        """Set, write, and save schedule settings to settings.txt file"""
        _dates = "".join([str(i) for i in self.get_dates()])
        if self.file_exist() is True:
            if self.file_is_empty() is False:
                self._overwrite(0, _dates)
                return self.settings()
        self._initial_write(_dates=_dates)
        return self.settings()

    def _set_time(self):
        """Set, write, and save alarm time setting to settings.txt file"""
        _time = self.get_alarm_time()
        if self.file_exist() is True:
            if self.file_is_empty() is False:
                self._overwrite(1, _time)
                return self.settings()
        self._initial_write(_time=_time)
        return self.settings()

    def _set_ringtone(self):
        """Set, write, and save ringtone setting to settings.txt file"""
        _path = input("""\
    Key in file path
    e.g.: 'alarm-volume-control/audio/sample.mp3'
    > """)
        if self.file_exist() is True:
            if self.file_is_empty() is False:
                self._overwrite(2, _path)
                return self.settings()
        self._initial_write(_ringtone=_path)
        return self.settings()

    def _set_volume(self):
        """Set, write, and save alarm volume setting to settings.txt file"""
        _vol = input("Alarm volume level: 0 to 100\n> ")
        if self.file_exist() is True:
            if self.file_is_empty() is False:
                self._overwrite(3, _vol)
                return self.settings()
        self._initial_write(_volume=_vol)
        return self.settings()

    def _view_settings(self):
        """
        View currently saved settings
        Currently, only 4 settings can be implemented
        therefore in the for loop, range is set to (4)
        to display all saved settings
        """
        if self.file_exist() is True:
            if self.file_is_empty() is False:
                for i in range(4):
                    self._read(i)
                return self.settings()
        print("\n\tNo settings saved\n")
        return self.settings()

    @staticmethod
    def _read(line_num):
        """Read settings.txt file"""
        with open("settings.txt", "r") as ftxt:
            lines = ftxt.readlines()
            ftxt.seek(0)
            for i, line in enumerate(lines):
                if i == line_num:
                    print(line, end="")

    @staticmethod
    def file_is_empty():
        """Check if text file is empty"""
        return os.stat("settings.txt").st_size == 0

    @staticmethod
    def file_exist():
        """Check if file exists"""
        return os.path.isfile("settings.txt")
