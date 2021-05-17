from src.interface.panels.left_panel import Components as lcomp
import os
from PyQt5 import QtWidgets as qtw

from src.interface.panels.right_bottom_panel import Components as rbcomp
from src.interface.panels.right_top_panel import Components as rtcomp

from src.interface.root import Root


app = qtw.QApplication(os.sys.argv)

lpanel = lcomp().widgets
t_rpanel = rtcomp().widgets
b_rpanel = rbcomp().widgets
stacked_widget = None
recipe_view = None
root_view = Root(app.primaryScreen().size())
