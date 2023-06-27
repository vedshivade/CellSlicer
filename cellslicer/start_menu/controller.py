import os, sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2 import QtWidgets
from PySide2.QtGui import QDesktopServices
from PySide2.QtCore import QUrl

import numpy as np
from skimage import io


class StartMenuController:
    def __init__(self, state):
        self.state = state
        
    def set_view(self, view):
        self.view = view

    def open_github(self):
        QDesktopServices.openUrl(QUrl("https://github.com/vedshivade/CellSlicer"))
