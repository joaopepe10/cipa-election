from django.urls import path

from management.views import  election

urlpatterns = [
    path('', election.elections, name='create_election_and_get_all_elections'),
    path('<str:election_id>', election.get_election_by_id, name='get_election_by_id'),
    path('<str:election_id>/apply-candidate/<str:user_id>', election.insert_candidate, name='insert_candidate'),
    path('end-election/', election.finish, name='end_election')
]


