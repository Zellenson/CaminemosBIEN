from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin



class UsuarioManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)

class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    telefono = models.CharField(max_length=15, blank=True)
    ciudad = models.CharField(max_length=100, blank=True)
    estado = models.CharField(max_length=100, blank=True)
    imagen = models.ImageField(upload_to='profile_images/', blank=True)
    tarjeta = models.CharField(max_length=16, blank=True)
    cvv = models.CharField(max_length=3, blank=True)
    caducidad = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'apellidos']

    def __str__(self):
        return self.email



    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

  

class Comentario(models.Model):
    usuario = models.CharField(max_length=12, verbose_name="Usuario ")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Registrado")
    coment = RichTextField(verbose_name="Comentario")

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
        ordering = ["-created"]

    def __str__(self):
        return self.coment

"""class Viaje(models.Model):
    destino = models.CharField(max_length=12, verbose_name="Destino: ")
    fecha_salida = models.DateField(verbose_name="Fecha de Salida: ")
    precio=models.IntegerField(verbose_name="Precio: ")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")  # Fecha y Tiempos
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Viaje"
        verbose_name_plural = "Viajes"
        ordering = ["-created"]

    def __str__(self):
        return self.destino"""

class Tours(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    imagen = models.ImageField(null=True, upload_to="fotos", verbose_name="Fotografía")
    destino = models.CharField(max_length=12, verbose_name="Destino ")
    descripcion = models.TextField(verbose_name="Descripcion ")
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de Actualización")

    class Meta:
        verbose_name = "Tour"
        verbose_name_plural = "Tours"
        ordering = ["-created"]

    def __str__(self):
        return self.destino

class Reserva(models.Model):
    id = models.AutoField(primary_key=True, verbose_name="Id")
    nombre = models.CharField(max_length=12, blank=True, null=True) 
    personas = models.IntegerField(blank=True, null=True) 
    apellidos = models.CharField(max_length=30, blank=True, null=True)  
    telefono = models.CharField(max_length=20, blank=True, null=True) 
    edad = models.IntegerField(blank=True, null=True)  
    fecha = models.DateField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.nombre,self.apellidos
    