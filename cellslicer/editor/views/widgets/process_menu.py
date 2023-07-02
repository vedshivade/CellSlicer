from PySide2.QtWidgets import QSpacerItem, QSizePolicy, QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QScrollArea, QComboBox, QGraphicsOpacityEffect
from PySide2.QtGui import QPixmap, QIcon, QImage, QFont
from PySide2.QtCore import Qt, QSize, QEvent
import sys


class SliceMenu(QWidget):
    def __init__(self, state = None, controller = None):

        self.std_style_sheet = ("QPushButton { background-color: black; border-style: outset; color: white; font-family: Roboto; border-radius: 2px; font: 16px; min-width: 3em; padding: 6px; border-color: beige;}"
                            "QPushButton::hover { background-color: white; color: black; border-style: solid; border: 2px solid black; padding: 4px; border-radius: 4px }"
                            "QPushButton::pressed { background-color: white; border-style: inset; border: 3px solid black; padding: 0px; border-radius: 4px}"
                            )
        
        super().__init__()

        self.current_process = ""

        self.state = state
        self.controller = controller

        self.state.inquiryMade.connect(self.view_processes)

        self.label = QLabel()
        self.label.setText(f"Slice")
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setFont(QFont("Roboto", 24))
        self.label.setStyleSheet("background-color: white; color: black;")

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(10)
        self.layout.addWidget(self.label)

        self.wire_to_label = QLabel()
        self.wire_to_label.setText("Wire To")
        self.wire_to_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.wire_to_label.setFont(QFont("Roboto", 16))
        self.wire_to_label.setStyleSheet("background-color: white; color: black;")
        self.layout.addWidget(self.wire_to_label)

        self.process_selection = QComboBox()
        self.process_selection.addItems(["Slice 0", "Slice 1", "Slice 2", "Slice 3", "Slice 4", "Slice 5"])
        self.process_selection.setFont(QFont("Roboto", 16))
        self.process_selection.currentIndexChanged.connect(self.update_process_ladder)
        self.process_selection.setStyleSheet("background-color: transparent; color: black; border: 1px solid black; border-radius: 2px; padding: 4px;")
        self.process_selection.setVisible(False)
        self.layout.addWidget(self.process_selection)

        self.select_a_process_label = QLabel()
        self.select_a_process_label.setText("Select a Slice")
        self.select_a_process_label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.select_a_process_label.setFont(QFont("Roboto", 16))
        self.select_a_process_label.setStyleSheet("background-color: white; color: black;")
        self.select_a_process_label.setVisible(False)
        self.layout.addWidget(self.select_a_process_label)

        self.graph_cut_button = QPushButton()
        self.graph_cut_button.setText("Graph Cut")
        self.graph_cut_button.setFont(QFont("Roboto", 16))
        self.graph_cut_button.setStyleSheet(self.std_style_sheet)
        self.graph_cut_button.clicked.connect(self.on_click_graph_cut)
        self.layout.addWidget(self.graph_cut_button)
        self.graph_cut_button.setVisible(False)

        self.skeletonize_button = QPushButton()
        self.skeletonize_button.setText("Skeletonize")
        self.skeletonize_button.setFont(QFont("Roboto", 16))
        self.skeletonize_button.setStyleSheet(self.std_style_sheet)
        self.skeletonize_button.clicked.connect(self.on_click_skeletonize)
        self.layout.addWidget(self.skeletonize_button)
        self.skeletonize_button.setVisible(False)



        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

    def view_processes(self, filename, process):
        self.select_a_process_label.setVisible(True)
        self.graph_cut_button.setVisible(True)

        if process != "":
            self.wire_to_label.setText(f"Wire {process} to")
            #self.process_selection.setCurrentIndex(self.state.process_ladder.get(process_int))
            self.current_process = process
            self.select_a_process_label.setText(f"Select a {process}")
        else:
            self.wire_to_label.setText("Wire image to")
            self.current_process = "Slice 0"
            self.select_a_process_label.setText(f"Select a Slice 0")

        self.process_selection.setVisible(True)

    def update_process_ladder(self, process):
        self.controller.update_process_ladder(self.current_process, self.process_selection.currentText())

    def on_click_graph_cut(self):
        self.controller.update_process_task(self.current_process, "Graph Cut")

    def on_click_skeletonize(self):
        print()

        


