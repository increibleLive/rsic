from django.contrib import admin
from enquiry.models import Enquries
# Register your models here.

# class CustomerEnquiry(admin.ModelAdmin):
#     readonly_fields = ['name','email','phone','subject','msg','date']
#     list_display = ['name','email','phone','subject','msg','date']

# admin.site.register(Enquries,CustomerEnquiry)

@admin.register(Enquries)
class CustomerEnquiry(admin.ModelAdmin):
    readonly_fields = ['name','email','phone','subject','msg','date']
    list_display = ['name','email','phone','subject','msg','date']

    def has_add_permission(self, request, obj=None):
        return False

