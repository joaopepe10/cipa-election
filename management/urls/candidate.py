from django.urls import path
from management.views import  candidate

urlpatterns = [
    path('', candidate.get_candidates, name='get_candidates'),
    path('<str:candidate_id>', candidate.candidates, name='get_by_id_and_update_speech'),

]