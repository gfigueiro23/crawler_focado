import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import WINDOW_CLOSED

def tela():
    sg.theme('Reddit')
    layout =  [[sg.Text('hello')]]
    window = sg.Window('Crawler focado', layout=layout, finalize=True, size=(500,300))
    while True:
        event, values = window.read()
        if event == WINDOW_CLOSED:
            break

tela()