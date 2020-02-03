from django.contrib.auth.models import Group
from .serilaizers import GroupSerializer
from .filter import GroupFilter

from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
class GroupsViewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    filter_class = GroupFilter
    filter_fields = ("name",)