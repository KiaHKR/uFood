"""Main class to handle all views."""

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from ui.components.templates.media_widgets import MediaWidgets as mw
from ui.components.components import Components as comp
from ui.components.right_panel import RightTopPanel, RightBottomPanel

app = qtw.QApplication(sys.argv)
product_name = 'uFood'
logo = 'logo_placeholder.png'
supported_diets = ['Vegan', 'Vegatarian', 'Pescatarian', 'Paleo', 'Keto']


class Views(qtw.QWidget):
    """Handles all views on the App."""

    def __init__(self, *args, **kwargs):
        """Build constructor."""
        super().__init__(*args, **kwargs)
        self.build_root_view()
        rp = qtw.QWidget()  # right panel
        rp.setLayout(qtw.QVBoxLayout())
        rp_fill = self.right_panel()
        rp.layout().addWidget(rp_fill[0], 0)
        rp.layout().addWidget(rp_fill[1], 10)
        self.layer_view(self.left_panel(), rp)
        self.run_gui()

    def set_product_icon():
        """Retrieve and build product icon from 'ui/assets'."""
        return mw().create_icon('carrot_icon.png')

    def build_root_view(self):
        """Build root window."""
        screen = app.primaryScreen().size()
        self.resize(screen.width() // 2, screen.height() // 2)
        self.setStyleSheet("background-color: #1c1c1c;")

    def build_search(self):
        """Build the search function in the left panel."""
        search = qtw.QWidget()
        search.setLayout(qtw.QHBoxLayout())
        search.layout().setSpacing(0)
        search.layout().addWidget(comp.search_bar())
        search.layout().addWidget(comp.dietary_filter(supported_diets))
        search.setFixedHeight(80)
        return search

    def build_donate(self):
        """Build the donate button + text."""
        donate = comp.donation_box()
        donate.setStyleSheet('border: none;')
        donate.layout().setAlignment(qtc.Qt.AlignBottom)
        return donate

    def left_panel(self):
        """Set left panel widgets."""
        lpanel = qtw.QWidget()
        lpanel_layout = qtw.QVBoxLayout()

        search = self.build_search()
        donate = self.build_donate()
        logo_pic = mw().create_imgWithScale(
                logo,
                lpanel.width()//2.5,
                lpanel.height()//1.8
            )
        logo_pic.setAlignment(qtc.Qt.AlignCenter)
        logo_pic.setContentsMargins(0, 50, 0, 0)
        lpanel_layout.addWidget(logo_pic)
        lpanel_layout.addWidget(search)
        lpanel_layout.addWidget(donate)
        lpanel.setLayout(lpanel_layout)
        return lpanel

    def right_panel(self):
        """Build the right panel."""
        rtp = qtw.QWidget()  # -- Right top panel
        rtp.setLayout(qtw.QHBoxLayout())
        rtp.layout().addWidget(RightTopPanel().build_panel('[ KEBAB ]'))

        rbp = qtw.QWidget()  # -- Right bottom panel
        rbp.setLayout(qtw.QVBoxLayout())
        rbp.layout().addWidget(RightBottomPanel.trending_page())
        return [rtp, rbp]

    def layer_view(self, *panels):
        """Layer the view with all created panels."""
        self.view = qtw.QHBoxLayout()
        if len(panels) != 2:
            print("""\n\n>> The # of HBOX panels has changed! \
            \nPlease see views.py. A traceback can be found below.\n\n\n""")
            raise SystemError(sys.last_traceback())
        self.view.addWidget(panels[0], 3)
        self.view.addWidget(panels[1], 7)

    def run_gui(self):
        """Finalize layout and show + execture GUI."""
        self.setLayout(self.view)
        self.show()
        sys.exit(app.exec_())
