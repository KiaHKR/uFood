"""
This class handles the building of all GUI elements.

pertaining to the static layout. rb_panel.py handles
page loading on the bottom rightmost panel.

"""

import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from GUI import ingredient_widget, rb_panel as rbp
from src import search, gui_slots as slots


class MainWindow(qtw.QWidget):
    """Builds the root stage."""

    gui_slots = slots.GuiSlots()
    search_obj = search.Search()

    def __init__(self, hsize, wsize, *args, **kwargs):
        """
        Build the constructor of this class.

        It sets the root layout (var 'layout').

        """
        super().__init__(*args, **kwargs)
        self.resize(int(wsize * 0.5), int(hsize * 0.5))
        self.setStyleSheet("background-color: #1c1c1c;")

        self.ingredients = ingredient_widget.IngredientWidget()
        self.left_panel = self.set_left_panel()
        self.rt_panel = self.set_right_tpanel()
        self.rb_panel = self.set_right_bpanel()

<<<<<<< HEAD
        rb_panel = qtw.QWidget()
        rb_panel.setLayout(qtw.QVBoxLayout())
        for _ in range(0, 40):
            rb_panel.layout().addWidget(
                self.set_right_bpanel('search_results')
                )
=======
        # for _ in range(0, 100):  # for testing purposes only
        #     button = qtw.QPushButton(
        #         """
        #     Helllllooooo000000000000000000000000000000000000000000000000000000000000000000000000000000
        #     """
        #     )
        #     self.rb_panel.layout().addWidget(button)
>>>>>>> dev_tom

        scroll_area = qtw.QScrollArea()
        scroll_area.setWidget(self.rb_panel)
        scroll_area.setWidgetResizable(True)
        scroll_area.verticalScrollBar().setStyleSheet(
            """
            background-color: powderblue;
            color: black;
        """
        )
        scroll_area.horizontalScrollBar().setStyleSheet(
            """
            background-color: powderblue;
            color: black;
        """
        )

        rpanel = qtw.QWidget()
<<<<<<< HEAD
        # rpanel.setStyleSheet('border: 2px solid green;')
=======
        rpanel.setStyleSheet("border: 2px solid green;")
>>>>>>> dev_tom
        rpanel.setLayout(qtw.QVBoxLayout())
        rpanel.layout().addWidget(self.rt_panel, 0)
        rpanel.layout().addWidget(scroll_area, 7)

        # -- root layout --
        layout = qtw.QHBoxLayout()
        layout.addWidget(self.left_panel, 3)
        layout.addWidget(rpanel, 7)

        self.setLayout(layout)

    def set_left_panel(self):
        """Build the left vbox panel."""
        logo = qtw.QLabel(
            pixmap=qtg.QPixmap("GUI/assets/logo_placeholder.png").scaled(
                200, 200
            )
        )
        # logo.setStyleSheet('border: 2px solid red;')
        logo.setAlignment(qtc.Qt.AlignCenter)

        left_panel = qtw.QWidget()
        # left_panel.setStyleSheet('border:2px solid white;')
        left_panel.setLayout(qtw.QVBoxLayout())
        left_panel.setFixedWidth(300)

        menu = qtw.QMenu()
<<<<<<< HEAD
        menu.setContentsMargins(0, 0, 0, 0)
        act1 = qtw.QAction('Vegan', menu)
=======
        menu.setContentsMargins(5, 0, 0, 0)
        act1 = qtw.QAction("Vegan", menu)
>>>>>>> dev_tom
        act1.setCheckable(True)
        act2 = qtw.QAction("Vegetarian", menu)
        act2.setCheckable(True)
        act3 = qtw.QAction("Pescatarian", menu)
        act3.setCheckable(True)
        act4 = qtw.QAction("Keto", menu)
        act4.setCheckable(True)
        act5 = qtw.QAction("Paleo", menu)
        act5.setCheckable(True)

        menu.addAction(act1)
        menu.addAction(act2)
        menu.addAction(act3)
        menu.addAction(act4)
        menu.addAction(act5)

        filter = qtw.QWidget()
        filter.setLayout(qtw.QHBoxLayout())
        filter.layout().setSpacing(0)
        # filter.setStyleSheet('border: 2px solid green;')
        filter.layout().setContentsMargins(5, 1, 0, 0)
        filter.setFixedWidth(50)

        dietary_filter = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap('assets/filter_icon.png'))
            )
        dietary_filter.setMenu(menu)
