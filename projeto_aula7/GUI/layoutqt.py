from PyQt5.QtWidgets import *

app = QApplication([])

def botao_clicado():
    alert = QMessageBox()
    alert.setText('Você clicou o botão acima')
    alert.exec()

btAcima = QPushButton('Acima')
btAcima.clicked.connect(botao_clicado)

layout = QHBoxLayout()
layout.addWidget(QLabel('Clique no botão'))
layout.addWidget(btAcima)
layout.addWidget(QPushButton('Abaixo'))

window = QWidget()
window.setLayout(layout)
window.show()

app.exec()