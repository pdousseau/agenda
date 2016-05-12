from PyQt4.QtGui import QMainWindow
from Janelas.Ui_JanelaConfiguracoes import *
from Configuracoes import *
import pickle

class JanelaConfiguracoes (QMainWindow, Ui_JanelaConfiguracoes):
    
    
    def __init__(self, parent=None):
        super(JanelaConfiguracoes, self).__init__(parent)
        self.setupUi(self)
        
    def salvar(self):
        peso = str( self.cxPeso.text() )
        caloriasDiarias = str( self.cxCalorias.text() )
        
        conf = Configuracoes(peso,caloriasDiarias)
        pickle.dumb(conf, file(MY_DIR + "configuracoes",'w'))
        