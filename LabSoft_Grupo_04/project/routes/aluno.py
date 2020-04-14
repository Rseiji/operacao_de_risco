from flask import render_template, url_for, redirect, request, flash
from flask_login import current_user, login_required
from project import app, db
from project.models.aluno import Aluno, horasDeVoo
from project.models.voo import Voo
from project.forms.vooSchema import VooForm
from project.forms.usuarioSchema import UsuarioForm
from project.routes.voo import check_breve, check_voo_solo
from datetime import datetime

@app.route('/cadastrar_alunoo', methods=['GET', 'POST'])
def cadastrar_aluno():
    form = UsuarioForm()
    if form.validate_on_submit():
        usuario = Aluno(nome = form.nome.data, cpf = form.cpf.data, email = form.email.data, senha = form.senha.data)    
        db.session.add(usuario)
        db.session.commit()
        flash('Aluno cadastrado com sucesso!', 'success')
        return redirect(url_for('listar_alunos'))
    return render_template('cadastrar_aluno.html', title='Cadastrar Usuario', legend='Cadastrar Usuario', form=form)

@app.route('/alunos_cadastrados')
def listar_alunos():
    alunos = Aluno.query.order_by(Aluno.usuario_id).all()
    for i in range(len(alunos)):
        alunos[i].breve = 'Sim' if check_breve(alunos[i]) else 'Não'
        alunos[i].vooSolo = 'Sim' if check_voo_solo(alunos[i]) else 'Não'
    return render_template('alunos_cadastrados.html', title='Alunos cadastrados', alunos=alunos)

@app.route('/aluno/<int:usuario_id>', methods=['GET', 'POST'])
def visualizar_aluno(usuario_id):
        aluno = Aluno.query.get_or_404(usuario_id)
        totalHoras = horasDeVoo(aluno.voos)
        Aluno.query.get(aluno.usuario_id).horas_de_voo = totalHoras
        db.session.commit()
        breve = check_breve(aluno)
        return render_template('visualizar_aluno.html', title=f'Aluno {aluno.usuario_id}', aluno=aluno, totalHoras = f'{format(int(totalHoras/60), "02")}:{format(totalHoras%60, "02")}', breve=breve)


@app.route('/aluno/<int:usuario_id>/deletar', methods=['POST'])
def deletar_aluno(usuario_id):
    aluno = Aluno.query.get_or_404(usuario_id)
    db.session.delete(aluno)
    db.session.commit()
    flash('Aluno apagado com sucesso', 'info')
    return redirect(url_for('listar_alunos'))

@app.route('/horas_voo')
def visualizar_horas_voo():
    return render_template('visualizar_horas_voo.html', title='Horas de Voo')

@app.route('/historico_voos')
@login_required
def historico_voos():
    voos = current_user.voos
    return render_template('voos_cadastrados.html', title='Histórico de voos', voos=voos)

@app.route('/aluno/<int:usuario_id>/atualizar', methods=['GET', 'POST'])
def atualizar_aluno(usuario_id):
    
    aluno = Aluno.query.get_or_404(usuario_id)
    form = UsuarioForm()
    if form.validate_on_submit():
        aluno.nome = form.nome.data
        aluno.cpf = form.cpf.data
        aluno.email = form.email.data
        aluno.senha = form.senha.data
        db.session.commit()
        flash(f'Dados atualizados com sucesso!', category='success')
        return redirect(url_for('visualizar_aluno', usuario_id=usuario_id))
    elif request.method == 'GET':
        form.nome.data = aluno.nome
        form.cpf.data = aluno.cpf
        form.email.data = aluno.email
        form.senha.data = aluno.senha
        form.confirma_senha.data = aluno.senha
    return render_template('cadastrar_aluno.html', title='Atualizar Aluno', legend="Atualizar Aluno", form=form)