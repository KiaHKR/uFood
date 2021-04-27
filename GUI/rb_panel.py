"""This class caters to all bottom panel events. It is a WIP."""

from PyQt5 import QtWidgets as qtw
# from PyQt5 import QtCore as qtc
# from PyQt5 import QtGui as qtg


class RightBottomPanel():
    """Returns relevant page settings for the right bottom panel."""

    def __init__(self, *args, **kwargs):
        """Build constructor."""
        pass

    def trending_page(self):
        """Build trending page."""
        rp_bottom = qtw.QWidget()
        rp_bottom.setStyleSheet(
                """border: 2px solid purple;
                color: white;
                font-size: 20px;"""
            )
        rp_bottom.setLayout(qtw.QVBoxLayout())
        rp_bottom.layout().addWidget(qtw.QLabel(text="this panel will change"))
        return rp_bottom

    def search_results_page(self):
        """Build search results page."""
        pass

    def favorite_page(self):
        """Build favorite page."""
        pass
