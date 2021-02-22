import os
from models import Pessoa, Sala, Cafe
from config import db, arquivobd

# Teste das classes criadas
if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()
    s1 = Sala(nome_sala="Sala 01",
              lotacao=10)
    s2 = Sala(nome_sala="Sala 02",
              lotacao=11)
    s3 = Sala(nome_sala="Sala 03",
              lotacao=10)
    s4 = Sala(nome_sala="Sala 04",
              lotacao=11)

    c1 = Cafe(nome_cafe="House")
    c2 = Cafe(nome_cafe="Cafee")

    db.session.add(s1)
    db.session.add(s2)
    db.session.add(s3)
    db.session.add(s4)
    db.session.add(c1)
    db.session.add(c2)
    db.session.commit()

    p1 = Pessoa(nome="Cristina",
                sobrenome="de Souza", sala=s1, cafe =c2)
    p2 = Pessoa(nome="Paulo",
                sobrenome="Silva", sala=s1, cafe =c2)
    p3 = Pessoa(nome="Tomas",
                sobrenome="Alberto", sala=s2, cafe =c2)
    p4 = Pessoa(nome="Ana",
                sobrenome="Clara", sala=s1, cafe =c2)

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.commit()

    db_salas = db.session.query(Sala).all()
    db_pessoas = db.session.query(Pessoa).all()
    
    print(s1)
    print(s2)
    print(s3)
    print(s4)

    print(db_salas)
    print(db_pessoas)

    print(p1)
    print(p4)
    
 
