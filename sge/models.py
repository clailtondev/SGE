from django.db import models
class Pessoa(models.Model):
    nome = models.CharField(max_length = 120)
    email = models.CharField(max_length=150)
    celular = models.CharField(max_length=15)

    def __str__(self):
        return self.nome