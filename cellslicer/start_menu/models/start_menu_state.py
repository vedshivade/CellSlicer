from PySide2.QtWidgets import QFileDialog, QProgressBar, QDialog, QVBoxLayout, QLabel, QApplication
import os

class StartMenuState:

    def __init__(self):
        print()

    def select_project(self):
        project_path = QFileDialog.getExistingDirectory(None, 'Select a project', os.getcwd(), QFileDialog.ShowDirsOnly)

        self.images = []
        self.project_name = ""
        self.data_labeled = False
        self.chosen_model = ""

        image_path = project_path + "/raw_images/"

        for file_name in os.listdir(image_path):
            if file_name.endswith('.png'):
                file_path = os.path.join(image_path, file_name)
                self.images.append(file_path)
        
        with open(project_path + "/data.txt", 'r') as text_file:
            # Read the lines from the file
            lines = text_file.readlines()

        # Process the lines and store the values in variables
            self.project_name = lines[0].split(": ")[1].strip()
            self.data_labeled = bool(lines[1].split(": ")[1].strip())
            self.chosen_model = lines[2].split(": ")[1].strip()

        print(self.project_name)

        return Project(self.project_name, self.images, self.data_labeled, self.chosen_model)
        

class Project:
    def __init__(self, project_name, images, data_labeled, chosen_model):
        self.project_name = project_name
        self.images = images
        self.data_labeled = data_labeled
        self.chosen_model = chosen_model

    