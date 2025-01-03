from django.urls import path
from .views import *
urlpatterns = [ 
    path('base/',base,name='base'),
    path('',home,name='home'),
    path('menu/',menu,name='menu'),
    path('about/',about,name='about'),
    path('reserve/', reserve_table, name='reserve'),

    path('place_order/', place_order, name='place_order'),
    path('order_success/', order_success, name='order_success'),
    
    ]

