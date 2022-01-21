from produto import Produto
#flask é um servidor web do python
#pip3 install flask==0.12.2
from flask import Flask, render_template, request, redirect, session, flash

app = Flask(__name__)
app.secret_key = "softgraf"

p1 = Produto(1, 'TV LG 40"', 1999, 10)
p2 = Produto(2, 'Computador i5', 3999, 5)
p3 = Produto(3, 'Liquidificador Britania', 199, 20)
lista = [p1, p2, p3]

@app.route('/')
def inicio():
    return render_template('relatorio.html', titulo='Relatório de Estoque', produtos = lista)

@app.route('/cadastrar')
def cadastrar():
    if 'usuario_logado' not in session or session['usuario_logado'] == None:
        return redirect('/login')
    return render_template('cadastro.html', titulo="Cadastro de Produtos")

@app.route('/salvar', methods = ['post'])
def salvar():
    #recupera as variáveis do formulário do cadastro
    codigo = request.form['codigo']
    descricao = request.form['descricao']
    precoUnitario = request.form['precoUnitario']
    quantEstoque = request.form['quantEstoque']
    produto = Produto(codigo, descricao, precoUnitario, quantEstoque)
    lista.append(produto)
    flash('Novo produto cadastrado.')
    return redirect('/')

@app.route('/login')
def login():
    return render_template('login.html', titulo="Login")

@app.route('/autenticar', methods = ['post'])
def autenticar():
    if request.form['senha'] == 'abc':
        session['usuario_logado'] = request.form['usuario']
        flash(request.form['usuario'] + ' logou com sucesso!')

        return redirect('/')
    else:
        flash('Senha inválida! Tente novamente.')
        return redirect('/login')

@app.route('/logout')
def logout():
    session['usuario_logado'] = None
    flash('Nenhum usuário logado.')
    return redirect('/')

if __name__ == '__main__':

    app.run(debug=True)

