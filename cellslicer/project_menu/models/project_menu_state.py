import os, sys
from PySide2.QtWidgets import QFileDialog, QProgressBar, QDialog, QVBoxLayout, QLabel, QApplication
from PySide2 import QtWidgets
from PySide2.QtGui import QDesktopServices
from PySide2.QtCore import Signal, QObject
import shutil

class ProgressDialog(QDialog):
    def __init__(self, total_files, parent=None):
        super(ProgressDialog, self).__init__(parent)
        self.setWindowTitle("Copying Files...")

        self.progress_bar = QProgressBar(self)
        self.status_label = QLabel(self)
        layout = QVBoxLayout(self)
        layout.addWidget(self.progress_bar)
        layout.addWidget(self.status_label)
        self.setStyleSheet("background-color: white; color: black;")

        self.progress_bar.setMinimum(0)
        self.progress_bar.setMaximum(100)
        self.total_files = total_files

    def update_progress(self, progress, copied_files):
        self.progress_bar.setValue(progress)
        self.status_label.setText(f"Copied {copied_files} out of {self.total_files} files")

class ProjectMenuState(QObject):

    progressChanged = Signal(int, int)
    copyingDone = Signal()
    launchEditor = Signal()

    def __init__(self):
        super().__init__()
        self.images = []
        self.project_name = ""
        self.data_labeled = False
        self.chosen_model = ""

    def import_images(self):
        folder_path = QFileDialog.getExistingDirectory(None, 'Select a folder:', os.getcwd(), QFileDialog.ShowDirsOnly)
        print(folder_path)

        images = []

        for file_name in os.listdir(folder_path):
            if file_name.endswith('.png'):
                file_path = os.path.join(folder_path, file_name)
                images.append(file_path)

        self.images = images

        return images
    
    def create_text_file(self):
        dir_path = "../cellslicer/projects/" + self.project_name + "/"
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        file_path = dir_path + "data.txt"
        f = open(file_path, "w")
        f.write("Project Name: " + self.project_name + "\n")
        f.write("Data Labeled: " + str(self.data_labeled) + "\n")
        f.write("Model: " + self.chosen_model + "\n")
        f.close()

    def create_sub_folders(self):
        dir_path = "../cellslicer/projects/" + self.project_name + "/"
        for i in range(1, 6):
            os.makedirs(dir_path + "process_" + str(i) + "/")

    def begin(self):
        dir_path = "../cellslicer/projects/" + self.project_name + "/raw_images/"
        os.makedirs(dir_path, exist_ok=True)

        copied_images = []
        i = 0
        for i, file in enumerate(self.images):
            i = i + 1
            new_file_path = os.path.join(dir_path, os.path.basename(file) + "_CS" + f"{i}.png")  # New file path with a different name
            shutil.copy(file, new_file_path)
            copied_images.append(new_file_path)

            progress = (i + 1) / len(self.images) * 100
            self.progressChanged.emit(progress, i+1)
            QApplication.instance().processEvents()

        self.images = copied_images
        self.create_sub_folders()
        self.create_text_file()
        self.copyingDone.emit()


    def update_project_name(self, text):
        self.project_name = text

    def update_data_labeled(self, text):
        if text == "Yes":
            self.data_labeled = True
        else:
            self.data_labeled = False

    def update_choose_model(self, text):
        self.chosen_model = text

    def launch_editor(self):
        self.launchEditor.emit()
