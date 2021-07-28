import pandas as pd
import json
from unidecode import unidecode
from io import StringIO

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
        topico = ''
        for x in self.text: self.text[self.text.index(x)] = unidecode(x).lower()
        self.text = ' '.join(self.text)
        for x in self.dfe.keys():
            for y in self.dfe[x]:
                y = unidecode(str(y)).lower()
                if y in self.text:
                    topico = x
        if topico == '':
            topico = self.text
        return topico                    
        

class Urlss():
    def __init__(self):
        pass
    def CadastrarUrl(self, urls,  topico):
        self.url = urls

        self.file = {
            topico: self.url
        }
        self.json2 = json.dumps(self.file)
        df = pd.read_json(StringIO(self.json2))
        df.reset_index(inplace=True, drop=True)
        df.to_excel('urls.xlsx', index=False)
    
    def getUrls(self, text):
        self.text =  text
        teste = ' '.join(self.text)
        if teste != IdentificarTopico(self.text).getTopico():
            self.text =  text
            teste = ' '.join(self.text)
            self.topico = IdentificarTopico(self.text).getTopico()
            urlsexcel = pd.read_excel('urls.xlsx')
            self.topico = self.topico.lower()
            list_urls = []
            if self.topico in urlsexcel:
                for x in urlsexcel[self.topico]:
                    list_urls.append(x)            
                    
            return list_urls
        else:
            list_urls = ['https://www.americanas.com.br/']
            return list_urls
            
        
    


