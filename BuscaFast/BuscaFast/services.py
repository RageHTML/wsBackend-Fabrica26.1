import requests
from BuscaFast.api_keys import TWITCH_CLIENT_ID, TWITCH_CLIENT_SECRET # abre api_keys_exemple explica melhor

def get_twitch_token(): # funcao para buscar o token
    url = "https://id.twitch.tv/oauth2/token" # Caminho padrao para authenticacao, nao altera

    params = { 
        "client_id": TWITCH_CLIENT_ID, 
        "client_secret": TWITCH_CLIENT_SECRET, 
        "grant_type": "client_credentials" # tipo de authenticacao 
    }

    response = requests.post(url, data=params) # enviando para a url, os params pelo o metodo post 

    return response.json()

def get_game_by_name(name): # buscar dados de um jogo pelo o nome
    token = get_twitch_token() # usar o token de auth na igbd
    url = "https://api.igdb.com/v4/games" # endpoint para buscar os jogos, nao altere

    headers = { # Dados necessarios para consultar a api
        "Client-ID": TWITCH_CLIENT_ID, # identificacao da sua aplicacao
        "Authorization": f"Bearer {token}" # prova que voce esta autheticado
    }

    body = f"fields id,name,rating; search'{name}'; limit 1;" # Query de busca (tipo GraphQL), # fields sao os dados que eu quero, search e onde o parametro vai ser inserido, limit traz apenas 1 dado 

    response = requests.post(url,headers=headers, data=body) # metodo post (apontando para o caminho url, passando o headers, body)

    return response.json() # converte a resposta da api (dict/list)


