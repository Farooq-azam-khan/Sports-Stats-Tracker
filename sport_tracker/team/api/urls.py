from django.urls import path, include
from .views import TeamViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'all', TeamViewSet)

urlpatterns = [
    path('', include(router.urls))
]