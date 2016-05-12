# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt/JanelaAgenda.ui'
#
# Created: Fri Oct 23 10:33:30 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_JanelaAgenda(object):
    def setupUi(self, JanelaAgenda):
        JanelaAgenda.setObjectName("JanelaAgenda")
        JanelaAgenda.resize(912, 515)
        self.tbAgenda = QtGui.QTableWidget(JanelaAgenda)
        self.tbAgenda.setGeometry(QtCore.QRect(160, 20, 711, 481))
        self.tbAgenda.setStyleSheet("""QTableWidget{
border:9px;
background-color: rgb(234, 255, 213);
gridline-color: rgb(165, 202, 130);

}""")
        self.tbAgenda.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tbAgenda.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tbAgenda.setRowCount(15)
        self.tbAgenda.setObjectName("tbAgenda")
        self.tbAgenda.setColumnCount(3)
        item = QtGui.QTableWidgetItem()
        self.tbAgenda.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbAgenda.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tbAgenda.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tbAgenda.setHorizontalHeaderItem(2, item)
        self.tbAgenda.horizontalHeader().setVisible(True)
        self.tbAgenda.horizontalHeader().setStretchLastSection(True)
        self.tbAgenda.verticalHeader().setVisible(False)
        self.tbAgenda.verticalHeader().setStretchLastSection(False)
        self.btAdicionar = QtGui.QPushButton(JanelaAgenda)
        self.btAdicionar.setGeometry(QtCore.QRect(10, 160, 92, 28))
        self.btAdicionar.setObjectName("btAdicionar")
        self.btModificar = QtGui.QPushButton(JanelaAgenda)
        self.btModificar.setGeometry(QtCore.QRect(10, 200, 92, 28))
        self.btModificar.setObjectName("btModificar")
        self.btRemover = QtGui.QPushButton(JanelaAgenda)
        self.btRemover.setGeometry(QtCore.QRect(10, 240, 92, 28))
        self.btRemover.setObjectName("btRemover")

        self.retranslateUi(JanelaAgenda)
        QtCore.QObject.connect(self.btAdicionar, QtCore.SIGNAL("clicked()"), JanelaAgenda.adicionar)
        QtCore.QObject.connect(self.btRemover, QtCore.SIGNAL("clicked()"), JanelaAgenda.remover)
        QtCore.QObject.connect(self.btModificar, QtCore.SIGNAL("clicked()"), JanelaAgenda.modificar)
        QtCore.QMetaObject.connectSlotsByName(JanelaAgenda)

    def retranslateUi(self, JanelaAgenda):
        JanelaAgenda.setWindowTitle(QtGui.QApplication.translate("JanelaAgenda", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.tbAgenda.verticalHeaderItem(0).setText(QtGui.QApplication.translate("JanelaAgenda", "as", None, QtGui.QApplication.UnicodeUTF8))
        self.tbAgenda.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("JanelaAgenda", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.tbAgenda.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("JanelaAgenda", "Calorias", None, QtGui.QApplication.UnicodeUTF8))
        self.tbAgenda.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("JanelaAgenda", "Comentarios", None, QtGui.QApplication.UnicodeUTF8))
        self.btAdicionar.setText(QtGui.QApplication.translate("JanelaAgenda", "Adicionar", None, QtGui.QApplication.UnicodeUTF8))
        self.btModificar.setText(QtGui.QApplication.translate("JanelaAgenda", "Modificar", None, QtGui.QApplication.UnicodeUTF8))
        self.btRemover.setText(QtGui.QApplication.translate("JanelaAgenda", "Remover", None, QtGui.QApplication.UnicodeUTF8))

