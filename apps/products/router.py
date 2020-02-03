from rest_framework.routers import DefaultRouter
from .views import ProductViewset, ProductManageViewSet


products_router = DefaultRouter()
products_router.register(r'products', ProductViewset, basename='products')
products_router.register(r'productmanage', ProductManageViewSet, basename="productmanage")