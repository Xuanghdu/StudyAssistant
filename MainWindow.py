from CustomControl import TabWidget

from DayTab import DayTab

from GlobalData import *

from MonthTab import MonthTab

from NewTaskTab import NewTaskTab

from datetime import datetime

from PyQt5.QtCore import QLocale, QTimer

from PyQt5.QtGui import QIcon

from PyQt5.QtWidgets import QApplication, QMainWindow


class MainWindow(QMainWindow):
    '''The program main window.'''

    UPDATE_INTERVAL = 1000
    '''Interval between calls of `updateUpcomingTasksDisplay` in seconds.'''

    REFRESH_COUNT = 60
    '''Force a data refresh every REFRESH_COUNT intervals.'''

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

        self.timer = QTimer()
        self.timer.setInterval(MainWindow.UPDATE_INTERVAL)
        self.refreshCounter = 0
        self.timer.timeout.connect(lambda: self.onTimerTimeOut())
        self.updateUpcomingTasksDisplay(True)
        self.timer.start()

    def onTimerTimeOut(self):
        self.refreshCounter += 1
        if self.refreshCounter >= MainWindow.REFRESH_COUNT:
            self.updateUpcomingTasksDisplay(True)
            self.refreshCounter = 0
        else:
            self.updateUpcomingTasksDisplay(False)

    def updateUpcomingTasksDisplay(self, forceRefresh):
        '''Update the upcoming tasks display. If `forceRefresh` is true,
        `updateUpcomingTasks` function is guaranteed to be rerun.'''

        now = datetime.now()
        if forceRefresh or \
                len(upcomingTasks) > 0 and now >= upcomingTasks[0][1]:
            updateUpcomingTasks(now)
        # TODO: Update display of its children


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    adder = MainWindow()
    adder.show()
    app.exec_()
