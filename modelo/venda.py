import datetime

from controle.controle_cliente import ControleCliente

class Venda:

    def __init__(self):
        self.__codvenda = 0
        self.__codcliente = 0
        self.__data = ""
        self.__valor_total = 0.0
        self.__lista='codcliente,data,valor_total'

        self.__dadosInserir=""
        self.__dadosUpdate=""
        self.__dadosDelete=""
        self.__dadosPesquisa=""
        self.__tabelaBanco = 'venda'

    @property
    def lista(self):
        return self.__lista

    @property
    def dadosInserir(self):
        self.__dadosInserir = f"'{self.codcliente}','{self.data}','{self.valor_total}'"
        return self.__dadosInserir

    @property
    def dadosUpdate(self):
        self.__dadosUpdate = (("codcliente='{}',data='{}',valor_total='{}'  where codvenda={}")
        .format(self.codcliente, self.data, self.valor_total, self.codvenda))

        return self.__dadosUpdate

    @property
    def dadosDelete(self):
        self.__dadosDelete = "codvenda = {}".format(self.codvenda)
        return self.__dadosDelete

    @property
    def dadosPesquisa(self):
        self.__dadosPesquisa = "select * from venda where codvenda={}".format(self.codvenda)
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
    def codcliente(self):
        #return ControleCliente.pesquisaCodigo(self)
        return self.__codcliente

    @codcliente.setter
    def codcliente(self,entrada):
        self.__codcliente=entrada

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, entrada):
        self.__data = entrada

    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, entrada):
        self.__valor_total = entrada

    def converte_data_str(self, data):
        if isinstance(data, datetime.date):
            return data.strftime("%d/%m/%Y")
        return str(data)

    def __repr__(self):
        if isinstance(self.__data,str):
           return ControleCliente.pesquisaCodigo(self.__codcliente) +' ' + self.__data+' '+str(self.__valor_total)
        if isinstance(self.__data,datetime.date):
           return ControleCliente.pesquisaCodigo(self.__codcliente) + ' ' + self.converte_data_str(self.__data) + ' ' + str(self.__valor_total)
