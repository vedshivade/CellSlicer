from PySide2.QtWidgets import QLabel, QFrame, QVBoxLayout
from PySide2.QtGui import QPixmap
import os, sys

class StartMenuImage(QFrame):

    def __init__(self, state = None, controller = None):
        super().__init__()
        self.state = state
        self.controller = controller

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.image_label = QLabel()
        pixmap = QPixmap("./cellslicer/icons/onion.jpeg")
        self.image_label.setPixmap(pixmap)
        
        self.layout.addWidget(self.image_label)
