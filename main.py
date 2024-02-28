import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLineEdit, QListWidget, QMessageBox

class ToDoListApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.task_input = QLineEdit(self)
        self.task_input.setPlaceholderText('Enter a new task...')
        layout.addWidget(self.task_input)

        add_task_btn = QPushButton('Add Task', self)
        add_task_btn.clicked.connect(self.add_task)
        layout.addWidget(add_task_btn)

        self.tasks_list = QListWidget(self)
        layout.addWidget(self.tasks_list)

        delete_task_btn = QPushButton('Delete Selected Task', self)
        delete_task_btn.clicked.connect(self.delete_task)
        layout.addWidget(delete_task_btn)

        self.setLayout(layout)
        self.setWindowTitle('To-Do List with PyQt')
        self.setGeometry(300, 300, 300, 200)  # x, y, width, height
        self.show()

    def add_task(self):
        task = self.task_input.text()
        if task:
            self.tasks_list.addItem(task)
            self.task_input.clear()
        else:
            QMessageBox.information(self, 'Empty Task', 'Please enter a task.')

    def delete_task(self):
        list_items = self.tasks_list.selectedItems()
        if not list_items: return
        for item in list_items:
            self.tasks_list.takeItem(self.tasks_list.row(item))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ToDoListApp()
    sys.exit(app.exec_())
