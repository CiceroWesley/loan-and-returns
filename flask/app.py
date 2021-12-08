from flask import Flask
from waitress import serve
from flask import render_template
from flask import request,url_for,redirect,flash,session
from flask_session import Session
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
import logging
import os
from datetime import date, datetime

from formEmprestimo import EmprestimoForm
from formEquipamento import EquipamentoForm
from formUsuario import UsuarioForm
from formLogin import LoginForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
CSRFProtect(app)
CSV_DIR = '/flask/'

app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = os.urandom(24)
app.config['WTF_CSRF_SSL_STRICT'] = False
Session(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + CSV_DIR + 'bd.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
db.init_app(app)

from Usuarios import Usuario
from Equipamentos import Equipamento
from Emprestimo import Emprestimo

@app.before_first_request
def inicializar_bd():
    db.create_all()

@app.route('/')
def root():
    return (render_template('index.html'))

@app.route('/equipamento/cadastrar',methods=['POST','GET'])
def cadastrar_equipamento():
    form = EquipamentoForm()
    if form.validate_on_submit():
        nome = request.form['nome']
        novoEquipamento = Equipamento(nome=nome)
        db.session.add(novoEquipamento)
        db.session.commit()
        return(redirect(url_for('root')))
    return (render_template('form.html',form=form,action=url_for('cadastrar_equipamento')))

@app.route('/usuario/cadastrar',methods=['POST','GET'])
def cadastrar_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        nome = request.form['nome']
        username = request.form['username']
        email = request.form['email']
        senha = request.form['senha']
        User = Usuario(name=nome,username=username,email=email,password=senha)
        db.session.add(User)
        db.session.commit()
        return(redirect(url_for('root')))
    return (render_template('form.html',form=form,action=url_for('cadastrar_usuario')))

@app.route('/equipamento/listar')
def listar_equipamentos():
    #selecionar os equipamentos e mostrar no template equipamentos
    return ('Falta implementar')

@app.route('/equipamento/listar_emprestimos')
def listar_emprestimos():
    return ('Falta')

@app.route('/usuario/listar')
def listar_usuarios():
    #selecionar os usuarios e mostrar no template usuarios
    return('Falta implementar')

@app.route('/equipamento/emprestar',methods=['POST','GET'])
def emprestar_equipamento():
    #esta dando erro, verificar oque é
    #return('teste')
    form = EmprestimoForm()
    equipamentos = Equipamento.query.filter(Equipamento.disponivel == True).order_by(Equipamento.nome).all()
    form.equipamento.choices = [(e.id,e.nome) for e in equipamentos]

    if form.validate_on_submit():
        nome = request.form['nome']
        equipamento = int(request.form['equipamento'])
        novoEmprestimo = Emprestimo(id_usuario=1,nome_pessoa=nome,id_equipamento=equipamento)
        equipamentoAlterado = Equipamento.query.get(equipamento)
        equipamentoAlterado.disponivel = False
        db.session.add(novoEmprestimo)
        db.session.commit()
        return(redirect(url_for('root')))
    return(render_template('form.html',form=form,action=url_for('emprestar_equipamento')))

@app.route('/equipamento/devolver/<id_emprestimo>',methods=['POST','GET'])
def devolver_equipamento(id_emprestimo):
    id_emprestimo = int(id_emprestimo)
    emprestimo = Emprestimo.query.get(id_emprestimo)
    emprestimo.data_devolucao = datetime.now()
    equipamento = Equipamento.query.get(emprestimo.id_equipamento)
    equipamento.disponivel = True
    db.session.commit()
    return (redirect(url_for('root')))

@app.route('/equipamento/remover/<id_emprestimo>',methods=['POST','GET'])
def remover_emprestimo(id_emprestimo):
    id_emprestimo = int(id_emprestimo)
    emprestimo = Emprestimo.query.get(id_emprestimo)
    id_equipamento = Emprestimo.id_equipamento
    equipamento = Equipamento.query.get(id_equipamento)
    equipamento.disponivel = True
    db.session.delete(emprestimo)
    db.session.commit()
    return (redirect(url_for('root')))

@app.route('/usuario/login',methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        usuario = request.form['usuario']
        senha = request.form['senha']
        registro = Usuario.query.filter(Usuario.username == usuario,Usuario.password == senha).all()
        if(len(registro) > 0):
            session['autenticado'] = True
            session['usuario'] = registro[0].id
            return(redirect(url_for('root')))
    return (render_template('form.html',form=form,action=url_for('login')))
    

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/app')
