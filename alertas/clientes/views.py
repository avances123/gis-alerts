from rest_framework import viewsets
from models import Cliente
from serializers import ClienteSerializer
# Create your views here.

class ClienteViewSet(viewsets.ModelViewSet):
	model = Cliente
	serializer_class = ClienteSerializer
