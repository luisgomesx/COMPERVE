import numpy as np
import cv2
import os

def giraGrava(nome_arquivo):

caminho = 'D:/Usuários/Miguel/Desktop/moveGira/destino/' #Diretório

imagemName = "letras_libras_201902 00140000063601004601.jpg" #Nome da imagem que será girada
imagem = cv2.imread(imagemName)
#print(imagem.shape)
altura, largura = imagem.shape[:2]
#cv2.imshow("Original",imagem) # Mostra a imagem com ("Nome da tela", arquivo_de_imagem)

larguraNew = (int(altura*0.6)-2) #ajuste da largura pós rotação e  redução
alturaNew = (int(largura*0.6)-10) #ajuste da altura pós rotação e  redução

ponto = (largura*0.5, altura*0.5)  # ponto no centro da figura, referência da rotação

# rotacao
print("Girando o arquivo "+imagemName+" ...")
rotacao = cv2.getRotationMatrix2D(ponto, 90, 0.6) # rotaciona 90 graus e daixa a imagem com 60% do tamonho
rotacionado = cv2.warpAffine(imagem, rotacao, (altura, largura))
#cv2.imshow("Rotacionado 90 graus", rotacionado)
print(imagemName+" girado!")

# translacao (deslocamento)
print("Deslocando o arquivo "+imagemName+" ...")
#deslocamento = np.float32([[1, 0, -260], [0, 1, -801]]) para 50%
#deslocamento = np.float32([[1, 0, -11], [0, 1, -660]]) #para 70%
deslocamento = np.float32([[1, 0, -137], [0, 1, -713]]) #para 60%
deslocado = cv2.warpAffine(rotacionado, deslocamento, (larguraNew, alturaNew))
#cv2.imshow("Rodado e deslocado", deslocado)
#cv2.waitKey(0)
print(imagemName+" Deslocado!")

os.chdir(caminho) # Trocando diretório de referência, para poder salvar na pasta de destino

print("salvando o arquivo "+imagemName)

cv2.imwrite(os.path.join(imagemName), deslocado) #gravando imagem

dados_nome = imagemName.split(' ')

dados_parte1 = dados_nome[1]
print(dados_parte1)

banco_nome = dados_nome[0]
print(banco_nome)

inscricao = dados_parte1[3:12]
print(inscricao)

print(imagemName+" salvo em "+caminho)

cv2.destroyAllWindows()