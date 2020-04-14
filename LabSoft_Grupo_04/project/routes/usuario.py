# ======= Flask Imports ======= #
from flask import render_template, url_for, redirect,flash, request
#from flash_login import login_required, login_user, logout_user

# ======= Project Imports ======= #
from project import app, db
from project.forms.usuarioSchema import UsuarioForm
from project.models.usuario import Usuario

# ======= External Library Imports ======= #
from datetime import datetime

@app.route('/cadastrar_usuario', methods=['GET', 'POST'])
def cadastrar_usuario():
    form = UsuarioForm()
    if form.validate_on_submit():
        usuario = Usuario(nome = form.nome.data, cpf = form.cpf.data, email = form.email.data, senha = form.senha.data)    
        db.session.add(usuario)
        db.session.commit()
        flash('Usuario cadastrado com sucesso!')
        return redirect(url_for('listar_usuarios'))
    return render_template('cadastrar_usuario.html', title='Cadastrar Usuario', form=form)

@app.route('/usuarios_cadastrados')
def listar_usuarios():
    usuarios = Usuario.query.order_by(Usuario.usuario_id).all()
    return render_template('usuario_cadastrados.html', title='Usuarios cadastrados', usuarios=usuarios)

@app.route('/usuario/<int:usuario_id>', methods=['GET', 'POST'])
def visualizar_usuario(usuario_id):
        usuario= usuario.query.get_or_404(usuario_id)
        return render_template('visualizar_usuario.html', title='Usuario {usuario.nome}', usuario=usuario)

@app.route('/usuario/<int:usuario_id>/atualizar', methods=['GET', 'POST'])
def atualizar_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(id)
    form = UsuarioForm()
    if form.validate_on_submit():
        usuario.nome = form.nome.data
        usuario.cpf = form.cpf.data
        usuario.email = form.email.data
        db.session.commit()
        flash('Dados atualizados com sucesso!')
        return redirect(url_for('visualizar_usuario', usuario_id=usuario_id))
    return render_template('cadastrar_usuario.html', title='Atualizar UsuariO', legend="Atualizar Usuario", form=form)

@app.route('/usuario/<int:usuario_id>/deletar', methods=['POST'])
def deletar_usuario(usuario_id):
    usuario = Usuario.query.get_or_404(id)
    db.session.delete(usuario)
    db.session.commit()
    flash('Usuario apagado com sucesso')
    return redirect(url_for('listar_usuarios'))
