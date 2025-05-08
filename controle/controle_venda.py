import json

from modelo.venda import Venda
from controle.controleGenerico import ControleGenerico

class ControleVenda(ControleGenerico):

    def incluirVenda(self, venda):
        venda.codvenda = self.incluir(venda)
        return venda.codvenda

    def alterarVenda(self, venda):
        if venda.codvenda is None:
            raise ValueError("O código da venda não pode ser None.")
        self.alterar(venda)

    def deletarVenda(self, venda):
        if venda.codvenda is None:
            raise ValueError("O código da venda não pode ser None.")
        self.delete(venda)

    def pesquisaCodigo(self, entrada: Venda):
        venda = self.procuraRegistro(entrada)
        retorno = Venda()
        if len(venda) >= 1:
            retorno = self.converte_venda(venda)
        return retorno

    def listarProdutosDaVenda(self, codvenda):
        try:
            query = f"SELECT p.nome, p.preco, iv.qtde, iv.valor FROM itemvenda iv JOIN produto p ON iv.codproduto = p.codproduto WHERE iv.codvenda = {codvenda}"
            resultados = self.procuraRegistroEspecifico(query)

            print(resultados)
            return [
                {"nome": r[0], "preco": r[1], "qtde": r[2], "valor": r[3]}
                for r in resultados
            ]
            #return resultados

        except Exception as e:
            print("Erro ao buscar produtos da venda:", e)
            return []

    def converte_venda(self, venda):
        retorno = Venda()
        retorno.idvenda = venda[0][0]
        retorno.cliente = venda[0][1]
        retorno.data = venda[0][2]
        retorno.valortotal = venda[0][3]
        return retorno

    def listarTodosRegistros(self, objeto):
        return self.listarTodos(objeto)

    def converteObjeto(self, entrada):
        if not entrada or len(entrada) < 4:
            raise ValueError("Dados inválidos para conversão em Venda.")
        venda = Venda()
        venda.idvenda = entrada[0]
        venda.cliente = entrada[1]
        venda.data = entrada[2]
        venda.valortotal = entrada[3]
        return venda
