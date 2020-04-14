from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from project import app, db
from project.models.instrutor import Instrutor
from project.models.voo import Voo
from project.forms.vooSchema import VooForm
from project.forms.instrutorSchema import InstrutorForm
from datetime import datetime
import re

@app.route('/cadastrar_instrutor', methods=['GET', 'POST'])
def cadastrar_instrutor():
    form = InstrutorForm()
    if form.validate_on_submit():
        usuario = Instrutor(nome = form.nome.data, cpf = form.cpf.data, email = form.email.data, senha = form.senha.data, breve = form.breve.data)    
        db.session.add(usuario)
        db.session.commit()
        flash('Instrutor cadastrado com sucesso!', 'success')
        return redirect(url_for('listar_instrutores'))
    return render_template('cadastrar_instrutor.html', title='Cadastrar Instrutor', legend='Cadastrar Instrutor', form=form)

@app.route('/instrutores_cadastrados')
def listar_instrutores():
    instrutores = Instrutor.query.all()
    return render_template('instrutores_cadastrados.html', title='Instrutores cadastrados', instrutores=instrutores)

@app.route('/instrutor/<string:breve>', methods=['GET', 'POST'])
def visualizar_instrutor(breve):
        instrutor = Instrutor.query.get_or_404(breve)
        return render_template('visualizar_instrutor.html', title=f'Instrutor {instrutor.breve}', instrutor=instrutor)


@app.route('/aluno/<string:breve>/deletar', methods=['POST'])
def deletar_instrutor(breve):
    instrutor = Instrutor.query.get_or_404(breve)
    db.session.delete(instrutor)
    db.session.commit()
    flash('Instrutor apagado com sucesso', 'info')
    return redirect(url_for('listar_instrutores'))

@app.route('/voos_monitorados')
@login_required
def voos_monitorados():
    voos = current_user.voos
    return render_template('voos_cadastrados.html', title='Voos monitorados', voos=voos)

@app.route('/instrutor/<int:breve>/atualizar', methods=['GET', 'POST'])
def atualizar_instrutor(breve):
    instrutor = Instrutor.query.get_or_404(breve)
    form = InstrutorForm()
    if form.validate_on_submit():
        instrutor.nome = form.nome.data
        instrutor.cpf = form.cpf.data
        instrutor.breve = form.breve.data
        instrutor.email = form.email.data
        instrutor.senha = form.senha.data
        db.session.commit()
        flash(f'Dados atualizados com sucesso!', category='success')
        return redirect(url_for('visualizar_instrutor', breve=breve))
    elif request.method == 'GET':
        form.nome.data = instrutor.nome
        form.cpf.data = instrutor.cpf
        form.breve.data = instrutor.breve
        form.email.data = instrutor.email
    return render_template('cadastrar_instrutor.html', title='Atualizar instrutor', legend="Atualizar instrutor", form=form)
