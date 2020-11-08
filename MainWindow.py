from DayTab import DayTab

from MonthTab import MonthTab

from NewTaskTab import NewTaskTab

from PyQt5.QtWidgets import (QApplication, QMainWindow, QTabWidget)


class MainWindow(QMainWindow):
    '''The program main window.'''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        self.monthTab = MonthTab()
        self.dayTab = DayTab()
        self.newTaskTab = NewTaskTab()

        centralWidget = QTabWidget()
        centralWidget.addTab(self.monthTab, 'Month')
        centralWidget.addTab(self.dayTab, 'Day')
        centralWidget.addTab(self.newTaskTab, 'New Task')

        self.setCentralWidget(centralWidget)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    adder = MainWindow()
    adder.show()
    app.exec_()
