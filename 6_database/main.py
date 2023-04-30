import os
import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel, QSqlRelationalTableModel, QSqlRelation, \
    QSqlRelationalDelegate
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QFileDialog

from main_window import UiMainWindow


class MyWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UiMainWindow()
        self.ui.setup_ui(self)
        self.ui.translate_ui(self)
        self.db_path = r'database.sqlite3'
        self.ui.path_db.setText(self.db_path)

        self.save_db = QAction(QIcon(os.path.join('icons', 'save.png')), 'Save', self)
        self.open_db_file = QAction(QIcon(os.path.join('icons', 'open-db.png')), 'Open', self)
        self.add_row = QAction(QIcon(os.path.join('icons', 'add.png')), 'Add row', self)
        self.del_row = QAction(QIcon(os.path.join('icons', 'del.png')), ' Del row', self)
        self.ui.toolBar.addAction(self.save_db)
        self.ui.toolBar.addAction(self.open_db_file)
        self.ui.toolBar.addAction(self.add_row)
        self.ui.toolBar.addAction(self.del_row)
        self.db = None
        self.table_model = None

        self.open_db()

        self.add_row.triggered.connect(self.add_row_action)
        self.del_row.triggered.connect(self.del_row_action)
        self.save_db.triggered.connect(self.save_change_db)
        self.open_db_file.triggered.connect(self.open_db_file_action)
        self.ui.comboBox.currentIndexChanged.connect(self.show_table)

    def open_db(self):
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName(self.db_path)
        self.db.open()
        self.get_tables_name()
        self.show_table()

    def get_tables_name(self):
        self.ui.comboBox.clear()
        for table_name in self.db.tables():
            self.ui.comboBox.addItem(table_name)

    def show_table(self):
        self.table_model = QSqlRelationalTableModel()
        table = self.ui.comboBox.currentText()
        if table == 'goods':
            self.create_goods_table_model()
        elif table == 'employees':
            self.create_employees_table_model()
        else:
            self.table_model.setTable(table)
            self.table_model.select()
        self.table_model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        view = self.ui.tableView
        view.setModel(self.table_model)
        view.setItemDelegate(QSqlRelationalDelegate(view))

    def create_goods_table_model(self):
        self.table_model.setTable('goods')
        self.table_model.setRelation(2, QSqlRelation('units', 'id', 'unit'))
        self.table_model.setRelation(3, QSqlRelation('categories', 'id', 'name'))
        self.table_model.select()

    def create_employees_table_model(self):
        self.table_model.setTable('employees')
        self.table_model.setRelation(2, QSqlRelation('positions', 'id', 'name'))
        self.table_model.select()

    def add_row_action(self):
        self.table_model.insertRows(self.table_model.rowCount(), 1)

    def del_row_action(self):
        selected_rows = list(map(lambda x: x.row(), self.ui.tableView.selectedIndexes()))
        print(selected_rows)
        for i in selected_rows:
            self.table_model.removeRows(i, 1)

    def open_db_file_action(self):
        self.db_path = QFileDialog.getOpenFileName(self, "Open file")[0]
        self.ui.path_db.setText(self.db_path)
        self.db.close()
        self.open_db()

    def save_change_db(self):
        if self.table_model.submitAll():
            self.ui.statusbar.showMessage('Изменения сохранены')
        else:
            self.ui.statusbar.showMessage(f'{self.table_model.lastError().text()}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = MyWindow()
    wnd.show()
    sys.exit(app.exec())
