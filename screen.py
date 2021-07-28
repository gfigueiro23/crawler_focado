import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

def tela():
    sg.theme('Reddit')
    layout =  [[sg.Text('Digite seu texto')], [sg.InputText(key='texto'), sg.Button('Pesquisar',size=(8,1))]]
    window = sg.Window('Crawler focado', layout=layout, finalize=True, size=(500,300), text_justification='center', element_justification='center')
    while True:
        event, values = window.read()
        if event == WINDOW_CLOSED:
            break

        if event == 'Pesquisar':
            print(values['texto'])

tela()