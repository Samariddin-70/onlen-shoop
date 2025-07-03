from itertools import product

from django.urls import path
from .site_views import index, account, cart, categories, checkout, search, products, product_d, change_cart

urlpatterns =[
    path('',index,name='home'),
    path('account/',account,name='account'),
    path('cart/',cart,name='cart'),
    path('categories/',categories,name='categories'),
    path('checkout/',checkout,name='checkout'),
    path('product-d/',product_d,name='product-d'),
    path('products/',products,name='products'),
    path('search/',search,name='search'),
    path('add-to-cart/<int:add_id>/', cart, name='cart_add'),
    path('ch/cart/<int:cart_id>/<int:inc>/', change_cart, name='change_cart')
        ]