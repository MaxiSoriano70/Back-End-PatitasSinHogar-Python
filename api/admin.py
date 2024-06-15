from django.contrib import admin
from .models import Usuario
from .models import Mascota
from .models import Adopcion

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Mascota)
admin.site.register(Adopcion)