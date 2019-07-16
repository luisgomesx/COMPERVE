import os.path

def retornaCaminho():

    existencia_caminho = False

    while(existencia_caminho == False):
        caminho = input("Digite ou cole o caminho >> ")
        existencia_caminho = os.path.exists(caminho)

        if (existencia_caminho == False):
            print("Digite algum caminho válido!")

    return caminho

def retornaCaminhoComParametro(caminho_entrada):

    existencia_caminho = False

    while(existencia_caminho == False):

        existencia_caminho = os.path.exists(caminho_entrada)

        if (existencia_caminho == False):
            print("Digite algum caminho válido!")

    return caminho_entrada

