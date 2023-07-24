from django.db import models
# Create your models here.
class Palavra(models.Model):
    palavra=models.CharField(max_length=50)
    image=models.CharField(max_length=100)
    def __str__(self):
        return self.palavra
    
class Informacao(models.Model):
    palavra=models.ForeignKey(Palavra, on_delete=models.CASCADE)
    titulo=models.CharField(max_length=200)
    texto=models.CharField(max_length=700)
    def __str__(self):
        return self.texto