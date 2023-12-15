
from django.db import models


class Voo(models.Model):
    idVoo = models.AutoField(primary_key=True)
    volumeinicialAgua = models.DecimalField(max_digits=6, decimal_places=2)
    pressaoInicial = models.DecimalField(max_digits=6, decimal_places=2)
    pesoFoguete = models.DecimalField(max_digits=6, decimal_places=2)
    pressaoBomba = models.DecimalField(max_digits=6, decimal_places=2)
    anguloLancamento = models.DecimalField(max_digits=6, decimal_places=2)

class Instante(models.Model):
    idInstante = models.AutoField(primary_key=True)
    tempo = models.IntegerField()
    latitude = models.DecimalField(max_digits=10, decimal_places=6)
    longitude = models.DecimalField(max_digits=10, decimal_places=6)
    altitude = models.DecimalField(max_digits=6, decimal_places=2)
    idVoo = models.ForeignKey(Voo, on_delete=models.CASCADE)

    

    
