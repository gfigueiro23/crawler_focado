import pandas as pd
import json
from unidecode import unidecode
from io import StringIO

# Cadastra a url 
class CadastrarUrl():
    def __init__(self, urls):
        self.url = urls

# Classe que cadastra topicos
class CadastrarTopico():
    def __init__(self, topicos, keywords):
        self.topicos =  topicos # topico
        self.keywords = keywords # palavras chaves do topico
        self.keys = {
            self.topicos : self.keywords
        }
    def getDict (self): # retorna a relação das palavras chaves com os topicos
        return self.keys
    
    def Salvar(self): # salva essa relação em uma planilha
        self.json = json.dumps(self.keys)
        df = pd.read_json(self.json)
        df.reset_index(inplace=True, drop=True)
        df.to_excel('topicos.xlsx', index=False)

# Classe que identifica o topico de acordo
# com as palavras chaves digitadas
class IdentificarTopico():
    def __init__(self, text):
        self.dfe = pd.read_excel('topicos.xlsx') # lê a planilha gerada na classe anterior
        self.text = text # Texto difitado pelo usuario
    
    def getTopico(self):
        topico = '' # por padrão, topico é vazio
        for x in self.text: self.text[self.text.index(x)] = unidecode(x).lower() # deixa o texto em lowercase
        self.text = ' '.join(self.text) # transforma o texto que é uma lista, em uma string
        for x in self.dfe.keys(): # pra cada topico dentro da planilha:
            for y in self.dfe[x]: # pra cada palavra chave dentro do topico:
                y = unidecode(str(y)).lower() # palavra chave em lowercase para evitar conflito
                if y in self.text: # verifica se existe o texto digitado nas palavras chaves
                    topico = x # topico recebe o topico do texto digitado 
        if topico == '': # se o topico for vazio:
            topico = self.text # topico = texto digitado pelo usuario
        return topico                    
        

class Urlss():
    def __init__(self):
        pass

    # Função que cadastra url
    def CadastrarUrl(self, urls,  topico):
        self.url = urls


        self.file = {
            topico: self.url    # dict com a relação dos tópicos com as suas urls
        }
        self.json2 = json.dumps(self.file) # gera um arquivo json 
        df = pd.read_json(StringIO(self.json2)) # le o json
        df.reset_index(inplace=True, drop=True) 
        df.to_excel('urls.xlsx', index=False) # transforma o json em uma planilha excel
    
    # Função que pega a url 
    def getUrls(self, text):
        self.text =  text # texto digitado pelo usuário
        teste = ' '.join(self.text) # transforma o texto digitado em uma string e armazena em uma variavel diferente
        if teste != IdentificarTopico(self.text).getTopico(): # Se o texto digitado NÃO é igual ao topico retornado:
            self.text =  text
            teste = ' '.join(self.text)
            self.topico = IdentificarTopico(self.text).getTopico() # topico
            urlsexcel = pd.read_excel('urls.xlsx') # le a planilha de urls gerada anteriormente
            self.topico = self.topico.lower() # topico em lowercase
            list_urls = []
            if self.topico in urlsexcel: # Se existir o topico na planilha
                for x in urlsexcel[self.topico]: # para cada url dentro desse topico:
                    list_urls.append(x) # lista de urls + url do topico        
                    
            return list_urls
        else: # Caso o texto digitado, não possuí um topico:
            list_urls = ['https://www.americanas.com.br/'] # url padrão de pesquisa
            return list_urls
            
        
    


