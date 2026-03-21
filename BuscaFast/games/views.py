from django.shortcuts import render
from BuscaFast.services import get_game_by_name
from .models import Game

def search_page(request):
    # lidando com dados invalidos 
    query = request.GET.get("game_name","") # coloca o id do form de search.html, para nao retorna none...
    query = query.strip() # removendo espacos fim/inicio
    query = query.replace('"','') # removendo aspas duplas
    query = query.replace("'",'') # removendo aspas simples
    results = "none" # definindo a variavel vazia por padrao
    if query:
        results = get_game_by_name(query) # enviando o dado ja tratado para get_game_by_name, e armazenando na variavel results
    return render(request, "games/search.html", {"results": results,"query": query}) # request e a requisicao, games/search.html e o template passando o contexto {query,results}

def list_page(request):

    return render(request, "games/list.html")

def save_from_api(igdb_id,name): # salvar jogos da api no db Game, sempre que alguemm pesquisar (para gerar insights futuros)
    data = get_game_by_name(name)
    if not data or len(data) == 0: # verificar se a data nao existe ou esta vazia, retorna none
        return None
    
    game_data = data[0] # indice da tabela raw (data)

    game,created = Game.objects.update_or_create(
        igdb_id=igdb_id, #id do jogo 
        defaults={ # dados do jogo 
            "name:": game_data["name"], # pega o nome
            "rating:": game_data["rating"], # pega a nota
            "cover_url:": game_data["cover_url"] # pega a imagem
        }
    )
    return game