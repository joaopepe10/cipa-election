from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include('users.api.urls'), name='api_rest_urls'),
]
