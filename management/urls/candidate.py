from django.urls import path
from management.views import  candidate

## LISTAR TODOS -> http://127.0.0.1:8000/api/candidates/
## LISTAR TODOS -> http://127.0.0.1:8000/api/candidates/${id}
urlpatterns = [
    path('', candidate.CandidateListView.as_view(), name='candidate-list'),
    path('<int:candidate_id>', candidate.CandidateDetailView.as_view(), name='candidate-detail'),

]