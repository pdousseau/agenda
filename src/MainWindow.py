from JanelaAgenda import *
from JanelaEstatisticas import *
from JanelaConfiguracoes import *
from JanelaAdicionar import *
from JanelaListaAlimentos import *
import sys,os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from Janelas.Ui_MainWindow import *
class MainWindow (QMainWindow, Ui_MainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pai = parent
        self.paginaAtual = None
        self.agenda()
        
    def configuracoes(self):
        pag = JanelaConfiguracoes()
        if self.paginaAtual != None:
            self.formLayout.removeWidget(self.paginaAtual)
            self.paginaAtual.hide()
        self.paginaAtual = pag
        self.formLayout.addWidget(pag)
        
    def agenda(self):
        pag = JanelaAgenda()
        pag.pai = self
        if self.paginaAtual != None:
            self.formLayout.removeWidget(self.paginaAtual)
            self.paginaAtual.hide()
        self.paginaAtual = pag
        self.formLayout.addWidget(pag)
        
        
    def estatisticas(self):
        pag = JanelaEstatisticas()
        if self.paginaAtual != None:
            self.formLayout.removeWidget(self.paginaAtual)
            self.paginaAtual.hide()
        self.paginaAtual = pag
        self.formLayout.addWidget(pag)
        
    def listaAlimentos(self):
        pag = JanelaListaAlimentos()
        if self.paginaAtual != None:
            self.formLayout.removeWidget(self.paginaAtual)
            self.paginaAtual.hide()
        self.paginaAtual = pag
        self.formLayout.addWidget(pag)
        
    def adicionar(self,dieta=None):
        pag = JanelaAdicionar()
        pag.pai = self
        if dieta is not None:
            pag.modificar(dieta)
        if self.paginaAtual != None:
            self.formLayout.removeWidget(self.paginaAtual)
            self.paginaAtual.hide()
        self.paginaAtual = pag
        self.formLayout.addWidget(pag)
        
        
    


        
