from PyQt5.QtWidgets import (QPushButton)


class BasePushButton(QPushButton):
    '''Basic button type without coloring.'''

    def __init__(self, text, parent=None):
        super(BasePushButton, self).__init__(text, parent)
        self.setStyleSheet(self.styleSheet() + '''
            QPushButton {
                font-family: Verdana, Geneva, sans-serif	
                border: none;
                font-size: 10pt;
                padding: 0.5em;
                min-width: 8em;
            }
        ''')

    def setForeground(self, color):
        '''Set foreground color (i.e. text color).'''

        self.setStyleSheet(self.styleSheet() + '''
            QPushButton {
                color: {};
            }
        '''.format(color))

    def setBackground(self, color, hover, pressed):
        '''Set background colors at normal time, when hovered, and when 
        pressed.'''

        self.setStyleSheet(self.styleSheet() + '''
            QPushButton {{
                background-color: {};
            }}

            QPushButton:hover {{
                background-color: {};
            }}

            QPushButton:pressed {{
                background-color: {};
            }}
        '''.format(color, hover, pressed))


class NormalPushButton(BasePushButton):
    '''Normal push button with gray color.'''

    def __init__(self, text, parent=None):
        super(NormalPushButton, self).__init__(text, parent)
        self.setBackground('rgb(240, 240, 240)',
                           'rgb(209, 209, 209)',
                           'rgb(187, 187, 187)')


class ImportantPushButton(BasePushButton):
    '''Important push button with blue color.'''

    def __init__(self, text, parent=None):
        super(ImportantPushButton, self).__init__(text, parent)
        self.setBackground('rgb(138, 186, 224)',
                           'rgb(69, 153, 219)',
                           'rgb(0, 120, 215)')
