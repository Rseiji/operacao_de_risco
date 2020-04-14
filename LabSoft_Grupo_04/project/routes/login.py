from flask import render_template, url_for, redirect, request, flash
from flask_login import login_user, current_user, logout_user, login_required
from project import app, db, login_manager
from project.models.aluno import Aluno
from project.models.instrutor import Instrutor
from project.models.usuario import Usuario
from project.models.admin import Admin
from project.forms.loginSchema import LoginForm

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
     return redirect(url_for('home'))
  form = LoginForm()
  if form.validate_on_submit():
    user = Aluno.query.filter_by(email = form.email.data).first()
    if not user:
      user = Instrutor.query.filter_by(email = form.email.data).first()
      if not user:
        user = Admin.query.filter_by(email = form.email.data).first()
      # if form.email.data in Instrutor.query.filter_by(email = form.email.data).first().email:
      #   user = Instrutor.query.filter_by(email = form.email.data).first()
    
    if user and form.senha.data == user.senha:
      login_user(user)
      flash('Login realizado com sucesso!', 'success')
      return redirect(url_for('home'))
    else:
      flash('email ou senha incorretos!', 'danger')
  return render_template("login.html", title="Login", form=form)

@app.route('/logout')
def logout():
    logout_user()
    flash('logout realizado!', 'info')
    return redirect(url_for('home'))


@login_manager.user_loader
def load_user(user_id):
    if Aluno.query.filter_by(email = user_id).first():
      return Aluno.query.filter_by(email = user_id).first()
    elif Instrutor.query.filter_by(email = user_id).first():
      return Instrutor.query.filter_by(email = user_id).first()
    elif Admin.query.filter_by(email = user_id).first():
      return Admin.query.filter_by(email = user_id).first()