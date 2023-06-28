from cellslicer.editor.views.main_window import EditorMenu
from cellslicer.editor.models.editor_state import EditorState
from cellslicer.editor.controllers.editor_controller import EditorController
from PySide2 import QtWidgets
from PySide2.QtCore import Qt

import os, sys

class EditorWindow():
    def __init__(self, project):
        self.state = EditorState(project)
        self.controller = EditorController(self.state)
        self.view = EditorMenu(self.controller, self.state)

        self.controller.set_view(self.view)
    
    def start(self):
        self.view.show()
        self.view.raise_()

if __name__ == "__main__":
    app = EditorWindow()
    app.start()