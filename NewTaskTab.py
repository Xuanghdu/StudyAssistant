from CustomControl import ImportantPushButton, NormalPushButton

from PyQt5.QtCore import QDateTime

from PyQt5.QtWidgets import (
    QApplication, QDateTimeEdit, QDoubleSpinBox, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSpinBox, QTabWidget, QWidget)


class NewTaskTab(QTabWidget):
    '''"New Task" tab of the program main window.'''

    TASK_DURATION_MAX = 10000
    '''Maximum duration of a task in minutes.'''

    def __init__(self, parent=None):
        super(NewTaskTab, self).__init__(parent)

        layout = QGridLayout()
        layout.addWidget(QLabel('Task name:'), 0, 0)
        layout.addWidget(QLabel('Duration:'), 1, 0)
        layout.addWidget(QLabel('min'), 1, 3)

        self.nameInput = QLineEdit()
        layout.addWidget(self.nameInput, 0, 1, 1, 3)

        self.durationInput = QSpinBox()
        self.durationInput.setRange(1, NewTaskTab.TASK_DURATION_MAX)
        layout.addWidget(self.durationInput, 1, 1, 1, 2)

        layout.addWidget(self.createEditorTabs(), 2, 0, 1, 4)

        self.addButton = ImportantPushButton('Add')
        layout.addWidget(self.addButton, 3, 2)

        self.cancelButton = NormalPushButton('Cancel')
        layout.addWidget(self.cancelButton, 3, 3)

        self.setLayout(layout)

    def createEditorTabs(self):
        '''Create and return a tab widget containing two types of task
        editors.'''

        widget = QTabWidget()
        widget.addTab(self.createScheduleForMe(), 'Schedule for Me')
        widget.addTab(self.createLetMeDecide(), 'Let Me Decide')
        return widget

    def createScheduleForMe(self):
        '''Create and return the "Schedule for me" tab.'''

        layout = QGridLayout()
        layout.addWidget(QLabel('Weight:'), 0, 0)
        layout.addWidget(QLabel('Deadline:'), 1, 0)

        self.weightInput = QDoubleSpinBox()
        self.weightInput.setRange(0.0, 1.0)
        layout.addWidget(self.weightInput, 0, 1)

        self.deadlineInput = QDateTimeEdit()
        self.deadlineInput.setMinimumDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.deadlineInput, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def createLetMeDecide(self):
        '''Create and return the "Let me decide" tab.'''

        layout = QGridLayout()
        layout.addWidget(QLabel('Start from:'), 0, 0)

        self.startFromInput = QDateTimeEdit()
        self.startFromInput.setMinimumDateTime(QDateTime.currentDateTime())
        layout.addWidget(self.startFromInput, 0, 1)

        widget = QWidget()
        widget.setLayout(layout)
        return widget


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    adder = NewTaskTab()
    adder.show()
    app.exec_()
