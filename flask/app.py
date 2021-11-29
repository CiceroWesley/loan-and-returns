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


app.config['SECRET_KEY'] = os.urandom(24)

@app.route('/')
def root():
    return (render_template('index.html'))

@app.route('/equipamento/cadastrar',methods=['POST','GET'])
def cadastrar_equipamento():
    form = EquipamentoForm()
    if form.validate_on_submit():
        return(redirect(url_for('root')))
    return (render_template('form.html',form=form,action=url_for('cadastrar_equipamento')))

@app.route('/usuario/cadastrar',methods=['POST','GET'])
def cadastrar_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        return(redirect(url_for('root')))
    return (render_template('form.html',form=form,action=url_for('cadastrar_usuario')))

if __name__ == "__main__":
    serve(app, host='0.0.0.0', port=80, url_prefix='/app')
