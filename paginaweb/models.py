from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class userManager(BaseUserManager):
    def create_user(self, nombre_completo, username, correo_electronico, password):
        # Crea un nuevo usuario con los datos proporcionados
        usuario = self.model(
            nombre_completo=nombre_completo,
            username=username,
            correo_electronico=correo_electronico,
        )
        usuario.set_password(password)  # Establece la contraseña cifrada
        usuario.save()
        return usuario

    def create_superuser(self, nombre_completo, username, correo_electronico, password):
        # Crea un superusuario con los datos proporcionados
        usuario = self.create_superuser(
            nombre_completo=nombre_completo,
            username=username,
            correo_electronico=correo_electronico,
            password=password,
        )
        usuario.is_admin = True
        usuario.is_staff = True
        usuario.save()
        return usuario

class Usuario(AbstractBaseUser):
    nombre_completo = models.CharField(max_length=255)
    username = models.CharField(max_length=50, unique=True)
    correo_electronico = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['nombre_completo', 'correo_electronico']

    objects = userManager()

    def __str__(self):
        return self.username

    def has_perm(self):
        return self.is_admin

    def has_module_perms(self):
        return self.is_admin

class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    imagen = models.CharField(max_length=2000)

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'