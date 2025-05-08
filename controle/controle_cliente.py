import json

from modelo.cliente import Cliente
from controle.controleGenerico import ControleGenerico

class ControleCliente(ControleGenerico):

    def incluirCliente(self,cliente):
        self.incluir(cliente)

    def alterarCliente(self, cliente):
        self.alterar(cliente)

    def deletarCliente(self, cliente):
        self.delete(cliente)

    def pesquisaCodigo(self, codcliente):
        entrada = Cliente()
        entrada._dadosPesquisa = f"SELECT * FROM Cliente WHERE codcliente = {codcliente}"

        resultado = self.procuraRegistro(entrada)
        retorno = Cliente()

        if resultado and len(resultado) >= 1:
            retorno = self.converte_cliente(resultado)

        return retorno

    def converte_cliente(self,cliente):
        retorno = Cliente()
        retorno.idcliente = cliente[0][0]
        retorno.nome = cliente[0][1]
        retorno.endereco = cliente[0][2]
        retorno.cidade = cliente[0][3]
        retorno.uf = cliente[0][4]
        retorno.cep = cliente[0][5]
        retorno.credito = cliente[0][6]
        retorno.saldo = cliente[0][7]
        return retorno

    def listarTodosRegistros(self,objeto):
        return self.listarTodos(objeto)

    def converteObjeto(self, entrada):
        if not entrada or len(entrada) < 8:
            raise ValueError("Dados inválidos para conversão em Cliente.")

        cliente = Cliente()
        cliente.idcliente = entrada[0]
        cliente.nome = entrada[1]
        cliente.endereco = entrada[2]
        cliente.cidade = entrada[3]
        cliente.uf = entrada[4]
        cliente.cep = entrada[5]
        cliente.credito = entrada[6]
        cliente.saldo = entrada[7]

        return cliente

    def dadosJson(self,dados):
        retorno = {}
        retorno = {'idcliente': dados.idcliente,
                   'nome': dados.nome,
                   'endereco': dados.endereco,
                   'cidade': dados.cidade,
                   'uf': dados.uf,
                   'cep': dados.cep,
                   'credito': str(dados.credito),
                   'saldo': str(dados.saldo)
                   }
        return json.dumps(retorno)


