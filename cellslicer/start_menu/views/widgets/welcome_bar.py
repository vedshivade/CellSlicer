from PySide2.QtWidgets import QLabel, QFrame, QVBoxLayout, QPushButton, QHBoxLayout
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt, QSize
import os, sys



class WelcomeBar(QFrame):

    def __init__(self, state = None, controller = None):

        std_style_sheet = ("QPushButton { background-color: black; border-style: outset; color: white; font-family: Roboto; border-radius: 2px; font: 16px; min-width: 3em; padding: 6px; border-color: beige;}"
                            "QPushButton::hover { background-color: white; color: black; border-style: solid; border: 2px solid black; padding: 4px; border-radius: 4px }"
                            "QPushButton::pressed { background-color: white; border-style: inset; border: 3px solid black; padding: 0px; border-radius: 4px}"
                            )
        
        transparent_style_sheet = (("QPushButton {background-color: transparent; border: none;}"))
        
        super().__init__()
        self.state = state
        self.controller = controller
        
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.big_label = QLabel()
        self.big_label.setText("CellSlicer")
        self.big_label.setFont(QFont("Roboto", 48))
        self.big_label.setStyleSheet("background-color: white; color: black;")
        self.big_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.big_label)

        self.import_new_images_button = QPushButton()
        self.import_new_images_button.setText("Create New Project")
        self.import_new_images_button.setStyleSheet(std_style_sheet)
        self.import_new_images_button.clicked.connect(self.on_click_create_new_project)

        self.open_project_button = QPushButton()
        self.open_project_button.setText("Open Project")
        self.open_project_button.setStyleSheet(std_style_sheet)

        self.freestyle_button = QPushButton()
        self.freestyle_button.setText("Freestyle")
        self.freestyle_button.setStyleSheet(std_style_sheet)

        self.layout.addWidget(self.open_project_button)
        self.layout.addWidget(self.import_new_images_button)
        self.layout.addWidget(self.freestyle_button)

        self.layout.addStretch(1)  

        self.config_layout = QHBoxLayout()

        self.configuration_button = QPushButton()
        self.configuration_button.setText("")
        self.configuration_button.setIcon(QIcon("./cellslicer/icons/configuration.svg"))
        self.configuration_button.setIconSize(QSize(35, 35))
        self.configuration_button.setStyleSheet(transparent_style_sheet)
        self.configuration_button.clicked.connect(self.on_click_configuration)

        self.profile_button = QPushButton()
        self.profile_button.setText("")
        self.profile_button.setIcon(QIcon("./cellslicer/icons/profile.svg"))
        self.profile_button.setIconSize(QSize(35, 35))
        self.profile_button.setStyleSheet(transparent_style_sheet)
        self.profile_button.clicked.connect(self.on_click_profile)

        self.github_button = QPushButton()
        self.github_button.setText("")
        self.github_button.setIcon(QIcon("./cellslicer/icons/github.png"))
        self.github_button.setIconSize(QSize(32, 32))
        self.github_button.setStyleSheet(transparent_style_sheet)
        self.github_button.clicked.connect(self.on_click_github)

        self.config_layout.addWidget(self.configuration_button)
        self.config_layout.addWidget(self.profile_button)
        self.config_layout.addWidget(self.github_button)

        self.layout.addLayout(self.config_layout)

    def on_click_github(self):
        self.controller.open_github()

    def on_click_configuration(self):
        print("Configuration")

    def on_click_profile(self):
        print("Profile")

    def on_click_create_new_project(self):
        self.controller.open_project_menu()


