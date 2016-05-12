from PyQt4.QtGui import QMainWindow 
from PyQt4.QtGui import QPixmap, QTableWidgetItem,QListWidgetItem
from Janelas.Ui_JanelaAdicionar import *
from Dieta import *
from Global import *
from Alimento import *
import os,pickle

class JanelaAdicionar (QMainWindow, Ui_JanelaAdicionar):
    
    
    def __init__(self, parent=None):
        super(JanelaAdicionar, self).__init__(parent)
        self.setupUi(self)
        self.popularListaAlimentos()
        self.pai = None
        

        
    def popularListaAlimentos(self):
        
        self.alimentos = {}
        
        #busca todos os arquivos
        for root, dirs, files in os.walk(MY_DIR_ALIMENTO):
            
            #para cada arquivo
            for f in files:
                
                #pega o arquivo, carrega e fecha
                arq = file(MY_DIR_ALIMENTO + f)
                alim = pickle.load(arq)
                arq.close()
                
                #adiciona o item na lista de alimento
                self.alimentos[str(alim.nome)] = alim

                #cria uma entrada na listaAlimentos
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(alim.imagem), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item = QListWidgetItem()
                item.setIcon(icon)
                item.setText(alim.nome)
                
                self.listaAlimentos.addItem(item)
        
    def removerAlimento(self):
        linha = self.listaRefeicao.currentRow()
        self.listaRefeicao.takeItem(linha).text()
        
    def adicionarAlimento(self):
        
        #seleciona o elemento que se quer adicionar e adiciona
        linha = self.listaAlimentos.currentRow()
        nomeAlimento = str(self.listaAlimentos.item(linha).text())
        self.listaRefeicao.addItem(nomeAlimento)
        
    def calcularCalorias(self):
        
        calorias = 0.0
        
        #para cada um dos itens na lista de refeicao
        for i in range(self.listaRefeicao.count(),-1,-1):
                alim = self.listaRefeicao.item(i)
                if alim is not None:
                    if self.alimentos[str(alim.text())].propriedades.get('Calorias') is not None:
                        calorias += self.alimentos[str(alim.text())].propriedades.get('Calorias')
        return calorias
                    
        
    def modificar(self,dieta):
        self.cxPeso.setText( str(dieta.peso) )
        self.cxAnotacoes.setText( str(dieta.anotacoes) )
        self.calendario.setSelectedDate( dieta.data )
        for i in dieta.listaAlimentos:
            self.listaRefeicao.addItem( QListWidgetItem(i.nome) )
        
    def salvar(self):
        
        #pega os valores passados
        peso = self.cxPeso.text()
        anotacoes = self.cxAnotacoes.toPlainText()
        data = self.calendario.selectedDate()
        calorias = self.calcularCalorias()

        alimentos = []
        
        #para cada um dos itens na lista de refeicao
        for i in range(self.listaRefeicao.count(),-1,-1):
                alimNome = self.listaRefeicao.item(i)
                if alimNome is not None:
                    alimentos.append( self.alimentos.get(str ( alimNome.text()) ) )
                    
        novaDieta = Dieta(data,calorias,alimentos,peso,anotacoes)
        
        pickle.dump(novaDieta, file(MY_DIR_DIETA  + str(data.day()) + "_" + str(data.month()) + "_" + str(data.year()), 'w'))
        self.pai.agenda()
        