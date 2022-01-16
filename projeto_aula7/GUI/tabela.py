#interface gráfica usando PyQt
#localizar o python
#..Python\Pythonxx\Scripts> pip install pyqt5
#github.com/pyqt/examples

#biblioteca do sistema operacional
from os.path import exists
from PyQt5.QtWidgets import *
from PyQt5.QtSql import *
import sys

if not exists('bancodedados.db'):
    print('banco de dados não encontrado!')
    sys.exit()

app = QApplication([])

db = QSqlDatabase.addDatabase(('QSQLITE'))
db.setDatabaseName(('bancodedados.db'))
db.open()

model = QSqlTableModel(None, db)
model.setTable('contato')
model.select()

view = QTableView()
view.setModel(model)
view.show()

app.exec_()


