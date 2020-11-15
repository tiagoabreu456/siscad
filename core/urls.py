from django.urls import path
from .views import home, ClienteListView, CreateCliente


app_name='core'

urlpatterns = [
    path('', home, name='home'),

    #url para listagem dos clientes
    path('lista_clientes/', ClienteListView.as_view(), name='list_client'),

    path('add_cliente/', CreateCliente.as_view(),  name='add_cliente')
]