from django.contrib import admin
from products.models import ProductInfo
from django.utils.html import format_html
# from categories.models import CategoryInfo


class ProductImagesAdmin(admin.ModelAdmin):
   
    list_display = ['name','image','get_category_name']
    
    def get_category_name(self, obj):
        return obj.category.categoryName
    get_category_name.short_description = 'Category'  # Sets column name

    
    def image(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="150" height="auto" />'.format(obj.photo.url))
        else:
            return 'No Image Found'
    image.short_description = 'Image Preview'

# admin.site.register(CategoryInfo)
admin.site.register(ProductInfo,ProductImagesAdmin)
# Register your models here.
