from PyQt4.QtCore import *
from  PyQt4.QtGui import QMainWindow 
from Janelas.Ui_JanelaEstatisticas import *
from Global import *
import os, pickle
from numpy import arange

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

from matplotlib import pylab



class JanelaEstatisticas (QMainWindow, Ui_JanelaEstatisticas):
    
    
    def __init__(self, parent=None):
        super(JanelaEstatisticas, self).__init__(parent)
        self.setupUi(self)
        self.carregarDietas()
        self.pag = None
        
    def plotar(self):
        if self.pag is not None: self.pag.hide()
        self.montarGrafico()
        self.pag = MyStaticMplCanvas(self.dias)
        self.formLayout.addWidget(self.pag)
        
    
    def carregarDietas(self):
        
        self.dietas = []
        
        #busca todos os arquivos
        for root, dirs, files in os.walk(MY_DIR_DIETA):
            
            #para cada arquivo
            for f in files:
                
                #pega o arquivo, carrega e fecha
                arq = file(MY_DIR_DIETA + f)
                dieta = pickle.load(arq)
                arq.close()
                #adiciona o item na lista de dietas

                self.dietas.append( dieta )
            
        
                
        
        
    def montarGrafico(self):
        
        # eh um dicionario de listas
        valores = {}
       
        
        if self.cbAcidoFolico.isChecked():
            valores['Acido Folico'] = 0.0
        if self.cbCalcio.isChecked():
            valores['Calcio'] = 0.0
        if self.cbCalorias.isChecked():
            valores['Calorias'] = 0.0
            
        if self.cbProteina.isChecked():
            valores['Proteinas'] = 0.0
            
        if self.cbColesterol.isChecked():
            valores['Colesterol'] = 0.0
        if self.cbFerro.isChecked():
            valores['Ferro'] = 0.0
        if self.cbFibraAlimentar.isChecked():
            valores['Fibra'] = 0.0
        if self.cbMagnesio.isChecked():
            valores['Magnesio'] = 0.0
        
        if self.cbPotassio.isChecked():
            valores['Potassio'] = 0.0
        if self.cbVitaminaA.isChecked():
            valores['Vitamina A'] = 0.0
            
        if self.cbVitaminaB1.isChecked():
            valores['Vitamina B1'] = 0.0
        if self.cbVitaminaB2.isChecked():
            valores['Vitamina B2'] = 0.0
        if self.cbVitaminaB6.isChecked():
            valores['Vitamina B6'] = 0.0
        if self.cbVitaminaB12.isChecked():
            valores['Vitamina B12'] = 0.0
        if self.cbVitaminaC.isChecked():
            valores['Vitamina C'] = 0.0
        if self.cbVitaminaD.isChecked():
            valores['Vitamina D'] = 0.0
        if self.cbVitaminaE.isChecked():
            valores['Vitamina E'] = 0.0
        if self.cbVitaminaK.isChecked():
            valores['Vitamina K'] = 0.0
        
        
            
       
        
        self.dias = {}
        
        #para cada uma das dietas
        for i in self.dietas:
            
            data = str(i.data.day()) + "/" + str(i.data.month()) + "/" + str(i.data.year())[2:4]
            
            #para cada um dos alimentos da dieta
            for j in i.listaAlimentos:
                
                #para cada um dos nutrientes
                for k in valores.keys():
                    valores[k] += j.propriedades[k]
                    
            self.dias[data] = valores.copy()
            for i in valores.keys() : valores[i] = 0.0
                    
        
                    
               
        
class MyMplCanvas(FigureCanvas):
    """Ultimately, this is a QWidget (as well as a FigureCanvasAgg, etc.)."""
    def __init__(self, dados, parent=None, width=5, height=4, dpi=100,):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.fig = fig
        self.axes = fig.add_subplot(111)
        # We want the axes cleared every time plot() is called
        #self.axes.hold(False)

        self.compute_initial_figure(dados)
        FigureCanvas.__init__(self, fig)
        #self.setParent(parent)

        #FigureCanvas.setSizePolicy(self,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        #FigureCanvas.updateGeometry(self)

   
from pylab import *

class MyStaticMplCanvas(MyMplCanvas):
    """Simple canvas with a sine plot."""
    
   
    def compute_initial_figure(self,dados):
        self.axes.grid(True)

        self.dias = dados
        d = []
        a = []
        for i in self.dias.keys():
            for j in self.dias.get(i).keys():
                a.append(self.dias.get(i).get(j))
            d.append( copy(a) )
            del a[:]

        
        data = d
        a = 1
        
        if (a==0):
            
                
    
            
            dim = len(data[0])
            w = 0.75
            dimw = w / dim
            
            x = pylab.arange(len(data))
            
            cor = ['r','y', 'b','p','c','w']
            g = [] 
            for i in range(len(data[0])) :
                y = [d[i] for d in data]
                g.append( self.axes.bar(x + i * dimw, y, dimw, color=cor[i], bottom=0.001) )
               
    
    
    #        self.axes.legend( (g[0][0],g[1][0],g[2][0]), ('Men', 'Women','Both') )
        else:
            
            
            
            t = range( len(data) )
            s = []
            
            
            def millions(x, t):
                'The two args are the value and tick position'
                return 'maria'
            
            formatter = FuncFormatter(millions)

            #self.axes.xaxis.set_major_formatter(formatter)

            
            
            #para cada um dos nutrientes
            for k in range(len(data[0])):
                #para cada um dos dias
                for a in range(len(data)):
                    s.append( data[ a ][k])
                    
                self.axes.plot(t, s)
                del s[:]
                
                
                
            w = 0.75
            
            x = pylab.arange(len(data))
            vb = self.dias.keys()
            self.axes.set_xticklabels(vb)
            vb = arange(len(vb))
            self.axes.set_xticks(vb)
            print x + w / 2
            

          
            
             


    



        
   
    