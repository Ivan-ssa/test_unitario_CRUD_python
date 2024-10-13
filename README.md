# Como clonar e rodar o projeto

1. Clonar o repositório:
   Execute o comando abaixo no terminal para clonar o projeto para sua máquina local:
git clone https://github.com/Ivan-ssa/test_unitario_CRUD_python.git

2. Acessar o diretório do projeto:
Navegue até o diretório do projeto recém-clonado:
cd test_unitario_CRUD_python

3. Criar e ativar um ambiente virtual:
Crie um ambiente virtual Python e ative-o.

No Windows:
python -m venv venv venv\Scripts\activate

No Linux/MacOS:
python3 -m venv venv source venv/bin/activate

4. Instalar as dependências:
Com o ambiente virtual ativado, instale as dependências necessárias:

pip install -r requirements.txt

5. Rodar o servidor Flask:
Após a instalação das dependências, execute o servidor Flask:
python app.py

O servidor estará rodando no endereço: `http://127.0.0.1:5000`

6. Testar o CRUD:
Utilize ferramentas como Insomnia ou Postman para testar as rotas do CRUD:
- POST, GET, PUT, DELETE em `http://127.0.0.1:5000/reservas`

Siga o exemplo de cada operação CRUD no código para realizar os testes.


