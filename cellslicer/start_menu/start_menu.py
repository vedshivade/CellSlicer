import sys

from cellslicer.start_menu.views.main_window import MainWindow
from cellslicer.start_menu.models.start_menu_state import StartMenuState
from cellslicer.start_menu.controller import StartMenuController
from Qt import QtWidgets
from PySide2.QtCore import Qt

class StartMenu:

    def __init__(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.app.setAttribute(Qt.AA_UseHighDpiPixmaps)


        self.state = StartMenuState()
        self.controller = StartMenuController(self.state)
        self.view = MainWindow(self.controller, self.state)

        self.controller.set_view(self.view)

    def start(self):
        self.view.show()
        self.app.exec_()