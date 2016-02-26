# prova
Teste de Desenvolvimento de API Rest com Python.

Dependências:

Python 2.7.10
Download: https://www.python.org/downloads/

PIP 8.0.2
Instalaçao: https://pip.pypa.io/en/stable/installing/

Virtualenv 13.1.2
Instalação: https://virtualenv.readthedocs.org/en/latest/installation.html

Mysql
Download: https://dev.mysql.com/downloads/installer/

Instalação:

Primeiro crie a virualenv:

virtualenv restapi

Entre na pasta da virtualenv e ative o roteiro:
	
	Linux: source bin/activate
	Windows: Scripts/activate.bat

Eu particularmente sempre crio uma pasta para colocar o projeto então
	
	mkdir src
	cd src

Crie a pasta do projeto:

	mkdir prova
	cd prova




Instale as dependências, deixe o arquivo requirements.txt na raiz do projeto:
	
	pip install -r requirements.txt

Observação no caso de Windows deixei o arquivo MySQL_python-1.2.5-cp27-none-win_amd64.whl na raiz do projeto então:

	pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl
