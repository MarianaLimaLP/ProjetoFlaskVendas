import json

from modelo.produto import Produto
from controle.controleGenerico import ControleGenerico

class ControleProduto(ControleGenerico):

    def incluirProduto(self,produto):
        self.incluir(produto)

    def alterarProduto(self, produto):
        self.alterar(produto)

    def deletarProduto(self, produto):
        self.delete(produto)

    def pesquisaCodigo(self, codproduto):
        entrada = Produto()
        entrada.codproduto = codproduto
        resultado = self.procuraRegistro(entrada)

        if len(resultado) >= 1:
            return self.converte_produto(resultado)
        return None

    def converte_produto(self,produto):
        retorno = Produto()
        retorno.codproduto = produto[0][0]
        retorno.nome = produto[0][1]
        retorno.preco = produto[0][2]
        return retorno

    def listarTodosRegistros(self,objeto):
        return self.listarTodos(objeto)

    def converteObjeto(self,entrada):
        if not entrada or len(entrada) < 4:
            raise ValueError("Dados inválidos para conversão em Produto.")

        produto = Produto()
        produto.codproduto = entrada[0]
        produto.nome = entrada[1]
        produto.preco = entrada[2]
        return produto

    def dadosJson(self,dados):
        retorno = {}
        retorno = {'codproduto': dados.codproduto,
                   'nome': dados.nome,
                   'preco': str(dados.preco),
                   }
        return json.dumps(retorno)


