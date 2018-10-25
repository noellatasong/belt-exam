"""exam_retake URL Configuration

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
from django.urls import path
from examapp import views
urlpatterns = [
    path('', views.index),
    path('new_user', views.new_user),
    path('login', views.login),
    path('logout', views.logout),
    path('wishlist', views.wishlist),
    path('create', views.create),
    path('create_item', views.create_item),
    path('details/<item_id>/', views.details),
    path('added/<item_id>/', views.added),
    path('delete/<item_id>/', views.delete),
    path('remove/<added_id>/', views.remove),
]
