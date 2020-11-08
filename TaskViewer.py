from CustomControl import Label, LCDNumber

from PyQt5.QtGui import QStandardItemModel

from PyQt5.QtWidgets import QApplication, QGridLayout, QTableView, QWidget


class TaskViewer(QWidget):
    '''Widget which diplays a countdown to the next deadline and the upcoming
    tasks.'''

    def __init__(self, parent=None):
        super(TaskViewer, self).__init__(parent)

        layout = QGridLayout()
        layout.addWidget(self.createCountDown(), 0, 0)
        layout.addWidget(self.createUpcomingTasks(), 1, 0)

        self.setLayout(layout)

    def displayCountDown(self, hour, minute):
        '''Display the hour and minute on the LCD displays. The hour and minute
        have two digits each. Extra digits are filled with zeros.'''

        assert hour >= 0 and hour < 100 and minute >= 0 and minute < 100
        self.countDownHour.display('{:02d}'.format(hour))
        self.countDownMinute.display('{:02d}'.format(minute))

    def createCountDown(self):
        '''Create and return a widget containing a countdown to the next
        deadline.'''

        layout = QGridLayout()
        layout.addWidget(Label('Next deadline comes in:'), 0, 0, 1, 4)
        layout.addWidget(Label('hr'), 1, 1)
        layout.addWidget(Label('min'), 1, 3)

        self.countDownHour = LCDNumber(2)
        layout.addWidget(self.countDownHour, 1, 0)

        self.countDownMinute = LCDNumber(2)
        layout.addWidget(self.countDownMinute, 1, 2)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def createUpcomingTasks(self):
        '''Create and return a table countaining the basic information of the
        upcoming tasks.'''

        layout = QGridLayout()
        layout.addWidget(Label('Upcoming tasks:'), 0, 0)

        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Name', 'Start', 'End'])

        self.tableView = QTableView()
        self.tableView.setModel(model)
        layout.addWidget(self.tableView, 1, 0)

        self.tableView.setStyleSheet(self.tableView.styleSheet() + '''
            QTableView * {
                font-family: Verdana, Geneva, sans-serif;
                font-size: 10pt;
            }
        ''')

        widget = QWidget()
        widget.setLayout(layout)
        return widget


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    viewer = TaskViewer()
    viewer.show()
    app.exec_()
