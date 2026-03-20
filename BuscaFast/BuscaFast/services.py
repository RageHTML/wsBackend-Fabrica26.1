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