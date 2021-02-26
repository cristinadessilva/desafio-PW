[autor-link]:https://img.shields.io/badge/Autora-Cristina%20de%20Souza%20e%20Silva-lightpink
[linguagem-link]:https://img.shields.io/badge/Linguagem-Python%20/%20JavaScript-lightpink
[licenca-link]:https://img.shields.io/badge/Licença-MIT-lightpink

# :memo: Desafio de Programação - ProWay

[![Autora][autor-link]](https://github.com/cristinadessilva)
[![Linguagem][linguagem-link]](https://www.python.org/)
[![licença][licenca-link]](https://github.com/cristinadessilva/desafio-PW/blob/main/LICENSE)

Desafio realizado pela ProWay:
A empresa realizará um treinamento para uma grande empresa de TI de Blumenau e o sistema realizará:
- O cadastro de pessoas, com nome e sobrenome;
- O cadastro das salas do evento, com nome e lotação;
- O cadastro dos espaços de café pelo nome;
- A consulta das pessoa;
- A consulta das salas e espaços;

# Requerimentos:  

- Python, versão utilizada: 3.8.2 (<a  href="https://www.python.org/downloads/">Link para download</a>)</li>

- Flask

- Flask-Cors

- SQLAlchemy

- flask_sqlalchemy

<hr>
 Caso queira, pode-se criar um ambiente virtual para a instalação dos requerimentos.
 
#### Para instalar a biblioteca venv, se não tiver:
>  `python -m pip install venv`

#### Para criar um ambiente virtual:
>  `python -m venv VIRTUAL_ENV_NOME` 

#### Para ativar seu ambiente virtual:
>  **WINDOWS:**  `VIRTUAL_ENV_NOME/Scripts/activate`

>  **LINUX:**  `source env/bin/activate`
  
#### Instalar os requerimentos:

>  `pip install -r requirements.txt`

ou

>`python -m pip install -r requirements.txt`

#### Caso queira desativar o ambiente virtual:
>  `deactivate`

  
#  Rodando o programa:

- Rodar o backend_server.py:
Para roda-lo você precisará entra no diretório onde ele se encontra, caso ocorrá algum tipo de erro, certifique-se que está no diretório do projeto. 
`python app/back_end/backend_server.py`

- Abrir o index.html contido na pasta front_end, manualmente, ou se preferir utilizar uma extensão para abrir direto no navegador padrão

# Banco de Dados
- Quando você rodar o backend_server ele se criará automaticamente 
- Você pode rodar os test.py antes caso queira começar o app com salas, café e pessoas adicionadas.
- Caso queira excluir os cadastros feitos, basta apagar o arquivo app.db, e rodar o backend_server novamente, assim não haverá mais nada cadastrado.

#  Rodando os testes:
Para rodar os teste utilizando a unittest:
  `python app/back_end/unittest_tests.py`
 
 Para rodar os teste utilizando apenas o banco de dados e o terminal:
  `python app/back_end/test.py`
