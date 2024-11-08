from django.urls import path

from management.views import  election

## LISTAR TODOS -> http://127.0.0.1:8000/api/elections/${electionId}/apply-candidate/${userId}

urlpatterns = [
    path('', election.elections, name='create_election_and_get_all_elections'),
    path('result', election.result, name='result'),
    path('<str:election_id>', election.get_election_by_id, name='get_election_by_id'),
    path('<str:election_id>/apply-candidate/<str:user_id>', election.insert_candidate, name='insert_candidate'),
]


