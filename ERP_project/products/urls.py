from django.urls import path

from . import views

urlpatterns = [
    path('', views.products_home, name='products_home'),
    path('add', views.add_product, name='add_product'),
    path('update/<int:p_id>', views.update_product, name='update_product'),
    path('delete/<int:p_id>', views.delete_product, name='delete_product'),
]