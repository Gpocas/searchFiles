import os
import PySimpleGUI as sg
from locate_files import search_files

working_directory = os.getcwd()
icon = r'C:\Users\Guilherme\Desktop\DESENVOLVIMENTO\PYTHON\Search-Files\icons\search.ico'
sg.theme('DarkGrey14')

def menuApp():
    layout = [
        [sg.Text('Selecione uma das opções abaixo:')],
        
        [sg.Radio('Pesquisa Completa', 'RADIO1', key='-SearchComplet-',pad=(0,15), default=True), 
        sg.Radio('Pesquisa por Usuario','RADIO1', key='-SearchByUser-', default=False),
        sg.Radio('Pesquisa Personalizada', 'RADIO1', key='-SearchPersonalized-',default=False) ],
        
        [sg.Push(),sg.Button('Enviar'), sg.Exit('Sair', size=(5,1)), sg.Push(),]
        
            ]
    return sg.Window("SearchFiles", icon=icon,layout=layout, finalize=True)

def SelectedTermApp():
    
    layout = [
        [sg.Text('Digite o termo que deseja pesquisar:')],
        [sg.InputText(key='-TermSearchAll-',size=(30,1),pad=(5,7))],
        [sg.Push(), sg.Button('Enviar',bind_return_key=True),sg.Button('Voltar'), sg.Exit('Sair', size=(5,1)), sg.Push()]
        
            ]
    return sg.Window("SearchFiles", icon=icon, layout=layout, finalize=True)

def SelectedUserApp():
    
    layout = [
        [sg.Text('Escolha o seu usuario:')],
        [sg.InputText(key='-UserFolderSearch-',size=(30,1)), sg.FolderBrowse(initial_folder='C:\\Users\\')],
        [sg.Text('Digite o termo que deseja pesquisar:')],
        [sg.InputText(key='-TermSearchUserFolder-',size=(30,1),pad=(5,8))],
        [sg.Button('Enviar', bind_return_key=True),sg.Button('Voltar'), sg.Exit('Sair', size=(5,1))]
        
            ]
    return sg.Window("SearchFiles", icon=icon, layout=layout, finalize=True)


def SelectedAdressApp():
    
    layout = [
        [sg.Text('Escolha o diretorio que deseja pesquisar:')],
        [sg.InputText(key='-AdressSearch-',size=(30,1)), sg.FolderBrowse()],
        [sg.Text('Digite o termo que deseja pesquisar:')],
        [sg.InputText(key='-TermSearchAdress-',size=(30,1),pad=(5,8))],
        [sg.Button('Enviar', bind_return_key=True),sg.Button('Voltar'), sg.Exit('Sair', size=(5,1))]
        
            ]
    return sg.Window("SearchFiles", icon=icon, layout=layout, finalize=True)



def SearchApp(adress, term):
        layout = [
        [sg.Text(f'Realizando Buscas em {adress}')],
        [sg.Text(f'Termo Buscado: "{term}"')],
        [sg.Multiline(key='-ResultsSearch-',size=(100,40), disabled=True)],
        [sg.Push(),sg.Button('Iniciar'),sg.Button('Menu'),sg.Button('Anterior'), sg.Exit('Sair', size=(5,1)), sg.Push(),]
                ]
        return sg.Window("SearchFiles", icon=icon, layout=layout, finalize=True)

window_menu, window_search, window_selectedTerm, window_selectedUser, window_selectedAdress = menuApp(), None, None, None, None

term = None
adress_search = None
previous = None

