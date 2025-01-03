from django.contrib import admin
from .models import*

# Register your models here.
admin.site.register(Menu)
from django.contrib import admin
from .models import Menu, Order, OrderItem

# admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)
