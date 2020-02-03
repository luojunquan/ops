from rest_framework.routers import DefaultRouter
from .views import IdcListViewset

idcs_router = DefaultRouter()
idcs_router.register(r'idcs', IdcListViewset, basename="idcs")
