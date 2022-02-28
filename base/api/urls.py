from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorView, BookView, UpcomingBookView

router = DefaultRouter()

router.register(r'authorapi', AuthorView, basename='author')
router.register(r'bookapi', BookView, basename='book')
router.register(r'upcommingbookapi', UpcomingBookView, basename='upcommingbook')

urlpatterns = [
    path('', include(router.urls)),        
]