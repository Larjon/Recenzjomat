from django.db import models
from django.contrib.auth.models import User

class Kategoria(models.Model):
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa

class Ksiazka(models.Model):
    tytul = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    opis = models.TextField()
    kategorie = models.ForeignKey(Kategoria, on_delete=models.CASCADE)
    okladka = models.ImageField(upload_to='okladki/', null=True, blank=True)
    info_autora = models.TextField(blank=True, default='')

    def srednia_ocena(self):
        oceny = self.recenzje.all().values_list('ocena', flat=True)
        return round(sum(oceny) / len(oceny), 1) if oceny else 0

class Recenzja(models.Model):
    ksiazka = models.ForeignKey(Ksiazka, on_delete=models.CASCADE, related_name='recenzje')
    autor_recenzji = models.ForeignKey(User, on_delete=models.CASCADE)
    tresc = models.TextField()
    ocena = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = ('ksiazka', 'autor_recenzji')

    def __str__(self):
        return f"{self.ksiazka} - {self.autor_recenzji} ({self.ocena}/5)"
