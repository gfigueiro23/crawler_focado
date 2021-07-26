import pandas as pd
import json

class CadastrarUrl():
    def __init__(self, urls):
        self.url = urls

class CadastrarTopico():
    def __init__(self, topicos, keywords):
        self.topicos =  topicos
        self.keywords = keywords
        self.keys = {
            self.topicos : self.keywords
        }
    def getDict (self):
        return self.keys
    
    def Salvar(self):
        self.json = json.dumps(self.keys)
        df = pd.read_json(self.json)
        df.reset_index(inplace=True, drop=True)
        df.to_excel('topicos.xlsx', index=False)

class IdentificarTopico():
    def __init__(self, text):
        self.dfe = pd.read_excel('topicos.xlsx')
        self.text = text
    
    def getTopico(self):
        for x in self.dfe.keys():
            for y in self.dfe[x]:
                if self.text == y:
                    print(f"tópico: {x}")
