from TaskViewer import TaskViewer

from PyQt5.QtWidgets import (
    QApplication, QCalendarWidget, QGridLayout, QWidget)


class DayTab(QWidget):
    '''"Day" tab of the program main window.'''

    def __init__(self, parent=None):
        super(DayTab, self).__init__(parent)

        layout = QGridLayout()

        # TODO: create a custom schedule display
        self.schedule = QCalendarWidget()
        layout.addWidget(self.schedule, 0, 0)

        self.taskViewer = TaskViewer()
        layout.addWidget(self.taskViewer, 0, 1)

        self.setLayout(layout)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    adder = DayTab()
    adder.show()
    app.exec_()