<<<<<<< HEAD
        dietary_filter.setStyleSheet("""
            background-color: white;
            """)
        dietary_filter.setFixedHeight(35)
        # dietary_filter.setFixedSize(60, 30)

        filter.layout().addWidget(dietary_filter)
=======
        dietary_filter.setStyleSheet(
            """
            margin-left: 5px;
            background-color: white;
            """
        )
        dietary_filter.setFixedWidth(25)
>>>>>>> dev_tom

        bg_search_icon = qtw.QLabel()
        bg_search_icon.setLayout(qtw.QStackedLayout())

        search_bar = qtw.QLineEdit()
<<<<<<< HEAD
        search_bar.setStyleSheet('background-color: white; font-size: 14px;')
        search_bar.setFixedSize(207, 40)
=======
        search_bar.setStyleSheet("background-color: white; font-size: 14px;")
        search_bar.setFixedSize(240, 40)
>>>>>>> dev_tom
        search_bar.setContentsMargins(20, 0, 20, 0)

        # Create drop down search results
        list_box = qtw.QListWidget()  # list_box to store result list
        list_box.setStyleSheet(  # Styling for box and scrollbar
            """
        QScrollBar:vertical {              
            border: none;
            background:white;
            width:4px;
            margin: 0px 0px 0px 0px;
        }
        QScrollBar::handle:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),
            stop: 1 rgb(32, 47, 130));
            min-height: 0px;
        }
        QScrollBar::add-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0 rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),
            stop:1 rgb(32, 47, 130));
            height: 0px;
            subcontrol-position: bottom;
            subcontrol-origin: margin;
        }
        QScrollBar::sub-line:vertical {
            background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
            stop: 0  rgb(32, 47, 130), stop: 0.5 rgb(32, 47, 130),
            stop:1 rgb(32, 47, 130));
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
        )
        list_box.setFixedWidth(
            search_bar.width()
        )  # Fixed width, same as search_bar
        list_box.setSpacing(0)  # No spacing between items
        list_box.setVisible(False)  # Invisible on start

        list_box.itemClicked.connect(  # executes when item in list is clicked
            lambda: self.gui_slots.select_ingredient(  # calls function
                self.ingredients,  # parametres
                list_box.selectedItems()[0].text(),
                search_bar,
            )
        )

        search_bar.textChanged.connect(  # executes when text changed
            lambda: self.gui_slots.on_search_changed(  # calls function
                self.left_panel,
                self.search_obj.db_ingredients,  # parametres
                search_bar.text(),
                list_box,
            )
        )

        search_button = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/search.png"))
        )
        search_button.setIconSize(qtc.QSize(25, 25))
        search_button.setStyleSheet(
            """
            background-color: transparent;
            margin-top: 1px;
            position: absolute;
<<<<<<< HEAD
            """)
        bg_search_icon.setStyleSheet("""
            background-color: white;
            margin-top: 1.1px;
            """)
        bg_search_icon.setFixedSize(qtc.QSize(30, search_bar.height()-1))
=======
        """
        )
        pre.setStyleSheet("background-color: white; margin-top: 1.1px;")
        pre.setFixedSize(qtc.QSize(30, search_bar.height() - 1))
>>>>>>> dev_tom
        search_button.setFixedSize(qtc.QSize(30, search_bar.height()))

        search = qtw.QWidget()
        search.setLayout(qtw.QGridLayout())
        # search.setStyleSheet('border: 2px solid red;')
        search.layout().addWidget(search_bar, 0, 0)
        search.layout().addWidget(bg_search_icon, 0, 2)
        search.layout().addWidget(search_button, 0, 2)
<<<<<<< HEAD
        search.layout().addWidget(filter, 0, 3)
=======
        search.layout().addWidget(list_box, 1, 0)
        search.layout().addWidget(dietary_filter, 0, 3)
