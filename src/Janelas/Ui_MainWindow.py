# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt/MainWindow.ui'
#
# Created: Thu Oct 22 14:27:35 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from Global import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1098, 660)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(-1, -5, 1121, 671))
        self.label.setPixmap(QtGui.QPixmap(MY_DIR_IMG + "fundoF.png"))
        self.label.setObjectName("label")
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(850, 10, 71, 81))
        self.label_2.setPixmap(QtGui.QPixmap(MY_DIR_IMG + "config.png"))
        self.label_2.setObjectName("label_2")
        self.lblconfiguracoes = QtGui.QLabel(self.centralwidget)
        self.lblconfiguracoes.setGeometry(QtCore.QRect(930, 40, 141, 18))
        self.lblconfiguracoes.setCursor(QtCore.Qt.PointingHandCursor)
        self.lblconfiguracoes.setPixmap(QtGui.QPixmap(MY_DIR_IMG + "conf.png"))
        self.lblconfiguracoes.setObjectName("lblconfiguracoes")
        self.lbllistaAlimentos = QtGui.QLabel(self.centralwidget)
        self.lbllistaAlimentos.setGeometry(QtCore.QRect(390, 25, 171, 51))
        self.lbllistaAlimentos.setCursor(QtCore.Qt.PointingHandCursor)
        self.lbllistaAlimentos.setPixmap(QtGui.QPixmap(MY_DIR_IMG + "listaalimentos.png"))
        self.lbllistaAlimentos.setObjectName("lbllistaAlimentos")
        self.btListaAlimentos = QtGui.QPushButton(self.centralwidget)
        self.btListaAlimentos.setGeometry(QtCore.QRect(380, 40, 161, 21))
        self.btListaAlimentos.setCursor(QtCore.Qt.PointingHandCursor)
        self.btListaAlimentos.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btListaAlimentos.setStyleSheet("""background-color:transparent;
border-radius:0px;""")
        self.btListaAlimentos.setObjectName("btListaAlimentos")
        self.btConfiguracoes = QtGui.QPushButton(self.centralwidget)
        self.btConfiguracoes.setGeometry(QtCore.QRect(930, 40, 131, 21))
        self.btConfiguracoes.setCursor(QtCore.Qt.PointingHandCursor)
        self.btConfiguracoes.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btConfiguracoes.setStyleSheet("""background-color:transparent;
border-radius:0px;""")
        self.btConfiguracoes.setObjectName("btConfiguracoes")
        
        
        self.formLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(140, 87, 921, 541))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        
        self.formLayout = QtGui.QVBoxLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        
        
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 10, 91, 71))
        self.label_5.setPixmap(QtGui.QPixmap(MY_DIR_IMG + "editar.png"))
        self.label_5.setObjectName("label_5")
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(80, 20, 71, 71))
        self.label_3.setPixmap(QtGui.QPixmap(MY_DIR_IMG + "agen.png"))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 40, 71, 18))
        self.label_4.setPixmap(QtGui.QPixmap(MY_DIR_IMG + "agenda.png"))
        self.label_4.setObjectName("label_4")
        self.btAgenda = QtGui.QPushButton(self.centralwidget)
        self.btAgenda.setGeometry(QtCore.QRect(150, 35, 92, 28))
        self.btAgenda.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btAgenda.setStyleSheet("""background-color:transparent;
border-radius:0px;""")
        self.btAgenda.setObjectName("btAgenda")
        
        
        
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(610, 20, 81, 51))
        self.label_6.setPixmap(QtGui.QPixmap(MY_DIR_IMG + "est.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(690, 40, 101, 18))
        self.label_7.setPixmap(QtGui.QPixmap(MY_DIR_IMG + "estat.png"))
        self.label_7.setObjectName("label_7")
        
        self.btEstatisticas = QtGui.QPushButton(self.centralwidget)
        self.btEstatisticas.setGeometry(QtCore.QRect(690, 32, 101, 28))
        self.btEstatisticas.setCursor(QtCore.Qt.PointingHandCursor)
        self.btEstatisticas.setFocusPolicy(QtCore.Qt.NoFocus)
        self.btEstatisticas.setStyleSheet("""border-radius:2px;
background-color:transparent;""")
        self.btEstatisticas.setObjectName("btEstatisticas")
        
        
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.btConfiguracoes, QtCore.SIGNAL("clicked()"), MainWindow.configuracoes)
        QtCore.QObject.connect(self.btListaAlimentos, QtCore.SIGNAL("clicked()"), MainWindow.listaAlimentos)
        QtCore.QObject.connect(self.btAgenda, QtCore.SIGNAL("clicked()"), MainWindow.agenda)
        QtCore.QObject.connect(self.btEstatisticas, QtCore.SIGNAL("clicked()"), MainWindow.estatisticas)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "Agenda de alimentos", None, QtGui.QApplication.UnicodeUTF8))
