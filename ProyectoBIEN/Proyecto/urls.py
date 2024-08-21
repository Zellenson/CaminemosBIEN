# Proyecto/urls.py
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from inicio import views
from inicio.views import registro
urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta principal
    path('', views.principal, name='Principal'),
    
    # Rutas de autenticación predeterminadas de Django
    path('accounts/', include('django.contrib.auth.urls')),
    # Otras rutas de tu aplicación
    path('cursos/', views.cursos, name='Cursos'),
    path('registro/', views.registro, name='Registro'),
    path('contacto/', views.contacto, name='Contacto'),
    path('tours/', views.tours, name='Tours'),
    ##path('toursprox/', views.proximos, name='toursprox'),
    path('perfilusuario/', views.perfilusuario, name='Perfil Usuario'),
    path('editar_perfil/', views.editar_perfil, name='Editar Perfil'),
    path('acerca/', views.acerca, name='Acerca'),
    path('acerca/caminemos/', views.caminemos, name='Caminemos'),
    path('acerca/kits/', views.kits, name='Kits'),
    path('acerca/nosotros/', views.nosotros, name='Nosotros'),
    path('acerca/seguro/', views.seguro, name='Seguro'),
    path('acerca/terminos/', views.terminos, name='Terminos'),
    path('formTour/', views.formTour, name='FormTour'),
    path('datosPago/', views.datosPago, name='datosPago'),
    path('toursprox/', views.lista_tours, name='toursprox'),
    path('finish/', views.finish, name='finish'),
    path('tours/<int:tour_id>/', views.detalle_tour, name='detalle_tour'),
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
