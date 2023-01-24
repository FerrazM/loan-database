from django.shortcuts import render, redirect
from .models import Cliente
from .forms import ClienteForm
from django.contrib.auth.decorators import login_required
from django.db.models import Sum



@login_required
def clientes(request):
    dados_cliente = {
        'dados': Cliente.objects.filter(usuario=request.user)
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
            cliente = cliente_form.save(commit=False)
            cliente.usuario = request.user
            cliente.save()
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
    soma_valor = Cliente.objects.filter(
        usuario=request.user).aggregate(Sum('valor'))
    soma_pagamento = Cliente.objects.filter(
        usuario=request.user).aggregate(Sum('juros_mes'))
    context = {'soma_valor': soma_valor, 'soma_pagamento': soma_pagamento}
    return render(request, 'loans/balanco.html', context)


@login_required
def balancomensal(request):
    inicio_mes = request.POST.get('start_date')
    fim_mes = request.POST.get('end_date')
    soma_valor_mes = Cliente.objects.filter(usuario=request.user, data__range=[
                                        inicio_mes, fim_mes]).aggregate(Sum('valor'))
    soma_pagamento_mes = Cliente.objects.filter(usuario=request.user, vencimento_mensal__range=[
                                            inicio_mes, fim_mes]).aggregate(Sum('juros_mes'))
    context = {'soma_valor_mes': soma_valor_mes, 'soma_pagamento_mes': soma_pagamento_mes}
    return render(request, 'loans/balanco_mensal.html', context)
