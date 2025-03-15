from django.core.validators import MinValueValidator
from django.db import models


class Bolim(models.Model):
    nom = models.CharField(max_length=255)

    def __str__(self):
        return self.nom


OLCHOV_SELECT = {
    'dona': 'dona',
    'blok': 'blok',
    'kg': 'kg',
    'gram': 'gram',
    'tonna': 'tonna',
    'quti': 'quti',
    'litr': 'litr',
    'qop': 'qop',
    'm': 'm',
    'm²': 'm²',
    'sm': 'sm',
    'km': 'km',

}


class Maxsulot(models.Model):
    nom = models.CharField(max_length=255)
    brend = models.CharField(max_length=255, blank=True, null=True)
    narx1 = models.FloatField(validators=[MinValueValidator(0)])
    narx2 = models.FloatField(validators=[MinValueValidator(1)], blank=True, null=True)
    miqdor = models.FloatField(validators=[MinValueValidator(0)])
    olchov = models.CharField(max_length=20, choices=OLCHOV_SELECT)
    sana = models.DateTimeField()
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Mijoz(models.Model):
    ism = models.CharField(max_length=255)
    dokon = models.CharField(max_length=255, blank=True, null=True)
    manzil = models.TextField(blank=True, null=True)
    telefon = models.CharField(max_length=15)
    qarz = models.FloatField(validators=[MinValueValidator(0)], default=0)
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return self.ism
