## Criar virtualenv e instalar dependências

(No Windows, usar sempre o CMD, e nas instalações
usar ele no modo ADM e não usar o console do VsCode)

Caso não tenha o virtualenv instalado, instalar com
$ pip install virtualenv

Em seguida, criar o ambiente virtual para instalar as dependências do python para o projeto
Linux | Windows
$ virtualenv venv | python -m venv venv
$ source venv/bin/activate | venv\Scripts\activate
(venv) $ pip install -r requirements.txt

## Inicializar banco de dados

    (Para funcionar no windows, geralmente você terá que mudar o 'python3' por 'python' apenas)

    $ python3 manage.py makemigrations
    $ python3 manage.py migrate

## Inicalizar servidor de desenvolvimento

    (Para funcionar no windows, geralmente você terá que mudar o 'python3' por 'python' apenas)

    $ python3 manage.py runserver
