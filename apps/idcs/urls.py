# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 18:40
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from django.urls import include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from idcs import views
############################版本一#############################
from idcs.views import IdcList,IdcDetail,IdcListV2,IdcDetailV2,UserList,UserDetail,IdcListV3,IdcDetailV3,UserListV2,UserDetailV2,IdcListDetailViewSet,UserListDetailSet

urlpatterns = [
    url('^idcs/$', views.idc_list),
    url("^idcs/(?P<pk>[0-9]+)/$", views.idc_detail ),
]
############################版本二#############################
urlpatterns = [
    url("^$",views.api_root),
    url('^idcs/$', views.idc_list_v2,name='idc_list'),
    url("^idcs/(?P<pk>[0-9]+)/$", views.idc_detail_v2,name='idc_detail'),
    url('^users/$',views.user_list,name='user_list'),
    url("^users/(?P<pk>[0-9]+)/$", views.user_detail,name='user_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
############################版本三#############################
urlpatterns = [
    url("^$",views.api_root),
    url('^idcs/$', IdcList.as_view(),name='idc_list'),
    url("^idcs/(?P<pk>[0-9]+)/$", IdcDetail.as_view(),name='idc_detail'),
    url('^users/$', views.user_list, name='user_list'),
    url("^users/(?P<pk>[0-9]+)/$", views.user_detail, name='user_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
############################版本四#############################
urlpatterns = [
    url("^$",views.api_root),
    url('^idcs/$', IdcListV2.as_view(),name='idc_list'),
    url("^idcs/(?P<pk>[0-9]+)/$", IdcDetailV2.as_view(),name='idc_detail'),
    url('^users/$',UserList.as_view() , name='user_list'),
    url("^users/(?P<pk>[0-9]+)/$", UserDetail.as_view(), name='user_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
############################版本五(混合)#############################
urlpatterns = [
    url("^$",views.api_root),
    url('^idcs/$', IdcListV3.as_view(),name='idc_list'),
    url("^idcs/(?P<pk>[0-9]+)/$", IdcDetailV3.as_view(),name='idc_detail'),
    url('^users/$',UserListV2.as_view() , name='user_list'),
    url("^users/(?P<pk>[0-9]+)/$", UserDetailV2.as_view(), name='user_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
############################版本六（Viewsets）#############################
list = {'get':'list',
        'post':'create'}
detail = {'get':'retrieve',
          'post':'update',
          'delete':'destroy'}
idc_list = views.IdcListDetailViewSet.as_view(list)
idc_detail = views.IdcListDetailViewSet.as_view(detail)
user_list = views.UserListDetailSet.as_view(list)
user_detail = views.UserListDetailSet.as_view(detail)
urlpatterns = [
    url("^$",views.api_root),
    url('^idcs/$', idc_list,name='idc_list'),
    url("^idcs/(?P<pk>[0-9]+)/$", idc_detail,name='idc_detail'),
    url('^users/$',user_list , name='user_list'),
    url("^users/(?P<pk>[0-9]+)/$", user_detail, name='user_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)
############################版本六（router）#############################
route = DefaultRouter()
route.register('idcs',views.IdcListDetailViewSet)
route.register('users',views.UserListDetailSet)
urlpatterns = [
    url(r'^',include(route.urls)),
]