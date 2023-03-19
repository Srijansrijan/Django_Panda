from django.contrib import admin
from django.urls import path
from panda_app import views

urlpatterns = [
    path("", views.indexx, name="home"),
    path("login", views.login, name='login'),
    path('about',views.about,name='about'),
    path('types',views.types,name='types')
]