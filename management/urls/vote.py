from django.urls import path
from management.views import  vote

urlpatterns = [
    path('', vote.post_vote, name='vote'),
]