"""Class for storing search bar templates"""
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class SearchWidgets:
    """Build premade search bars."""

    def create_search_bar(w=None, h=None, filter=False, icon=None, btn_bg_color='transparent', icon_bg_color='white'):  # noqa: E501
        """Build left-panel main search bar."""
        search_bar = qtw.QLineEdit()
        search_bar.setStyleSheet('background-color: white; font-size: 14px;')
        if w is not None:
            search_bar.setFixedWidth(w)
        if h is not None:
            search_bar.setFixedHeight(h)
        search_button = icon
        if icon is not None:
            bg_search_icon = qtw.QLabel()
            bg_search_icon.setLayout(qtw.QStackedLayout())
            search_button.setStyleSheet(f"""
                border: none;
                background-color: {btn_bg_color};
                margin-top: 1px;
                position: absolute;
                """)
            bg_search_icon.setStyleSheet(f"""
                background-color: {icon_bg_color};
                margin-top: 1.1px;
                """)
            bg_search_icon.setFixedSize(qtc.QSize(30, search_bar.height()-1))
            search_button.setFixedSize(qtc.QSize(30, search_bar.height()))

        search = qtw.QWidget()
        search.setLayout(qtw.QGridLayout())
        search.layout().addWidget(search_bar, 0, 0)
        if icon:
            search.layout().addWidget(bg_search_icon, 0, 2)
        if search_button is not None:
            search.layout().addWidget(search_button, 0, 2)
        if filter:
            search.layout().addWidget(filter, 0, 3)
        search.layout().setAlignment(qtc.Qt.AlignTop)
        search.layout().setSpacing(0)
        search.layout().setAlignment(qtc.Qt.AlignCenter)
        search.layout().setContentsMargins(20, 0, 0, 0)
        return search
