from PySide2.QtWidgets import QLabel, QFrame, QVBoxLayout, QPushButton, QHBoxLayout, QLineEdit, QFileDialog, QCheckBox, QComboBox
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt, QSize
import os, sys


class BasicInfo(QFrame):
    def __init__(self, state = None, controller = None):

        std_style_sheet = ("QPushButton { background-color: black; border-style: outset; color: white; font-family: Roboto; border-radius: 2px; font: 16px; min-width: 3em; padding: 6px; border-color: beige;}"
                            "QPushButton::hover { background-color: white; color: black; border-style: solid; border: 2px solid black; padding: 4px; border-radius: 4px }"
                            "QPushButton::pressed { background-color: white; border-style: inset; border: 3px solid black; padding: 0px; border-radius: 4px}"
                            )
        
        iab_style_sheet = ("QPushButton { background-color: seagreen; border-style: outset; color: white; font-family: Roboto; border-radius: 2px; font: 16px; min-width: 3em; padding: 6px; border-color: beige;}"
                            "QPushButton::hover { background-color: white; color: black; border-style: solid; border: 2px solid black; padding: 4px; border-radius: 4px }"
                            "QPushButton::pressed { background-color: white; border-style: inset; border: 3px solid black; padding: 0px; border-radius: 4px}"
                            )
        
        transparent_style_sheet = (("QPushButton {background-color: transparent; border: none;}"))

        super().__init__()
        self.state = state
        self.controller = controller

        self.state.progressChanged.connect(self.on_progress_changed)
        self.state.copyingDone.connect(self.on_copying_done)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(5)
        self.layout.addStretch(1)
        self.setLayout(self.layout)

        self.project_name_label = QLabel()
        self.project_name_label.setText("Name Your Project")
        self.project_name_label.setFont(QFont("Roboto", 16))
        self.project_name_label.setStyleSheet("background-color: white; color: black;")
        self.layout.addWidget(self.project_name_label)

        self.project_name_entry = QLineEdit()
        self.project_name_entry.setPlaceholderText("Project Name")
        self.project_name_entry.textChanged.connect(self.on_project_name_changed)
        self.project_name_entry.setStyleSheet("background-color: white; color: black; border: 1px solid black; border-radius: 2px; padding: 4px;")
        self.layout.addWidget(self.project_name_entry)  

        self.project_saved_label = QLabel()
        self.project_saved_label.setText("")
        self.project_saved_label.setFont(QFont("Roboto", 12)) 
        self.project_saved_label.setVisible(False)
        self.project_saved_label.setStyleSheet("background-color: white; color: black;")
        self.layout.addWidget(self.project_saved_label)

        self.layout.addSpacing(5)

        self.data_labeled = QLabel()
        self.data_labeled.setText("Is Your Data Labeled?")
        self.data_labeled.setFont(QFont("Roboto", 16))
        self.data_labeled.setStyleSheet("background-color: white; color: black;")
        self.layout.addWidget(self.data_labeled)

        self.data_labeled_checkbox = QComboBox()
        self.data_labeled_checkbox.addItem("Yes")
        self.data_labeled_checkbox.addItem("No")
        self.data_labeled_checkbox.currentIndexChanged.connect(self.on_click_data_labeled)
        self.data_labeled_checkbox.setStyleSheet("background-color: transparent; color: black; border: 1px solid black; border-radius: 2px; padding: 4px;")
        self.layout.addWidget(self.data_labeled_checkbox)

        self.layout.addSpacing(5)

        self.choose_model_label = QLabel()
        self.choose_model_label.setText("Choose a Model")
        self.choose_model_label.setFont(QFont("Roboto", 16))
        self.choose_model_label.setStyleSheet("background-color: white; color: black;")
        self.layout.addWidget(self.choose_model_label)

        self.model_box = QComboBox()
        self.model_box.addItem("Model 1")
        self.model_box.addItem("Model 2")
        self.model_box.currentIndexChanged.connect(self.on_click_choose_model)
        self.model_box.setStyleSheet("background-color: transparent; color: black; border: 1px solid black; border-radius: 2px; padding: 4px;")
        self.layout.addWidget(self.model_box)

        self.layout.addSpacing(5)

        self.import_images_label = QLabel()
        self.import_images_label.setText("Import Images")
        self.import_images_label.setFont(QFont("Roboto", 16))
        self.import_images_label.setStyleSheet("background-color: white; color: black;")
        self.layout.addWidget(self.import_images_label)

        self.import_images_button = QPushButton()
        self.import_images_button.setText("Import Images (*.png)")
        self.import_images_button.setStyleSheet(std_style_sheet)
        self.import_images_button.clicked.connect(self.on_click_import_images)
        self.layout.addWidget(self.import_images_button)

        self.layout.addSpacing(5)

        self.import_and_begin_button = QPushButton()
        self.import_and_begin_button.setText("Begin")
        self.import_and_begin_button.setVisible(False)
        self.import_and_begin_button.setStyleSheet(iab_style_sheet)
        self.import_and_begin_button.clicked.connect(self.on_click_begin)
        self.layout.addWidget(self.import_and_begin_button)

        self.on_click_data_labeled()
        self.on_click_choose_model()

    def on_click_data_labeled(self):
        self.controller.handle_data_labeled_changed(self.data_labeled_checkbox.currentText())

    def on_click_choose_model(self):
        self.controller.handle_choose_model_changed(self.model_box.currentText())

    def on_project_name_changed(self):        
        if self.project_name_entry.text() != "":
            self.project_saved_label.setVisible(True)
            self.project_saved_label.setText("Project will be saved at " + os.getcwd() + "/projects/" + self.project_name_entry.text())
            self.controller.handle_project_name_changed(self.project_name_entry.text())
        else:
            self.project_saved_label.setVisible(False)

    def on_click_import_images(self):
        images = self.controller.handle_import_images()
        self.import_images_button.setText(str(len(images)) + " images detected.")
        self.import_and_begin_button.setVisible(True)

    def on_click_begin(self):
        if self.project_name_entry.text() == "":
            self.project_name_entry.setPlaceholderText("Please enter a project name")
            self.project_name_entry.setStyleSheet("background-color: white; color: red; border: 1px solid red; border-radius: 2px; padding: 4px;")
        else:
            self.controller.handle_begin()

    def on_progress_changed(self, progress, copied_files):

        self.import_and_begin_button.setStyleSheet("background-color: seagreen; border-style: outset; color: white; font-family: Roboto; border-radius: 2px; font: 16px; min-width: 3em; padding: 6px; border-color: beige;")

        if progress == 100:
            self.import_and_begin_button.setText("Done!")
        else:
            self.import_and_begin_button.setText("Copied " + str(copied_files) + "/" + str(len(self.state.images)) + " files")

    def on_copying_done(self):
        self.controller.handle_launch_editor()


        

