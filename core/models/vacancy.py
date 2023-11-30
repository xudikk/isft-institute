#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
from django.db import models


class Candidate(models.Model):
    FIO = models.CharField("Ism Familiya Sharif", max_length=256)
    pasport_seria = models.CharField("Pasport Seriasi", max_length=2)
    pasport_number = models.CharField("Seria Raqami", max_length=2)

    def __str__(self):
        return self.FIO


class Test(models.Model):
    quest = models.TextField("Savolning To'lliq ko'rinishi")
    a = models.CharField("A variant", max_length=1024)
    b = models.CharField("B variant", max_length=1024)
    c = models.CharField("C variant", max_length=1024)
    d = models.CharField("D variant", max_length=1024)

    true = models.CharField("Tog'ri Javob", max_length=1)

    def __str__(self):
        return self.quest



