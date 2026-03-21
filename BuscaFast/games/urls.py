from django.urls import path
from .views import search_page

urlpatterns = [
    path("buscar_jogos/", search_page, name="search_page"),
]
