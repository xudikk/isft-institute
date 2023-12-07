#  Created by Xudoyberdi Egamberdiyev
#
#  Please contact before making any changes
#
#  Tashkent, Uzbekistan
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class Candidate(models.Model):
    FIO = models.CharField("Ism Familiya Sharif", max_length=256)
    pasport_seria = models.CharField("Pasport Seriasi", max_length=2)
    pasport_number = models.CharField("Seria Raqami", max_length=10)
    phone = PhoneNumberField(verbose_name=_("Telefon raqami"), null=True, blank=True)

    def __str__(self):
        return self.FIO


class Test(models.Model):
    quest = models.TextField("Savolning To'lliq ko'rinishi")
    a = models.CharField("A variant", max_length=1024)
    b = models.CharField("B variant", max_length=1024)
    c = models.CharField("C variant", max_length=1024)
    d = models.CharField("D variant", max_length=1024)

    true = models.SmallIntegerField("Tog'ri Javob",choices=[(1, "A"), (2, "B"), (3, "C"), (4, "D")])

    def get_true(self):
        return {
            1: "A",
            2: "B",
            3: "C",
            4: "D",
        }.get(self.true)

    def get_quest(self):
        return {
            1: self.a,
            2: self.b,
            3: self.c,
            4: self.d,
        }.get(self.true)


    def __str__(self):
        return self.quest


class ResultTest(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.SET_NULL, null=True, blank=True)
    status = models.CharField(max_length=56, default='Boshlandi', choices=[("Boshlandi", "Boshlandi"), ("Tugadi", "Tugadi"), ("Tugallanmay qoldi", "Tugallanmay qoldi")])
    test_ids = models.CharField("Tushgan Test savollari", max_length=128, default='[]')
    corrects_cnt = models.IntegerField(default=0)
    incorrects_cnt = models.IntegerField(default=0)
    corrects = models.CharField(max_length=125, default='[]')
    incorrects = models.CharField(max_length=125, default='[]')
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True, blank=True)
    percentage = models.SmallIntegerField(default=0, blank=True)

    def save(self, *args, **kwargs):
        if self.corrects_cnt > 0:
            self.percentage = int((self.corrects_cnt/len(eval(self.test_ids)) ) * 100)
        try:
            self.corrects_cnt = len(eval(self.corrects))
            self.incorrects_cnt = len(eval(self.incorrects))
        except:
            pass

        return super(ResultTest, self).save(*args, **kwargs)

    def result_test(self):
        return eval(self.test_ids) if self.test_ids else []


    def __str__(self):
        return f'{self.candidate.FIO} || Tog`ri Javoblar: {self.corrects_cnt}'
