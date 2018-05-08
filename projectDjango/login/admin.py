from django.contrib import admin

# Register your models here.
from .models import CustomUser
class CustomAdmin(admin.ModelAdmin):
    list_display=[f.name for f in CustomUser._meta.fields]
admin.site.register(CustomUser,CustomAdmin)