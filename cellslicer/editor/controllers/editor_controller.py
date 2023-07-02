import os, sys
from PySide2.QtWidgets import QApplication, QPushButton
from PySide2 import QtWidgets
from PySide2.QtGui import QDesktopServices
from PySide2.QtCore import QUrl

import numpy as np
from skimage import io


class EditorController:
    def __init__(self, state):
        self.state = state
        
    def set_view(self, view):
        self.view = view

    def handle_current_image(self, filename):
        self.state.set_current_image(filename)

    def handle_process_inquiry(self, filename, process):
        self.state.process_inquiry(filename, process)

    def update_process_ladder(self, current_process, process):
        self.state.update_ladder(current_process, process)

    def update_process_task(self, process, task):
        self.state.update_process_task(process, task)

    def handle_start_queue(self):
        self.state.start_queue_worker()

    def handle_apply_queue_to_all(self):
        self.state.worker_queue_all()


