from django.urls import path
from .views import home, ClienteListView


app_name='core'

urlpatterns = [
    path('', home, name='home'),

    #url para listagem dos clientes
    path('lista_clientes/', ClienteListView.as_view(), name='list_client'),
]