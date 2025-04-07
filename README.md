
# Recenzjomat

**Recenzjomat** to nowoczesna aplikacja webowa stworzona w Django, umożliwiająca przeglądanie książek, dodawanie recenzji i ocenianie ulubionych tytułów. Projekt zawiera system autoryzacji użytkowników, panel administracyjny, AJAX-owe recenzje oraz elegancki interfejs z wykorzystaniem Bootstrap Flatly.

---

##  Funkcjonalności

-  Lista książek z filtrowaniem po kategoriach
-  Szczegóły książki z recenzjami i oceną
-  Formularz recenzji tylko dla zalogowanych
-  AJAX: dodawanie recenzji bez przeładowania
-  Średnia ocena aktualizowana w czasie rzeczywistym
-  Rejestracja, logowanie, wylogowanie
-  Strona profilu z listą dodanych recenzji
-  Panel administratora
-  Bootstrap + Bootstrap Icons
-  Responsywny i nowoczesny interfejs

---

##  Technologie

- Python 3.12
- Django 5.2
- SQLite
- Bootstrap 5 (Flatly theme)
- JavaScript (AJAX)
- HTML5 + CSS3

---

##  Instalacja

1. **Sklonuj repozytorium**:

```bash
git clone https://github.com/Larjon/Recenzjomat.git
cd Recenzjomat
```

2. **Utwórz i aktywuj środowisko wirtualne**:

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Linux/Mac
```

3. **Zainstaluj zależności**:

```bash
pip install -r requirements.txt
```

4. **Wykonaj migracje i uruchom serwer**:

```bash
python manage.py migrate
python manage.py runserver
```

5. **(Opcjonalnie) Stwórz konto administratora**:

```bash
python manage.py createsuperuser
```

---

##  Zrzuty ekranu

> ![alt text](image.png)
> ![alt text](image-1.png)
> ![alt text](image-2.png)
> ![alt text](image-3.png)

##  Autor

Projekt stworzony przez **Larjon**

- GitHub: [@Larjon](https://github.com/Larjon)
- Email: lukasz.kowalka.21@gmail.com

---

##  Licencja

Ten projekt jest dostępny na licencji **MIT**.
