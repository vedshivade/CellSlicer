from PySide2 import QtWidgets, QtCore, QtGui
from PySide2.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QGraphicsOpacityEffect
from PySide2.QtCore import QPropertyAnimation, QEasingCurve
import os
import sys

from .widgets.welcome_bar import WelcomeBar
from .widgets.image import StartMenuImage

class MainWindow(QMainWindow):

    def __init__(self, controller = None, state = None):
        super().__init__()
        self.controller = controller
        self.state = state

        try:
            base_path = getattr(sys, "_MEIPASS", ".") + "/icons"
        except Exception:
            base_path = os.path.abspath("/icons")

        self.main_layout = QHBoxLayout()
        self.main_widget = QWidget()
        self.main_widget.setLayout(self.main_layout)

        self.setCentralWidget(self.main_widget)
        self.setWindowTitle("CellSlicer v0.1.0")
        self.setFixedSize(640, 480)
        self.setStyleSheet("background-color: white;"
                           "color: white")
        
        self.welcome_bar = WelcomeBar(self.state, self.controller)
        self.main_layout.addWidget(self.welcome_bar, 1)

        self.start_menu_image = StartMenuImage(self.state, self.controller)
        self.main_layout.addWidget(self.start_menu_image, 1)

        # Create an opacity effect and animation
        self.opacity_effect = QGraphicsOpacityEffect(self.welcome_bar)
        self.welcome_bar.setGraphicsEffect(self.opacity_effect)
        self.opacity_anim = QPropertyAnimation(self.opacity_effect, b'opacity')
        self.opacity_anim.setDuration(2500)  # 1 second fade-in
        self.opacity_anim.setStartValue(0)
        self.opacity_anim.setEndValue(1)
        self.opacity_anim.setEasingCurve(QEasingCurve.InOutQuad)
        self.opacity_anim.start()

    def closeEvent(self, event):
        event.accept()
