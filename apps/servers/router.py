from rest_framework.routers import DefaultRouter
from .views import ServerViewset, NetwokDeviceViewset, IPViewset, ServerAutoReportViewset, ServerCountViewset

servers_router = DefaultRouter()
servers_router.register(r'servers', ServerViewset, basename="servers")
servers_router.register(r'network_device', NetwokDeviceViewset, basename="network_device")
servers_router.register(r'ip', IPViewset, basename="ip")
servers_router.register(r'ServerAutoReport', ServerAutoReportViewset, basename="ServerAutoReport")
servers_router.register(r'ServerCount', ServerCountViewset, basename="ServerCount")