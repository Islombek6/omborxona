from django.db import models
from django.contrib.auth.models import User
from main.models import Bolim


class Sotuvchi(models.Model):
    rasm = models.ImageField(upload_to='sotuvchilar/')
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username