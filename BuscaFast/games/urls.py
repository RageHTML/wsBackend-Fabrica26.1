from django.urls import path
from .views import search_page,list_page,add_to_list

urlpatterns = [
    path("buscar_jogos/", search_page, name="search_page"), # "buscar_jogos" e a rota, search_page func de view, name e para chamar no html 
    path("minha_lista/", list_page, name="list_page"), # pagina mostrando lista de jogos favoritos
    path("add_to_list/", add_to_list, name="add_to_list"), # rota para enviar game_name para add_to_list
]
