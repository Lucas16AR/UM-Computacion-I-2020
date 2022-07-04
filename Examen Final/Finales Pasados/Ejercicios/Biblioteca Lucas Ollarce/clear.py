import os
import platform


class Clear():
    def clear():
        system = platform.system()
        if system in ['Linux']:
            return os.system('clear')
        if system in ['Windows']:
            return os.system('cls')
