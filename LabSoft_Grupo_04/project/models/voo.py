from datetime import datetime, time
from project import db
from project.models.aluno import Aluno
from project.models.instrutor import Instrutor


class Voo(db.Model):
    __tablename__ = 'voo'
    voo_id = db.Column(db.Integer, primary_key=True)
    dataVoo = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    duracaoVoo = db.Column(db.String(5), nullable=False)
    horaSaida = db.Column(db.String(5), nullable=False)
    parecer = db.Column(db.Integer, nullable=False)
    aluno_id = db.Column(db.Integer, db.ForeignKey('aluno.usuario_id'), nullable=False)
    #instrutor = db.Column(db.String(60), nullable=False)
    instrutor_breve = db.Column(db.String(60), db.ForeignKey('instrutor.breve'), nullable=False)
    #supervisionado = db.Column(db.Boolean)

    def __repr__(self):
        return f"Voo(Instrutor:'{self.instrutor.nome}', data:'{self.dataVoo}', Aluno:'{self.aluno_id}' )"
