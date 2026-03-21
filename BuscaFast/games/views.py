from django.shortcuts import render
from BuscaFast.services import get_game_by_name
import uuid
from .models import Game


def save_from_api(igdb_id,name): # salvar jogos da api no db Game, sempre que alguemm pesquisar (para gerar insights futuros)
    data = get_game_by_name(name)
    if not data or len(data) == 0: # verificar se a data nao existe ou esta vazia, retorna none
        return None
    
    game_data = data[0] # indice da tabela raw (data)

    game,created = Game.objects.update_or_create(
        igdb_id=igdb_id, #id do jogo 
        defaults={ # dados do jogo 
            "name": game_data["name"], # pega o nome
            "rating": game_data.get("rating"), # pega a nota
            "cover_url": game_data.get("cover_url") # pega a imagem
        }
    )
    return game

def search_page(request):
    # lidando com dados invalidos 
    query = request.GET.get("game_name","") # coloca o id do form de search.html, para nao retorna none...
    query = query.strip() # removendo espacos fim/inicio
    query = query.replace('"','') # removendo aspas duplas
    query = query.replace("'",'') # removendo aspas simples
    results = [] # criando umma tabela vazia para os dados

    if query:
        results = list(Game.objects.filter(name__icontains=query)) # buscar jogo no bd primeiro

        if not results: # se nao encontrar no bd
            data = get_game_by_name(query) # buscar dados do jogo na api
            for item in data: # acessando os dados
                game = save_from_api(item["id"],item["name"]) # salvando no bd
                if game: 
                    results.append(game) # adicionando o resultado a resutls


    return render(request, "games/search.html", {"results": results,"query": query}) # request e a requisicao, games/search.html e o template passando o contexto {query,results}

def list_page(request):
    token = request.session.get("user_token") # verificar se o usuario ja tem token
    if not token:
        token = str(uuid.uuid4())
        request.session["user_token"] = token
    return render(request, "games/list.html", {"user_token": token})
