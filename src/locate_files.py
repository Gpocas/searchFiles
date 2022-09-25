import os
from format_size import formata_tamanho

# caminho_procura = input("Digite um caminho: ")
# caminho_procura = caminho_procura.replace('"', '').replace("'", '').strip()
# termo_procura = input("Digite um termo: ").strip()

def search_files(caminho_procura, termo_procura):
    
    for root, dirs, files in os.walk(caminho_procura):
        for file in files:
            if termo_procura.casefold() in file.casefold():
                try:
                    file_abspath = os.path.join(root, file)
                    file_name, file_ext = os.path.splitext(file)
                    file_size = os.path.getsize(file_abspath)
                    file_size_f = formata_tamanho(file_size)
                    
                    retorno = f'''Caminho do arquivo: {file_abspath}
Nome do arquivo: {file_name}
Extensão do arquivo: {file_ext}
Tamanho em bytes: {file_size}
Tamanho formatado: {file_size_f}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------'''
                    yield retorno
                    
                except PermissionError as e:
                   yield "Sem permissao nesse arquivo"
                except FileNotFoundError as e:
                    yield "Arquivo nao encontrado"
                except Exception as e:
                    yield f"Erro desconhecido: {e}" 
