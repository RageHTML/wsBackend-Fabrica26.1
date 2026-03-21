from django.shortcuts import render
from BuscaFast.services import get_game_by_name

def search_page(request):
    # lidando com dados invalidos 
    query = request.GET.get("game_name","") # coloca o id do form de search.html, para nao ter problemas...
    query = query.strip() # removendo espacos fim/inicio
    query = query.replace('"','') # removendo aspas duplas
    query = query.replace("'",'') # removendo aspas simples
    results = "none" # definindo a variavel vazia por padrao
    if query:
        results = get_game_by_name(query) # enviando o dado ja tratado para get_game_by_name, e armazenando na variavel results
    return render(request, "games/search.html", {"results": results,"query": query}) # request e a requisicao, games/search.html e o template passando o contexto {query,results}