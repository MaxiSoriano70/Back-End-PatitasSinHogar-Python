from django.urls import path, include
from rest_framework import routers
from api import views
from django.urls import re_path

router = routers.DefaultRouter()
router.register(r'usuarios', views.UsuarioViewSet)
router.register(r'mascotas', views.MascotaViewSet)
router.register(r'adopciones', views.AdopcionViewSet)

urlpatterns = [
    path('', include(router.urls)),
    re_path('login', views.login),
    re_path('register', views.register),
]
