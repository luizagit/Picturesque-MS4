from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_photobag, name='view_photobag')
]