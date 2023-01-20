from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum



@login_required
def clientes(request):
    dados_cliente = {
        'dados': Cliente.objects.all()
    }
    return render(request, 'loans/clientes.html', dados_cliente)


@login_required
def detalhe(request, id_cliente):
    dados = {
        'dados': Cliente.objects.get(pk=id_cliente)
    }
    return render(request, 'loans/detalhe.html', dados)


@login_required
def criar(request):
    if request.method == 'POST':
        cliente_form = ClienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
        return redirect('clientes')
    else:
        cliente_form = ClienteForm()
        formulario = {
            'formulario': cliente_form
        }
        return render(request, 'loans/novo_emprestimo.html', context=formulario)


@login_required
def editar(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    if request.method == 'GET':
        formulario = ClienteForm(instance=cliente)
        return render(request, 'loans/novo_emprestimo.html', {'formulario': formulario})
    else:
        formulario = ClienteForm(request.POST, instance=cliente)
        if formulario.is_valid():
            formulario.save()
        return redirect('clientes')


@login_required
def excluir(request, id_cliente):
    cliente = Cliente.objects.get(pk=id_cliente)
    if request.method == 'POST':
        cliente.delete()
        return redirect('clientes')
    return render(request, 'loans/confirmar_exclusao.html', {'item': cliente})


@login_required
def somaemprestimos(request):
    soma_valor = Cliente.objects.aggregate(Sum('valor'))
    soma_pagamento = Cliente.objects.aggregate(Sum('juros_mes'))
    context = {'soma_valor': soma_valor, 'soma_pagamento': soma_pagamento}
    return render(request, 'loans/balanco.html', context)
