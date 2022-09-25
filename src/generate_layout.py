import PySimpleGUI as sg
from list_users import list_users_windows


layout = [[sg.Text('Selecione algum dos usuraios abaixo:')],]
list_usures = list_users_windows()

for user in list_usures:
    layout.append([sg.Radio(f'{user}', 'RADIO2',)])

layout.append([sg.Button('Submit'), sg.Exit()])

window_users = sg.Window("Test", layout=layout)

while True:
    event, values = window_users.read()