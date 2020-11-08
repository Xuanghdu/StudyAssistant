from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import (
    QCalendarWidget, QDateTimeEdit, QDoubleSpinBox, QLabel, QLCDNumber,
    QLineEdit, QMessageBox, QPushButton, QSpinBox, QTabWidget)


class CalendarWidget(QCalendarWidget):
    '''Basic calendar widget type.'''

    def __init__(self, parent=None):
        super(CalendarWidget, self).__init__(parent)
        self.setStyleSheet(self.styleSheet() + '''
            QCalendarWidget * {
                font-family: Verdana, Geneva, sans-serif;
                font-size: 10pt;
            }
        ''')


class DateTimeEdit (QDateTimeEdit):
    '''Basic date time edit type.'''

    def __init__(self, parent=None):
        super(DateTimeEdit, self).__init__(parent)
        self.setStyleSheet(self.styleSheet() + '''
            QDateTimeEdit {
                font-family: Verdana, Geneva, sans-serif;
                font-size: 10pt;
                padding: 0.3em;
                border-style: solid;
                border-width: 1px;
                border-color: rgb(206, 206, 206);
                border-radius: 8px;
            }

            QDateTimeEdit:hover {
                border-width: 2px;
            }

            QDateTimeEdit:focus {
                border-width: 2px;
                border-color: rgb(138, 186, 224);
            }
        ''')


class DoubleSpinBox(QDoubleSpinBox):
    '''Basic spin box type.'''

    def __init__(self, parent=None):
        super(DoubleSpinBox, self).__init__(parent)
        self.setSingleStep(0.05)

        self.setStyleSheet(self.styleSheet() + '''
            QDoubleSpinBox {
                font-family: Verdana, Geneva, sans-serif;
                font-size: 10pt;
                padding: 0.3em;
                border-style: solid;
                border-width: 1px;
                border-color: rgb(206, 206, 206);
                border-radius: 8px;
            }

            QDoubleSpinBox:hover {
                border-width: 2px;
            }

            QDoubleSpinBox:focus {
                border-width: 2px;
                border-color: rgb(138, 186, 224);
            }
        ''')


class Label(QLabel):
    '''Basic label type.'''

    def __init__(self, text, parent=None):
        super(Label, self).__init__(text, parent)
        self.setStyleSheet(self.styleSheet() + '''
            QLabel {
                font-family: Verdana, Geneva, sans-serif;
                font-size: 10pt;
            }
        ''')


class LCDNumber(QLCDNumber):
    '''Basic LCD number type.'''

    def __init__(self, numDigits, parent=None):
        super(LCDNumber, self).__init__(numDigits, parent)
        self.setSegmentStyle(QLCDNumber.Flat)

        self.setStyleSheet(self.styleSheet() + '''
            QLCDNumber {
                min-height: 5em;
                min-width: 10em;
                background-color: rgb(247, 247, 247);
                border-style: solid;
                border-width: 1px;
                border-color: rgb(206, 206, 206);
                border-radius: 8px;
            }

            QLCDNumber:hover {
                border-width: 2px;
            }
        ''')


class LineEdit(QLineEdit):
    '''Basic line edit type.'''

    def __init__(self, parent=None):
        super(LineEdit, self).__init__(parent)
        self.setStyleSheet(self.styleSheet() + '''
            QLineEdit {
                font-family: Verdana, Geneva, sans-serif;
                font-size: 10pt;
                padding: 0.3em;
                border-style: solid;
                border-width: 1px;
                border-color: rgb(206, 206, 206);
                border-radius: 8px;
            }

            QLineEdit:hover {
                border-width: 2px;
            }

            QLineEdit:focus {
                border-width: 2px;
                border-color: rgb(138, 186, 224);
            }
        ''')


