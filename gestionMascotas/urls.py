from django.urls import path
from gestionMascotas.views import home, crear, guardar, editar, eliminar, actualizar

urlpatterns = [
    path('', home),
    path('crear/', crear),
    path('guardar/', guardar),
    path('editar/<codigo>', editar),
    path('actualizar/', actualizar),
    path('eliminar/<codigo>/', eliminar),

]