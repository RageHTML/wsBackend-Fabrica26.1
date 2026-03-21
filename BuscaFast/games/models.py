from django.db import models
from django.contrib.auth.models import User

class Game(models.Model): # Avisando ao DB que vou criar uma tabela chamada Game
    igdb_id = models.IntegerField(unique=True) # Id vindo da api, nao pode repitir 
    name = models.CharField(max_length=250) # nome do jogo, limute maximo de 250 caracteres
    rating = models.FloatField(null=True,blank=True) # nota do jogo, numero decimal, pode ser nulo(nem todo jogo tem nota)
    cover_url = models.CharField(max_length=500, null=True, blank=True) # armazena a url da imagem

    def __str__ (self):
        return self.name
    
class UserGameList(models.Model):
    user_token = models.CharField(max_length=100)    # identificador do usario (token)
    games = models.ManyToManyField(Game, blank=True) # lista de jogos, sem duplicantes
    created_at = models.DateTimeField(auto_now_add=True) # data que o jgoo foi favoritado

    def __str__(self):
        return f"Lista de {self.user.username}"