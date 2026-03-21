from django.shortcuts import render

def search_page(request):
    return render(request, "games/search.html") # request e a requisicao, games/search.html e o template renderizado