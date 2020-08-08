from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Product)
admin.site.register(Related_Product)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)




