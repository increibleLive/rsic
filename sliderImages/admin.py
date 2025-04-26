from django.contrib import admin
from sliderImages.models import ImageSlider
from django.utils.html import format_html

class MyImageModelAdmin(admin.ModelAdmin):
    # list_display = ['title','image_tag']
    list_display = ['image_tag']

    # def __str__(self):
    #     return self.title
    
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="auto" />'.format(obj.image.url))
        else:
            return 'No Image Found'
    image_tag.short_description = 'Image Preview'

admin.site.register(ImageSlider,MyImageModelAdmin)
# Register your models here.
