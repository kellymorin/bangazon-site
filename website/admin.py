from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Customer)
admin.site.register(ProductType)
admin.site.register(Product)
admin.site.register(PaymentType)
admin.site.register(Order)
admin.site.register(OrderProduct)