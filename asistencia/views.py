from django.shortcuts import render, redirect, get_object_or_404
from .models import RegistroAsistencia
from .forms import RegistroAsistenciaForm


def lista_asistencia(request):
    registros = RegistroAsistencia.objects.all().order_by('-fecha')
    return render(request, 'asistencia/lista.html', {'registros': registros})


def crear_asistencia(request):
    if request.method == 'POST':
        form = RegistroAsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_asistencia')
    else:
        form = RegistroAsistenciaForm()
    return render(request, 'asistencia/form.html', {'form': form, 'titulo': 'Nuevo Registro'})


def editar_asistencia(request, pk):
    registro = get_object_or_404(RegistroAsistencia, pk=pk)
    if request.method == 'POST':
        form = RegistroAsistenciaForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_asistencia')
    else:
        form = RegistroAsistenciaForm(instance=registro)
    return render(request, 'asistencia/form.html', {'form': form, 'titulo': 'Editar Registro'})


def eliminar_asistencia(request, pk):
    registro = get_object_or_404(RegistroAsistencia, pk=pk)
    if request.method == 'POST':
        registro.delete()
        return redirect('lista_asistencia')
    return render(request, 'asistencia/eliminar_confirmar.html', {'registro': registro})