# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt/JanelaConfiguracoes.ui'
#
# Created: Thu Oct 22 15:26:50 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_JanelaConfiguracoes(object):
    def setupUi(self, JanelaConfiguracoes):
        JanelaConfiguracoes.setObjectName("JanelaConfiguracoes")
        JanelaConfiguracoes.resize(907, 518)
        self.label = QtGui.QLabel(JanelaConfiguracoes)
        self.label.setGeometry(QtCore.QRect(20, 30, 101, 18))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(JanelaConfiguracoes)
        self.label_2.setGeometry(QtCore.QRect(20, 70, 191, 18))
        self.label_2.setObjectName("label_2")
        self.cxPeso = QtGui.QLineEdit(JanelaConfiguracoes)
        self.cxPeso.setGeometry(QtCore.QRect(120, 25, 113, 26))
        self.cxPeso.setObjectName("cxPeso")
        self.cxCalorias = QtGui.QLineEdit(JanelaConfiguracoes)
        self.cxCalorias.setGeometry(QtCore.QRect(210, 66, 113, 26))
        self.cxCalorias.setObjectName("cxCalorias")
        self.btSalvar = QtGui.QPushButton(JanelaConfiguracoes)
        self.btSalvar.setGeometry(QtCore.QRect(110, 190, 92, 28))
        self.btSalvar.setObjectName("btSalvar")

        self.retranslateUi(JanelaConfiguracoes)
        QtCore.QObject.connect(self.btSalvar, QtCore.SIGNAL("clicked()"), JanelaConfiguracoes.salvar)
        QtCore.QMetaObject.connectSlotsByName(JanelaConfiguracoes)

    def retranslateUi(self, JanelaConfiguracoes):
        JanelaConfiguracoes.setWindowTitle(QtGui.QApplication.translate("JanelaConfiguracoes", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("JanelaConfiguracoes", "Peso desejado", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("JanelaConfiguracoes", "Calorias diarias necessarias", None, QtGui.QApplication.UnicodeUTF8))
        self.btSalvar.setText(QtGui.QApplication.translate("JanelaConfiguracoes", "Salvar", None, QtGui.QApplication.UnicodeUTF8))

