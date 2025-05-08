from flask import Flask, render_template, request, redirect

from controle.controle_cliente import ControleCliente
from controle.controle_produto import ControleProduto
from controle.controle_venda import ControleVenda
from controle.controle_item_venda import ControleItemVenda

from modelo.cliente import Cliente
from modelo.produto import Produto
from modelo.venda import Venda
from modelo.item_venda import ItemVenda

from datetime import datetime
app = Flask(__name__)

daoCliente = ControleCliente()
daoProduto = ControleProduto()
daoVenda = ControleVenda()
daoItemVenda = ControleItemVenda()

@app.route('/')
def principal():
    return render_template('index.html')

@app.route('/cadastrar/<tipo>')
def cadastrar(tipo):
    if tipo == 'cliente':
        campos = [
            {'nome': 'nome', 'label': 'Nome do Cliente'},
            {'nome': 'endereco', 'label': 'Endereço'}
        ]
    elif tipo == 'produto':
        campos = [
            {'nome': 'nome', 'label': 'Nome do Produto'},
            {'nome': 'preco', 'label': 'Preço'}
        ]
    else:
        return 'Tipo inválido', 404

    return render_template('cadastro.html', titulo=f'Cadastrar {tipo.capitalize()}', tipo=tipo, campos=campos)

@app.route('/salvar/<tipo>', methods=['POST'])
def salvar(tipo):
    if tipo == 'cliente':
        cliente = Cliente()
        cliente.nome = request.form['nome']
        cliente.endereco = request.form['endereco']

        daoCliente.incluir(cliente)
    elif tipo == 'produto':
        produto = Produto()
        produto.nome = request.form['nome']
        produto.preco = request.form['preco']

        daoProduto.incluir(produto)
    else:
        return 'Tipo inválido', 404

    return redirect(f'/lista/{tipo}')

@app.route('/lista/<tipo>')
def listar(tipo):
    if tipo == 'cliente':
        lista = daoCliente.listarTodosRegistros(Cliente())
        titulo = 'Lista de Clientes'
    elif tipo == 'produto':
        lista = daoProduto.listarTodosRegistros(Produto())
        titulo = 'Lista de Produtos'
    else:
        return 'Tipo inválido', 404

    return render_template('lista.html', lista=lista, tipo=tipo, titulo=titulo)

@app.route('/venda')
def form_venda():
    clientes = daoCliente.listarTodosRegistros(Cliente())
    produtos = daoProduto.listarTodosRegistros(Produto())
    return render_template('venda.html', clientes=clientes, produtos=produtos)

@app.route('/efetuar_venda', methods=['POST'])
def efetuar_venda():
    codcliente = int(request.form['codcliente'])
    produtos_selecionados = request.form.getlist('codproduto')
    quantidades = request.form.getlist('qtde')

    venda = Venda()
    venda.codcliente = codcliente
    venda.data = datetime.now()  # Adicionei a data para garantir que o campo "data" seja preenchido

    # Inclui a venda no banco e gera o codvenda
    venda.codvenda = daoVenda.incluir(venda)  # Aqui a venda tem o codvenda atribuído corretamente

    valor_total = 0

    for i in range(len(produtos_selecionados)):
        print("produtos")
        codproduto = int(produtos_selecionados[i])
        qtde = int(quantidades[i])
        produto = daoProduto.pesquisaCodigo(codproduto)
        valor = produto.preco * qtde

        item = ItemVenda()
        item.codvenda = venda.codvenda  # Agora o codvenda já está atribuído corretamente
        item.codproduto = codproduto
        item.qtde = qtde
        item.valor = valor
        daoItemVenda.incluir(item)
        valor_total = valor_total + valor

    venda.valor_total = valor_total
    print(f"valor total {valor_total}")
    daoVenda.alterarVenda(venda)  # Atualiza a venda com o valor total

    return redirect('/')

#@app.route("/vendas")
#def tela_venda():
 #   vendas = daoVenda.listarTodosRegistros(Venda())
 #   itens = daoItemVenda.listarTodosRegistros(ItemVenda())
  #  produtos = daoProduto.listarTodosRegistros(Produto())
  #  return render_template("vendas.html", vendas=vendas, itens_venda=itens, produtos=produtos)

@app.route("/vendas")
def listar_vendas():
    vendas = daoVenda.listarTodosRegistros(Venda())
    return render_template("vendas.html", vendas=vendas)

@app.route("/vendas/<int:codvenda>")
def produtos_da_venda(codvenda):
    produtos = daoVenda.listarProdutosDaVenda(codvenda)
    return render_template("produtos_venda.html", codvenda=codvenda, produtos=produtos)

if __name__ == '__main__':
    app.run(debug=True)
