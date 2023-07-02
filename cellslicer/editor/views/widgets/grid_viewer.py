from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QHBoxLayout, QScrollArea, QGridLayout, QGraphicsOpacityEffect
from PySide2.QtGui import QPixmap, QIcon, QImage, QFont
from PySide2.QtCore import Qt, QSize, QEvent
import sys
import os

class ImageWidget(QWidget):
    def __init__(self, filename, process):
        super().__init__()
        self.filename = filename

        self.pixmap = QPixmap(filename)
        image = self.pixmap.scaled(300, 300, Qt.KeepAspectRatio)

        icon = QIcon(image)
        self.has_icon = not icon.isNull()

        self.button = QPushButton()
        self.button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: black;
                border: 1px solid gray;
            }
            QPushButton:hover {
                border: transparent;
                border: 1px solid gray
            }
            QPushButton:checked {
                border: 2px solid black;
            }
        """)

        self.button.setIcon(icon)
        self.button.setIconSize(image.size())
        self.button.setCheckable(True)

        self.button.setMinimumSize(200, 200)

        self._text = ""

        if not self.has_icon:
            self.button.setText(f"Slice {process}")
            self._text = f"Slice {process}"
            self.button.setFont(QFont("Roboto", 48))

        if self.has_icon:
            self.button.setText("")
            self._text = f"Slice {process}"
            self.button.setFont(QFont("Roboto", 0))


        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(0)
        layout.addWidget(self.button)

        self.opacity_effect = QGraphicsOpacityEffect(opacity=1)
        self.button.setGraphicsEffect(self.opacity_effect)

        self.button.installEventFilter(self)

    def eventFilter(self, obj, event):
        if obj == self.button:
            if event.type() == QEvent.Enter:
                self.opacity_effect.setOpacity(0.7)
            elif event.type() == QEvent.Leave:
                self.opacity_effect.setOpacity(1)
        return super().eventFilter(obj, event)
    
class ImageGridView(QWidget):
    def __init__(self, state=None, controller=None):
        super().__init__()
        self.state = state
        self.controller = controller

        self.layout = QGridLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(5)
        self.setLayout(self.layout)

        self.state.imageSelected.connect(self.on_image_selected)
        self.state.tasksUpdated.connect(self.update_tasks)
        self.state.processDone.connect(self.rebuild_grid)


        self.image_widgets = []
        self.create_empty_grid()

    def update_tasks(self, process, task):
        print(process)

    def create_empty_grid(self):
        for i in range(3):
            for j in range(3):
                image_widget = ImageWidget('', i*3+j)
                self.layout.addWidget(image_widget, i+1, j+1)
                self.image_widgets.append(image_widget)
                image_widget.button.clicked[bool].connect(lambda checked, image_widget=image_widget: self.handle_button_click(checked, image_widget))
        
    def rebuild_grid(self):
        self.clear_layout(self.layout)
        self.image_widgets = []

        main_img = self.state.current_image
        path = os.path.dirname(os.path.dirname(main_img))
        print(path)

        process = -1
        for i in range(3):
            for j in range(3):
                process = process + 1
                if i == 0 and j == 0:
                    image_widget = ImageWidget(self.state.current_image, process)
                else:
                    image_widget = ImageWidget(f"{path}/" + "process_" + str(process) + "/" + os.path.basename(self.state.current_image), process)

                self.layout.addWidget(image_widget, i+1, j+1)
                self.image_widgets.append(image_widget)
                image_widget.button.clicked[bool].connect(lambda checked, image_widget=image_widget: self.handle_button_click(checked, image_widget))


    def on_image_selected(self, filename):
        self.clear_layout(self.layout)
        self.image_widgets = []

        path = os.path.dirname(os.path.dirname(filename))
        print(path)

        process = -1
        for i in range(3):
            for j in range(3):
                process = process + 1
                if i == 0 and j == 0:
                    image_widget = ImageWidget(filename, process)
                else:
                    image_widget = ImageWidget(f"{path}/" + "process_" + str(process) + "/" + os.path.basename(self.state.current_image), process)

                self.layout.addWidget(image_widget, i+1, j+1)
                self.image_widgets.append(image_widget)
                image_widget.button.clicked[bool].connect(lambda checked, image_widget=image_widget: self.handle_button_click(checked, image_widget))


    def handle_button_click(self, checked, image_widget):
        if checked:
            self.controller.handle_process_inquiry(image_widget.filename, image_widget._text)
            for other_image_widget in self.image_widgets:
                if other_image_widget != image_widget:
                    other_image_widget.button.setChecked(False)


    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()


        
    
