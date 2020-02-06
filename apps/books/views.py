from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BasicAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets, filters
# Create your views here.
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from books.filters import PublishFilter, AuthorFilter, BookFilter
from books.models import Publish, Author, Book
from books.serializer import PublishSerializer, AuthorSerializer, BookSerializer


class Pagination(PageNumberPagination):
    page_size = 5
    page_size_query_param = 'page_size'
    page_query_param = "page"
    max_page_size = 100

class PublishViewSet(viewsets.ModelViewSet):
    """
    出版商信息
    """
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication,TokenAuthentication,BasicAuthentication)

    queryset = Publish.objects.all()
    serializer_class = PublishSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = PublishFilter
    search_fields = ('name','city')
    ordering_fields = ('city',)

class AuthorViewSet(viewsets.ModelViewSet):
    """
    list:
      列出所有作者信息
    retrieve:
      某个作者的详细信息
    create:
      创建作者
    update:
      更新作者
    delete:
      删除作者
    """

    authentication_classes = (JSONWebTokenAuthentication,TokenAuthentication,SessionAuthentication,BasicAuthentication)
    # permission_classes = (IsAuthenticated,)

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = AuthorFilter
    search_fields = ('name', 'email')
    ordering_fields = ('name',)

class BookViewSet(viewsets.ModelViewSet):
    """
    图书信息
    """
    authentication_classes = (JSONWebTokenAuthentication,SessionAuthentication,BasicAuthentication)
    rmission_classespe = (IsAuthenticated,)

    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = Pagination
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = BookFilter
    search_fields = ('name',)
    ordering_fields = ('publication_date',)