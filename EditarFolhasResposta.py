import numpy as np
import cv2
import os

class EditarFolhasResposta:

    def __init__(self, caminho_entrada, caminho_saida, nome_banco, status, bloco_entrada, bloco_saida):
        self.caminho_entrada = caminho_entrada
        self.caminho_saida = caminho_saida
        self.nome_banco = nome_banco
        self.status = status
        self.bloco_entrada = bloco_entrada
        self.bloco_saida = bloco_saida

    def giraGrava(self):

        os.chdir(self.caminho_entrada) #Torna o caminho de entrada referência

        imagem = cv2.imread(self.bloco_entrada[0]) # TEMPORÁRIO | Ler o arquivo na posição [0] do bloco de imagens de entrada

        altura, largura = imagem.shape[:2] # Captura as dimensões da imagem

        angulo_rotacao = 90 # Angulo em graus, no sentido anti-horário, que a imagem será rotacionada
        tamanho_final = 0.6 # Tamanho final da imagem em relação ao original

        larguraNew = (int(altura * tamanho_final) - 2)  # ajuste da largura pós rotação e redução
        alturaNew = (int(largura * tamanho_final) - 10)  # ajuste da altura pós rotação e redução

        ponto = (largura * 0.5, altura * 0.5)  # ponto no centro da figura, referência da rotação

        # rotacao
        print("Girando o arquivo " + self.bloco_entrada[0] + " ...") # TEMPORÁRIO | Mensagem1 de giro do arquivo na posição [0]
        rotacao = cv2.getRotationMatrix2D(ponto, angulo_rotacao, tamanho_final)  # rotaciona angulo_rotacao graus e daixa a imagem com tamanho_final do tamanho original
        rotacionado = cv2.warpAffine(imagem, rotacao, (altura, largura)) #imagem rotacionada

        print(self.bloco_entrada[0] + " girado!") # TEMPORÁRIO | Mensagem2 de giro do arquivo na posição [0]

        # translacao (deslocamento)
        print("Deslocando o arquivo " + self.bloco_entrada[0] + " ...") # TEMPORÁRIO | Mensagem1 de translação do arquivo na posição [0]

        deslocamento = np.float32([[1, 0, -137], [0, 1, -713]])  # para 60% | posicionando a imagem corretamente
        deslocado = cv2.warpAffine(rotacionado, deslocamento, (larguraNew, alturaNew)) #imgem rotacionada e ajustada

        print(self.bloco_entrada[0] + " Deslocado!") # TEMPORÁRIO | Mensagem2 de translação do arquivo na posição [0]

        os.chdir(self.caminho_saida)  # Trocando diretório de referência, para poder salvar na pasta de destino

        print("salvando o arquivo " + self.bloco_entrada[0]) # TEMPORÁRIO

        cv2.imwrite(os.path.join(self.bloco_entrada[0]), deslocado)  # gravando imagem em self.caminho_saida

        print(self.bloco_entrada[0] + " salvo em " + self.caminho_saida)