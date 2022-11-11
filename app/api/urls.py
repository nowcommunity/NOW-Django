from django.urls import path
from django.urls.conf import include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'museums', views.MuseumViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
