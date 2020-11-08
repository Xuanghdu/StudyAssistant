from CustomControl import (
    DateTimeEdit, DoubleSpinBox, ImportantPushButton, Label, LineEdit,
    NormalPushButton, SpinBox, TabWidget, WarningBox)

from PyQt5.QtCore import QDateTime

from PyQt5.QtWidgets import QApplication, QGridLayout, QWidget


class NewTaskTab(TabWidget):
    '''"New Task" tab of the program main window.'''

    TASK_DURATION_MAX = 10000
    '''Maximum duration of a task in minutes.'''

    def __init__(self, parent=None):
        super(NewTaskTab, self).__init__(parent)

        layout = QGridLayout()
        layout.addWidget(Label('Task name:'), 0, 0)
        layout.addWidget(Label('Duration:'), 1, 0)
        layout.addWidget(Label('min'), 1, 3)

        self.nameInput = LineEdit()
        layout.addWidget(self.nameInput, 0, 1, 1, 3)

        self.durationInput = SpinBox()
        self.durationInput.setRange(1, NewTaskTab.TASK_DURATION_MAX)
        layout.addWidget(self.durationInput, 1, 1, 1, 2)

        self.editorTabs = self.createEditorTabs()
        layout.addWidget(self.editorTabs, 2, 0, 1, 4)

        self.addButton = ImportantPushButton('Add')
        self.addButton.clicked.connect(lambda: self.onAddClicked())
        layout.addWidget(self.addButton, 3, 2)

        self.cancelButton = NormalPushButton('Cancel')
        self.cancelButton.clicked.connect(lambda: self.onCancelClicked())
        layout.addWidget(self.cancelButton, 3, 3)

        self.setLayout(layout)
        self.resetInputs()

    def resetInputs(self):
        '''Reset the values of inputs and restore the tab status.'''

        self.editorTabs.setCurrentIndex(0)
        self.nameInput.setText('')
        self.durationInput.setValue(1)
        self.weightInput.setValue(0.5)
        currentDateTime = QDateTime.currentDateTime()
        self.deadlineInput.setDateTime(currentDateTime)
        self.deadlineInput.setMinimumDateTime(currentDateTime)
        self.startFromInput.setDateTime(currentDateTime)
        self.startFromInput.setMinimumDateTime(currentDateTime)

    def onAddClicked(self):
        '''Action when the "Add" button is clicked.'''

        taskName = self.nameInput.text().strip()
        if len(taskName) == 0:
            WarningBox('No Task Name', 'Task name cannot be empty!').exec()
            return

        currentIndex = self.editorTabs.currentIndex()
        if currentIndex == 0:
            self.onAddClickedScheduleForme()
        elif currentIndex == 1:
            self.onAddClickedLetMeDecide()
        else:
            WarningBox('Unknown error',
                       'Cannot find the corresponding tab!').exec()
            return

        self.resetInputs()

    def onAddClickedScheduleForme(self):
        '''Action when the "Add" button is clicked and the "Schedule for Me" tab
        is selected.'''

        pass

    def onAddClickedLetMeDecide(self):
        '''Action when the "Add" button is clicked and the "Schedule for Me" tab
        is selected.'''

        pass

    def onCancelClicked(self):
        self.resetInputs()

    def createEditorTabs(self):
        '''Create and return a tab widget containing two types of task
        editors.'''

        widget = TabWidget()
        widget.addTab(self.createScheduleForMe(), 'Schedule for Me')
        widget.addTab(self.createLetMeDecide(), 'Let Me Decide')
        return widget

    def createScheduleForMe(self):
        '''Create and return the "Schedule for me" tab.'''

        layout = QGridLayout()
        layout.addWidget(Label('Weight:'), 0, 0)
        layout.addWidget(Label('Deadline:'), 1, 0)

        self.weightInput = DoubleSpinBox()
        self.weightInput.setRange(0.0, 1.0)
        layout.addWidget(self.weightInput, 0, 1)

        self.deadlineInput = DateTimeEdit()
        layout.addWidget(self.deadlineInput, 1, 1)

        widget = QWidget()
        widget.setLayout(layout)
        return widget

    def createLetMeDecide(self):
        '''Create and return the "Let me decide" tab.'''

        layout = QGridLayout()
        layout.addWidget(Label('Start from:'), 0, 0)

        self.startFromInput = DateTimeEdit()
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
