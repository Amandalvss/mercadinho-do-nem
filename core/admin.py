from django.contrib import admin
from .models import Cliente, Produto, Venda

# Personalizando o painel do admin para o Mercadinho do Nem
admin.site.site_header = "Administração do Mercadinho do Nem"
admin.site.site_title = "Mercadinho do Nem"
admin.site.index_title = "Painel de Gestão"

admin.site.register(Cliente)
admin.site.register(Produto)
admin.site.register(Venda)

# Ordem de exibicao dos modelos no painel