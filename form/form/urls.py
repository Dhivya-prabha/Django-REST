"""form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from upload.views import ShipPositionAPIView, ShipsViewSet, Index

from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=True)
router.register(r'ships', ShipsViewSet)


urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('api-auth/', include(router.urls)),
        re_path('api/positions/(?P<uid>[0-9A-Za-z_\-]+)/', ShipPositionAPIView.as_view(), name='position-api')
]
