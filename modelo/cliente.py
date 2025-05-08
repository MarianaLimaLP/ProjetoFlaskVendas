import datetime

class Cliente:

    def __init__(self):
        self.__codcliente = 0
        self.__nome = ""
        self.__endereco = ""
        self.__lista='nome,endereco'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'cliente'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.nome}','{self.endereco}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = (("nome='{}',endereco='{}'  where codcliente={}")
        .format(self.nome,self.endereco, self.codcliente))

        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where codcliente={}".format(self.codcliente)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from cliente where codcliente={}".format(self.codcliente)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def codcliente(self):
        return self.__codcliente

    @codcliente.setter
    def codcliente(self, entrada):
        self.__codcliente = entrada

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self,entrada):
        self.__nome=entrada

    @property
    def endereco(self):
        return self.__endereco

    @endereco.setter
    def endereco(self, entrada):
        self.__endereco = entrada

    def __repr__(self):
        return self.__nome + ' ' + self.__endereco
