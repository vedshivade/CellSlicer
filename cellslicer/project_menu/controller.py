import os, sys
from PySide2.QtWidgets import QFileDialog
from PySide2 import QtWidgets
from PySide2.QtGui import QDesktopServices
from PySide2.QtCore import QUrl
from PySide2.QtWidgets import QApplication

from cellslicer.editor.editor import EditorWindow

class ProjectMenuController:

    def __init__(self, state):
        self.state = state

    def set_view(self, view):
        self.view = view

    def handle_import_images(self):
        return self.state.import_images()
    
    def handle_begin(self):
        self.state.begin()

    def handle_project_name_changed(self, text):
        self.state.update_project_name(text)

    def handle_data_labeled_changed(self, text):
        self.state.update_data_labeled(text)

    def handle_choose_model_changed(self, text):
        self.state.update_choose_model(text)

    def handle_launch_editor(self):
        self.state.launch_editor()

        editor_menu = EditorWindow(self.state)
        editor_menu.start()

