from django.urls import path, include

from management.views import  user
from management.views import  candidate
from management.views import  election

urlpatterns = [
    path('', user.get_users, name='get_users'),
    path('user/', user.create_user, name='create_user'),
    path('user/<str:id>', user.get_user_by_id, name='get_user_by_id'),
    path('user/<str:id>/apply-candidate', candidate.apply_candidate, name='apply_candidate'),
    path('candidates/', candidate.get_candidates, name='get_candidates'),
    path('candidates/<str:candidate_id>', candidate.delete_candidate, name='delete_candidate'),
    path('election', election.create_election, name='create_election'),
    path('election/<str:election_id>', election.get_election_by_id, name='get_election_by_id'),
    path('elections', election.get_elections, name='get_elections'),
    path('elections/insert-canidate/<str:election_id>/<str:candidate_id>', election.insert_candidate, name='insert_candidate'),
]


