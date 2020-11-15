from django.shortcuts import render

from django.urls import reverse

from django.views import generic #Import para class-based view
from django.views.generic.edit import CreateView

from clientes.models import Cliente #Import model Cliente

# Create your views here.

#View para a pagina principal
def home(request):
    return render(request, 'home.html')

#View para listagem dos clientes
class ClienteListView(generic.ListView):
    template_name = 'clientes.html'
    model = Cliente
    context_object_name = 'clientes'

class CreateCliente(CreateView):
    template_name = 'add_cliente.html'
    model = Cliente
    fields = ['nome', 'cpf', 'data_nascimento', 'email', 'endereço', 'cidade', 'celular', 'curso']
    success_url = '/lista_clientes/'
    