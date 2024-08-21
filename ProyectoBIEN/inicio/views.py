# Create your views here.
from django.shortcuts import render, HttpResponse, redirect, get_object_or_404
from inicio.forms import CustomUserCreationForm
from django.contrib import messages
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from modelos.models import Usuario
from modelos.models import Tours
from modelos.models import Comentario
from .forms import ReservaForm


from .forms import PerfilForm, EditarPerfilForm

# Create your views here.
def principal(request):
    return render(request, "inicio/principal.html")

def cursos(request):
    return render(request, "inicio/cursos.html")

def contacto(request):
    return render(request, "inicio/contacto.html")

def tours(request):
    return render(request, "inicio/tours.html")

def proximos(request):
    return render(request, "inicio/toursprox.html")

def formTour(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Reserva realizada con éxito.')
            return redirect('Tours')  # Redirige a la vista tours
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ReservaForm()

    return render(request, 'inicio/formTour.html', {'form': form})

def datosPago(request):
    return render(request,"inicio/datosPago.html")


#todo de la seccion de Usuario
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(email=formulario.cleaned_data["email"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, 'Usuario registrado correctamente')
            return redirect('Principal')
        data["form"] = formulario

    return render(request, "registration/registro.html", data)


# views.py

@login_required
def perfilusuario(request):
    # Obtén el usuario actualmente autenticado
    usuario = request.user
    # Pasa el usuario a la plantilla
    return render(request, 'inicio/usuario/perfilusuario.html', {'usuario': usuario})

@login_required
def editar_perfil(request):
    usuario = request.user

    if request.method == 'POST':    
        form = EditarPerfilForm(request.POST, request.FILES, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, 'Perfil actualizado correctamente')  # Mensaje de éxito
            return redirect('Perfil Usuario')  # Redirige a la página de perfil después de guardar
    else:
        form = EditarPerfilForm(instance=usuario)

    return render(request, 'inicio/usuario/editarperfil.html', {'form': form})
# todo de la sección de Acerca

def acerca(request):
    return render(request, "inicio/acerca/acerca.html")

def caminemos(request):
    return render(request, "inicio/acerca/caminemos.html")

def kits(request):
    return render(request, "inicio/acerca/kits.html")

def nosotros(request):
    return render(request, "inicio/acerca/nosotros.html")

def seguro(request):
    return render(request, "inicio/acerca/seguro.html")

def terminos(request):
    return render(request, "inicio/acerca/terminos.html")

def tours(request):
    return render(request, "inicio/tours.html")

def finish(request):
    return render(request, "inicio/finish.html")

# ----------------------------------------------------------------

def lista_tours(request):
    tours = Tours.objects.all()
    return render(request, "inicio/toursprox.html",{'tours':tours})


# -------------------------------------------------------------



def comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, "inicio/finish.html", {'comentarios': comentarios})

def detalle_tour(request, tour_id):
    usuarios = Usuario.objects.all()
    return render(request, 'inicio/detalle_tour.html', {'usuarios': usuarios})

