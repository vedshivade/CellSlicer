from PySide2.QtWidgets import QApplication, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PySide2.QtGui import QFont
from PySide2.QtCore import Qt, QThread

class QueueMenu(QWidget):
    def __init__(self, state=None, controller=None):
        super().__init__()

        self.state = state
        self.controller = controller

        self.std_style_sheet = (
            "QPushButton { background-color: black; border-style: outset; color: white; font-family: Roboto; border-radius: 2px; font: 16px; min-width: 3em; padding: 6px; border-color: beige;}"
            "QPushButton::hover { background-color: white; color: black; border-style: solid; border: 2px solid black; padding: 4px; border-radius: 4px }"
            "QPushButton::pressed { background-color: white; border-style: inset; border: 3px solid black; padding: 0px; border-radius: 4px}"
        )

        self.state.ladderUpdated.connect(self.update_ladder_UI)
        self.state.tasksUpdated.connect(self.on_tasks_update)

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
        self.configs = {}

        for i in range(6):
            label_button_layout = QHBoxLayout()
            label_button_layout.setContentsMargins(0, 0, 0, 0)

            label = QPushButton()
            label.setFont(QFont("Roboto", 16))
            label.setText(f"Slice {i}")
            label.setStyleSheet(self.std_style_sheet)
            label.setFixedSize(300, 30)
            label_button_layout.addWidget(label)

            config_button = QPushButton()
            config_button.setFont(QFont("Roboto", 12))
            config_button.setText("Config")
            config_button.setStyleSheet(self.std_style_sheet)
            config_button.setFixedSize(100, 30)
            label_button_layout.addWidget(config_button)

            self.labels[i] = label
            self.configs[i] = config_button

            self.layout.addLayout(label_button_layout)

        self.layout.addStretch()

        self.apply_queue_to_all = QPushButton()
        self.apply_queue_to_all.setText("Apply Queue to All")
        self.apply_queue_to_all.setStyleSheet(self.std_style_sheet)
        self.apply_queue_to_all.clicked.connect(self.on_click_apply_queue_to_all)
        self.layout.addWidget(self.apply_queue_to_all)


    def on_click_start_queue(self):
        self.controller.handle_start_queue()

    def on_tasks_update(self, index, task):
        self.configs[index].setText(task)

    def on_click_apply_queue_to_all(self):
        self.controller.handle_apply_queue_to_all()

    def update_ladder_UI(self, ladder):
        for key, value in ladder.items():
            if key in self.labels:
                if key == 0:
                    self.labels[key].setText(f"Image -> Slice {value}")
                else:
                    self.labels[key].setText(f"Slice {key} -> Slice {value}")

