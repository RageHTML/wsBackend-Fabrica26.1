# BuscaFast - Salve seus jogos Favoritos



## Primeiros Passos

Crie uma virtualenv:

```bash
python -m venv venv
```

Ative a virtualenv:

Linux / Mac:

```bash
source venv/bin/activate
```

Windows:

```bash
venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

Você precisa configurar o banco de dados `settings_db_exemple.py` antes de rodar o projeto.

1. Renomeie o arquivo: `settings_db.py`
2. Preencha as informacoes como o arquivo informa

Você precisa configurar `api_keys_exemple.py` depois

1. Renomeie o arquivo: `api_keys.py`
2. Acesse o link https://api-docs.igdb.com/#account-creation
3. Gere um Django SECRET_KEY 

Com a venv ativada execute:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Você precisa configurar `docker-compose.yml`:
1. Preencha igual o arquivo informa 

Após configurar tudo, execute:

```bash
docker compose up --build
```


## Features



## Contributing

