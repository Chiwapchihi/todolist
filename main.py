import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QTableView, QTableWidgetItem
from PySide6.QtGui import QStandardItemModel, QStandardItem

from todo import Ui_MainWindow

from connection import create_table, add_task, delete_task, get_task, update_task

def setup_connections(ui):
    ui.pushButton_4.clicked.connect(lambda: on_add_task(ui))
    ui.pushButton_5.clicked.connect(lambda: on_delete_task(ui))
    ui.pushButton_3.clicked.connect(lambda: on_update_task(ui))

def on_add_task(ui):
    task_text = ui.lineEdit.text()
    if task_text:
        add_task(task_text)
        ui.lineEdit.clear()
        load_tasks(ui)

def on_delete_task(ui):
    selected_items = ui.tableView.selectionModel().selectedRows()
    if selected_items:
        row = selected_items[0].row()
        task_id = int(ui.tableView.model().item(row, 0).text())
        delete_task(task_id)
        load_tasks(ui)

def on_update_task(ui):
    selected_items = ui.tableView.selectionModel().selectedRows()
    if selected_items:
        row = selected_items[0].row()
        task_id = int(ui.tableView.model().item(row, 0).text())
        current_status = ui.tableView.model().item(row, 2).text() == 'Да'
        new_status = 0 if current_status else 1
        update_task(task_id, new_status)
        load_tasks(ui)

def load_tasks(ui):
    tasks = get_task()
    model = QStandardItemModel(len(tasks), 3)
    model.setHorizontalHeaderLabels(['ID', 'Задача', 'Выполнена'])

    for row, task in enumerate(tasks):
        task_id, task_text, completed = task
        model.setItem(row, 0, QStandardItem(str(task_id)))
        model.setItem(row, 1, QStandardItem(task_text))
        model.setItem(row, 2, QStandardItem("Да" if completed else "Нет"))

    ui.tableView.setModel(model)

def main():
    app = QApplication(sys.argv)

    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    create_table()
    load_tasks(ui)

    setup_connections(ui)

    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
