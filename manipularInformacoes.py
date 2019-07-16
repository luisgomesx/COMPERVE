class Informacoes:

    def __init__(self, nome_arquivo):

        self.nome_arquivo = nome_arquivo
        self.dados_nome = nome_arquivo.split(' ')

    def getInscricao(self):
        inscricao = self.dados_nome[1][3:12]
        return inscricao

    def getNomeBanco(self):
        banco_nome = self.dados_nome[0]
        return banco_nome

    def getTurma(self):
        turma = self.dados_nome[1][12:15]
        return turma

    def getOrdem(self):
        ordem = self.dados_nome[1][15:18]
        return ordem