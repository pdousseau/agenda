# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt/JanelaAdicionar.ui'
#
# Created: Thu Oct 22 15:49:36 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_JanelaAdicionar(object):
    def setupUi(self, JanelaAdicionar):
        JanelaAdicionar.setObjectName("JanelaAdicionar")
        JanelaAdicionar.resize(911, 518)
        self.cxPeso = QtGui.QLineEdit(JanelaAdicionar)
        self.cxPeso.setGeometry(QtCore.QRect(87, 266, 61, 26))
        self.cxPeso.setObjectName("cxPeso")
        self.cxAnotacoes = QtGui.QTextEdit(JanelaAdicionar)
        self.cxAnotacoes.setGeometry(QtCore.QRect(10, 340, 291, 161))
        self.cxAnotacoes.setObjectName("cxAnotacoes")
        self.calendario = QtGui.QCalendarWidget(JanelaAdicionar)
        self.calendario.setGeometry(QtCore.QRect(10, 60, 288, 171))
        self.calendario.setObjectName("calendario")
        self.label = QtGui.QLabel(JanelaAdicionar)
        self.label.setGeometry(QtCore.QRect(10, 270, 81, 18))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(JanelaAdicionar)
        self.label_2.setGeometry(QtCore.QRect(10, 319, 221, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(JanelaAdicionar)
        self.label_3.setGeometry(QtCore.QRect(150, 270, 21, 18))
        self.label_3.setObjectName("label_3")
        self.listaRefeicao = QtGui.QListWidget(JanelaAdicionar)
        self.listaRefeicao.setGeometry(QtCore.QRect(315, 20, 271, 321))
        self.listaRefeicao.setObjectName("listaRefeicao")
        self.listaAlimentos = QtGui.QListWidget(JanelaAdicionar)
        self.listaAlimentos.setGeometry(QtCore.QRect(620, 20, 261, 461))
        self.listaAlimentos.setObjectName("listaAlimentos")
        self.label_4 = QtGui.QLabel(JanelaAdicionar)
        self.label_4.setGeometry(QtCore.QRect(10, 10, 241, 31))
        self.label_4.setPixmap(QtGui.QPixmap("../../../../Desktop/refeicao.png"))
        self.label_4.setObjectName("label_4")
        
#        self.label_5 = QtGui.QLabel(JanelaAdicionar)
#        self.label_5.setGeometry(QtCore.QRect(-10, 140, 931, 521))
#        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
#        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtGui.QLabel(JanelaAdicionar)
        self.label_6.setGeometry(QtCore.QRect(590, 160, 31, 31))
        self.label_6.setPixmap(QtGui.QPixmap("../../../../Desktop/seta2.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(JanelaAdicionar)
        self.label_7.setGeometry(QtCore.QRect(300, 320, 311, 201))
        self.label_7.setPixmap(QtGui.QPixmap("../../../../Desktop/fundo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.btSalvar = QtGui.QPushButton(JanelaAdicionar)
        self.btSalvar.setGeometry(QtCore.QRect(640, 490, 92, 28))
        self.btSalvar.setObjectName("btSalvar")

        self.retranslateUi(JanelaAdicionar)
        QtCore.QObject.connect(self.listaRefeicao, QtCore.SIGNAL("doubleClicked(QModelIndex)"), JanelaAdicionar.removerAlimento)
        QtCore.QObject.connect(self.listaAlimentos, QtCore.SIGNAL("doubleClicked(QModelIndex)"), JanelaAdicionar.adicionarAlimento)
        QtCore.QObject.connect(self.btSalvar, QtCore.SIGNAL("clicked()"), JanelaAdicionar.salvar)
        QtCore.QMetaObject.connectSlotsByName(JanelaAdicionar)

    def retranslateUi(self, JanelaAdicionar):
        JanelaAdicionar.setWindowTitle(QtGui.QApplication.translate("JanelaAdicionar", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("JanelaAdicionar", "Peso Atual", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("JanelaAdicionar", "Digite aqui qualquer anotacao", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("JanelaAdicionar", "Kg", None, QtGui.QApplication.UnicodeUTF8))
        self.btSalvar.setText(QtGui.QApplication.translate("JanelaAdicionar", "Salvar", None, QtGui.QApplication.UnicodeUTF8))

