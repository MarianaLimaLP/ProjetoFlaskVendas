import json

from modelo.item_venda import ItemVenda
from controle.controleGenerico import ControleGenerico

from controle.controle_produto import ControleProduto
from controle.controle_venda import ControleVenda

class ControleItemVenda(ControleGenerico):

    def incluirItemVenda(self,itemvenda):
        self.incluir(itemvenda)

    def alterarItemVenda(self, itemvenda):
        self.alterar(itemvenda)

    def deletarItemVenda(self, itemvenda):
        self.delete(itemvenda)

    def pesquisaCodigo(self,entrada:ItemVenda):
        itemvenda = self.procuraRegistro(entrada)
        retorno = ItemVenda()
        if len(itemvenda) >= 1:
           retorno = self.converte_itemvenda(itemvenda)
        return retorno

    def converte_itemvenda(self,itemvenda):
        retorno = ItemVenda()
        retorno.venda = itemvenda[0][0]
        retorno.produto = itemvenda[0][1]
        retorno.qtde = itemvenda[0][2]
        retorno.valor = itemvenda[0][3]
        return retorno

    def listarTodosRegistros(self,objeto):
        return self.listarTodos(objeto)

    def converteObjeto(self,entrada):
        if not entrada or len(entrada) < 4:
            raise ValueError("Dados inválidos para conversão em ItemVenda.")

        itemvenda = ItemVenda()
        itemvenda.venda = entrada[0]
        itemvenda.produto = entrada[1]
        itemvenda.qtde = entrada[2]
        itemvenda.valor = entrada[3]
        return itemvenda

    def dadosJson(self,dados):
        retorno = {}
        retorno = {'venda': ControleVenda.pesquisaCodigo(dados.venda),
                   'produto': ControleProduto.pesquisaCodigo(dados.produto),
                   'qtde': str(dados.qtde),
                   'valor': str(dados.valor)
                   }
        return json.dumps(retorno)


