from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from src.interface.styling import qss



class Compontents:
    widgets = {}
    __object_names = (
        'back_btn',
        'win_text',
        'fav_btn',
        'recipes_btn'
    )
    __path = 'src/interface/assets/'

    def __init__(self):
        self.widgets[self.__object_names[0]] = self.__back_btn()
        self.widgets[self.__object_names[1]] = self.__win_text()
        self.widgets[self.__object_names[2]] = self.__fav_btn()
        self.widgets[self.__object_names[3]] = self.__recipes_btn()

    def __win_text(self):
        win_text = qtw.QLabel('[ TEXT ]')
        win_text.setObjectName('win_text')
        win_text.setStyleSheet('font-size: 18px; font-weight: bold; color: white;')
        return win_text

    def __back_btn(self):
        back_btn = qtw.QPushButton(
            icon=qtg.QIcon(
                qtg.QPixmap(self.__path + 'back_icon.png')
            )
        )
        back_btn.setIconSize(qtc.QSize(30, 30))
        back_btn.setObjectName(self.__object_names[0])
        return back_btn
    
    def __fav_btn(self):
        fav_btn = qtw.QPushButton(
            icon=qtg.QIcon(
                qtg.QPixmap(self.__path + 'fav_icon.png')
            )
        )
        fav_btn.setIconSize(qtc.QSize(30, 30))
        fav_btn.setObjectName(self.__object_names[1])
        return fav_btn

    def __recipes_btn(self):
        recipes_btn = qtw.QPushButton(
            icon=qtg.QIcon(
                qtg.QPixmap(self.__path + 'recipes_icon.png')
            )
        )
        recipes_btn.setIconSize(qtc.QSize(30, 30))
        recipes_btn.setObjectName(self.__object_names[2])
        return recipes_btn
