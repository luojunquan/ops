from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from cabinet.models import Cabinet
from cabinet.serializers import CabinetServerSerializer

@api_view(['GET'])
def api_root(request, format=None, *args, **kwargs):
    return Response({
        'cabinetserver': reverse('cabinetserver', request=request, format=format),
    })

class CabinetServer(viewsets.ModelViewSet):
    queryset = Cabinet.objects.all()
    serializer_class = CabinetServerSerializer