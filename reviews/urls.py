from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'reviews'

urlpatterns = [
    path('', views.lista_ksiazek, name='lista_ksiazek'),
    path('ksiazka/<int:pk>/', views.szczegoly_ksiazki, name='szczegoly_ksiazki'),
    path('dodaj/', views.dodaj_ksiazke, name='dodaj_ksiazke'),
    path('register/', views.register, name='register'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
