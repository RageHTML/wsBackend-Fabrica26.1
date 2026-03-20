# Arquivo de exemplo de configuração do database
# Copie este arquivo para settings_db.py e preencha com seus dados reais

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'seu_db',
        'USER': 'seu_user',
        'PASSWORD': 'sua_senha',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}