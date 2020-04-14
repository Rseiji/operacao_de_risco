from project import db, login_manager
from project.models.usuario import Usuario
import re
from flask import flash
from flask_login import UserMixin

class Aluno(Usuario, UserMixin):
    __tablename__ = 'aluno'
    usuario_id = db.Column(db.Integer, primary_key=True)
    voos = db.relationship('Voo', backref='aluno', lazy=True)
    horas_de_voo = db.Column(db.Integer, nullable = False, default = 0)

    def get_id(self):
        return str(self.email)

def check_breve(aluno):
    # Atualiza total de horas do aluno
    total_horas = horasDeVoo(aluno.voos)
    Aluno.query.get(aluno.usuario_id).horas_de_voo = total_horas
    db.session.commit()
    if (aluno.voos):
        pareceres = sum([voo.parecer >= 3 for voo in aluno.voos])
        pareceres /= len(aluno.voos)
        if (total_horas >= 60 * 340 and pareceres >= .85):
            return True

def check_voo_solo(aluno):
    # Atualiza total de horas do aluno
    total_horas = horasDeVoo(aluno.voos)
    Aluno.query.get(aluno.usuario_id).horas_de_voo = total_horas
    db.session.commit()
    if (aluno.voos):
        pareceres = sum([voo.parecer >= 3 for voo in aluno.voos])
        pareceres /= len(aluno.voos)
        if (total_horas >= 30 * 340 and pareceres >= .85):
            return True

def horasDeVoo(voos):
    total = 0
    horas = []
    for voo in voos:
        hora = [int(s) for s in re.findall(r'\b\d+\b', voo.duracaoVoo)]
        horas.append(hora)
    for tempo in horas:
        total = total + tempo[0]*60 + tempo[1]
    return total


def get_id(usuario_id):
    return unicode(usuario_id)