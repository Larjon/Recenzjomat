import csv
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_review_project.settings")
django.setup()

from reviews.models import Ksiazka, Kategoria

CSV_PATH = "ksiazki_import.csv"

with open(CSV_PATH, newline='', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)
    reader.fieldnames = [name.lstrip('\ufeff') for name in reader.fieldnames]

    for row in reader:
        kat, _ = Kategoria.objects.get_or_create(nazwa=row['kategoria'])
        Ksiazka.objects.create(
            tytul=row['tytul'],
            autor=row['autor'],
            opis=row['opis'],
            kategorie=kat
        )
print(" Import zakończony pomyślnie.")
