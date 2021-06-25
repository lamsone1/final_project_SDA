from django.contrib import admin

from utils.models import Box, Layer, Fefco, OrderItem, Order

admin.site.register(Fefco)
admin.site.register(Layer)
admin.site.register(Box)


admin.site.register(OrderItem)
admin.site.register(Order)
