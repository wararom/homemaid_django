from django.contrib import admin
from customer.models import Customer, Maid, Reserve
# Register your models here.
class MaidAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Maid._meta.fields]
admin.site.register(Maid,MaidAdmin)

class CustomerAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Customer._meta.fields]
admin.site.register(Customer,CustomerAdmin)

class ReserveAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Reserve._meta.fields]
admin.site.register(Reserve,ReserveAdmin)