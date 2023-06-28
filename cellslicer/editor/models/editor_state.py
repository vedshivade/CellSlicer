import os, sys
from PySide2.QtWidgets import QFileDialog, QProgressBar, QDialog, QVBoxLayout, QLabel, QApplication
from PySide2 import QtWidgets
from PySide2.QtGui import QDesktopServices
from PySide2.QtCore import Signal, QObject
import shutil

class EditorState(QObject):

    imageSelected = Signal(str)
    inquiryMade = Signal(str, str)
    ladderUpdated = Signal(dict)

    def __init__(self, project):
        super().__init__()
        self.images = project.images
        print(self.images)
        self.current_image = ""
        self.project_name = project.project_name
        self.chosen_model = project.chosen_model
        self.process_ladder = {}
        self.process_items = {}

    def import_images(self):
        print()

    def set_current_image(self, filename):
        self.current_image = filename
        self.imageSelected.emit(filename)

    def process_inquiry(self, filename, process):
        self.inquiryMade.emit(filename, process)

    def update_ladder(self, current_process, process):
        print(current_process)
        print(process)
        current_process_int = int(''.join(filter(str.isdigit, current_process)))
        process_int = int(''.join(filter(str.isdigit, process)))

        self.process_ladder[current_process_int] = process_int
        print(self.process_ladder)

        self.ladderUpdated.emit(self.process_ladder)


    