import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_review_project.settings")
django.setup()

from reviews.models import Ksiazka

for i in range(2, 20):
    try:
        ksiazka = Ksiazka.objects.get(pk=i)
        ksiazka.okladka.name = f"okladki/{i}.webp"
        ksiazka.save()
        print(f"✓ {ksiazka.tytul} ⟶ {i}.webp")
    except Ksiazka.DoesNotExist:
        print(f"Książka o ID {i} nie istnieje")
import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "book_review_project.settings")
django.setup()

from reviews.models import Ksiazka

for i in range(2, 23):
    try:
        ksiazka = Ksiazka.objects.get(pk=i)
        ksiazka.okladka.name = f"okladki/{i}.webp"
        ksiazka.save()
        print(f"✓ {ksiazka.tytul} ⟶ {i}.webp")
    except Ksiazka.DoesNotExist:
        print(f"Książka o ID {i} nie istnieje")
