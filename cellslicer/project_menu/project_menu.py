from cellslicer.project_menu.views.main_window import MainWindow
from cellslicer.project_menu.models.project_menu_state import ProjectMenuState
from cellslicer.project_menu.controller import ProjectMenuController

class ProjectMenu:

    def __init__(self):
        self.state = ProjectMenuState()
        self.controller = ProjectMenuController(self.state)
        self.view = MainWindow(self.controller, self.state)

        self.controller.set_view(self.view)

    def start(self):
        self.view.show()
        self.view.raise_()

if __name__ == "__main__":
    app = ProjectMenu()
    app.start()