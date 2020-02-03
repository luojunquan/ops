from rest_framework.routers import DefaultRouter
from .views import PublishViewSet,BookViewSet,AuthorViewSet

book_router = DefaultRouter()
book_router.register(r'publish', PublishViewSet, basename="publish")
book_router.register(r'book', BookViewSet, basename="book")
book_router.register(r'author', AuthorViewSet, basename="author")

