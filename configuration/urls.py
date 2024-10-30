from django.urls import path, include
from management.views import home

urlpatterns = [
    path('', home.home, name='home'),
    path('api/users/', include('management.urls.user'), name='api_rest_user'),
    path('api/candidates/', include('management.urls.candidate'), name='api_rest_candidate'),
    path('api/elections/', include('management.urls.election'), name='api_rest_election'),
    path('api/votes/', include('management.urls.vote'), name='api_rest_vote')
]
