from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel
from PySide2.QtGui import QFont, QIcon
from PySide2.QtCore import Qt, QSize

import os, sys

from .widgets.image_scroll import ScrollableThumbnailsArea
from .widgets.grid_viewer import ImageGridView
from .widgets.process_menu import SliceMenu
from .widgets.queue_menu import QueueMenu

class EditorMenu(QMainWindow):
    def __init__(self, controller=None, state=None, image_filenames=[]):
        super().__init__()
        self.controller = controller
        self.state = state

        self.main_layout = QVBoxLayout()
        self.main_widget = QWidget()
        self.setCentralWidget(self.main_widget)

        self.main_widget.setLayout(self.main_layout)

        self.setWindowTitle("CellSlicer Sliceor")
        self.setFixedSize(1700, 820)
        self.setStyleSheet("background-color: white; color: black")

        self.initialize_editor(self.state, self.controller)

    def initialize_editor(self, state, controller):
        self.main_layout.setSpacing(0)

        self.cell_slicer_label = QLabel()
        self.cell_slicer_label.setText("CellSlicer Slicer")
        self.cell_slicer_label.setFont(QFont("Roboto", 36))
        self.cell_slicer_label.setStyleSheet("background-color: white; color: black;")
        self.cell_slicer_label.setSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        self.cell_slicer_label.setAlignment(Qt.AlignCenter)
        self.main_layout.addWidget(self.cell_slicer_label)

        self.scrollable_thumbnails_area = ScrollableThumbnailsArea(self.state, self.controller)
        self.scrollable_thumbnails_area.setMaximumHeight(200)
        self.main_layout.addWidget(self.scrollable_thumbnails_area)

        self.horizontal_line_2 = QtWidgets.QFrame()
        self.horizontal_line_2.setFrameShape(QtWidgets.QFrame.HLine)

        self.main_layout.addWidget(self.horizontal_line_2)
        self.main_layout.addSpacing(10)

        self.sub_layout = QHBoxLayout()
        self.sub_layout.setContentsMargins(0, 0, 0, 0)
        self.sub_layout.setSpacing(10)

        self.main_layout.addLayout(self.sub_layout)

        self.image_grid_view = ImageGridView(self.state, self.controller)
        self.sub_layout.addWidget(self.image_grid_view)

        self.vertical_line_2 = QtWidgets.QFrame()
        self.vertical_line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.sub_layout.addWidget(self.vertical_line_2)

        self.process_menu = SliceMenu(self.state, self.controller)
        self.sub_layout.addWidget(self.process_menu)

        self.vertical_line = QtWidgets.QFrame()
        self.vertical_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.sub_layout.addWidget(self.vertical_line)

        self.annotate_menu = QueueMenu(self.state, self.controller)
        self.sub_layout.addWidget(self.annotate_menu)


        
        

