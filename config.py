ambiente = 'producao'
if ambiente == 'teste':

#CONFIG BANCO DE DADOS
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = 'senai'
    DB_NAME = 'blog'

if ambiente == 'producao':
    DB_HOST = 'Domantunes.mysql.pythonanywhere-services.com'
    DB_USER = 'Domantunes'
    DB_PASSWORD = 'Femh5x3r'
    DB_NAME = 'Domantunes$Blog'

#CONFIG CHAVE SECRETA DE SESSÃO
SECRET_KEY = 'blog'

#SENHA DO ADM
MASTER_EMAIL = "teste@teste"
MASTER_PASSWORD = "1234"