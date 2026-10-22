from django.urls import path
from .views import garment_view, publication_view

urlpatterns = [
    path('guardar_publicacion/', publication_view.save_publication, name='api_guardar_publicacion'),
    path('guardar_prenda/', garment_view.save_garment, name='api_guardar_prenda'),
]