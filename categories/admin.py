from django.contrib import admin
from categories.models import CategoryInfo
# Register your models here.

# class CategoryAdmin(admin.ModelAdmin):
#     list_display=['categoryName']

# admin.site.register(CategoryInfo,CategoryAdmin)
admin.site.register(CategoryInfo)