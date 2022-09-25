from os import listdir, chdir

def list_users_windows():
    adress = 'C:\\Users\\'
    list_not_users = ['All Users','Default','Default User','desktop.ini','Todos os Usuários','Usuário Padrão']
    list_users = []
    for user in listdir(adress):
        if user not in list_not_users:
            list_users.append(user)
    return list_users

if __name__ == '__main__':
    lista_de_usuarios = list_users_windows()
    print(lista_de_usuarios)