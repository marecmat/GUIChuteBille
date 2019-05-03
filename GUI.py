import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from PyQt5.QtWidgets import (QDialog, QApplication, QPushButton, QLabel, QCheckBox, QComboBox,
                            QVBoxLayout, QHBoxLayout, QGridLayout, QFileDialog, QMessageBox,
                            QSpacerItem, QFrame, QSlider)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class GUI(QDialog):
    def __init__(self):
        super(GUI, self).__init__()
        self.setWindowTitle("Ploc")

        self.filename = "mes_cam_bille1_1"

        self.Objets()
        self.display()

    def Objets(self):
        self.figSpec = Figure(figsize=(8, 4), dpi=100)
        self.figTemp = Figure(figsize=(8, 4), dpi=100)
        self.figMicro = Figure(figsize=(8, 4), dpi=100)
        self.figSign = Figure(figsize=(15, 3), dpi=100)

        self.canvasSpec = FigureCanvas(self.figSpec)
        self.canvasTemp = FigureCanvas(self.figTemp)
        self.canvasMicro = FigureCanvas(self.figMicro)
        self.canvasSign = FigureCanvas(self.figSign)

        # self.toolbarSpec = NavigationToolbar(self.canvasSpec, self)
        self.Slider = QSlider(Qt.Horizontal)

    def display(self):
        MainLayout = QVBoxLayout()
        grid = QGridLayout()
        grid.addWidget(self.video, 0, 0)
        grid.addWidget(self.canvasSpec, 1, 0)
        grid.addWidget(self.canvasTemp, 0, 1)
        grid.addWidget(self.canvasMicro, 1, 1)

        MainLayout.addLayout(grid)
        MainLayout.addWidget(self.canvasSign)
        MainLayout.addWidget(self.Slider)
        self.setLayout(MainLayout)

    def testVideo(self):
        path = "/media/mathieu/Nouveau nom/videos_bille/{}.avi".format(self.filename)
        self.cvVideo = cv2.VideoCapture(path)
        length = int(self.cvVideo.get(cv2.CAP_PROP_FRAME_COUNT))
        width = int(self.cvVideo.get(cv2.CAP_PROP_FRAME_WIDTH))
        height = int(self.cvVideo.get(cv2.CAP_PROP_FRAME_HEIGHT))
        rate = int(self.cvVideo.get(cv2.CAP_PROP_POS_FRAMES))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    clock = GUI()
    clock.show()
    sys.exit(app.exec_())
