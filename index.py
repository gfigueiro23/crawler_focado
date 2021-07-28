from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED
from navegar import Navegar
from bs4 import BeautifulSoup
from unidecode import unidecode
import PySimpleGUI as sg

from urls import CadastrarTopico, CadastrarUrl, IdentificarTopico, Urlss

def tela():
    resultado = ''
    sg.theme('Reddit')
    layout =  [[sg.Text('Digite seu texto')], [sg.InputText(key='texto'), sg.Button('Pesquisar',size=(8,1))], 
    [sg.Text(key='produto', size=(50, 100))], [sg.Text(key='price', size=(100, 100))], [sg.Text(key='link', size=(100,100))]]
    window = sg.Window('Crawler focado', layout=layout, finalize=True, size=(500,300), text_justification='center', element_justification='center', auto_size_text=True)
    while True:
        event, values = window.read()
        if event == WINDOW_CLOSED:
            break

        if event == 'Pesquisar':
            text = values['texto']
            # separação de palavras desse texto
            text = text.split(" ")
        
            urls = Urlss()
            # chama a classe Urlss

            # chama a classe que identifica o topico
            identificar = IdentificarTopico(text)
            lista_urls = urls.getUrls(text) # pega a url de acordo com o texto
            
            text = ' '.join(text)
            details = Navegar(lista_urls[0], str(text)).getItem() # detalhes do item
            price = details[list(details.keys())[0]]['price'] # preço do item
            link = details[list(details.keys())[0]]['link'] # link do item
            produto = list(details.keys())[0]
            produto = list(details.keys())[0]
            window['produto'].update(f'Produto: {produto}')
            window['price'].update(f'Preço: R$ {price}')
            window['link'].update(f'Link: {link}')
            


if __name__ == '__main__':
    tela()


