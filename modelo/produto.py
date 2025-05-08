import datetime

class Produto:

    def __init__(self):
        self.__codproduto = 0
        self.__nome = ""
        self.__preco = 0.0
        self.__lista='nome,preco'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'produto'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.nome}','{self.preco}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = (("nome='{}',preco='{}'  where codproduto={}")
        .format(self.nome, self.preco, self.codproduto))

        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where codproduto={}".format(self.codproduto)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from produto where codproduto={}".format(self.codproduto)
        return self.__dadosPesquisa

    @dadosPesquisa.setter
    def dadosPesquisa(self, entrada):
        self.__dadosPesquisa = entrada

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def codproduto(self):
        return self.__codproduto

    @codproduto.setter
    def codproduto(self, entrada):
        self.__codproduto = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,entrada):
        self.__nome=entrada

    @property
    def preco(self):
        return self.__preco

    @preco.setter
    def preco(self, entrada):
        self.__preco = entrada

    def __repr__(self):
        return self.__nome + ' ' + self.__preco
