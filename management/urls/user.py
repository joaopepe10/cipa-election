from django.urls import path
from management.views import  user


urlpatterns = [
    path('', user.create_user, name='create_user'),
    path('<str:user_id>', user.get_user_by_id, name='get_user_by_id'),
]