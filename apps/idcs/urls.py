# -*- coding: utf-8 -*-
# @Time    : 2019/12/23 18:40
# @Author  : Luoxiaojian
# @Email   : ljq906416@gmail.com
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from idcs import views
############################版本一#############################
from idcs.views import IdcList,IdcDetail,IdcListV2,IdcDetailV2

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
    url('^users/$', views.user_list, name='user_list'),
    url("^users/(?P<pk>[0-9]+)/$", views.user_detail, name='user_detail'),
]
urlpatterns = format_suffix_patterns(urlpatterns)