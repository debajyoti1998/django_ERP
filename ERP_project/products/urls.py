from django.urls import path

from . import views

urlpatterns = [
    path('', views.products_home, name='products_home'),
    path('add', views.add_product, name='add_product'),
    # path('update', views.purchase_product, name='purchase_product'),
    # path('delete', views.purchase_product, name='purchase_product'),
]