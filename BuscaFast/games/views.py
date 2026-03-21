from django.shortcuts import render,redirect
from BuscaFast.services import get_game_by_name
import uuid
from .models import Game, UserGameList

# BUSCAR_JOGOS 
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

# Minha_Lista
def get_token(request): # Obter token ou gerar
    token = request.session.get("user_token") # verificar se o usuario ja tem token
    if not token: # gerar um token para o novo usuario
        token = str(uuid.uuid4())
        request.session["user_token"] = token
    return token
   
def add_to_list(request): # adiciona Jogo a lista
    token = get_token(request) # obter token unico
    game_name = request.GET.get("game_name") # recebendo o nome do jogo enviado de search.html
    game = Game.objects.filter(name=game_name).first() # procurando no bd(Game) pelo game_name

    if not game and game_name: # caso nao ache no bd(Game)
        data = get_game_by_name(game_name) # Busca na api em services
        if data: 
            api_game = data[0] 
            game = save_from_api(api_game["id"],api_game["name"]) # salvar no bd(Game)
    
    if game: # quando estiver com o game, salvar no bd (UserGamerList)
        user_list, created = UserGameList.objects.get_or_create(user_token=token) # retorna uma tupla(user_list,created)
        user_list.games.add(game) # add por causa que o campo games e ManyToManyFields

    return redirect("list_page")

 
def list_page(request):
    token = get_token(request) # obter token 

    user_list, created = UserGameList.objects.get_or_create(user_token=token) # buscar a lista com o id do usuario
    games = user_list.games.all() # pegar todos os jogos da lista 

    return render(request, "games/list.html", {"user_token": token, "games": games})

