from random import randint
from PyQt5 import uic, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem

import sys


class Bingo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.tela = uic.loadUi('tela.ui', self)
        self.tela.btSortear.clicked.connect(self.sortear_numero)
        self.tela.showEvent = self.on_show_event
        self.numeros_sorteados = []
        self.tabela = self.tela.tabela


    def on_show_event(self, event):
        self.popular_tabela()

    def sortear_numero(self):
        numeroSorteado = self.sortear_numero_unico()
        self.numeros_sorteados.append(numeroSorteado)
        self.tela.numeros.setText(f"{numeroSorteado}")
        self.marcar_numero(numeroSorteado)


    def marcar_numero(self, numeroSorteado):

        for i in range(self.tabela.rowCount()):
            for j in range(self.tabela.columnCount()):
                item = self.tabela.item(i, j)
                if item is not None and int(item.text()) == numeroSorteado:
                    item.setBackground(QtGui.QColor(255, 255, 0))
    def sortear_numero_unico(self):
        numero = randint(1, 75)
        while numero in self.numeros_sorteados:
            numero = randint(1, 75)
        return numero

    def popular_tabela(self):

        self.tabela.setColumnCount(5)
        self.tabela.setRowCount(15)
        for i in range(15):
            for j in range(5):
                numero = j * 15 + i + 1
                item = QTableWidgetItem(str(numero))
                self.tabela.setItem(i, j, item)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    bingo = Bingo()
    bingo.show()
    sys.exit(app.exec_())
