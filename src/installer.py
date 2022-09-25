# -*- coding: utf-8 -*-
"""
Created on Wed Aug 31 12:45:06 2022

@author: guilhermepocas-trp
"""

import PyInstaller.__main__

PyInstaller.__main__.run([
    'interface.py',
    '--onefile', # --onedir (cria o aplicativo em um diretorio com varios arquivos deixando a aplicação mais leve)
    '--windowed',
    '--icon=C:\\Users\\Guilherme\\Desktop\\DESENVOLVIMENTO\\PYTHON\\Search-Files\\icons\\search.ico'

])