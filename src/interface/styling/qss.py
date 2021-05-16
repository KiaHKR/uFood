"""QSS styling constants."""


def scrollbar():
    """Return style for scrollbars."""
    return """QScrollBar{
                border: none;
                background: white;
                width:7px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle{
                background: #333333;
                min-height: 0px;
            }
            QScrollBar::add-line{
                background: #333333;
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line{
                background: #333333;
                height: 0 px;
                subcontrol-position: top;
                subcontrol-origin: margin;
            }
            QListWidget{
                background-color: white;
                margin-left: 20px;
                font-size: 14px;
        }"""
