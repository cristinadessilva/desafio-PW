from config import *

class Sala(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_sala = db.Column(db.String(254))
    lotacao = db.Column(db.String(254))
    pessoa = db.relationship('Pessoa')

    def __str__(self):
        return f'''
                - id: ({self.id}) 
                - nome: {self.nome_sala} 
                - lotacao: {self.lotacao} 
                - pessoa: {self.pessoa}              
                '''

    def json(self):
        return {
            "id": self.id,
            "nome_sala": self.nome_sala,
            "lotacao": self.lotacao,
        }

class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome_cafe = db.Column(db.String(254))
    lotacao_cafe = db.Column(db.String(254))
    pessoa = db.relationship('Pessoa')

    def __str__(self):
        return f'''
                - id: ({self.id}) 
                - nome: {self.nome_cafe} 
                - lotacao: {self.lotacao_cafe} 
                - pessoa: {self.pessoa}
                '''
    
    def json(self):
        return {
            "id":self.id,
            "nome_cafe":self.nome_cafe,
            "lotacao_cafe":self.lotacao_cafe,
        }

class Pessoa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    sobrenome = db.Column(db.String(254))
    
    sala_id = db.Column(db.Integer, db.ForeignKey(Sala.id),
                        nullable=False)
    sala = []
    sala = db.relationship("Sala")
    
    cafe_id = db.Column(db.Integer, db.ForeignKey(Cafe.id),
                        nullable=False)
    cafe = []
    cafe = db.relationship("Cafe")

    def __str__(self):
        return f'''
                - id: ({self.id}) 
                - nome: {self.nome} 
                - sobrenome: {self.sobrenome} 
                - sala: {self.sala} 
                - cafe: {self.cafe} 
                '''

    def json(self):
        return ({
            "id": self.id,
            "nome": self.nome,
            "sobrenome": self.sobrenome,

            "sala_id": self.sala_id,
            "sala": self.sala.nome_sala,

            "cafe_id": self.cafe_id,
            "cafe": self.cafe.nome_cafe,
        })
