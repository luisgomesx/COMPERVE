import numpy as np
import cv2
import os
import consultaArquivosParaMover
import retornaCaminho

'''
arquivos = consultaArquivosParaMover.nomeArquivos(retornaCaminho.retornaCaminho())
print(arquivos)
'''

def rotacionaReduzGrava(caminho_entrada, caminho_saida):

    arquivos = consultaArquivosParaMover.nomeArquivos(retornaCaminho.retornaCaminhoComParametro(caminho_entrada))
    print(arquivos)

    for img in arquivos:

        os.chdir(caminho_entrada) #Torna o caminho de entrada referência

        imagem = cv2.imread(img) # TEMPORÁRIO | Ler o arquivo na posição [0] do bloco de imagens de entrada

        altura, largura = imagem.shape[:2] # Captura as dimensões da imagem

        angulo_rotacao = 90 # Angulo em graus, no sentido anti-horário, que a imagem será rotacionada
        tamanho_final = 0.6 # Tamanho final da imagem em relação ao original

        larguraNew = (int(altura * tamanho_final) - 2)  # ajuste da largura pós rotação e redução
        alturaNew = (int(largura * tamanho_final) - 10)  # ajuste da altura pós rotação e redução

        ponto = (largura * 0.5, altura * 0.5)  # ponto no centro da figura, referência da rotação

        # rotacao
        print("Girando o arquivo " + img + " ...") # TEMPORÁRIO | Mensagem1 de giro do arquivo na posição [0]
        rotacao = cv2.getRotationMatrix2D(ponto, angulo_rotacao, tamanho_final)  # rotaciona angulo_rotacao graus e daixa a imagem com tamanho_final do tamanho original
        rotacionado = cv2.warpAffine(imagem, rotacao, (altura, largura)) #imagem rotacionada

        print(img + " girado!") # TEMPORÁRIO | Mensagem2 de giro do arquivo na posição [0]

        # translacao (deslocamento)
        print("Deslocando o arquivo " + img + " ...") # TEMPORÁRIO | Mensagem1 de translação do arquivo na posição [0]

        deslocamento = np.float32([[1, 0, -137], [0, 1, -713]])  # para 60% | posicionando a imagem corretamente
        deslocado = cv2.warpAffine(rotacionado, deslocamento, (larguraNew, alturaNew)) #imgem rotacionada e ajustada

        print(img + " Deslocado!") # TEMPORÁRIO | Mensagem2 de translação do arquivo na posição [0]

        os.chdir(caminho_saida)  # Trocando diretório de referência, para poder salvar na pasta de destino

        print("salvando o arquivo " + img) # TEMPORÁRIO

        cv2.imwrite(os.path.join(img), deslocado)  # gravando imagem em self.caminho_saida

        print(img + " salvo em " + caminho_saida)

entrada = retornaCaminho.retornaCaminho()
saida = retornaCaminho.retornaCaminho()
rotacionaReduzGrava(entrada, saida)