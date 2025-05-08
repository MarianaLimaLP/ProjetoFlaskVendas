from controle.conectarbanco import *

class ControleGenerico:

    def __init__(self):
        self.ob = Banco()
        self.ob.configura(ho="177.190.74.69",
                          db="tpc06",
                          us="trabtpc",
                          se="trabtpc",
                          po=65004)

    def incluir(self, objeto):
        self.ob.abrirConexao()
        sql = f"INSERT INTO {objeto.tabelaBanco} ({objeto.lista}) VALUES ({objeto.dadosInserir})"

        try:
            self.ob.execute(sql)
            self.ob.gravar()
            return self.ob.lastInsertId()
        except Exception as e:
            print(f"Houve um erro ao incluir: {e}")
            self.ob.descarte()
            return None

    def alterar(self, objeto):
        self.ob.abrirConexao()
        sql = f"UPDATE {objeto.tabelaBanco} SET {objeto.dadosUpdate}"

        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except Exception as e:
            print(f"Houve um erro ao alterar: {e}")
            self.ob.descarte()

    def delete(self, objeto):
        self.ob.abrirConexao()
        sql = "delete from {} ".format(objeto.tabelaBanco)
        sql += objeto.dadosDelete

        try:
            self.ob.execute(sql)
            self.ob.gravar()
        except Exception as e:
            print(f"Houve um erro ao excluir: {e}")
            self.ob.descarte()

    def procuraRegistro(self,objeto):
        self.ob.abrirConexao()

        objeto = self.ob.selectQuery(objeto.dadosPesquisa)
        return objeto

    def procuraRegistroEspecifico(self,query):
        self.ob.abrirConexao()

        objeto = self.ob.selectQuery(query)
        return objeto

    def apagar(self,entrada):
        self.ob.abrirConexao()
        sql = "delete from aluno where idaluno = {}".format(entrada)
        self.ob.execute(sql)
        self.ob.gravar()

    def listarTodos(self,objeto):
        self.ob.abrirConexao()
        dados = self.ob.selectQuery("select * from {}".format(objeto.tabelaBanco))
        return dados




