from django.urls import path
from .views import search_page,list_page

urlpatterns = [
    path("buscar_jogos/", search_page, name="search_page"), # "buscar_jogos" e a rota, search_page func de view, name e para chamar no html 
    path("minha_lista/", list_page, name="list_page"), 
]
