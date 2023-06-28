from PySide2.QtWidgets import QSpacerItem, QSizePolicy, QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QScrollArea, QGridLayout, QGraphicsOpacityEffect
from PySide2.QtGui import QPixmap, QIcon, QImage, QFont
from PySide2.QtCore import Qt, QSize, QEvent
import sys

class QueueMenu(QWidget):
    def __init__(self, state = None, controller = None):
        super().__init__()

        self.state = state
        self.controller = controller

        self.std_style_sheet = ("QPushButton { background-color: black; border-style: outset; color: white; font-family: Roboto; border-radius: 2px; font: 16px; min-width: 3em; padding: 6px; border-color: beige;}"
                            "QPushButton::hover { background-color: white; color: black; border-style: solid; border: 2px solid black; padding: 4px; border-radius: 4px }"
                            "QPushButton::pressed { background-color: white; border-style: inset; border: 3px solid black; padding: 0px; border-radius: 4px}"
                            )

        self.state.ladderUpdated.connect(self.update_ladder_UI)

        self.label = QLabel()
        self.label.setText(f"Queue")
        self.label.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.label.setFont(QFont("Roboto", 24))
        self.label.setStyleSheet("background-color: white; color: black;")

        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.label)
        self.layout.setSpacing(10)

        self.start_queue = QPushButton()
        self.start_queue.setText("Start Queue")
        self.start_queue.setStyleSheet(self.std_style_sheet)
        self.start_queue.clicked.connect(self.on_click_start_queue)
        self.layout.addWidget(self.start_queue)

        self.labels = {}
        self.labels[0] = QPushButton()
        self.labels[0].setFont(QFont("Roboto", 16))
        self.labels[0].setText("Process 0")
        self.labels[0].setStyleSheet(self.std_style_sheet)
        self.layout.addWidget(self.labels[0])

        self.labels[1] = QPushButton()
        self.labels[1].setFont(QFont("Roboto", 16))
        self.labels[1].setText("Process 1")
        self.labels[1].setStyleSheet(self.std_style_sheet)
        self.layout.addWidget(self.labels[1])

        self.labels[2] = QPushButton()
        self.labels[2].setFont(QFont("Roboto", 16))
        self.labels[2].setText("Process 2")
        self.labels[2].setStyleSheet(self.std_style_sheet)
        self.layout.addWidget(self.labels[2])

        self.labels[3] = QPushButton()
        self.labels[3].setFont(QFont("Roboto", 16))
        self.labels[3].setText("Process 3")
        self.labels[3].setStyleSheet(self.std_style_sheet)
        self.layout.addWidget(self.labels[3])

        self.labels[4] = QPushButton()
        self.labels[4].setFont(QFont("Roboto", 16))
        self.labels[4].setText("Process 4")
        self.labels[4].setStyleSheet(self.std_style_sheet)
        self.layout.addWidget(self.labels[4])

        self.labels[5] = QPushButton()
        self.labels[5].setFont(QFont("Roboto", 16))
        self.labels[5].setText("Process 5")
        self.labels[5].setStyleSheet(self.std_style_sheet)
        self.layout.addWidget(self.labels[5])

        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

    def on_click_start_queue(self):
        print("Verifying queue...")

    def update_ladder_UI(self, ladder):
        for key, value in ladder.items():
            if key in self.labels:
                if key == 0:
                    self.labels[key].setText(f"Image -> Process {value}")
                else:
                    self.labels[key].setText(f"Process {key} -> Process {value}")
