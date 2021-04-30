"""Stores built components for easy, convenient access."""

from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc

from ui.components.templates.media_widgets import MediaWidgets as mw
from ui.components.templates.search_widget import SearchWidgets as sw


class Components:
    """Stores built gui elements/components."""

    def search_bar():
        """Build the search bar."""
        sb_icon = mw().create_pushIcon("search.png")
        sb_icon.setIconSize(qtc.QSize(25, 25))
        search_bar = sw.create_search_bar(
            h=40, icon=sb_icon, icon_bg_color="white"
        )
        return search_bar

    def drop_down_filter():

        return

    def donation_box():
        """Build the donations box."""
        donate = qtw.QWidget()
        donate.setLayout(qtw.QHBoxLayout())
        fb_icon = mw().create_pushIcon("fb_icon.png")
        fb_icon.setIconSize(qtc.QSize(30, 30))
        text = qtw.QLabel(text="DONATE")
        text.setStyleSheet("font-weight: bold; font-size: 18px; color: white;")
        donate.layout().addWidget(fb_icon, 0)
        donate.layout().addWidget(text, 10)
        return donate

    def dietary_filter(options_list):
        """Create a drop-down menu and fill it with items."""
        menu = qtw.QMenu()
        menu.setContentsMargins(0, 0, 0, 0)

        for a in options_list:
            act = qtw.QAction(a, menu)
            act.setCheckable(True)
            menu.addAction(act)

        dietary_filter = mw().create_pushIcon("filter_icon.png")
        dietary_filter.setMenu(menu)
        dietary_filter.setStyleSheet(
            """
            background-color: white;
            """
        )
        dietary_filter.setFixedHeight(35)

        filter = qtw.QWidget()
        filter.setLayout(qtw.QHBoxLayout())
        filter.layout().setSpacing(0)
        filter.layout().setContentsMargins(5, 1, 0, 0)
        filter.setFixedWidth(50)

        filter.layout().addWidget(dietary_filter)
        return filter

    def scroll_area(child):
        sa = qtw.QScrollArea()
        sa.setWidgetResizable(True)
        sa.setWidget(child)

        sb_styling = """
            QScrollBar:vertical {              
                border: none;
                background:white;
                width:15px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle:vertical {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop: 0 #202f82, 
                    stop: 0.5 #202f82,
                    stop: 1 #202f82
                );
                min-height: 0px;
            }
            QScrollBar::add-line:vertical {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop: 0 #202f82,
                    stop: 0.5 #202f82,
                    stop:1 #202f82
                );
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line:vertical {
                background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                stop: 0  #202f82,
                stop: 0.5 #202f82,
                stop: 1  #202f82);
                height: 0 px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QListWidget{
                background-color: white;
                margin-left: 20px;
                font-size: 14px;
        }
        """
        sa.verticalScrollBar().setStyleSheet(sb_styling)
        sa.horizontalScrollBar().setStyleSheet(sb_styling)

        return sa