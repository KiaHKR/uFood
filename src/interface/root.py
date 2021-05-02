import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc

from src.interface.panels.left_panel import Components as lcomp
from src.interface.panels.right_top_panel import Compontents as rtcomp
from src.interface.panels.right_bottom_panel import Components as rbcomp

# import bottom rpanel
# import logic/query


app = qtw.QApplication(sys.argv)
lpanel = {}
t_rpanel = {}
b_rpanel = {}

class Root(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # -- Build root panel
        layout = qtw.QHBoxLayout()
        self.screen = app.primaryScreen().size()
        self.resize(self.screen.width() // 2, self.screen.height() // 2)
        self.setStyleSheet("background-color: #1c1c1c;")
        self.setLayout(layout)
        self.show()
        sys.exit(app.exec_())
        

class View(qtw.QWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        root_view = Root()
        left_comps = lcomp()
        top_right_comps = rtcomp()
        bottom_right_comps = rbcomp()
        lpanel = left_comps.widgets
        t_rpanel = top_right_comps.widgets
        b_rpanel = bottom_right_comps.widgets
    
    def __build_root(self):
        
        pass

class Controller:
    pass
