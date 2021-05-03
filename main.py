<<<<<<< HEAD
from src.interface.root import View


if __name__ == '__main__':
    v = View()
=======
import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from GUI import main_screen_wip as msw

if __name__ == "__main__":
    product_name = "uFood"
    app = qtw.QApplication(sys.argv)
    win_icon = qtg.QIcon(qtg.QPixmap("GUI/assets/carrot_icon.png"))
    screen = app.primaryScreen().size()
    hsize = screen.height()  # kept seperate rather than list
    wsize = screen.width()  # ... so that it is more pythonic
    mw = msw.MainWindow(
        windowTitle=product_name, windowIcon=win_icon, hsize=hsize, wsize=wsize
    )
    mw.show()

    sys.exit(app.exec_())
>>>>>>> dev_tom
