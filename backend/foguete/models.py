
from django.db import models


class DadosVoo(models.Model):

    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    altitude = models.DecimalField(max_digits=6, decimal_places=2)
    duracao_segundos = models.PositiveSmallIntegerField()
    volume_agua = models.DecimalField(max_digits=6, decimal_places=2)
    peso_foguete = models.DecimalField(max_digits=6, decimal_places=2)
    pressao_bomba = models.DecimalField(max_digits=6, decimal_places=2)
    angulo_lancamento = models.DecimalField(max_digits=6, decimal_places=2)
