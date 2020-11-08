from TaskViewer import TaskViewer

from PyQt5.QtWidgets import (
    QApplication, QCalendarWidget, QGridLayout, QWidget)


class MonthTab(QWidget):
    '''"Month" tab of the program main window.'''

    def __init__(self, parent=None):
        super(MonthTab, self).__init__(parent)

        layout = QGridLayout()

        self.calender = QCalendarWidget()
        layout.addWidget(self.calender, 0, 0)

        self.taskViewer = TaskViewer()
        layout.addWidget(self.taskViewer, 0, 1)

        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    adder = MonthTab()
    adder.show()
    app.exec_()
