from django.urls import path, include

urlpatterns = [
    path('api/', include('management.api.user.urls'), name='api_rest_urls'),
]
