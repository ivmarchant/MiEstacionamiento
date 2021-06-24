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

def esta_view(request):
    estacionamientos = Estacionamiento.objects.all()
    context = { 'estacionamientos': estacionamientos }
    return render(request, 'estacionamiento/estacionamientos.html', context)


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
            return redirect('estacionamientos')
    else:
        form = EstacionamientoForm()
    return render(request, 'estacionamiento/crear_estacionamiento.html', {'form' : form })

def perfil(request, username=None):
    current_user = request.user
    if username and username != current_user.username:
        user = User.objects.get(username=username)
        estacionamientos = user.estacionamientos.all()
    else:
        estacionamientos = current_user.estacionamientos.all()
        user = current_user
    return render(request, 'perfil.html', {'user':user, 'estacionamientos':estacionamientos})

