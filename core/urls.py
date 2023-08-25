from api.views import BookViewSet, AuthorViewSet, PublisherViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.contrib import admin

router = DefaultRouter()
router.register(r'book', BookViewSet, basename='book')
router.register(r'author', AuthorViewSet, basename='author')
router.register(r'publisher', PublisherViewSet, basename='publisher')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
