from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QScrollArea, QSizePolicy, QVBoxLayout, QGraphicsOpacityEffect
from PySide2.QtGui import QPixmap, QIcon, QImage
from PySide2.QtCore import Qt, QSize, QEvent
import sys

class ThumbnailWidget(QWidget):
    def __init__(self, filename):
        super().__init__()

        self.filename = filename

        # Load the image
        pixmap = QPixmap(filename)

        # Resize it to 64x64 while keeping aspect ratio
        thumbnail = pixmap.scaled(64, 64, Qt.KeepAspectRatio)

        # Create a QIcon from the QPixmap
        icon = QIcon(thumbnail)

        # Create a QPushButton and set its icon
        self.button = QPushButton()
        self.button.setStyleSheet("""
            QPushButton {
                background-color: white;
                border: transparent;
            }
            QPushButton:hover {
                border: transparent;
            }
            QPushButton:checked {
                border: 2px solid black;
            }
        """)

        self.button.setIcon(icon)
        self.button.setIconSize(thumbnail.size())
        self.button.setCheckable(True)

        self.button.setMinimumSize(80, 80)

        # Set the layout
        layout = QVBoxLayout(self)
        layout.addWidget(self.button)

        # Set the opacity
        self.opacity_effect = QGraphicsOpacityEffect(opacity=1)
        self.button.setGraphicsEffect(self.opacity_effect)

        # Hover effect
        self.button.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.button:
            if event.type() == QEvent.Enter:
                self.opacity_effect.setOpacity(0.7)
            elif event.type() == QEvent.Leave:
                self.opacity_effect.setOpacity(1)
        return super().eventFilter(obj, event)

class ScrollableThumbnailsArea(QWidget):
    def __init__(self, state = None, controller = None):
        super().__init__()
        self.state = state
        self.controller = controller

        image_filenames = self.state.images

        self.scrollArea = QScrollArea()
        #self.scrollArea.setMinimumSize(2000, 100)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)


        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setStyleSheet("""
            QScrollArea {
                border: transparent;
            }
            QScrollBar:horizontal {
                background-color: black;
                width: 15px; 
            }
            QScrollBar::handle:horizontal {
                background-color: #000000;
                border-radius: 7px; 
                min-height: 5px; 
            }
            QScrollBar::add-line:horizontal,
            QScrollBar::sub-line:horizontal {
                background-color: black;
            }
            QScrollBar::add-page:horizontal,
            QScrollBar::sub-page:horizontal {
                background-color: black;
            }
        """)

        self.scrollAreaContent = QWidget()
        self.scrollAreaContent.setSizePolicy(QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred))

        self.scrollLayout = QHBoxLayout(self.scrollAreaContent)
        self.scrollLayout.setContentsMargins(0, 0, 0, 0)

        self.thumbnail_widgets = []
        for filename in image_filenames:
            thumbnail_widget = ThumbnailWidget(filename)
            self.scrollLayout.addWidget(thumbnail_widget)
            self.thumbnail_widgets.append(thumbnail_widget)
            thumbnail_widget.button.clicked[bool].connect(lambda checked, thumbnail_widget=thumbnail_widget: self.handle_button_click(checked, thumbnail_widget))

        self.scrollArea.setWidget(self.scrollAreaContent)

        layout = QVBoxLayout(self)
        layout.addWidget(self.scrollArea)

    def handle_button_click(self, checked, thumbnail_widget):
        if checked:
            self.controller.handle_current_image(thumbnail_widget.filename)
            for other_thumbnail_widget in self.thumbnail_widgets:
                if other_thumbnail_widget != thumbnail_widget:
                    other_thumbnail_widget.button.setChecked(False)



