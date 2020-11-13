from django.db import models
from cpf_field.models import CPFField # Modelo para cpf

class Cliente(models.Model):
    slug = models.SlugField('Atalho')
    nome = models.CharField('Nome Completo', max_length=100)
    cpf = CPFField('Cpf')
    data_nascimento = models.DateField('Data de nascimento')
    email = models.EmailField()
    endereço = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    celular = models.CharField(max_length=12)
    observações = models.TextField('Observações', blank=True)
    start_date = models.DateTimeField('start date', auto_now_add=True)

    def __str__(self):
        return self.nome
    