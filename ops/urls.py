"""ops URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.urls import include
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework_jwt.views import obtain_jwt_token
from permissions.router import permission_router
from cabinet.router import cabinet_router
from products.router import products_router
from groups.router import group_router
from books.router import book_router
from idcs.router import idcs_router
from manufacturer.router import manufacturer_router
from users.router import users_router

route = DefaultRouter()
route.registry.extend(group_router.registry)
route.registry.extend(idcs_router.registry)
route.registry.extend(manufacturer_router.registry)
route.registry.extend(cabinet_router.registry)
route.registry.extend(permission_router.registry)
route.registry.extend(products_router.registry)
route.registry.extend(users_router.registry)
route.registry.extend(book_router.registry)

urlpatterns = [
    url(r'^',include(route.urls)),
    url(r'^api-auth',include("rest_framework.urls",namespace="rest_framework")),
    url(r'^docs/',include_docs_urls('运维平台接口文档')),
    url(r'^api-token-auth/', obtain_jwt_token),
]