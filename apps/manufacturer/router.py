from rest_framework.routers import DefaultRouter
from .views import ManufacturerViewSet, ProductModelViewSet

manufacturer_router = DefaultRouter()
manufacturer_router.register(r'manufacturer', ManufacturerViewSet, basename="manufacturer")
manufacturer_router.register(r'productmodel', ProductModelViewSet, basename="productmodel")
