from cellslicer.start_menu.start_menu import StartMenu
import os
from PySide2.QtCore import Qt

os.environ['QT_MAC_WANTS_LAYER'] = '1'

class CellSlicer:

    def __init__(self):
        self.start_menu = StartMenu()

    def start(self):
        self.start_menu.start()

if __name__ == "__main__":
    app = CellSlicer()
    app.start()
    