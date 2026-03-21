from django.db import models
from django.contrib.auth.models import User

class Game(models.Model): # Avisando ao DB que vou criar uma tabela chamada Game
    igbd_id = models.IntegerField(unique=True) # Id vindo da api, nao pode repitir 
    name = models.CharField(max_length=250) # nome do jogo, limute maximo de 250 caracteres
    rating = models.FloatField(null=True,blank=True) # nota do jogo, numero decimal, pode ser nulo(nem todo jogo tem nota)

    def __str__ (self):
        return self.name