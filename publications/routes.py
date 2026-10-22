from django.urls import path
from .views import garment_view, publication_view

urlpatterns = [
    path('save_publication/', publication_view.save_publication, name='api_guardar_publicacion'),
    path('save_garment/', garment_view.save_garment, name='api_guardar_prenda'),
]