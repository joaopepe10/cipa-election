from django.urls import path
from management.views import  vote

urlpatterns = [
    path('', vote.create_vote, name='vote'),
]