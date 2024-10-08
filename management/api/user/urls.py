from django.urls import path, include

from management.views import  user
from management.views import  candidate

urlpatterns = [
    path('', user.get_users, name='get_users'),
    path('user/', user.create_user, name='create_user'),
    path('user/<str:id>', user.get_user_by_id, name='get_user_by_id'),
    path('user/<str:id>/apply-candidate', candidate.apply_candidate, name='apply_candidate'),
    path('candidates/', candidate.get_candidates, name='get_candidates'),
    path('candidates/<str:candidate_id>', candidate.delete_candidate, name='delete_candidate'),
]