while True:
    
    window, event, values = sg.read_all_windows()

    # ==========================================================================================================================
    #                                       Triggers para sair do Aplicativo
    

    if window == window_menu and event in (sg.WIN_CLOSED, 'Sair'):
        break

    if window == window_search and event in (sg.WIN_CLOSED, 'Sair'):
        break
    
    if window == window_selectedTerm and event in (sg.WIN_CLOSED, 'Sair'):
        break
    
    if window == window_selectedUser and event in (sg.WIN_CLOSED, 'Sair'):
        break
    
    if window == window_selectedAdress and event in (sg.WIN_CLOSED, 'Sair'):
        break
    
    # ==========================================================================================================================
    #                                       Triggers para voltar ao menu do Aplicativo
    if window == window_search and event == 'Menu':
        window_search.hide()
        window_menu.un_hide()
        
    if window == window_selectedTerm and event == 'Voltar':
        window_selectedTerm.hide()
        window_menu.un_hide()
    
    if window == window_selectedUser and event == 'Voltar':
        window_selectedUser.hide()
        window_menu.un_hide()
    
    if window == window_selectedAdress and event == 'Voltar':
        window_selectedAdress.hide()
        window_menu.un_hide()
    
    # ==========================================================================================================================
    #                                       Trigger para selecionar opção de Busca
    
    if window == window_menu and event == 'Enviar':

        if values['-SearchComplet-'] == True:
            window_menu.hide()
            window_selectedTerm = SelectedTermApp()

        if values['-SearchByUser-'] == True:
            window_menu.hide()
            window_selectedUser = SelectedUserApp()
            
        if values['-SearchPersonalized-'] == True:
            window_menu.hide()
            window_selectedAdress = SelectedAdressApp()
            
    # ==========================================================================================================================
    #                                       Triggers para redrecionar para a tela de Pesquisa do arquivos
    if window == window_selectedTerm and event == 'Enviar':
        
        if values['-TermSearchAll-'] != '':
            adress_search = 'C:\\'
            term = values['-TermSearchAll-']
            previous = 'selectedTerm'
            window_selectedTerm.hide()
            window_search = SearchApp(adress_search, term)
            window['-TermSearchAll-'].update('')
        else:
             sg.popup('Por favor, Digite um termo para a pesquisa', title='Aviso')
             
    # ==========================================================================================================================

    if window == window_selectedUser and event == 'Enviar':
        
        if values['-UserFolderSearch-'] != '' and values['-TermSearchUserFolder-'] != '':
            term = values['-TermSearchUserFolder-']
            adress_search = values['-UserFolderSearch-']
            if os.path.exists(adress_search) == True:
                previous = 'selectedUser'
                window_selectedUser.hide()
                window_search = SearchApp(adress_search, term)
                window['-UserFolderSearch-'].update('')
                window['-TermSearchUserFolder-'].update('')
                
            else:
                sg.popup(f'''Usuario digitado invalido.
caminho inexistente: {adress_search}''', title='Aviso')
                
        elif values['-UserFolderSearch-'] == '':
            sg.popup('A informação de usuario é Obrigatório.', title='Aviso')
        
        elif values['-TermSearchUserFolder-'] == '':
            sg.popup('A informação de termo de pesquisa é Obrigatório.', title='Aviso')
            
    # ==========================================================================================================================
    
    if window == window_selectedAdress and event == 'Enviar':
        if values['-AdressSearch-'] != '' and values['-TermSearchAdress-'] != '':
            term = values['-TermSearchAdress-']
            adress_search = values['-AdressSearch-']
            if os.path.exists(adress_search) == True:
                previous = 'selectedAdress'
                window_selectedAdress.hide()
                window_search = SearchApp(adress_search, term)
                window['-AdressSearch-'].update('')
                window['-TermSearchAdress-'].update('')
            else:
                sg.popup(f'caminho inexistente: {adress_search}', title='Aviso')
        elif values['-AdressSearch-'] == '':
            sg.popup('A informação de diretorio da pesquisa é Obrigatório.', title='Aviso')
            
        elif values['-TermSearchAdress-'] == '':
             sg.popup('A informação de termo de pesquisa é Obrigatório.', title='Aviso')

    # ==========================================================================================================================
    
    if window == window_search and event == 'Iniciar':
        
        results_search = search_files(adress_search, term)
        value_textBoxSearch = values['-ResultsSearch-']
        while True:
            try:
                if value_textBoxSearch != '':
                    value_textBoxSearch = value_textBoxSearch + '\n' + next(results_search)
                else:
                    value_textBoxSearch = '-----------------------------------------------------------------------------------------------------------------------------------------------------------------'
                    value_textBoxSearch = value_textBoxSearch + '\n' + next(results_search)
                window['-ResultsSearch-'].update(value_textBoxSearch)
            
            except StopIteration:
                break
        # sg.popup('Busca Finalizada !!!',title='Concluido')
        sg.popup_timed('Busca Finalizada !!!',title='Concluido')
    if window == window_search and event == 'Anterior':
        match(previous):
            case 'selectedTerm':
                window_search.hide()
                window_selectedTerm.un_hide()

            case 'selectedUser':
                window_search.hide()
                window_selectedUser.un_hide()
            case 'selectedAdress':
                window_search.hide()
                window_selectedAdress.un_hide()

# x = search_files('C:\\Users\\Guilherme\\', 'Senhas')
# while True:
#     try:
#         print(next(x))
#     except StopIteration:
#         break