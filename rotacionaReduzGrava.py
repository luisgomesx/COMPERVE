import numpy as np
import cv2
import os
import time
import consultaArquivosParaMover
import retornaCaminho
import manipularInformacoes

'''
arquivos = consultaArquivosParaMover.nomeArquivos(retornaCaminho.retornaCaminho())
print(arquivos)
'''

def rotacionaReduzGrava(caminho_entrada, caminho_saida):


    arquivos = consultaArquivosParaMover.nomeArquivos(retornaCaminho.retornaCaminhoComParametro(caminho_entrada))
    print(arquivos)

    cont = 0

    start = time.time()

    for img in arquivos:

        os.chdir(caminho_entrada) #Torna o caminho de entrada referência

        Informacoes = manipularInformacoes.Informacoes(img)

        cont += 1

        print("- INSCRIÇÃO:", Informacoes.getInscricao(),"(", cont, "de", len(arquivos), ")")

        imagem = cv2.imread(img) # TEMPORÁRIO | Ler o arquivo na posição [0] do bloco de imagens de entrada

        altura, largura = imagem.shape[:2] # Captura as dimensões da imagem

        angulo_rotacao = 90 # Angulo em graus, no sentido anti-horário, que a imagem será rotacionada
        tamanho_final = 0.6 # Tamanho final da imagem em relação ao original

        larguraNew = (int(altura * tamanho_final) - 2)  # ajuste da largura pós rotação e redução
        alturaNew = (int(largura * tamanho_final) - 10)  # ajuste da altura pós rotação e redução

        ponto = (largura * 0.5, altura * 0.5)  # ponto no centro da figura, referência da rotação

        # rotacao
        print("      -> Girando (inscrição: " + Informacoes.getInscricao()+")") # TEMPORÁRIO | Mensagem1 de giro do arquivo na posição [0]
        rotacao = cv2.getRotationMatrix2D(ponto, angulo_rotacao, tamanho_final)  # rotaciona angulo_rotacao graus e daixa a imagem com tamanho_final do tamanho original
        rotacionado = cv2.warpAffine(imagem, rotacao, (altura, largura)) #imagem rotacionada

        # translacao (deslocamento)
        print("      -> Ajustando (inscrição: " + Informacoes.getInscricao()+")") # TEMPORÁRIO | Mensagem1 de translação do arquivo na posição [0]

        deslocamento = np.float32([[1, 0, -137], [0, 1, -713]])  # para 60% | posicionando a imagem corretamente
        deslocado = cv2.warpAffine(rotacionado, deslocamento, (larguraNew, alturaNew)) #imgem rotacionada e ajustada

        os.chdir(caminho_saida)  # Trocando diretório de referência, para poder salvar na pasta de destino

        print("      -> Salvando (inscrição: " + Informacoes.getInscricao()+")") # TEMPORÁRIO

        cv2.imwrite(os.path.join(img), deslocado)  # gravando imagem em self.caminho_saida

    end = time.time()

    tempo = end - start

    print("\nCopiadas", len(arquivos), "imagens. Tempo transcorrido", str(tempo)[:4]+"s")


entrada = retornaCaminho.retornaCaminho()
saida = retornaCaminho.retornaCaminho()
rotacionaReduzGrava(entrada, saida)