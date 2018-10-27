import platform
import subprocess
from main import menu


class Adapter:
    def __init__(self):
        self._check_os = platform.system()
        self.os_dict = {
            "Darwin": self.osx,
            "Windows": self.windows10,
            "Linux": self.linux
        }

    def run_app(self):
        if self.os_dict.get(self._check_os) is None:
            return "OS not supported"
        self.os_dict[self._check_os]()

    def osx(Self):
        from alarm_OS.mac_alarm import mac_app
        menu(mac_app)        

    def windows10(self):
        from alarm_OS.win_alarm import win_app
        menu(win_app)

    def linux(self):
        linux_type = subprocess.check_output(["lsb_release", "-is"]).decode("utf-8")[:-1]
        linux_dict = {
            "Ubuntu": self.ubuntu,
            "Kali": self.kali
        }
        if linux_dict.get(linux_type) is None:
            return "Linux OS not supported"
        linux_dict[linux_type]()

    def ubuntu(self):
        print("ubuntu")

    def kali(self):
        print("kali")


if __name__ == "__main__":
    a = Adapter()
    a.run_app()
