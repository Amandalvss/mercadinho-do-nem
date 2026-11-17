from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.menu, name='menu'),
    path('venda/', views.nova_venda, name='nova_venda'),
]