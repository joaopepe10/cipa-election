from django.urls import path
from management.views import  home

urlpatterns = [
    path('', home.home, name='login')
]