from django.urls import path
from management.views import  candidate

urlpatterns = [
    path('', candidate.CandidateListView.as_view(), name='candidate-list'),
    path('<int:candidate_id>', candidate.CandidateDetailView.as_view(), name='candidate-detail'),

]