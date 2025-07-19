from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_redirect, name='home'),
    path('upload/', views.upload_resume, name='upload_resume'),
]

