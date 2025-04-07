from django.db import IntegrityError
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
from .models import Ksiazka, Recenzja, Kategoria
from .forms import RecenzjaForm, KsiazkaForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404


def lista_ksiazek(request):
    kategorie = Kategoria.objects.all()
    kategoria_id = request.GET.get('kategorie')
    ksiazki = Ksiazka.objects.all().order_by('id')

    if kategoria_id:
        ksiazki = ksiazki.filter(kategorie__id=kategoria_id)

    paginator = Paginator(ksiazki, 9)
    page = request.GET.get('page')

    context = {
        'ksiazki': paginator.get_page(page),
        'kategorie': kategorie,
    }
    return render(request, 'reviews/lista_ksiazek.html', context)

def szczegoly_ksiazki(request, pk):
    ksiazka = get_object_or_404(Ksiazka, pk=pk)
    recenzje = ksiazka.recenzje.all()
    uzytkownik_juz_recenzowal = False

    if request.user.is_authenticated:
        uzytkownik_juz_recenzowal = Recenzja.objects.filter(
            ksiazka=ksiazka,
            autor_recenzji=request.user
        ).exists()

    form = RecenzjaForm()

    if request.method == 'POST' and request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
        form = RecenzjaForm(request.POST)
        if form.is_valid():
            recenzja = form.save(commit=False)
            recenzja.ksiazka = ksiazka
            recenzja.autor_recenzji = request.user
            try:
                recenzja.save()
            except IntegrityError:
                return JsonResponse({'error': 'Już dodałeś recenzję tej książki'}, status=400)

            html = render_to_string("reviews/fragment_recenzji.html", {'recenzja': recenzja})
            return JsonResponse({
            'html': html,
            'srednia': ksiazka.srednia_ocena()
        })
        else:
            return JsonResponse({'error': 'Niepoprawny formularz'}, status=400)

    return render(request, 'reviews/szczegoly_ksiazki.html', {
        'ksiazka': ksiazka,
        'recenzje': recenzje,
        'form': form,
        'uzytkownik_juz_recenzowal': uzytkownik_juz_recenzowal
    })

@permission_required('reviews.add_ksiazka')
def dodaj_ksiazke(request):
    if request.method == 'POST':
        form = KsiazkaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_ksiazek')
    else:
        form = KsiazkaForm()
    return render(request, 'reviews/dodaj_ksiazke.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def profil(request):
    recenzje = Recenzja.objects.filter(autor_recenzji=request.user)
    return render(request, 'reviews/profil.html', {'recenzje': recenzje})
