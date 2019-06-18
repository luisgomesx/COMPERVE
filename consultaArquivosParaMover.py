import glob

from os import listdir
from os.path import isfile, join

def arquivosDoDiretorio(diretorio_raiz):

    arquivos_caminho = [f for f in glob.glob(diretorio_raiz + "*.jpg", recursive=True)]

    return arquivos_caminho #retorna os arquivos com a extensão .jpg no diretório informado com o nome do diretório

def qtdArquivosNoDiretorio(diretorio_raiz):

    arquivos_caminho = [f for f in glob.glob(diretorio_raiz + "*.jpg", recursive=True)]

    tamanho = len(arquivos_caminho) #retorna a quantidade de arquivos com a extensão .jpg no diretório informado

    return tamanho

def nomeArquivos(diretorio_arquivos):

    nome_arquivos = [f for f in listdir(diretorio_arquivos) if isfile(join(diretorio_arquivos, f))]

    return nome_arquivos # retorna apenas o nome dos arquivos

#print(nomeArquivos('D:/Usuários/Miguel/Desktop/moveGira/origem/'))

'''
Testes da funcao
print(qtdArquivosNoDiretorio('D:/Usuários/Miguel/Desktop/moveGira/origem/'))
for f in arquivosDoDiretorio('D:/Usuários/Miguel/Desktop/moveGira/origem/'):
    print(f)
 '''