from django.urls import path, include

urlpatterns = [
    path('api/users/', include('management.urls.user'), name='api_rest_user'),
    path('api/candidates/', include('management.urls.candidate'), name='api_rest_candidate'),
    path('api/elections/', include('management.urls.election'), name='api_rest_election'),
]
