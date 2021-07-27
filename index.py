from navegar import Navegar
from bs4 import BeautifulSoup
from unidecode import unidecode

from urls import CadastrarTopico, CadastrarUrl, IdentificarTopico, Urlss


if __name__ == '__main__':
    text = input('Digite um assunto: ')

    text = text.split(" ")
  
    urls = Urlss()


    text = ' '.join(text)
    identificar = IdentificarTopico(text)
    lista_urls = urls.getUrls(text)
    
    details = Navegar(lista_urls[0], str(text)).getItem()
    price = details[list(details.keys())[0]]['price']
    link = details[list(details.keys())[0]]['link']
    produto = list(details.keys())[0]
    print(f"---------- PRODUTO ---------- \n"
    f"PREÇO: {price} \n"
    f"LINK: {link}")