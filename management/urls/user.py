from django.urls import path
from management.views import  user


urlpatterns = [
    # DEFINIR A URL QUE A TELA SERA ACESSADA, IR PARA A VIEW CRIAR A FUNCAO DO RENDER PARA RENDERIZAR A TELA DESEJADA
    path('', user.index, name='create_user'),
    path('cadastro-usuario', user.register_user, name='create_user'),
    path('create', user.create_user, name='create_user'),
    path('<str:user_id>', user.get_user_by_id, name='get_user_by_id'),
]