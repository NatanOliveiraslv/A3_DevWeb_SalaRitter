from django.contrib import admin
from django.urls import path, include
from apps.home import views

urlpatterns = [
    path('',views.home,name='home'),
    path('admin/', admin.site.urls),
    path('categorias/', include('categories.urls', namespace='categories')),
    path('produtos/', include('products.urls', namespace='products')),
    path('redessociais/', include('socialnetworks.urls', namespace='socialnetworks')),
    path('clientes/', include('clients.urls', namespace='clients')),
    path('clientes_redessociais/', include('clients.urls', namespace='clients_socialnetworks')),
    path('pedidos/', include('orders.urls', namespace='orders')),
    path('pedidos_itens/', include('orders.urls', namespace='orders_items')),
]
