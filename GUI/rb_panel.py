from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg


class RightBottomPanel():
    
    def __init__(self, *args, **kwargs):
        pass
    


    def trending_page(self):
        rp_bottom = qtw.QWidget()
        rp_bottom.setStyleSheet('border: 2px solid purple; color: white; font-size: 20px;')
        rp_bottom.setLayout(qtw.QVBoxLayout())
        rp_bottom.layout().addWidget(qtw.QLabel(text="this panel will change..."))
        return rp_bottom


    def search_results_page(self):
        pass

    def favorite_page(self):
        pass
