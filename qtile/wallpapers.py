from typing import Callable
from itertools import cycle, islice
from libqtile import qtile
from random import choice
from os.path import isfile, join
from os import listdir


def get_files_from_folder(folder: str) -> list:
    return list(filter(lambda file: isfile(join(folder, file)), listdir(folder)))


class QtileTimer:
    def __init__(self, timeout: int, callback: Callable):
        self.timeout = timeout
        self.callback = callback

    def call(self):
        self.callback()
        self.timer()

    def timer(self):
        qtile.call_later(self.timeout, self.call)


class QtileWallpaper:
    def __init__(self, img_path: str) -> None:
        self.img_path = img_path

    def _set(self):
        for screen in qtile.screens:
            screen.cmd_set_wallpaper(self.img_path, "fill")

    def set(self):
        self._set()


class QtileRandomWallpaper(QtileWallpaper):
    def __init__(self, folder_path: str) -> None:
        img = choice(get_files_from_folder(folder_path))
        super().__init__(join(folder_path, img))


class QtileDynamicWallpaper(QtileTimer, QtileWallpaper):
    def __init__(self, timeout: int, path: str, start: int = 0):
        self.path = path
        img_files = list(
            map(lambda file: join(self.path, file), get_files_from_folder(self.path))
        )

        self.images = islice(
            cycle(img_files),
            start,
            None,
        )

        super().__init__(timeout, self.set_next)

    def set(self):
        self.call()

    def set_next(self):
        self.img_path = next(self.images)
        self._set()
