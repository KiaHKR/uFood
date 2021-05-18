from src.interface.panels.left_panel import Components as lcomp
import os
from PyQt5 import QtWidgets as qtw

import src.interface.panels.right_bottom_panel as rbcomp
import src.interface.panels.right_top_panel as rtcomp

from src.interface.root import Root


app = qtw.QApplication(os.sys.argv)

lpanel = lcomp().widgets
t_rpanel = rtcomp.Components().widgets
b_rpanel = rbcomp.Components().widgets
stacked_widget = None
recipe_view = None
root_view = Root(app.primaryScreen().size())
selected_ingredients = []
