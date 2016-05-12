from PyQt4.QtGui import QMainWindow
from PyQt4.QtGui import QPixmap, QTableWidgetItem,QListWidgetItem
from Janelas.Ui_JanelaListaAlimentos import *
from Alimento import *

class JanelaListaAlimentos (QMainWindow, Ui_JanelaListaAlimentos):
    
    
    def __init__(self, parent=None):
        super(JanelaListaAlimentos, self).__init__(parent)
        self.setupUi(self)
        self.limparCampos()
        self.popularListaAlimentos()
        
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
                
                icon = QtGui.QIcon()
                icon.addPixmap(QtGui.QPixmap(alim.imagem), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                item = QListWidgetItem()
                item.setIcon(icon)
                item.setText(alim.nome)
                
                self.listaAlimentos.addItem(item)
        
    def limparCampos(self):
        #limpa todos os seus campos
        self.txtCarregarFoto.setText("")
        self.txtNome.setText("")
        self.lblImagem.setPixmap(QPixmap())
        self.lblImagem.setText("Imagem")
        self.nomeArquivo = ""
        self.imagem = ""
        for i in range(0,self.tbPropriedades.rowCount()):
            self.tbPropriedades.setItem(i-1,1,QTableWidgetItem(""))
        
    def salvar(self):

        #verifica se o nome esta vazio
        if self.txtNome.text().isEmpty():
            dialog = QMessageBox.warning(self, "Adicionar Alimento","Ooops! Eh necessario entrar com um nome.",QMessageBox.Ok );
            return
        else:
            self.nome = self.txtNome.text()
            props = {}
            
            #para cada propriedade
            for i in range(0,self.tbPropriedades.rowCount()):
                
                #pega o nome da propriedade
                item = self.tbPropriedades.item(i,0)
            
                #caso nao seja vazia
                if ( item != None):
                    key = str(self.tbPropriedades.verticalHeaderItem(i).text())
                    try:
                        if (item.text() != ""):
                            props[key] = float(item.text())
                        else:
                           props[key] = 0.0 
                    except:
                        dialog = QMessageBox.information(self, "Adicionar Alimento","So eh possivel entrar com \n valores numericos.",QMessageBox.Ok );
                        return
                    
            
            

            if (self.nomeArquivo is not None and self.nomeArquivo != ""):
                extensao = self.nomeArquivo.split(".")
                self.imagem = str(MY_DIR_IMG + self.nome + "." +  extensao[len(extensao)-1])
                
                #verifica se o nome da img contem espaco (necessario apenas para o copy)
                img= self.imagem
                arq = self.nomeArquivo
                
                #tratando espaco
                img = self.imagem.replace(" ", "\ ")
                arq = self.nomeArquivo.replace(" ","\ ")
                
                #tratando caracteres especiais
                img = img.replace("(", "\(")
                arq = arq.replace("(","\(")
                img = img.replace(")", "\)")
                arq = arq.replace(")","\)")
                
                
                os.system ("cp %s %s" % (arq, img))
            
            
            #cria um novo alimento com os respectivos nome e propriedades
            alimento = Alimento(self.nome, props, self.imagem)
            
            #salva isso em um arquivo
            pickle.dump(alimento, file(MY_DIR_ALIMENTO  + alimento.nome, 'w'))
            
            self.limparCampos()
            self.alimentos[ str(self.nome) ] = alimento
            
           
                
            icon = QtGui.QIcon()
            icon.addPixmap(QtGui.QPixmap(alimento.imagem), QtGui.QIcon.Normal, QtGui.QIcon.Off)
            item = QListWidgetItem()
            item.setIcon(icon)
            item.setText(self.nome)
            
            self.listaAlimentos.addItem(item)
            
            
            
        
    def modificar(self):
        self.limparCampos()
        nome = self.listaAlimentos.currentItem().text()
        alimento = self.alimentos.get( str(nome) )
        self.txtCarregarFoto.setText(alimento.imagem)
        self.lblImagem.setPixmap(QPixmap(alimento.imagem))
        
        self.txtNome.setText( alimento.nome )
        
        #para cada nome da propriedade
        for i in alimento.propriedades.keys():
            
            #corre todas as colunas
            for j in range(0,self.tbPropriedades.rowCount()):
                
                #verifica o nome da coluna atual
                coluna = self.tbPropriedades.verticalHeaderItem(j)
                if (not coluna == None):
                    
                    #caso esteja na coluna certa, valora
                    if ( str(coluna.text()) == str(i) ):
                        self.tbPropriedades.setItem(j-1,1,QTableWidgetItem(str(alimento.propriedades[i])))
        
    def remover(self):
        
        #pega a linha seleciona
        linha = self.listaAlimentos.currentRow()
        
        if (linha >= 0):
            
            #remove esse elemento da lista de alimentos
            nomeAlimento = str(self.listaAlimentos.takeItem(linha).text())
            os.remove(MY_DIR_ALIMENTO + nomeAlimento)
        
    def carregarFoto(self):
        self.nomeArquivo = str(QtGui.QFileDialog.getOpenFileName(self, 'Abrir arquivo','/home/',"Images (*.jpg *.jpeg *.gif *.png)"))
        self.txtCarregarFoto.setText(self.nomeArquivo)
        self.lblImagem.setPixmap(QPixmap(self.nomeArquivo))