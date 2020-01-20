from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('inventory', views.inventory_view, name='inventory'),
    path('top_hits', views.inventory_top_hits_view, name='top_hits'),
    path('product/new/', views.product_new, name='product_new'),
    path('product/<str:pk>/edit/', views.product_edit, name='product_edit'),
    path('product/<str:pk>/product_remove', views.product_remove, name='product_remove'),
    path('customers', views.customers, name='customers'),
    path('contributions', views.contributions, name='contributions'),
    path('profile', views.profile, name='profile'),
    path('presence', views.presence, name='presence'),
    path('sales', views.sales, name='sales'),
]