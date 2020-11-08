from PyQt5.QtGui import QStandardItemModel

from PyQt5.QtWidgets import (
    QApplication, QGridLayout, QLabel, QLCDNumber, QTableView, QWidget)


class TaskViewer(QWidget):
    '''Widget which diplays a countdown to the next deadline and the following
    tasks.'''

    def __init__(self, parent=None):
        super(TaskViewer, self).__init__(parent)

        layout = QGridLayout()
        layout.addWidget(self.createCountDown(), 0, 0)
        layout.addWidget(self.createFollowingTasks(), 1, 0)

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
        layout.addWidget(QLabel('Next deadline comes in'), 0, 0, 1, 4)
        layout.addWidget(QLabel('hr'), 1, 1)
        layout.addWidget(QLabel('min'), 1, 3)

        self.countDownHour = QLCDNumber(2)
        layout.addWidget(self.countDownHour, 1, 0)

        self.countDownMinute = QLCDNumber(2)
        layout.addWidget(self.countDownMinute, 1, 2)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def createFollowingTasks(self):
        '''Create and return a table countaining the basic information of the
        following tasks.'''

        layout = QGridLayout()
        layout.addWidget(QLabel('Following tasks:'), 0, 0)

        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(
            ['Name', 'From', 'Duration', 'Weight'])

        self.tableView = QTableView()
        self.tableView.setModel(self.model)
        layout.addWidget(self.tableView, 1, 0)

        widget = QWidget()
        widget.setLayout(layout)
        return widget


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    viewer = TaskViewer()
    viewer.show()
    app.exec_()
