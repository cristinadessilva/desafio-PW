import os
from models import Pessoa, Sala, Cafe
from config import db, arquivobd


# Teste das classes criadas
if __name__ == "__main__":
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    db.create_all()
    s1 = Sala(nome_sala="Sala 01",
              lotacao="Blumenau")
    s2 = Sala(nome_sala="Sala 02",
              lotacao="Blumenau")
    
    c1 = Cafe(nome_cafe="House",
              lotacao_cafe="Blumenau")

    db.session.add(s1)
    db.session.add(s2)
    db.session.commit()

    p1 = Pessoa(nome="Cristina",
                sobrenome="de Souza", sala=s1, cafe =c1)
    p2 = Pessoa(nome="Paulo",
                sobrenome="Silva", sala=s1, cafe =c1)
    p3 = Pessoa(nome="Tomas",
                sobrenome="Alberto", sala=s2, cafe =c1)
    p4 = Pessoa(nome="Ana",
                sobrenome="Clara", sala=s1, cafe =c1)

    db.session.add(p1)
    db.session.add(p2)
    db.session.add(p3)
    db.session.add(p4)
    db.session.commit()
    print(s1)
    print(s2)

    db_salas = db.session.query(Sala).all()
    db_pessoas = db.session.query(Pessoa).all()
    print(db_salas)
    print(db_pessoas)

    s3 = Sala(nome_sala="Sala 03",
              lotacao="Blumenau")

    s4 = Sala(nome_sala="Sala 04",
              lotacao="São paulo")

    db.session.add(s3)
    db.session.add(s4)
    db.session.commit()
    print(s3)

    print(p4)
    print(s4)
    print(p1)
