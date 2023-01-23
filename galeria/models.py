from django.db import models
from datetime import datetime


class Fotografia(models.Model):
    CHOICES_CATEGORIA = [
        ("NEBULOSA", 'Nebulosa'),
        ("ESTRELA","Estrela"),
        ("GALAXIA", "Galáxia"),
        ("PLANETA", "Planeta")
    ]
    
    nome = models.CharField(max_length=100, null=False, blank=False)
    legenda = models.CharField(max_length=150, null=False, blank=False)
    categoria = models.CharField(max_length=20,choices=CHOICES_CATEGORIA)
    descricao = models.TextField(null=False, blank=False, verbose_name="Descrição" )
    foto = models.ImageField(upload_to="fotos/%Y/%m/%d", blank=True)
    publicado = models.BooleanField(default=False)
    data_fotografia = models.DateTimeField(default=datetime.now, blank=False)

    def __str__(self):
        return self.nome