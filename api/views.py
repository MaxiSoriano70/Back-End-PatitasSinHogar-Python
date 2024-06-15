from rest_framework import viewsets
from .models import Usuario
from .models import Mascota
from .models import Adopcion
from .serializer import UsuarioSerializer
from .serializer import MascotaSerializer
from .serializer import AdopcionSerializer


from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
import uuid


def generate_token():
    return str(uuid.uuid4())

@api_view(['POST'])
def login(request):
    usuario = get_object_or_404(Usuario, email=request.data['email'])
    if not usuario.contrasenia == request.data['contrasenia']:
        return Response({"error": "Contraseña inválida"}, status=status.HTTP_400_BAD_REQUEST)
    token = generate_token()
    return Response({'token': token, 'usuario': UsuarioSerializer(usuario).data}, status=status.HTTP_200_OK)

@api_view(['POST'])
def register(request):
    serializer = UsuarioSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        token = generate_token()
        return Response({'token': token, 'usuario': serializer.data}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class MascotaViewSet(viewsets.ModelViewSet):
    queryset = Mascota.objects.all()
    serializer_class = MascotaSerializer

class AdopcionViewSet(viewsets.ModelViewSet):
    queryset = Adopcion.objects.all()
    serializer_class = AdopcionSerializer