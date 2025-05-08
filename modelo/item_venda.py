import datetime

from controle.controle_produto import ControleProduto
from controle.controle_venda import ControleVenda

class ItemVenda:

    def __init__(self):
        self.__codvenda = 0
        self.__codproduto = 0
        self.__qtde = 0
        self.__valor = 0.0
        self.__lista='codvenda,codproduto,qtde,valor'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'itemvenda'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.codvenda}','{self.codproduto}','{self.qtde}','{self.valor}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = (("qtde='{}',valor='{}' where codvenda={} and codproduto = {}")
        .format(self.qtde, self.valor, self.codvenda, self.codproduto))

        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "where codvenda={} and codproduto = {}".format(self.codvenda,self.codproduto)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from itemvenda where codvenda = {} and codproduto = {}".format(self.codvenda,self.codproduto)
        return self.__dadosPesquisa

    @property
    def tabelaBanco(self):
        return self.__tabelaBanco

    @property
    def codvenda(self):
        return self.__codvenda

    @codvenda.setter
    def codvenda(self, entrada):
        self.__codvenda = entrada

    @property
    def codproduto(self):
        return self.__codproduto

    @codproduto.setter
    def codproduto(self,entrada):
        self.__codproduto=entrada

    @property
    def qtde(self):
        return self.__qtde

    @qtde.setter
    def qtde(self, entrada):
        self.__qtde = entrada

    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, entrada):
        self.__valor = entrada

    def __repr__(self):
        return  ControleVenda.pesquisaCodigo(self.__codvenda) + ' ' + ControleProduto.pesquisaCodigo(self.__codproduto) + ' ' + str(self.__qtde) + ' ' + str(self.__valor)
