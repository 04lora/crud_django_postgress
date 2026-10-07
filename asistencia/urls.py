from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_asistencia, name='lista_asistencia'),
    path('nuevo/', views.crear_asistencia, name='crear_asistencia'),
    path('editar/<int:pk>/', views.editar_asistencia, name='editar_asistencia'),
    path('eliminar/<int:pk>/', views.eliminar_asistencia, name='eliminar_asistencia'),
]