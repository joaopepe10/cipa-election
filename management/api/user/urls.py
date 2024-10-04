from django.contrib import admin
from django.urls import path, include

from management import  views

urlpatterns = [
    path('', views.get_users, name='get_all_users'),
    path('user/', views.user, name='user'),
    path('user/<str:id>', views.get_user_by_id, name='get_user_by_id'),
    path('user/<str:id>/apply-candidate', views.apply_candidate, name='apply_candidate'),
    path('candidates/', views.get_candidates, name='get_candidates'),
]
