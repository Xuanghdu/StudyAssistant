from CustomControl import TabWidget

from DayTab import DayTab

from MonthTab import MonthTab

from NewTaskTab import NewTaskTab

from PyQt5.QtCore import QLocale

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    '''The program main window.'''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setLocale(QLocale(QLocale.English))
        self.setWindowTitle('Study Assistant')
        self.setWindowIcon(QIcon('calendar-icon.png'))

        self.monthTab = MonthTab()
        self.dayTab = DayTab()
        self.newTaskTab = NewTaskTab()

        centralWidget = TabWidget()
        centralWidget.addTab(self.monthTab, 'Month')
        centralWidget.addTab(self.dayTab, 'Day')
        centralWidget.addTab(self.newTaskTab, 'New Task')

        self.setCentralWidget(centralWidget)

        self.setStyleSheet(self.styleSheet() + '''
            MainWindow {
                background-color: rgb(206, 206, 206);
            }
        ''')


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    adder = MainWindow()
    adder.show()
    app.exec_()
