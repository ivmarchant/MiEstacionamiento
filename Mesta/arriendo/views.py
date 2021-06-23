from django.shortcuts import get_object_or_404, render, redirect
from .models import *
from .forms import UserRegistroForm, EstacionamientoForm
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    estacionamientos = Estacionamiento.objects.all()
    context = { 'estacionamientos': estacionamientos }
    return render(request, 'index.html', context)

def registrar(request):
    if request.method == 'POST':
        form = UserRegistroForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado')
            return redirect('perfil')
    else:
        form = UserRegistroForm()
        
    context = { 'form' : form }
    return render(request, 'registro/registrar.html', context)

def estacionamiento(request):
    current_user = get_object_or_404(User, pk=request.user.pk)
    if request.method == 'POST':
        form = EstacionamientoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
            messages.success(request, 'Estacionamiento creado')
            return redirect('perfil')
    else:
        form = EstacionamientoForm()
    return render(request, 'estacionamiento/crear_estacionamiento.html', {'form' : form })

def perfil(request):
    estacionamientos = Estacionamiento.objects.all()
    context = { 'estacionamientos': estacionamientos }
    return render(request, 'perfil.html', context)

