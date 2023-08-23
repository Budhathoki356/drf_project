from api.views import ItemViewSet, LocationViewSet
from rest_framework.routers import DefaultRouter
from django.urls import include, path
from django.contrib import admin

router = DefaultRouter()
router.register(r'item', ItemViewSet, basename='item')
router.register(r'location', LocationViewSet, basename='location')
urlpatterns = [
    path('admin/',admin.site.urls),
    path('api/', include(router.urls))
]