>>>>>>> dev_tom
        search.layout().setAlignment(qtc.Qt.AlignTop)
        search.layout().setSpacing(0)

        donate_text = qtw.QLabel(text="DONATE")
        donate_text.setStyleSheet("color: white; font-weight: bold;")
        fb_icon = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/fb_icon.png"))
        )
        fb_icon.setIconSize(qtc.QSize(30, 30))
<<<<<<< HEAD
        fb_icon.setStyleSheet('background: transparent;')
        
        
=======
        fb_icon.setStyleSheet("background: transparent;")
>>>>>>> dev_tom
        donate = qtw.QWidget()
        # donate.setStyleSheet('border: 2px solid red')
        donate.setLayout(qtw.QHBoxLayout())
        donate.layout().addWidget(fb_icon, 0)
        donate.layout().addWidget(donate_text, 10)
        donate.setFixedHeight(60)
        donate.layout().setAlignment(qtc.Qt.AlignBottom)

        # !--- run with vs. without margins and pick bg_search_iconference
        logo.setContentsMargins(0, 150, 0, 0)

        left_panel.layout().addWidget(logo)
        left_panel.layout().addWidget(search)
        left_panel.layout().addWidget(self.ingredients.ingredient_widget)
        left_panel.layout().addWidget(donate)
        left_panel.layout().setSpacing(0)

        return left_panel

    def set_right_tpanel(self):
        """Set top rightmost hbox panel [icon bar]."""
        r_top = qtw.QWidget()
<<<<<<< HEAD
        # r_top.setStyleSheet('border:2px solid powderblue;')
=======
        r_top.setStyleSheet("border:2px solid powderblue;")
>>>>>>> dev_tom
        r_top.setLayout(qtw.QHBoxLayout())
        self.rtop_text = qtw.QLabel('')
        self.rtop_text.setStyleSheet("""
            color: white;
            font-size: 20px;
            """)

<<<<<<< HEAD
=======
        text = qtw.QLabel()
        text.setStyleSheet("border: none; color: white; font-size: 20px")
>>>>>>> dev_tom
        favorites_icon = qtw.QPushButton(
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/fav_icon.png"))
        )
        favorites_icon.setStyleSheet("border: None; margin: auto;")
        # favorites_icon.setStyleSheet('background-color: white;')
        favorites_icon.setFixedSize(40, 30)
        favorites_icon.setIconSize(qtc.QSize(30, 30))

        recipes_icon = qtw.QPushButton(
<<<<<<< HEAD
            icon=qtg.QIcon(qtg.QPixmap('assets/recipes_icon.png'))
            )
        recipes_icon.setStyleSheet('border: None; margin-top: 4px;')
=======
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/recipes_icon.png"))
        )
        recipes_icon.setStyleSheet("border: None; margin-top: 4px;")
        # favorites_icon.setStyleSheet('background-color: white;')
>>>>>>> dev_tom
        recipes_icon.setFixedSize(40, 30)
        recipes_icon.setIconSize(qtc.QSize(30, 30))

        back_icon = qtw.QPushButton(
<<<<<<< HEAD
            icon=qtg.QIcon(qtg.QPixmap('assets/back_icon.png'))
            )
        back_icon.setStyleSheet('border: None;')
=======
            icon=qtg.QIcon(qtg.QPixmap("GUI/assets/back_icon.png"))
        )
        back_icon.setStyleSheet("border: None;")
        # favorites_icon.setStyleSheet('background-color: white;')
>>>>>>> dev_tom
        back_icon.setFixedSize(40, 30)
        back_icon.setIconSize(qtc.QSize(30, 30))

        r_top.layout().addWidget(back_icon)
        r_top.layout().addWidget(self.rtop_text)
        r_top.layout().addWidget(favorites_icon)
        r_top.layout().addWidget(recipes_icon)
        return r_top

    # responsive slot method that governs what pages load from the
    # ... rbp.RightBottomPanel() class?
    def set_right_bpanel(self, page="trending"):
        """Set right bottom panel/widget w.r.t. emitted signals/events."""
        rp_bottom = None
        if page.lower() == "trending":
            rp_bottom = rbp.RightBottomPanel().trending_page()
        elif page.lower() == "search_results":
            rp_bottom = rbp.RightBottomPanel().search_results_page()
        elif page.lower() == "favorites":
            rp_bottom = rbp.RightBottomPanel().favorite_page()
        return rp_bottom
