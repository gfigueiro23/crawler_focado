from bs4 import BeautifulSoup

from urls import CadastrarTopico, CadastrarUrl, IdentificarTopico


if __name__ == '__main__':
    text = input('Digite um assunto: ')
    identificar = IdentificarTopico(text)
    identificar.getTopico()

        
        
    
