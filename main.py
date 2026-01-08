import pygame
from pygame_managers import AudioManager, DataManager, TimeManager, LanguagesManager


class Main:
    def __init__(self):
        self.managers = {
            "audio": AudioManager(),
            "data": DataManager(),
            "time": TimeManager(),
            "language": LanguagesManager(),
        }


if __name__ == '__main__':
    main = Main()