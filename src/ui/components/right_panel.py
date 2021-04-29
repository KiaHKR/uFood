"""A class covering builds for the right top panel and right bottom panel"""

from ui.components.templates.media_widgets import MediaWidgets
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc


class RightTopPanel:
    """Contains all functionality for building the right top-most panel."""

    def __init__(self):
        """Build constructor."""
        self.r_top = qtw.QWidget()
        self.r_top.setLayout(qtw.QHBoxLayout())

    def build_panel(self, input_text=None):
        """Build top panel."""
        if input_text is not None:
            input_text = self.__set_text(input_text)

        favorites_icon = self.__set_toolbar_icon('fav_icon.png')
        recipes_icon = self.__set_toolbar_icon('recipes_icon.png')
        back_icon = self.__set_toolbar_icon('back_icon.png')
        self.r_top.layout().addWidget(back_icon, 1)
        self.r_top.layout().addWidget(input_text, 9)
        self.r_top.layout().addWidget(favorites_icon, 1)
        self.r_top.layout().addWidget(recipes_icon, 1)
        return self.r_top

    def __set_text(self, input_text='[ TEXT ]', font_size=24, text_color='white'):  # noqa: E501
        rtop_text = qtw.QLabel(text=input_text)
        rtop_text.setStyleSheet(f"""
            color: {text_color};
            font-size: {font_size};
            font-weight: bold;
            """)
        rtop_text.setAlignment(qtc.Qt.AlignCenter)
        return rtop_text

    def __set_toolbar_icon(self, filename):
        toolbar_icon = MediaWidgets().create_pushIcon(filename)
        toolbar_icon.setStyleSheet('border: None; margin: auto;')
        toolbar_icon.setFixedSize(40, 30)
        toolbar_icon.setIconSize(qtc.QSize(30, 30))
        return toolbar_icon


class RightBottomPanel:
    """Handles all views on the right bottom panel (rbp)."""

    def trending_page():
        """Build the trending page onto the right bottom panel."""
        fill = qtw.QLabel(text='This panel will change...')
        fill.setStyleSheet("""
                color: white;
                font-size: 28px;
                border: 2px solid powderblue;
            """)
        return fill

    def search_results_page():
        """Build the search results page on the right bottom panel (rbp)."""
        pass

    def favorites_page():
        """Build the favorites page on the right bottom panel (rbp)."""
        pass
