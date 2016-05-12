from PyQt4.QtGui import QMainWindow,QTableWidgetItem
from Janelas.Ui_JanelaAgenda import *
from Global import *
import os,pickle

class JanelaAgenda (QMainWindow, Ui_JanelaAgenda):
    
    
    def __init__(self, parent=None):
        super(JanelaAgenda, self).__init__(parent)
        self.setupUi(self)
        self.popularAgenda()
        
        
    def popularAgenda(self):
        
        linha = 0
        self.dietas = {}
        
        #busca todos os arquivos
        for root, dirs, files in os.walk(MY_DIR_DIETA):
            
            #verifica quantos arquivos existem para saber qnts linhas criar
            numArqs = len(files)
            if numArqs > 16:
                self.tbAgenda.setRowCount( numArqs )
            
            #para cada arquivo
            for f in files:
                
                #pega o arquivo, carrega e fecha
                arq = file(MY_DIR_DIETA + f)
                dieta = pickle.load(arq)
                arq.close()
                
                #adiciona o item na agenda
                itemData = QTableWidgetItem()
                itemAnotacoes = QTableWidgetItem()
                itemCalorias = QTableWidgetItem()

                #seta a data
                data = str(dieta.data.day()) + "/" + str(dieta.data.month()) + "/" + str(dieta.data.year())
                itemData.setText(data)
                self.tbAgenda.setItem(linha,0,itemData)
                
                #seta as calorias
                itemCalorias.setText(str(dieta.calorias))
                self.tbAgenda.setItem(linha,1,itemCalorias)
                
                #seta o anotacoes
                itemAnotacoes.setText(dieta.anotacoes)
                self.tbAgenda.setItem(linha,2,itemAnotacoes)
                linha+=1
                
                self.dietas[data] = dieta 
                
        
    def adicionar(self):
        self.pai.adicionar()
        
        
    def modificar(self):
        
        #pega a linha selecionada
        linha = self.tbAgenda.currentRow()
        
        #pega a data para formar o nome do arquivo dieta
        data = self.tbAgenda.item(linha,0).text()
        
        dieta = self.dietas.get(str(data))
        
        self.pai.adicionar(dieta)
        
        
        
    def remover(self):
        linha = self.tbAgenda.currentRow()
        dieta = self.tbAgenda.item(linha,0).text().replace("/","_")
        self.tbAgenda.removeRow(linha)
        os.remove(MY_DIR_DIETA + dieta)