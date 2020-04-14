from flask import render_template, url_for, redirect, request, flash
from project import app, db
from project.models.usuario import Usuario
from project.models.aluno import Aluno
from project.models.instrutor import Instrutor
from project.forms.dadosSchema import DadosForm

@app.route('/dados', methods=['GET', 'POST'])
def dados():
    form = DadosForm()
    if form.validate_on_submit():
        if (form.tipo.data == 'aluno'):
            return redirect(url_for('dados_aluno', usuario_id = int(form.cadastro.data)))
        elif (form.tipo.data == 'instrutor'):
            return redirect(url_for('dados_instrutor', breve = form.cadastro.data))
    return render_template('dados.html', title='Dados Cadastrais')

@app.route('/dados/<int:usuario_id>', methods=['GET', 'POST'])
def dados_aluno(usuario_id):
    aluno = Aluno.query.get_or_404(usuario_id)
    return render_template('dados_aluno.html', title='Usuario {aluno.nome}', aluno=aluno)

@app.route('/dados/<string:breve>', methods=['GET', 'POST'])
def dados_instrutor(breve):
    instrutor = Instrutor.query.get_or_404(breve)
    return render_template('dados_instrutor.html', title='Usuario {instrutor.nome}', instrutor=instrutor)

#@app.route('/dados/<int:usuario_id>', methods=['GET', 'POST'])
#def dados_usuario(usuario_id):
#    usuario = usuario.query.get_or_404(usuario_id)
#    return render_template('dados_usuario.html', title='Usuario {usuario.nome}', usuario=usuario)

