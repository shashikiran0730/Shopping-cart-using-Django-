from django.contrib import admin

from.models import product,mycart,orderconform,previousorders,adminlogin

admin.site.register(product)
admin.site.register(mycart)
admin.site.register(orderconform)
admin.site.register(previousorders)
admin.site.register(adminlogin)