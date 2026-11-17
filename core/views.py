from django.shortcuts import render, redirect
from .models import Cliente, Produto, Venda
from django.contrib.auth.decorators import login_required

# Tela 1: Menu Inicial
def menu(request):
    return render(request, 'menu.html')

# Tela 2: Registro de Venda
def nova_venda(request):
    if request.method == 'POST':
        # Pega os dados do formulário
        produto_id = request.POST.get('produto')
        quantidade = int(request.POST.get('quantidade', 1))
        forma_pagamento = request.POST.get('forma_pagamento')
        cliente_id = request.POST.get('cliente')

        # Busca o produto no banco
        produto = Produto.objects.get(id=produto_id)
        valor_total = produto.preco_venda * quantidade

        # Cria a venda
        cliente = Cliente.objects.get(id=cliente_id) if cliente_id else None
        Venda.objects.create(
            valor_total=valor_total,
            forma_pagamento=forma_pagamento,
            cliente=cliente
        )

        # Se for fiado, atualiza o saldo do cliente
        if forma_pagamento == 'Fiado' and cliente:
            cliente.saldo_devedor += valor_total
            cliente.save()

        return redirect('menu') # Volta pro menu após a venda

    # Se for acessar a tela, mostra os produtos e clientes
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()
    return render(request, 'nova_venda.html', {'produtos': produtos, 'clientes': clientes})