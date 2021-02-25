import unittest
from models import Pessoa, Sala, Cafe
from config import db, arquivobd

# Teste do cadastro da sala
def testCriarSala():
    s1 = Sala(nome_sala="Sala 01",
              lotacao=10)
    s2 = Sala(nome_sala="Sala 02",
              lotacao=5)
    try:
        db.session.add(s1)
        db.session.add(s2)
    except:
        return "Erro"

    return s1.nome_sala, s1.lotacao, s2.nome_sala, s2.lotacao


# Teste do cadastro do cafe
def testCriarCafe():
    c1 = Cafe(nome_cafe="House")
    c2 = Cafe(nome_cafe="Mais Cafe")
    try:
        db.session.add(c1)
        db.session.add(c2)
    except:
        return "Erro"

    return c1.nome_cafe, c2.nome_cafe


# Teste do cadastro da pessoa
def testCriarPessoa():
    s2 = Sala(nome_sala="Sala 02",
            lotacao=11)
    c2 = Cafe(nome_cafe="CoffePlus")
    p1 = Pessoa(nome="Cristina",
                sobrenome="de Souza", sala=s2, cafe =c2)
    p2 = Pessoa(nome="Berta",
                sobrenome="Maria", sala=s2, cafe =c2)
    try:
        db.session.add(p1)
        db.session.add(p2)
    except:
        return "Erro"

    return p1.nome, p1.sobrenome, p2.nome, p2.sobrenome


# Classe que chama todos os testes e faz a comparação
class MyTest(unittest.TestCase):
    def test_sala(self):
        self.assertEqual(testCriarSala(),("Sala 01", 10, "Sala 02", 5))
    def test_cafe(self):
        self.assertEqual(testCriarCafe(),("House", "Mais Cafe"))
    def test_pessoa(self):
        self.assertEqual(testCriarPessoa(),("Cristina","de Souza","Berta", "Maria"))
        

if __name__ == '__main__':
    unittest.main()
