from rest_framework.routers import DefaultRouter
from servers.views import ServerViewSet,NetworkDeviceViewSet,IPViewSet,ServerAutoReportViewSet,ServerCountViewset
servers_router = DefaultRouter()
servers_router.register(r'server', ServerViewSet, basename="server")
servers_router.register(r'network_device', NetworkDeviceViewSet, basename="network_device")
servers_router.register(r'ip', IPViewSet, basename="ip")
servers_router.register(r'ServerAutoReport', ServerAutoReportViewSet, basename="ServerAutoReport")
servers_router.register(r'ServerCount', ServerCountViewset, basename="ServerCount")