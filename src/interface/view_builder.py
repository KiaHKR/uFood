from PyQt5 import QtWidgets as qtw

from src.interface.panels.right_bottom_panel import Components as rbcomp
import src.interface.view as view
import src.interface.globals as globals
import src.interface.styling.qss as qss
import src.interface.controller as controller


class ViewBuilder:
    def recipe_card(
        name="[RECIPE NAME]",
        diet_type="[DIET TYPE]",
        total_time="[TOTAL TIME]",
        ingr="[INGREDIENT LIST]",
        pk_id="Error",
        thumbnail=None,
    ):
        """Widgets of recipe cards."""
        recipe_card = qtw.QPushButton()
        recipe_card.setLayout(qtw.QHBoxLayout())
        recipe_card.setStyleSheet(
            "QWidget::hover" "{background-color : #6c899d;}"
        )

        info = qtw.QWidget()
        info.setLayout(qtw.QVBoxLayout())
        info.setStyleSheet("background-color: transparent;")
        # info.setStyleSheet("border: none;")
        info.layout().addWidget(rbcomp().recipe_title(name))
        info.layout().addWidget(rbcomp().diet_type(diet_type))

        time = qtw.QWidget()

        recipe_card.setObjectName(pk_id)
        recipe_card.setFixedHeight(150)

        buttons = qtw.QWidget()
        buttons.setLayout(qtw.QVBoxLayout())
        buttons.setStyleSheet("background-color: transparent;")
        buttons.layout().addWidget(
            view.View.save_build(recipe_card.objectName())
        )

        buttons.layout().addWidget(
            view.View.export_build(recipe_card.objectName())
        )
        buttons.layout().setSpacing(0)

        recipe_card.layout().addWidget(rbcomp().thumbnail_img(thumbnail), 1)
        recipe_card.layout().addWidget(info, 20)
        recipe_card.layout().addWidget(buttons, 0)

        time.setLayout(qtw.QHBoxLayout())
        time.layout().addWidget(globals.b_rpanel["total_time_icon"])
        time.layout().addWidget(rbcomp().total_time(total_time))
        time.layout().setContentsMargins(0, 0, 0, 0)
        time.layout().setSpacing(0)
        info.layout().addWidget(time)
        info.layout().addWidget(rbcomp().ingredients(ingr))
        info.layout().setContentsMargins(0, 0, 0, 0)
        info.layout().setSpacing(0)
        # recipe_card.setCursor(qtg.QCursor(qtc.Qt.OpenHandCursor))

        return recipe_card

    def build_recipe_view():
        """Build recipe view."""
        recipe_view_widget_box = qtw.QWidget()
        recipe_view_widget_box.setLayout(qtw.QVBoxLayout())

        top_widget = qtw.QWidget()
        top_widget.setLayout(qtw.QHBoxLayout())

        top_widget.layout().addWidget(globals.b_rpanel["recipe_view_title"], 1)
        top_widget.layout().addWidget(globals.b_rpanel["recipe_view_exit"], 0)

        bottom_widget = qtw.QScrollArea()  # scrollarea
        bottom_widget.setStyleSheet(qss.scrollbar())
        bottom_widget.setFrameShape(qtw.QFrame.Shape.NoFrame)

        bottom_widget_container = qtw.QWidget()
        bottom_widget_container.setLayout(qtw.QHBoxLayout())

        bottom_widget_left = qtw.QWidget()  # vbox
        bottom_widget_left.setLayout(qtw.QVBoxLayout())

        bottom_widget_container.layout().addWidget(bottom_widget_left)  # hbox
        bottom_widget_container.layout().addWidget(
            globals.b_rpanel["recipe_view_steps"]
        )

        bottom_widget_left.layout().addWidget(
            (globals.b_rpanel["recipe_view_img"])
        )
        bottom_widget_left.layout().addWidget(
            (globals.b_rpanel["recipe_view_cook_diet_label"])
        )
        bottom_widget_left.layout().addWidget(
            (globals.b_rpanel["recipe_view_ingredients"])
        )

        bottom_widget.setWidget(bottom_widget_container)

        recipe_view_widget_box.layout().addWidget(top_widget)
        recipe_view_widget_box.layout().addWidget(bottom_widget)

        globals.b_rpanel["recipe_view_exit"].clicked.connect(
            lambda: controller.Controller.set_recipe_view_vis(False)
        )

        return recipe_view_widget_box
