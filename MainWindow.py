from CustomControl import TabWidget

from DayTab import DayTab

from GlobalData import *

from MonthTab import MonthTab

from NewTaskTab import NewTaskTab

from datetime import datetime

from PyQt5.QtCore import QLocale, QTimer

from PyQt5.QtGui import QIcon, QStandardItem, QStandardItemModel

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

        self.newTaskTab.addButton.clicked.connect(
            lambda: self.onAddButtonClicked())

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

    def onAddButtonClicked(self):
        self.refreshCounter = MainWindow.REFRESH_COUNT - 1

    def updateUpcomingTasksDisplay(self, forceRefresh):
        '''Update the upcoming tasks display. If `forceRefresh` is true,
        `updateUpcomingTasks` function is guaranteed to be rerun.'''

        now = datetime.now()
        if forceRefresh or len(upcomingTasks) == 0 or \
                now >= upcomingTasks[0][1]:
            updateUpcomingTasks(now)

        rows = len(upcomingTasks)
        model = QStandardItemModel(rows, 4)
        model.setHorizontalHeaderLabels(['Name', 'Start', 'End', 'Deadline'])

        def sft(time): return time.strftime('%m/%d/%Y, %H:%M')

        for row in range(rows):
            name, startTime, endTime, deadline = upcomingTasks[row]
            model.setItem(row, 0, QStandardItem(name))
            model.setItem(row, 1, QStandardItem(sft(startTime)))
            model.setItem(row, 2, QStandardItem(sft(endTime)))
            if deadline is not None:
                model.setItem(row, 3, QStandardItem(sft(deadline)))

        tableView = self.monthTab.taskViewer.tableView
        tableView.setModel(model)
        tableView.resizeColumnsToContents()

        tableView = self.dayTab.taskViewer.tableView
        tableView.setModel(model)
        tableView.resizeColumnsToContents()

        if len(upcomingTasks) > 0:
            delta = upcomingTasks[0][1] - now
            if delta.days < 3:
                hour = delta.days * 24 + delta.seconds // 3600
                minute = delta.seconds // 60 % 60
            else:
                hour = 99
                minute = 99
        else:
            hour = 99
            minute = 99

        self.monthTab.taskViewer.displayCountDown(hour, minute)
        self.dayTab.taskViewer.displayCountDown(hour, minute)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    adder = MainWindow()
    adder.show()
    app.exec_()
