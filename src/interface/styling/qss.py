"""QSS styling constants."""


def scrollbar():
    """Return style for scrollbars."""
    return """QScrollBar{
                border: none;
                background:white;
                width:15px;
                margin: 0px 0px 0px 0px;
            }
            QScrollBar::handle{
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop: 0 #202f82,
                    stop: 0.5 #202f82,
                    stop: 1 #202f82
                );
                min-height: 0px;
            }
            QScrollBar::add-line{
                    background: qlineargradient(x1:0, y1:0, x2:1, y2:0,
                    stop: 0 #202f82,
                    stop: 0.5 #202f82,
                    stop:1 #202f82
                );
                height: 0px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
            }
            QScrollBar::sub-line{
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
        }"""
