import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtSql import *
import sys


class MyWindow(QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('not_coffee.sqlite')
        db.open()

        view = self.tableView
        model = QSqlTableModel(self, db)
        model.setTable('coffee_table')
        model.select()

        view.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
