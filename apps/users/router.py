from rest_framework.routers import DefaultRouter
from .views import UserViewSet,UserInfoViewset,DashboardStatusViewset

users_router = DefaultRouter()
users_router.register(r'users', UserViewSet, basename="users")
users_router.register(r'userinfo', UserInfoViewset, basename="userinfo")
users_router.register(r'dashboard', DashboardStatusViewset, basename="dashboard")
