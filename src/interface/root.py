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
lpanel = lcomp().widgets
t_rpanel = rtcomp().widgets
b_rpanel = rbcomp().widgets


class Root(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # -- Build root panel
        layout = qtw.QHBoxLayout()
        self.screen = app.primaryScreen().size()
        self.resize(self.screen.width() // 2, self.screen.height() // 2)
        self.setStyleSheet("background-color: #1c1c1c;")
        self.setLayout(layout)


class View(qtw.QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        root_view = Root()

        self.left_panel_widget = self.__left_panel_build()
        root_view.layout().addWidget(self.left_panel_widget)

        self.qTimer = qtc.QTimer()
        self.qTimer.setInterval(1)
        self.qTimer.timeout.connect(
            lambda: Controller.update_logo_size(self.left_panel_widget)
        )
        self.qTimer.start()

        root_view.show()
        sys.exit(app.exec_())

    def __left_panel_build(self):
        left_panel_widget = qtw.QWidget()
        left_panel_widget.setLayout(qtw.QVBoxLayout())
        Controller.update_logo_size(
            left_panel_widget
        )  # Grabbing logo size from window size
        left_panel_widget.layout().addWidget(lpanel["logo"])
        left_panel_widget.layout().addWidget(self.__search_widget_build())

        return left_panel_widget

    def __search_widget_build(self):
        """Build parent search widget."""
        search_widget = qtw.QWidget()
        search_widget.setLayout(qtw.QGridLayout())

        # Construct search button
        search_icon_widget = qtw.QWidget()
        search_icon_widget.setLayout(qtw.QStackedLayout())

        # Connect filter btn to filter menu
        lpanel["search_filter_btn"].setMenu(lpanel["search_filter_menu"])

        # Add widgets to parent search layout
        search_widget.layout().addWidget(lpanel["search_bar"], 0, 0)
        search_widget.layout().addWidget(lpanel["search_btn_bg"], 0, 2)
        search_widget.layout().addWidget(lpanel["search_btn"], 0, 2)
        search_widget.layout().addWidget(lpanel["search_filter_btn"], 0, 3)
        search_widget.layout().setAlignment(qtc.Qt.AlignmentFlag.AlignTop)
        search_widget.layout().setSpacing(0)

        return search_widget


class Controller:
    def update_logo_size(left_panel_widget):
        """Changes size of logo pixmap, based on parent panel size."""
        lpanel["logo"].setPixmap(
            qtg.QPixmap(lcomp._path + "logo_placeholder.png").scaled(
                left_panel_widget.width() // 1.9,
                left_panel_widget.height() // 2.5,
                qtc.Qt.AspectRatioMode.KeepAspectRatio,
            )
        )
