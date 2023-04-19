from subprocess import Popen
from time import time
from threading import Thread


class Image:
    def __init__(self, name: str, image_path: str, presenter_path: str, max_display_time: float):
        self._image_path: str = image_path
        self._presenter_path: str = presenter_path
        self.name: str = name
        self.max_display_time: float = max_display_time

        self.is_opened: bool = False
        self._process: Popen = None
        self._time_of_last_open: float = 0

    def open(self):
        self._process = Popen(rf'python "{self._presenter_path}" {self.name} {self._image_path}')
        self.is_opened = True
        self._time_of_last_open = time()
        Thread(target=self.wait_to_die).start()

    def close(self):
        if self._process:
            self._process.kill()
            self._process = None

        self.is_opened = False

    def wait_to_die(self):
        while self.time_opened() < self.max_display_time:
            if not self.is_opened:
                return
        self.close()

    def time_opened(self):
        if not self._process:
            return 0
        return time() - self._time_of_last_open
