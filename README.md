# Teste de Desenvolvimento de API Rest com Python.

## Dependências:

Python 2.7.10

Download: https://www.python.org/downloads/

PIP 8.0.2

Instalaçao: https://pip.pypa.io/en/stable/installing/

Virtualenv 13.1.2

Instalação: https://virtualenv.readthedocs.org/en/latest/installation.html

Mysql

Download: https://dev.mysql.com/downloads/installer/

## Instalação:

Primeiro crie a virualenv:

	virtualenv restapi

Eu particularmente sempre crio uma pasta para colocar o projeto então
	
	mkdir src
	cd src

Clone o projeto:

	git clone https://github.com/kanayamazappa/prova.git
	
Retone na pasta da virtualenv e ative o roteiro:

	cd ..	
	Linux: source bin/activate
	Windows: Scripts/activate.bat

Instale as dependências, deixe o arquivo requirements.txt na raiz do projeto:
	
	cd src/prova	
	pip install -r requirements.txt

Observação no caso de Windows deixei o arquivo MySQL_python-1.2.5-cp27-none-win_amd64.whl na raiz do projeto então remove a linha MySQL-python=1.2.5 do arquivo requirements.txt e:

	pip install MySQL_python-1.2.5-cp27-none-win_amd64.whl
	pip install -r requirements.txt

Crie a base de dados Mysql para o projeto e edit o arquivo prova/settings.py:

	DATABASES = {
    		'default': {
        		'ENGINE': 'django.db.backends.mysql',
        		'NAME': 'prova', # Nome de sua base de dados
        		'USER': 'root', # Nome do usuário
        		'PASSWORD': '', # Senha
        		'HOST': '', # Host
        		'PORT': '3306', # Porta
    		}
	}
	
Importe os dados, deixe o arquivo db.json na raiz do projeto:

	python manage.py migrate
	python manage.py loaddata db.json

Agora apenas rode o projeto:

	python manage.py runserver 0.0.0.0:8080

