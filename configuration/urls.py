from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('api/', include('management.api.user.urls'), name='api_rest_urls'),
]
