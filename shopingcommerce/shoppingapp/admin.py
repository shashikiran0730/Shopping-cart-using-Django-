from django.contrib import admin

from.models import product,mycart

class ProductAdmin(admin.ModelAdmin):
    list_display=['Itemid','Itemname','category','imageurl','description','price','available']
    list_editable=['price','available']

class MycartAdmin(admin.ModelAdmin):
    list_display=['customeremail','Itemid','Itemname','category','imageurl','description','price','quantity']

admin.site.register(product,ProductAdmin)
admin.site.register(mycart,MycartAdmin)
