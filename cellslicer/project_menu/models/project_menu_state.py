import os, sys
from PySide2.QtWidgets import QFileDialog, QProgressBar, QDialog, QVBoxLayout, QLabel, QApplication
from PySide2 import QtWidgets
from PySide2.QtGui import QDesktopServices
from PySide2.QtCore import QUrl
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

class ProjectMenuState:

    def __init__(self):
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

    def begin(self):
        dir_path = "../cellslicer/projects/" + self.project_name + "/raw_images/"
        os.makedirs(dir_path, exist_ok=True)

        dialog = ProgressDialog(len(self.images))
        dialog.show()

        for i, file in enumerate(self.images):
            shutil.copy(file, dir_path)

            progress = (i + 1) / len(self.images) * 100
            dialog.update_progress(progress, i+1)
            QApplication.instance().processEvents()

        dialog.close()

    def update_project_name(self, text):
        self.project_name = text
        print(self.project_name)

    def update_data_labeled(self, text):
        if text == "Yes":
            self.data_labeled = True
        else:
            self.data_labeled = False
        print(self.data_labeled)

    def update_choose_model(self, text):
        self.chosen_model = text
        print(self.chosen_model)
