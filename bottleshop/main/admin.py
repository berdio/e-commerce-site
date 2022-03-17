from csv import list_dialects
from django.contrib import admin
from .models import *

admin.site.register(Banner)
admin.site.register(Brand)
admin.site.register(Size)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag')
admin.site.register(Category,CategoryAdmin)

class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_bg')
admin.site.register(Color,ColorAdmin)

# Product Admin
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'brand', 'color', 'size', 'status')
    list_editable = ('status',)
admin.site.register(Product,ProductAdmin)

# Product Attribute 
class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'size')
admin.site.register(ProductAttribute,ProductAttributeAdmin)