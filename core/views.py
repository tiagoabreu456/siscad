from django.shortcuts import render

from django.views import generic #Import para class-based view

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