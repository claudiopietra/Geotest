"""Geotest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from Geotest import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('location/<int:location_id>/', views.display_location),
    path('item/<int:item_id>/add', views.add_item)
    path('item/<int:item_id>/remove', views.remove_item)

    #---the not valid URL's:
    path('location/<str:entered_url>/', views.not_valid),
    path('<int:entered_url>', views.not_valid),
    path('<str:entered_url>', views.not_valid),
]
