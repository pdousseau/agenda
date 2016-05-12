# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PyQt/JanelaEstatisticas.ui'
#
# Created: Fri Oct 23 13:24:33 2009
#      by: PyQt4 UI code generator 4.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_JanelaEstatisticas(object):
    def setupUi(self, JanelaEstatisticas):
        JanelaEstatisticas.setObjectName("JanelaEstatisticas")
        JanelaEstatisticas.resize(913, 513)
        
        
        self.formLayoutWidget = QtGui.QWidget(JanelaEstatisticas)
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayoutWidget.setGeometry(QtCore.QRect(350, 20, 541, 471))
        
        self.formLayout = QtGui.QVBoxLayout(self.formLayoutWidget)
        self.formLayout.setObjectName("formLayout")
        
        
        
        self.cbCalorias = QtGui.QCheckBox(JanelaEstatisticas)
        self.cbCalorias.setGeometry(QtCore.QRect(20, 50, 93, 23))
        self.cbCalorias.setObjectName("cbCalorias")
        self.cbPeso = QtGui.QCheckBox(JanelaEstatisticas)
        self.cbPeso.setGeometry(QtCore.QRect(20, 80, 93, 23))
        self.cbPeso.setObjectName("cbPeso")
        self.groupBox = QtGui.QGroupBox(JanelaEstatisticas)
        self.groupBox.setGeometry(QtCore.QRect(10, 190, 321, 311))
        self.groupBox.setStyleSheet("""QGroupBox {
    
     border: 1px solid gray;
     border-radius: 5px;
     margin-top: 1ex; /* leave space at the top for the title */
    background-color: rgb(230, 255, 213);
 }

 QGroupBox::title {
     subcontrol-origin: margin;
     subcontrol-position: top center; /* position at the top center */
     padding: 0 3px;
 }""")
        self.groupBox.setObjectName("groupBox")
        self.cbProteina = QtGui.QCheckBox(self.groupBox)
        self.cbProteina.setGeometry(QtCore.QRect(20, 20, 93, 23))
        self.cbProteina.setObjectName("cbProteina")
        self.cbFerro = QtGui.QCheckBox(self.groupBox)
        self.cbFerro.setGeometry(QtCore.QRect(20, 50, 93, 23))
        self.cbFerro.setObjectName("cbFerro")
        self.cbCarboidrato = QtGui.QCheckBox(self.groupBox)
        self.cbCarboidrato.setGeometry(QtCore.QRect(20, 80, 111, 23))
        self.cbCarboidrato.setObjectName("cbCarboidrato")
        self.cbCalcio = QtGui.QCheckBox(self.groupBox)
        self.cbCalcio.setGeometry(QtCore.QRect(20, 110, 93, 23))
        self.cbCalcio.setObjectName("cbCalcio")
        self.cbFibraAlimentar = QtGui.QCheckBox(self.groupBox)
        self.cbFibraAlimentar.setGeometry(QtCore.QRect(20, 140, 131, 23))
        self.cbFibraAlimentar.setObjectName("cbFibraAlimentar")
        self.cbColesterol = QtGui.QCheckBox(self.groupBox)
        self.cbColesterol.setGeometry(QtCore.QRect(20, 170, 93, 23))
        self.cbColesterol.setObjectName("cbColesterol")
        self.cbVitaminaA = QtGui.QCheckBox(self.groupBox)
        self.cbVitaminaA.setGeometry(QtCore.QRect(190, 20, 101, 23))
        self.cbVitaminaA.setObjectName("cbVitaminaA")
        self.cbVitaminaB1 = QtGui.QCheckBox(self.groupBox)
        self.cbVitaminaB1.setGeometry(QtCore.QRect(190, 50, 111, 23))
        self.cbVitaminaB1.setObjectName("cbVitaminaB1")
        self.cbVitaminaB2 = QtGui.QCheckBox(self.groupBox)
        self.cbVitaminaB2.setGeometry(QtCore.QRect(190, 80, 111, 23))
        self.cbVitaminaB2.setObjectName("cbVitaminaB2")
        self.cbVitaminaB6 = QtGui.QCheckBox(self.groupBox)
        self.cbVitaminaB6.setGeometry(QtCore.QRect(190, 110, 111, 23))
        self.cbVitaminaB6.setObjectName("cbVitaminaB6")
        self.cbVitaminaB12 = QtGui.QCheckBox(self.groupBox)
        self.cbVitaminaB12.setGeometry(QtCore.QRect(190, 140, 111, 23))
        self.cbVitaminaB12.setObjectName("cbVitaminaB12")
        self.cbVitaminaC = QtGui.QCheckBox(self.groupBox)
        self.cbVitaminaC.setGeometry(QtCore.QRect(190, 170, 101, 23))
        self.cbVitaminaC.setObjectName("cbVitaminaC")
        self.cbAcidoFolico = QtGui.QCheckBox(self.groupBox)
        self.cbAcidoFolico.setGeometry(QtCore.QRect(20, 200, 101, 23))
        self.cbAcidoFolico.setObjectName("cbAcidoFolico")
        self.cbPotassio = QtGui.QCheckBox(self.groupBox)
        self.cbPotassio.setGeometry(QtCore.QRect(20, 230, 93, 23))
        self.cbPotassio.setObjectName("cbPotassio")
        self.cbMagnesio = QtGui.QCheckBox(self.groupBox)
        self.cbMagnesio.setGeometry(QtCore.QRect(20, 260, 93, 23))
        self.cbMagnesio.setObjectName("cbMagnesio")
        self.cbVitaminaD = QtGui.QCheckBox(self.groupBox)
        self.cbVitaminaD.setGeometry(QtCore.QRect(190, 200, 101, 23))
        self.cbVitaminaD.setObjectName("cbVitaminaD")
        self.cbVitaminaE = QtGui.QCheckBox(self.groupBox)
        self.cbVitaminaE.setGeometry(QtCore.QRect(190, 230, 101, 23))
        self.cbVitaminaE.setObjectName("cbVitaminaE")
        self.cbVitaminaK = QtGui.QCheckBox(self.groupBox)
        self.cbVitaminaK.setGeometry(QtCore.QRect(190, 260, 101, 23))
        self.cbVitaminaK.setObjectName("cbVitaminaK")
        self.cbFormato = QtGui.QComboBox(JanelaEstatisticas)
        self.cbFormato.setGeometry(QtCore.QRect(220, 74, 85, 27))
        self.cbFormato.setObjectName("cbFormato")
        self.cbFormato.addItem("")
        self.cbFormato.addItem("")
        self.cbFormato.addItem("")
        self.cbFormato.addItem("")
        self.label = QtGui.QLabel(JanelaEstatisticas)
        self.label.setGeometry(QtCore.QRect(130, 80, 81, 18))
        self.label.setObjectName("label")
        self.groupBox_2 = QtGui.QGroupBox(JanelaEstatisticas)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 110, 321, 71))
        self.groupBox_2.setStyleSheet("""QGroupBox {
    
    background-color: rgb(230, 255, 213);
     border: 1px solid gray;
     border-radius: 5px;
     margin-top: 1ex; /* leave space at the top for the title */
 }

 QGroupBox::title {
     subcontrol-origin: margin;
     subcontrol-position: top center; /* position at the top center */
     padding: 0 3px;
 }""")
        self.groupBox_2.setObjectName("groupBox_2")
        self.deDe = QtGui.QDateEdit(self.groupBox_2)
        self.deDe.setGeometry(QtCore.QRect(30, 30, 110, 28))
        self.deDe.setObjectName("deDe")
        self.deAte = QtGui.QDateEdit(self.groupBox_2)
        self.deAte.setGeometry(QtCore.QRect(200, 30, 110, 28))
        self.deAte.setObjectName("deAte")
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(10, 35, 21, 18))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setGeometry(QtCore.QRect(172, 35, 21, 18))
        self.label_3.setObjectName("label_3")
        self.label_5 = QtGui.QLabel(JanelaEstatisticas)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 291, 31))
        self.label_5.setWordWrap(True)
        self.label_5.setObjectName("label_5")
        self.btPlotar = QtGui.QPushButton(JanelaEstatisticas)
        self.btPlotar.setGeometry(QtCore.QRect(120, 40, 92, 28))
        self.btPlotar.setObjectName("btPlotar")

        self.retranslateUi(JanelaEstatisticas)
        QtCore.QObject.connect(self.btPlotar, QtCore.SIGNAL("clicked()"), JanelaEstatisticas.plotar)
        QtCore.QMetaObject.connectSlotsByName(JanelaEstatisticas)

    def retranslateUi(self, JanelaEstatisticas):
        JanelaEstatisticas.setWindowTitle(QtGui.QApplication.translate("JanelaEstatisticas", "Form", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCalorias.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Calorias", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPeso.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Peso", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("JanelaEstatisticas", "Nutrientes", None, QtGui.QApplication.UnicodeUTF8))
        self.cbProteina.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Proteina", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFerro.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Ferro", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCarboidrato.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Carboidrato", None, QtGui.QApplication.UnicodeUTF8))
        self.cbCalcio.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Calcio", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFibraAlimentar.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Fibra alimentar", None, QtGui.QApplication.UnicodeUTF8))
        self.cbColesterol.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Colesterol", None, QtGui.QApplication.UnicodeUTF8))
        self.cbVitaminaA.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Vitamina A", None, QtGui.QApplication.UnicodeUTF8))
        self.cbVitaminaB1.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Vitamina B1", None, QtGui.QApplication.UnicodeUTF8))
        self.cbVitaminaB2.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Vitamina B2", None, QtGui.QApplication.UnicodeUTF8))
        self.cbVitaminaB6.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Vitamina B6", None, QtGui.QApplication.UnicodeUTF8))
        self.cbVitaminaB12.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Vitamina B12", None, QtGui.QApplication.UnicodeUTF8))
        self.cbVitaminaC.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Vitamina C", None, QtGui.QApplication.UnicodeUTF8))
        self.cbAcidoFolico.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Acido Folico", None, QtGui.QApplication.UnicodeUTF8))
        self.cbPotassio.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Potassio", None, QtGui.QApplication.UnicodeUTF8))
        self.cbMagnesio.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Magnesio", None, QtGui.QApplication.UnicodeUTF8))
        self.cbVitaminaD.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Vitamina D", None, QtGui.QApplication.UnicodeUTF8))
        self.cbVitaminaE.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Vitamina E", None, QtGui.QApplication.UnicodeUTF8))
        self.cbVitaminaK.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Vitamina K", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFormato.setItemText(0, QtGui.QApplication.translate("JanelaEstatisticas", "Dias", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFormato.setItemText(1, QtGui.QApplication.translate("JanelaEstatisticas", "Semanas", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFormato.setItemText(2, QtGui.QApplication.translate("JanelaEstatisticas", "Meses", None, QtGui.QApplication.UnicodeUTF8))
        self.cbFormato.setItemText(3, QtGui.QApplication.translate("JanelaEstatisticas", "Anos", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Mostrar por:", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox_2.setTitle(QtGui.QApplication.translate("JanelaEstatisticas", "Filtrar data", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("JanelaEstatisticas", "De", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Até", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Selecione o que voce deseja que apareca no grafico", None, QtGui.QApplication.UnicodeUTF8))
        self.btPlotar.setText(QtGui.QApplication.translate("JanelaEstatisticas", "Plotar", None, QtGui.QApplication.UnicodeUTF8))

