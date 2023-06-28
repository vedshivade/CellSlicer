from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt, QSize

import os, sys

from .widgets.basic_info import BasicInfo
#from .widgets.image_import import ImageImport
#

class MainWindow(QMainWindow):
    def __init__(self, controller = None, state = None):
        super().__init__()
        self.controller = controller
        self.state = state

        self.state.launchEditor.connect(self.handle_launch_editor)

        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)
        self.setWindowTitle("Configure Project")
        self.setFixedSize(640, 420)
        self.setStyleSheet("background-color: white;"
                            "color: white")
        
        self.configure_label = QLabel()
        self.configure_label.setText("Configure Project")
        self.configure_label.setFont(QFont("Roboto", 32))
        self.configure_label.setStyleSheet("background-color: white; color: black;")
        self.configure_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.main_layout.addWidget(self.configure_label)

        line = QtWidgets.QFrame()
        line.setFrameShape(QtWidgets.QFrame.HLine)
        line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.main_layout.addWidget(line)

        
        self.basic_info = BasicInfo(self.state, self.controller)
        self.main_layout.addWidget(self.basic_info, 0)

        self.main_layout.addStretch(1)  

    def closeEvent(self, event):
        event.accept()

    def handle_launch_editor(self):
        self.close()
        

