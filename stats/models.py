from django.db import models
from main.models import *


class Sotiv(models.Model):
    mahsulot = models.ForeignKey(Maxsulot, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz,on_delete=models.CASCADE)
    bolim = models.ForeignKey(Bolim,on_delete=models.CASCADE)
    sana = models.DateTimeField(auto_now_add=True)
    miqdor = models.FloatField(validators=[MinValueValidator(0.0)])
    jami_summa = models.FloatField(validators=[MinValueValidator(0.0)])
    tolandi = models.FloatField(validators=[MinValueValidator(0.0)])
    qarz = models.FloatField(validators=[MinValueValidator(0.0)])

    def __str__(self):
        return f"{self.mahsulot.nom} - {self.mijoz.ism}"


