from flask import Flask
from waitress import serve
from flask import render_template
from flask import request,url_for,redirect,flash,session
from flask_bootstrap import Bootstrap
from flask_wtf.csrf import CSRFProtect
import logging
import os

from formEquipamento import EquipamentoForm
from formUsuario import UsuarioForm

app = Flask(__name__)
bootstrap = Bootstrap(app)
CSRFProtect(app)
CSV_DIR = '/flask/'

app.config['SECRET_KEY'] = os.urandom(24)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + CSV_DIR + 'bd.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
from database import db
db.init_app(app)

from Usuarios import Usuario
from Equipamentos import Equipamento

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


@app.route('/usuario/listar')
def listar_usuarios():
    #selecionar os usuarios e mostrar no template usuarios
    return('Falta implementar')



if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/app')
