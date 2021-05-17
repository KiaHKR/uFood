"""Root file to carry root, Views and controller class."""
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg

from src.interface.panels.left_panel import Components as lcomp


class Root(qtw.QWidget):
    """Parent class for containing ui."""

    def __init__(self, screen, *args, **kwargs):
        """Is constructor of root class."""
        super().__init__(*args, **kwargs)
        # -- Build root panel
        layout = qtw.QHBoxLayout()
        self.screen = screen
        self.resize(self.screen.width() // 2, self.screen.height() // 2)
        self.setStyleSheet("background-color: #1c1c1c;")
        self.setLayout(layout)
        self.setWindowTitle("uFood")
        self.setWindowIcon(
            qtg.QIcon(qtg.QPixmap(lcomp.path + "carrot_icon.png"))
        )
