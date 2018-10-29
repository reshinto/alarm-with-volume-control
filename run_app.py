"""Check OS and run app"""

import platform
import subprocess
from main import AlarmMenu


class Adapter:
    """
    Find the current OS distribution and provide the alarm app menu with the
    required OS command app for the alarm app to work
    """
    def __init__(self):
        self._check_os = platform.system()
        self.os_dict = {
            "Darwin": self.osx,
            "Windows": self.windows10,
            "Linux": self.linux
        }

    def run_app(self):
        """Check current OS distribution"""
        if self.os_dict.get(self._check_os) is None:
            return "OS not supported"
        self.os_dict[self._check_os]()

    def osx(Self):
        """Run Mac OSX commands (High Seirra and Mojave)"""
        from alarm_OS.mac_alarm import mac_app
        run = AlarmMenu(mac_app)
        run.menu()

    def windows10(self):
        """Run Windows 10 commands (currently not working)"""
        from alarm_OS.win_alarm import win_app
        run = AlarmMenu(win_app)
        run.menu()

    def linux(self):
        """Check linux distribution"""
        linux_type = subprocess.check_output(["lsb_release",
                                              "-is"]).decode("utf-8")[:-1]
        linux_dict = {
            "Ubuntu": self.ubuntu,
            "Kali": self.kali
        }
        if linux_dict.get(linux_type) is None:
            return "Linux OS not supported"
        linux_dict[linux_type]()

    def ubuntu(self):
        """Run Ubuntu 18.04 commands"""
        from alarm_OS.ubuntu_alarm import ubuntu_app
        run = AlarmMenu(ubuntu_app)
        run.menu()

    def kali(self):
        """To be implemented soon"""
        print("kali")


if __name__ == "__main__":
    a = Adapter()
    a.run_app()
