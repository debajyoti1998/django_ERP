from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    # path('products', views.products, name='products'),
    path('logout', views.logout, name='logout'),
]