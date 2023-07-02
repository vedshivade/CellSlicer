import os, sys
from PySide2.QtWidgets import QFileDialog, QProgressBar, QDialog, QVBoxLayout, QLabel, QApplication
from PySide2 import QtWidgets
from PySide2.QtGui import QDesktopServices
from PySide2.QtCore import Signal, QObject
import shutil
from collections import defaultdict
import io
import cv2

from cellslicer.util.graphcut import graph_cut

class EditorState(QObject):

    imageSelected = Signal(str)
    inquiryMade = Signal(str, str)
    ladderUpdated = Signal(dict)
    tasksUpdated = Signal(int, str)
    processDone = Signal()

    def __init__(self, project):
        super().__init__()
        self.images = project.images
        print(self.images)
        self.current_image = ""
        self.project_name = project.project_name
        self.chosen_model = project.chosen_model
        self.process_ladder = {}
        self.process_items = {}
        self.job_q = defaultdict(list)

    def import_images(self):
        print()

    def set_current_image(self, filename):
        self.current_image = filename
        self.imageSelected.emit(filename)

    def process_inquiry(self, filename, process):
        self.inquiryMade.emit(filename, process)

    def update_ladder(self, current_process, process):

        current_process_int = int(''.join(filter(str.isdigit, current_process)))
        process_int = int(''.join(filter(str.isdigit, process)))

        self.process_ladder[current_process_int] = process_int
        print(self.process_ladder)

        self.ladderUpdated.emit(self.process_ladder)

    def update_process_task(self, process, task):
        process_int = int(''.join(filter(str.isdigit, process)))
        self.process_items[process_int] = task
        self.tasksUpdated.emit(process_int, task)

    def start_queue(self):
        job_q = defaultdict(list)
        for key in self.process_items:
            job_q[key].append(self.process_items.get(key))
            job_q[key].append(self.process_ladder.get(key))

        self.job_q = job_q

        for key in job_q:
            task = job_q.get(key)[0]
            forward = job_q.get(key)[1]

            if task == "Graph Cut":
                edited_image = graph_cut(cv2.imread(self.current_image, 0))
                self.save_edited_image(edited_image, forward)

    def save_edited_image(self, edited_image, forward):
        edited_image_path = "../cellslicer/projects/" + self.project_name + f"/process_{forward}/" + str(os.path.basename(self.current_image))
        print(edited_image_path)
        cv2.imwrite(edited_image_path, edited_image)
        self.processDone.emit()




    