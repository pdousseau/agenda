import pickle
import sys
import os
from Global import *

class Alimento(object):
    
    global nome, propriedades, imagem
    
    def __init__(self,nm, props, img = ""):
        
        self.nome = nm
        self.propriedades = props #dicionario
        if (img == ""):
            self.imagem = MY_DIR_IMG + IMG_PADRAO
        else:
            self.imagem = img
        
