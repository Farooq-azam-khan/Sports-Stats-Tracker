"""sport_tracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path

# from django.views.generic import TemplateView

# urlpatterns = [
#     path('', TemplateView.as_view(template_name='home.html'), name='home'),
#     path('admin/', admin.site.urls),
# ]
from django.urls import include, path
from django.contrib import admin
from django.views.generic import TemplateView

# from .api import

urlpatterns = [
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    # path('api/', include('sport_tracker.api')),
    path('api/leagues/', include('sport.api.urls'), name='leauge-list'),
    path('api/teams/', include('team.api.urls'), name='team-list'),
    path('api/players/', include('player.api.urls'), name='players-list'),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]
