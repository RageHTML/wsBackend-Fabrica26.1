# Arquivo de exemplo de configuração do database
# Copie este arquivo para settings_db.py e preencha com seus dados reais

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seu_db', # nome do seu banco de dados MySQL
        'USER': 'seu_user', # nome do seu User
        'PASSWORD': 'sua_senha',  # a senha do banco de dado MySQL
        'HOST': 'db', # nao altere fixo
        'PORT': '3306', # altere a porta se souber o que esta fazendo 
    }
}