class MessageBox(QMessageBox):
    '''Basic message box type without specifying an icon.'''

    def __init__(self, icon, title, text, buttons, parent=None):
        super(MessageBox, self).__init__(icon, title, text, buttons, parent)
        self.setStyleSheet(self.styleSheet() + '''
            QMessageBox {
                font-family: Verdana, Geneva, sans-serif;
                font-size: 10pt;
            }

            QMessageBox QPushButton {
                font-family: Verdana, Geneva, sans-serif;
                border: none;
                font-size: 10pt;
                min-width: 5em;
                height: 2em;
                border-radius: 8px;
            }

            QMessageBox QPushButton {
                background-color: rgb(138, 186, 224);
            }

            QMessageBox QPushButton:hover {
                background-color: rgb(69, 153, 219);
            }

            QMessageBox QPushButton:pressed {
                background-color: rgb(0, 120, 215);
            }
        ''')


class WarningBox(MessageBox):
    '''Warning message box type.'''

    def __init__(self, title, text, parent=None):
        super(WarningBox, self).__init__(
            WarningBox.Warning, title, text, WarningBox.Ok)

        self.setWindowIcon(QIcon(self.iconPixmap()))


class PushButton(QPushButton):
    '''Basic button type without coloring.'''

    def __init__(self, text, parent=None):
        super(PushButton, self).__init__(text, parent)
        self.setStyleSheet(self.styleSheet() + '''
            QPushButton {
                font-family: Verdana, Geneva, sans-serif;
                border: none;
                font-size: 10pt;
                min-width: 5em;
                height: 2em;
                border-radius: 8px;
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


class NormalPushButton(PushButton):
    '''Normal push button with gray color.'''

    def __init__(self, text, parent=None):
        super(NormalPushButton, self).__init__(text, parent)
        self.setBackground('rgb(240, 240, 240)',
                           'rgb(209, 209, 209)',
                           'rgb(187, 187, 187)')


class ImportantPushButton(PushButton):
    '''Important push button with blue color.'''

    def __init__(self, text, parent=None):
        super(ImportantPushButton, self).__init__(text, parent)
        self.setBackground('rgb(138, 186, 224)',
                           'rgb(69, 153, 219)',
                           'rgb(0, 120, 215)')


class SpinBox(QSpinBox):
    '''Basic spin box type.'''

    def __init__(self, parent=None):
        super(SpinBox, self).__init__(parent)
        self.setStyleSheet(self.styleSheet() + '''
            QSpinBox {
                font-family: Verdana, Geneva, sans-serif;
                font-size: 10pt;
                padding: 0.3em;
                border-style: solid;
                border-width: 1px;
                border-color: rgb(206, 206, 206);
                border-radius: 8px;
            }

            QSpinBox:hover {
                border-width: 2px;
            }

            QSpinBox:focus {
                border-width: 2px;
                border-color: rgb(138, 186, 224);
            }
        ''')


class TabWidget(QTabWidget):

    def __init__(self, parent=None):
        super(TabWidget, self).__init__(parent)
        self.setStyleSheet(self.styleSheet() + '''
            QTabWidget {
                background: transparent;
            }

            QTabBar::tab {
                font-family: Verdana, Geneva, sans-serif;
                border: none;
                font-size: 10pt;
                width: 8em;
                height: 2em;
                border-top-left-radius: 8px;
                border-top-right-radius: 8px;
            }

            QTabBar::tab:selected {
                border-style: solid;
            }
        ''')

        self.setBackground('rgb(206, 206, 206)',
                           'rgb(219, 219, 219)',
                           'rgb(247, 247, 247)')

    def setForeground(self, color):
        '''Set foreground color (i.e. text color).'''

        self.setStyleSheet(self.styleSheet() + '''
            QTabBar::tab {
                color: {}
            }
        '''.format(color))

    def setBackground(self, color, hover, selected):
        '''Set background colors at normal time, when hovered, and when 
        selected.'''

        self.setStyleSheet(self.styleSheet() + '''
            QTabBar::tab {{
                background-color: {}
            }}

            QTabBar::tab:hover {{
                background-color: {}
            }}

            QTabBar::tab:selected {{
                background-color: {}
            }}
        '''.format(color, hover, selected))
